########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.PC.PC import PC

from API.ComponentBox import ComponentBoxConst
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbar import GoldenPhysicalToolbar
from API.Workspace.Physical import Physical, Closet

#Function initialization
util = Util()
goldenToolbar = GoldenPhysicalToolbar()

#Device initialization
admin = PC(ComponentBoxConst.DeviceModel.PC, 70, 347, 'Admin')
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 359, 74, 'PC0')
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 483, 78, 'PC1')

hqOfficeX = 77 
hqOfficeY = 145
hqOffice = ":HQ Office_QGraphicsItem"
ispBuildingX = 83
ispBuildingY = 311
ispBuilding = ":ISP Building_QGraphicsItem"
frameRelayX = 203
frameRelayY = 84
frameRelay = ":Frame Relay ISP_QGraphicsItem"
wiringClosetX = 413
wiringClosetY = 254
wiringCloset = ":Wiring Closet_QGraphicsItem"
ciscoIp = "209.165.202.134"
newBPcIp = "10.4.5.11"
wpksIp = "10.0.1.2"
pc0Ip = "1.1.1.1"
pc1Ip = "1.1.1.2"

def main():
    util.init()
    connectDevices()
    checkConnectivity()
    connectWrongPorts()
    checkDisconnection()

def connectDevices():
    util.open("PhysicalWorkspace_AddRemoveConnections.pkt", UtilConst.UI_TEST)  
    util.clickOnPhysical()

    util.connectOnPhysical(pc0.x, pc0.y, pc1.x, pc1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    hqOffice = Physical().getObject('HQ Office')
    util.connectOnPhysical(hqOffice.x, hqOffice.y, hqOffice.x, hqOffice.y, ComponentBoxConst.Connection.CONN_SERIAL_DCE, "Serial0/0/1", "Serial0/0/0", "Wiring Closet/Rack/HQ", "Wiring Closet/Rack/NewB")
    hqOffice = Physical().getObject('HQ Office')
    ispBuilding = Physical().getObject('ISP Building')
    util.connectOnPhysical(ispBuilding.x, ispBuilding.y, hqOffice.x, hqOffice.y, ComponentBoxConst.Connection.CONN_SERIAL_DCE, "Serial0/0/0", "Serial0/1/0", "ISP Wiring Closet/Rack/ISP", "Wiring Closet/Rack/HQ")
    hqOffice = Physical().getObject('HQ Office')
    frameRelay = Physical().getObject('Frame Relay ISP')
    util.connectOnPhysical(frameRelay.x, frameRelay.y, hqOffice.x, hqOffice.y, ComponentBoxConst.Connection.CONN_SERIAL_DCE, "Serial0", "Serial0/0/0", "Frame Relay ISP Wiring Closet/Rack/Frame Relay", "Wiring Closet/Rack/HQ")
    hqOffice = Physical().getObject('HQ Office')
    frameRelay = Physical().getObject('Frame Relay ISP')
    util.connectOnPhysical(frameRelay.x, frameRelay.y, hqOffice.x, hqOffice.y, ComponentBoxConst.Connection.CONN_SERIAL_DCE, "Serial1", "Serial0/0/0", "Frame Relay ISP Wiring Closet/Rack/Frame Relay", "Wiring Closet/Rack/B1")
    util.speedUpConvergence()

def checkConnectivity():
    util.clickOnPhysicalWorkspace(pc0.x, pc0.y)
    pc0.updateName()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping " + pc1Ip)
    util.fastForwardTime()
    snooze(2)
    pc0.desktop.commandPrompt.textCheckPoint("Received = [1234]")
    pc0.close()
    
    util.clickOnLogical()
    
    util.clickOnWorkspace(admin.x, admin.y)
    admin.updateName()
    admin.clickDesktopTab()
    admin.desktop.applications.commandPrompt()
    
    pingList = [ciscoIp, newBPcIp, wpksIp]
    for i,ip in enumerate(pingList):
        admin.desktop.commandPrompt.setText("ping " + ip)
        util.fastForwardTime()
        snooze(2)
        admin.desktop.commandPrompt.textCheckPoint("Received = [1234]", i+1)
    admin.close()

def connectWrongPorts():
    util.clickOnPhysical()
    util.clickButton(GoldenPhysicalToolbarConst.MOVE_OBJECT)
    util.clickOnPhysicalWorkspace(pc0.x, pc0.y)
    util.activateItem(GoldenPhysicalToolbarConst.MOVE_DROPDOWN, "HQ Office")
    snooze(1)
    util.activateItem(GoldenPhysicalToolbarConst.MOVE_DROPDOWN + ".HQ Office", "Move to Wiring Closet")
    Physical().goTo('HQ Office', 'Wiring Closet')
    util.maximizePT()
    util.clickButton(MainToolbarConst.ZOOM_OUT)     
    util.dragAndDrop(GoldenPhysicalToolbarConst.RACK_BASE + "1.CPhysicalCable6", 3, 3, GoldenPhysicalToolbarConst.RACK_BASE + "1.CModuleContainer3", 117, 29)
    #Drag the PC cable to the switch
    dragAndDrop(waitForObject(":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CRackView1.qt_scrollarea_viewport.CRackViewWidget1.Table Object.QWidget2.QWidget1.CModuleContainer1.CPhysicalCable1"), 1, 4, ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CRackView1.qt_scrollarea_viewport.CRackViewWidget1.QWidget1.CModuleContainer8.CModuleTarget18", 3, 1, Qt.CopyAction)
    #util.dragAndDrop(GoldenPhysicalToolbarConst.TABLE_BASE_1 + "2.QWidget1.CModuleContainer1.CPhysicalCable1", 3, 3, GoldenPhysicalToolbarConst.RACK_BASE + "1.CModuleContainer8.CModuleTarget23", 0, 1)
    util.speedUpConvergence()
        
def checkDisconnection():
    util.restoreWindow()
    util.clickButton(GoldenPhysicalToolbarConst.GO_TO_BUILDING)
    util.clickButton(GoldenPhysicalToolbarConst.GO_TO_INTERCITY)

    util.clickOnPhysicalWorkspace(pc1.x, pc1.y)
    pc1.updateName()
    pc1.clickDesktopTab()
    pc1.desktop.applications.commandPrompt()
    pc1.desktop.commandPrompt.setText("ping " + pc0Ip)
    util.fastForwardTime()
    snooze(10)
    pc1.desktop.commandPrompt.textCheckPoint("Received = [1234]", 0)
    pc1.close()
    
    util.clickOnLogical()
        
    util.clickOnWorkspace(admin.x, admin.y)
    admin.updateName()
    admin.clickDesktopTab()
    admin.desktop.applications.commandPrompt()
    
    pingList = [ciscoIp, newBPcIp, wpksIp]
    for i,ip in enumerate(pingList):
        admin.desktop.commandPrompt.setText("ping " + ip)
        util.fastForwardTime()
        snooze(10)
        admin.desktop.commandPrompt.textCheckPoint("Received = [1234]", 3)
    admin.close()
    
    
