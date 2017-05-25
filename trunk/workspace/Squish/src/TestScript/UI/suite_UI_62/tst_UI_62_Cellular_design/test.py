######################
#Author: Alex Leung ##
######################

from API.Utility import UtilConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.CellTower.CellTower import CellTower
from API.Device.COServer.COServer import COServer
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbar import GoldenPhysicalToolbar
from API.SimulationPanel.EventList.EventList import EventList
from API.SimulationPanel.PlayControls.PlayControls import PlayControls
from API.functions import check
from API.Workspace.Physical import Physical
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst

#function initialization
util = Util()
pda0 = PC(ComponentBoxConst.DeviceModel.PDA, 200, 100, "Pda0")
pda1 = PC(ComponentBoxConst.DeviceModel.PDA, 200, 200, "Pda1")
ct = CellTower(ComponentBoxConst.DeviceModel.CELL_TOWER, 100, 100, "Cell Tower0")
cos = COServer(ComponentBoxConst.DeviceModel.CO_SERVER, 100, 200, "Central OfficeServer0")
gpt = GoldenPhysicalToolbar()
gptc = GoldenPhysicalToolbarConst()


def main():
    util.init()
    maketop()
    checksettings()
    movephysical()

def maketop():
    pda0.create()
    pda1.create()
    ct.create()
    cos.create()
    ct.connect(cos, ComponentBoxConst.Connection.CONN_COAXIAL, "Coaxial0", "Coaxial0/0")
    util.speedUpConvergence()
    
def checksettings():
    ct.select()
    ct.clickConfigTab()
    ct.close()
    
    cos.select()
    cos.clickConfigTab()
    cos.config.selectInterface('Cell Tower')
    cos.config.interface.cellTower.check.ip("172.16.1.1")
    cos.config.interface.cellTower.check.subnet('255.255.255.0')
    cos.config.interface.cellTower.check.ipv6("2001::1")
    cos.config.interface.cellTower.check.subnetv6("64")
    cos.config.interface.cellTower.check.linkLocal("FE80::[A-F\d]{1,4}:[A-F\d]{1,4}:[A-F\d]{1,4}:[A-F\d]{1,4}")
    
    cos.clickServicesTab()
    cos.services.selectInterface('DHCP')
    cos.services.dhcp.check.ip("172.16.1.1")
    cos.services.dhcp.check.subnet("255.255.255.0")
    cos.services.dhcp.check.startIp1("172")
    cos.services.dhcp.check.startIp2('16')
    cos.services.dhcp.check.startIp3('1')
    cos.services.dhcp.check.startIp4('100')
    cos.services.dhcp.check.maxUsers('50')
    
    cos.services.selectInterface('DHCPv6')
    #cos.services.dhcpv6.on()
    cos.services.dhcpv6.check.on(True)
    test.compare(findObject(cos.squishName + ServicesConst.dhcpv6.PREFIX_TABLE).rowCount, 1)
    test.compare(findObject(cos.squishName + ServicesConst.dhcpv6.LOCAL_TABLE).rowCount, 1)
    
    cos.services.selectInterface("CELL TOWER")
    test.compare(findObject(cos.squishName + ServicesConst.cellTower.CELL_TOWER_LIST).rowCount, 1)
    cos.services.cellTower.refreshButton()
    test.compare(findObject(cos.squishName + ServicesConst.cellTower.CELL_TOWER_LIST).rowCount, 1)
    cos.services.cellTower.clickItem("0/0")
    test.compare(findObject(cos.squishName + ServicesConst.cellTower.CELL_DEVICE_LIST).rowCount, 2)
    cos.services.selectInterface("PAP/CHAP")
    cos.close()
    
def movephysical():
    util.clickOnPhysical()
    gpt.clickButton(gptc.NAVIGATION)
    gpt.clickItem(gptc.NAVIGATION_LIST, "Intercity_1.Home City.Corporate Office.Smartphone0")
    gpt.clickButton(gptc.JUMP_TO_SELECTED_LOCATION)
    # gpt.scrollTo(gptc.RACK_VIEW_V_SCROLL_BAR, 409)
    # gpt.scrollTo(gptc.RACK_VIEW_V_SCROLL_BAR, 818)
    gpt.clickButton(gptc.MOVE_OBJECT)
    util.clickOnPhysicalWorkspace(172, 215)
    #mouseClick(waitForObject(gptc.TABLE1_DEVICE1), 39, 848, 0, Qt.LeftButton)
    #sendEvent("QMouseEvent", waitForObject(gptc.TABLE1_DEVICE1), QEvent.MouseButtonRelease, 38, 95, Qt.LeftButton, 0, 0)
    activateItem(waitForObjectItem(gptc.MOVE_DROPDOWN, "Move to Intercity"))
    snooze(5)
    #gpt.clickButton(gptc.NAVIGATION)
    gpt.clickItem(gptc.NAVIGATION_LIST, "Intercity_1")
    gpt.clickButton(gptc.JUMP_TO_SELECTED_LOCATION)
    smartphone = Physical().getObject('Smartphone0')
    util.dragAndDrop(smartphone, 10, 10, UtilConst.PHYSICAL_WORKSPACE, 500, 300)
    util.clickOnLogical()
    pda0.select()
    pda0.clickDesktopTab()
    pda0.desktop.applications.commandPrompt()
    pda0.desktop.commandPrompt.setText("ping 172.16.1.1")
    util.fastForwardTime()
    pda0.desktop.commandPrompt.textCheckPoint("Received = 0", 1)
    #checkpoint phone outside range
    #checkpoint phone not getting reception
    pda0.close()
    
    util.clickOnPhysical()
    smartphone = Physical().getObject('Smartphone0')
    util.dragAndDrop(smartphone, 10, 10, UtilConst.PHYSICAL_WORKSPACE, 200, 200)
    util.clickOnLogical()
    
    util.clickOnSimulation()    
    pda0.select()
    pda0.clickTab('Desktop')
    pda0.desktop.applications.commandPrompt()
    pda0.desktop.commandPrompt.setText('ping 172.16.255.255')
    PlayControls().captureForward(10)
    
    foundEvent = []
    foundEvent.append(EventList().findEventAt('Smartphone0', 'Cell Tower0', 'ICMP'))
    foundEvent.append(EventList().findEventAt('Smartphone1', 'Cell Tower0', 'ICMP'))
    foundEvent.append(EventList().findEventAt('Central Office Server0', 'Cell Tower0', 'ICMP'))
    
    check(not False in foundEvent)    
