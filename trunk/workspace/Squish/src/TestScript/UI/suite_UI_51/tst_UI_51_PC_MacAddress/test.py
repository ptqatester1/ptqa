from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util
from API.Utility import UtilConst
from API import functions

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")

def main():
    util.init()
    createTopology()
    checkpoint()

def createTopology():
    pc0.create()

def checkpoint():
    pc0.select()
    pc0.clickConfigTab()
    pc0.config.selectInterface("FastEthernet0")
    pc0.config.interface.wired.mac("1212.1212.1212")
    pc0.config.interface.wired.check.mac("1212.1212.1212")
    pc0.config.interface.wired.mac("0000.0000.0000")
    pc0.config.interface.wired.mac("<Tab>")
    snooze(1)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Invalid MAC address entered")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    pc0.config.interface.wired.mac("0122.1212.1212")
    pc0.config.interface.wired.mac("<Tab>")
    snooze(1)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Invalid MAC address entered")