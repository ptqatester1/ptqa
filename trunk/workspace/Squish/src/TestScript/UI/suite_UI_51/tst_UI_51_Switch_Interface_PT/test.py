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
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 100, 200, "Switch0")
interfaces = ["FastEthernet0/1", "FastEthernet1/1", "FastEthernet2/1", "FastEthernet3/1", "FastEthernet4/1", "FastEthernet5/1"]
def main():
    util.init()
    createTopology()
    switch_PT()

def createTopology():
    switch0.create()
    util.clickOnSimulation()
    util.clickOnRealtime()

def switch_PT():
    switch0.select()  
    switch0.clickConfigTab()
    for i in range(0, len(interfaces)):
        switch0.config.selectInterface(interfaces[i])
        checkPortStatus(switch0, i+1)
        if ((interfaces[i] == "FastEthernet4/1") or (interfaces[i] == "FastEthernet5/1")):
            continue
        checkBandwidth(switch0, i+1)
        checkDuplex(switch0, i+1)
        #checkTrunk(switch0, i+1)
        #checkAccess(switch0, i+1)

