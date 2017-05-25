from API.ComponentBox import ComponentBoxConst

from API.Device.Switch.Switch import Switch
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Interface_2950_24.test import checkAccess
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Interface_2950_24.test import checkBandwidth
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Interface_2950_24.test import checkDuplex
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Interface_2950_24.test import checkPortStatus
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Interface_2950_24.test import checkTrunk
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 100, 200, "Switch0")
interfaces = ["FastEthernet0/1", "FastEthernet0/2", "FastEthernet0/3", "FastEthernet0/4", "FastEthernet0/5",
              "FastEthernet0/6", "FastEthernet0/7", "FastEthernet0/8", "FastEthernet0/9", "FastEthernet0/10",
              "FastEthernet0/11", "FastEthernet0/12", "FastEthernet0/13", "FastEthernet0/14", "FastEthernet0/15",
              "FastEthernet0/1", "FastEthernet0/17", "FastEthernet0/18", "FastEthernet0/19", "FastEthernet0/20",
              "FastEthernet0/21", "FastEthernet0/22", "FastEthernet0/23", "FastEthernet0/24", "GigabitEthernet0/1", "GigabitEthernet0/2"]
def main():
    util.init()
    createTopology()
    switch_3560()
    
def createTopology():
    switch0.create()
    util.fastForwardTime()

def switch_3560():
    switch0.select()  
    switch0.clickConfigTab()
    for i in range(0, 2):
        test.log(str(i) + ' ' + interfaces[i])
        switch0.config.selectInterface(interfaces[i])
        if i == 1:
            snooze(1)
            None
        checkPortStatus(switch0, i+1)
        checkBandwidth(switch0, i+1)
        checkDuplex(switch0, i+1)
        checkTrunk(switch0, i+1)
        checkAccess(switch0, i+1)

def checkPortStatus(device, occurrence_num):
    device.config.interface.switch.portStatus()
    device.cli.textCheckPoint("Switch\(config-if\)\#shutdown", occurrence_num)
    device.config.interface.switch.portStatus()
    device.cli.textCheckPoint("Switch\(config-if\)\#no shutdown", occurrence_num)

def checkBandwidth(device, occurrence_num):
    device.config.interface.switch.bandwidth('100')
    device.cli.textCheckPoint("speed 100", lines=2)
    device.config.interface.switch.bandwidth('10')
    device.cli.textCheckPoint("speed 10", lines=2)
    device.config.interface.switch.bandwidth('Auto')
    device.cli.textCheckPoint("speed auto", lines=2)


def checkDuplex(device, occurrence_num):
    device.config.interface.switch.duplex('Half')
    device.cli.textCheckPoint("duplex half", lines=2)    
    device.config.interface.switch.duplex('Full')
    device.cli.textCheckPoint("duplex full", lines=2)
    device.config.interface.switch.duplex('Auto')   
    device.cli.textCheckPoint("duplex auto", lines=2)   

def checkAccess(device, occurrence_num):
    device.config.interface.switch.portType('Access')
    device.cli.textCheckPoint("switchport mode access", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1002', 'fddi-default')
    device.cli.textCheckPoint("switchport access vlan 1002", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1003', 'token-ring-default')
    device.cli.textCheckPoint("switchport access vlan 1003", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1004', 'fddinet-default')
    device.cli.textCheckPoint("switchport access vlan 1004", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1005', 'trnet-default')
    device.cli.textCheckPoint("switchport access vlan 1005", occurrence_num)

def checkTrunk(device, occurrence_num):
    device.config.interface.switch.portType('Trunk')
    device.cli.textCheckPoint("switchport mode trunk")
    
    device.config.interface.switch.vlanNumber('1', 'default')
    device.cli.textCheckPoint("switchport trunk allowed vlan remove 1\n", occurrence_num)

    device.config.interface.switch.vlanNumber('1', 'default')
    device.cli.textCheckPoint("switchport trunk allowed vlan add 1\n", occurrence_num)

    device.config.interface.switch.vlanNumber('1002', 'fddi-default')
    device.cli.textCheckPoint("switchport trunk allowed vlan remove 1002", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1002', 'fddi-default')
    device.cli.textCheckPoint("switchport trunk allowed vlan add 1002", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1003', 'token-ring-default')
    device.cli.textCheckPoint("switchport trunk allowed vlan remove 1003", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1003', 'token-ring-default')
    device.cli.textCheckPoint("switchport trunk allowed vlan add 1003", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1004', 'fddinet-default')
    device.cli.textCheckPoint("switchport trunk allowed vlan remove 1004", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1004', 'fddinet-default')
    device.cli.textCheckPoint("switchport trunk allowed vlan add 1004", occurrence_num)
    
    device.config.interface.switch.vlanNumber('1005', 'trnet-default')
    device.cli.textCheckPoint("switchport trunk allowed vlan remove 1005", occurrence_num)
    device.config.interface.switch.vlanNumber('1005', 'trnet-default')
    device.cli.textCheckPoint("switchport trunk allowed vlan add 1005", occurrence_num)
