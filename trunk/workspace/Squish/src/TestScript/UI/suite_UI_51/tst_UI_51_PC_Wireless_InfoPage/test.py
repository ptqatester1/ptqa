from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Utility.Util import Util
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar

common = CommonToolsBar()
util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 200, 200, "PC0")
linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 300, 200, "Wireless Router0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    checkpoint2()

def createTopology():
    pc0.create()
    linksys.create()
    util.fastForwardTime()

def checkpoint1():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.pcWireless()
    snooze(5)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.ASSOCIATION_FRAME).visible, True)
    pc0.desktop.pcWireless.linkInformation.moreInformationButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.linkInformationTab.LINK_WIRELESS_NETWORK_STATUS_PAGE).visible, True)
    pc0.desktop.pcWireless.linkInformation.statisticsButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.linkInformationTab.LINK_WIRELESS_NETWORK_STATISTICS_PAGE).visible, True)
    pc0.desktop.pcWireless.linkInformation.statusButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.linkInformationTab.LINK_WIRELESS_NETWORK_STATUS_PAGE).visible, True)
    pc0.desktop.pcWireless.linkInformation.backButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.ASSOCIATION_FRAME).visible, True)
    pc0.close()

def checkpoint2():
    util.clickOnWorkspace(5, 5)
    common.deleteItem(linksys.x, linksys.y)
    
    pc0.select()
    pc0.desktop.applications.pcWireless()
    snooze(5)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.NO_ASSOCIATION_FRAME).visible, True)   