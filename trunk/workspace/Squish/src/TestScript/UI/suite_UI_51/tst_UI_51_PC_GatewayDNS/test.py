from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util
from API.Utility import UtilConst

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
    pc0.config.settings.static()
    pc0.config.settings.dns("2.1.1.1")
    pc0.config.settings.gateway("1.1.1.1")
    pc0.config.settings.check.dns("2.1.1.1")
    pc0.config.settings.gateway("1.1.1.1")
    pc0.config.settings.gateway("0.0")
    pc0.config.settings.gateway("<Tab>")
    snooze(1)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Invalid gateway address entered.")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    pc0.config.settings.dns("0.0")
    pc0.config.settings.dns("<Tab>")
    snooze(1)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Invalid DNS entered")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    