from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Utility.Util import Util
from API.Utility import UtilConst

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 200, 200, "PC1")
linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 300, 200, "Wireless Router0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    checkpoint2()

def createTopology():
    pc0.create()
    pc1.create()
    
def checkpoint1():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.pcWireless()
    snooze(1)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "A WMP300N or WPC300N wireless interface is required to connect.")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)

def checkpoint2():
    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.pcWireless()
    snooze(2)
    test.compare(findObject(pc1.squishName + DesktopConst.pcwireless.NO_ASSOCIATION_FRAME).visible, True)


    pc1.desktop.pcWireless.tabs.connect()
    pc1.desktop.pcWireless.connect.refreshButton()
    snooze(15)
    test.compare(findObject(pc1.squishName + DesktopConst.pcwireless.connectTab.NETWORK_TABLE).rowCount, 0)
    pc1.desktop.pcWireless.connect.connectButton()

    #pc1.desktop.pcWireless.clickButton(PCConst.Desktop.PCWireless.Connect.CONNECT_NO_ASSOCIATION_BTN)
    snooze(1)
    if object.exists(pc1.squishName + DesktopConst.pcwireless.connectTab.ERROR_SELECT_WIRELESS_NETWORK_WINDOW):
        util.textCheckPoint(pc1.squishName + DesktopConst.pcwireless.connectTab.ERROR_SELECT_WIRELESS_NETWORK_LABEL, "Select Wireless Network to proceed.")
    else:
        test.fail("Select Wireless Network window is not visible")