from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Toolbar.GoldenRealtimeToolbar.GoldenRealtimeToolbar import GoldenRealtimeToolbar
from API.Toolbar.GoldenRealtimeToolbar.GoldenRealtimeToolbarConst import GoldenRealtimeToolbarConst

from API.Device.EndDevice.PC.PC import PC
from API.ComponentBox import ComponentBoxConst

util = Util()
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 87, 102, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 172, 89, "PC1")
pc2 = PC(ComponentBoxConst.DeviceModel.PC, 258, 93, "PC2")
pc3 = PC(ComponentBoxConst.DeviceModel.PC, 340, 94, "PC3")

def main():
    util.init()
    util.open("UI4_PowerCycleDevice.pkt", UtilConst.UI_TEST)
    util.speedUpConvergence()
    pc0.select()
    pc0.clickConfigTab()
    pc0.config.selectInterface("FastEthernet0")
    pc0.config.interface.wired.check.ip("192.168.1.33")
    
    pc1.select()
    pc1.clickConfigTab()
    pc1.config.selectInterface("FastEthernet0")
    pc1.config.interface.wired.check.ip("192.168.1.34")
    
    pc2.select()
    pc2.clickConfigTab()
    pc2.config.selectInterface("FastEthernet0")
    pc2.config.interface.wired.check.ip("192.168.1.249")
    
    pc3.select()
    pc3.clickConfigTab()
    pc3.config.selectInterface("FastEthernet0")
    pc3.config.interface.wired.check.ip("192.168.1.250")

    GoldenRealtimeToolbar().powerCycleDevice(True)
    util.speedUpConvergence()
    
    pc0.select()
    pc0.clickConfigTab()
    pc0.config.selectInterface("FastEthernet0")
    snooze(2)
    pc0.config.interface.wired.check.ip("192.168.1.33")
    
    pc1.select()
    pc1.clickConfigTab()
    pc1.config.selectInterface("FastEthernet0")
    pc1.config.interface.wired.check.ip("192.168.1.34")
    
    pc2.select()
    pc2.clickConfigTab()
    pc2.config.selectInterface("FastEthernet0")
    pc2.config.interface.wired.check.ip("192.168.1.249")
    
    pc3.select()
    pc3.clickConfigTab()
    pc3.config.selectInterface("FastEthernet0")
    pc3.config.interface.wired.check.ip("192.168.1.250")
    
    GoldenRealtimeToolbar().powerCycleDevice(True)
    util.speedUpConvergence()

    pc0.select()
    pc0.clickConfigTab()
    pc0.config.selectInterface("FastEthernet0")
    pc0.config.interface.wired.check.ip("192.168.1.33")
    
    pc1.select()
    pc1.clickConfigTab()
    pc1.config.selectInterface("FastEthernet0")
    pc1.config.interface.wired.check.ip("192.168.1.34")
    
    pc2.select()
    pc2.clickConfigTab()
    pc2.config.selectInterface("FastEthernet0")
    pc2.config.interface.wired.check.ip("192.168.1.249")
    
    pc3.select()
    pc3.clickConfigTab()
    pc3.config.selectInterface("FastEthernet0")
    pc3.config.interface.wired.check.ip("192.168.1.250")