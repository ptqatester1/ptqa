from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 200, "PC1")

def main():
    util.init()
    createTopology()
    checkpoint()

def createTopology():
    pc0.create()
    pc1.create()
    pc0.connect(pc1, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def checkpoint():
    pc0.select()
    pc0.clickConfigTab()
    pc0.config.selectInterface("FastEthernet0")
    pc0.config.interface.wired.portStatus(None)
    pc0.config.interface.wired.check.portStatus(False)
    pc0.config.interface.wired.portStatus(None)
    pc0.config.interface.wired.check.portStatus(True)