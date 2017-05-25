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
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 100, 200, "Switch0")
interfaces = ["FastEthernet0/1", "FastEthernet0/2", "FastEthernet0/3", "FastEthernet0/4", "FastEthernet0/5",
              "FastEthernet0/6", "FastEthernet0/7", "FastEthernet0/8", "FastEthernet0/9", "FastEthernet0/10",
              "FastEthernet0/11", "FastEthernet0/12", "FastEthernet0/13", "FastEthernet0/14", "FastEthernet0/15",
              "FastEthernet0/1", "FastEthernet0/17", "FastEthernet0/18", "FastEthernet0/19", "FastEthernet0/20",
              "FastEthernet0/21", "FastEthernet0/22", "FastEthernet0/23", "FastEthernet0/24", "GigabitEthernet1/1", "GigabitEthernet1/2"]
def main():
    util.init()
    createTopology()
    switch_2950T()
def createTopology():
    switch0.create()
    util.clickOnSimulation()
    util.clickOnRealtime()

def switch_2950T():
    switch0.select()  
    switch0.clickConfigTab()
    for i in range(0, 3):
        switch0.config.selectInterface(interfaces[i])
        snooze(2)
        checkPortStatus(switch0, i+1)
        checkBandwidth(switch0, i+1)
        checkDuplex(switch0, i+1)
        checkTrunk(switch0, i+1)
        checkAccess(switch0, i+1)

