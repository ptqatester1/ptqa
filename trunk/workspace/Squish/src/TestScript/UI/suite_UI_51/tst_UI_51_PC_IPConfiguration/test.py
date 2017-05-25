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
    pc0.config.selectInterface("FastEthernet0")
    pc0.config.interface.wired.dhcp()
    snooze(2)
    pc0.config.interface.wired.check.ip(None, property='enabled', value=False)
    pc0.config.interface.wired.check.subnet(None, property='enabled', value=False)
    pc0.config.interface.wired.static()
    pc0.config.interface.wired.check.ip(None, property='enabled', value=True)
    pc0.config.interface.wired.check.subnet(None, property='enabled', value=True)
    pc0.config.interface.wired.ip("1.1.1.1")
    pc0.config.interface.wired.subnet('255.0.0.0')
    pc0.config.interface.wired.check.ip("1.1.1.1")
    pc0.config.interface.wired.check.subnet("255.0.0.0")
    pc0.config.interface.wired.ip("<Del>")
    pc0.config.interface.wired.subnet("<Del>")
    pc0.config.interface.wired.check.ip('')
    pc0.config.interface.wired.check.subnet('')
    pc0.config.interface.wired.ip("0.0.0")
    pc0.config.interface.wired.ip("<Tab>")  
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "invalid IP address")    
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    
    pc0.select()
    pc0.config.interface.wired.ip("1.1.1.1")
    pc0.config.interface.wired.subnet("0.0.0.0")
    pc0.config.interface.wired.subnet("<Tab>")
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Invalid subnet address entered.")