from API.ComponentBox import ComponentBoxConst

from API.Device.Switch.Switch import Switch
from API.Device.Router.Router import Router

from API.Device.Bridge.Bridge import Bridge

from API.Utility.Util import Util
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Physical.test import createTopology
#Function initialization
util = Util()

#Device initialization
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 200, "Switch0")
switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 200, 200, "Switch1")
switch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 300, 200, "Switch2")
switch3 = Router(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 400, 200, "Multilayer Switch0")
switch4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 500, 200, "Switch3")
switch5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 600, 200, "Switch4")
bridge0 = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 700, 200, "Bridge0")

def main():
    util.init()
    createTopology()
    eraseNVRAM()
    saveNVRAM()
          
   
def eraseNVRAM():
    for switch in [switch0, switch1, switch2, switch3, switch4, switch5]:
        switch.select()
        switch.clickConfigTab()
        
        switch.config.settings.eraseButton()
        switch.config.settings.popups.eraseStartupConfigNoButton()
        switch.cli.textCheckPoint("Erase of nvram: complete", 0)
        
        switch.config.settings.eraseNvram()
        switch.cli.textCheckPoint("Erase of nvram: complete")

     
def saveNVRAM():
    for switch in [switch0, switch1, switch2, switch3, switch4, switch5]:
        switch.select()
        switch.config.settings.saveButton()
        switch.cli.textCheckPoint("Switch#copy running-config startup-config")
        switch.cli.textCheckPoint("Destination filename \[startup-config\]?")
        switch.cli.textCheckPoint("Building configuration...")
        switch.cli.textCheckPoint("\[OK\]")
        switch.close()