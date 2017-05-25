from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Utility.Util import Util
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar

common = CommonToolsBar()
util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 200, 200, "PC0")


def main():
    util.init()
    createTopology()
    checkpoint()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, pc0.model, pc0.x, pc0.y)

def checkpoint():
    #Check that the table is empty
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.pcWireless()
    pc0.desktop.pcWireless.tabs.connect()
    util.fastForwardTime()
    snooze(5)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.connectTab.NETWORK_TABLE).rowCount, 0)

