from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Utility.Util import Util
from API.Device.AccessPoint.AccessPoint import AccessPoint
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar

common = CommonToolsBar()
util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 100, 200, "PC0")
linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 300, 200, "Wireless Router0")
access = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 500, 200, "Access Point0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    deleteLinksys()
    changeSSID()
    deleteAccess()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, pc0.model, pc0.x, pc0.y)
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, linksys.model, linksys.x, linksys.y)
    util.fastForwardTime()
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, access.model, access.x, access.y)    

def checkpoint1():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.pcWireless()
    pc0.desktop.pcWireless.linkInformation.moreInformationButton()
    pc0.desktop.pcWireless.linkInformation.statisticsButton()
    snooze(1)
    pc0.desktop.pcWireless.linkInformation.check.transmitRate("300 Mbps")
    pc0.desktop.pcWireless.linkInformation.backButton()
    pc0.desktop.pcWireless.tabs.connect()
    snooze(5)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.connectTab.NETWORK_TABLE).rowCount, 2)
    pc0.close()
    
def deleteLinksys():
    util.clickOnWorkspace(5, 5)
    common.deleteItem(linksys.x, linksys.y)
    
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.pcWireless()
    snooze(3)
    pc0.desktop.pcWireless.linkInformation.moreInformationButton()
    pc0.desktop.pcWireless.linkInformation.statisticsButton()
    util.fastForwardTime()
    snooze(3)
    #pc0.clickButton(PCConst.Desktop.PCWireless.Link_Information.LINK_MORE_INFO_BUTT)
    #pc0.desktop.pcWireless.linkInformation.statisticsButton()
    pc0.desktop.pcWireless.linkInformation.check.transmitRate("54 Mbps") #Bug 15606
    pc0.desktop.pcWireless.linkInformation.backButton()
    pc0.desktop.pcWireless.tabs.connect()
    snooze(5)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.connectTab.NETWORK_TABLE).rowCount, 1)
    pc0.close()
    
def changeSSID():
    access.select()
    access.clickConfigTab()
    access.config.selectInterface("Port 1")
    access.config.interface.port1.ssid("Test")
    access.close()
    
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.pcWireless()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.NO_ASSOCIATION_FRAME).visible, True)
    pc0.close()
    
def deleteAccess():
    util.clickOnWorkspace(5, 5)
    common.deleteItem(access.x, access.y)
    
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.pcWireless()
    pc0.desktop.pcWireless.tabs.connect()
    util.fastForwardTime()
    snooze(5)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.connectTab.NETWORK_TABLE).rowCount, 0)
    pc0.close()