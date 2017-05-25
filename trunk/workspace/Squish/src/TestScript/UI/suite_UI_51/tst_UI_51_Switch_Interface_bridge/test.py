from API.ComponentBox import ComponentBoxConst
from API.Device.Bridge.Bridge import Bridge

from API.Utility.Util import Util
#Function initialization
util = Util()

bridge0 = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 700, 200, "Bridge0")
def main():
    util.init()
    createTopology()
    bridge_PT()
    
def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, bridge0.model, bridge0.x, bridge0.y)
    util.fastForwardTime()

def bridge_PT():
    util.clickOnWorkspace(bridge0.x, bridge0.y)
    bridge0.updateName()  
    bridge0.clickConfigTab()
    bridge0.config.selectInterface("Ethernet0/1")
    checkPortStatus(bridge0)
    checkBandwidth(bridge0)
    checkDuplex(bridge0)
    bridge0.config.selectInterface("Ethernet1/1")
    checkPortStatus(bridge0)
    checkBandwidth(bridge0)
    checkDuplex(bridge0)
    bridge0.close()
    checkPoint()

def checkPortStatus(device):
    device.config.interface.wired.portStatus()

def checkBandwidth(device):
    bridge0.config.interface.wired.bandwidth('10')

def checkDuplex(device):
    bridge0.config.interface.wired.duplex('half')

def checkPoint():
    util.clickOnWorkspace(bridge0.x, bridge0.y)
    bridge0.updateName()  
    bridge0.clickConfigTab()
    bridge0.config.selectInterface("Ethernet0/1")
    snooze(2)
    bridge0.config.interface.wired.check.portStatus(False)
    bridge0.config.selectInterface("Ethernet1/1")
    snooze(2)
    bridge0.config.interface.wired.check.portStatus(False)