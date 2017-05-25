from API.ComponentBox import ComponentBoxConst

from API.Device.Switch.Switch import Switch
from API.Device.Bridge.Bridge import Bridge

from API.Utility.Util import Util
from API.Utility import UtilConst
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Physical.test import createTopology
#Function initialization
util = Util()

#Device initialization
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 200, "Switch0")
switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 200, 200, "Switch1")
switch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 300, 200, "Switch2")
switch3 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 400, 200, "Multilayer Switch0")
switch4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 500, 200, "Switch3")
switch5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 600, 200, "Switch4")
bridge0 = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 700, 200, "Bridge0")

paths = ["UI17_Switch2950_24_running-config.txt", "UI17_Switch2950T_running-config.txt", "UI17_Switch2960_running-config.txt",
         'UI17_Switch3560_running-config.txt', 'UI17_SwitchPT_running-config.txt', 'UI17_SwitchPT_Empty_running-config.txt']

def main():
    util.init()
    createTopology()
    exportRunningConfig()
    mergeConfig()
    
def exportRunningConfig():
    for i, switch in enumerate([switch0, switch1, switch2, switch3, switch4, switch5]):
        switch.select()
        switch.clickConfigTab()
        switch.config.settings.hostname('newName')
        switch.config.settings.exportRunningConfigButton()
        switch.config.settings.fileDialog.cancelButton()
        switch.config.settings.exportRunningConfig(util.getFilePath(paths[i], UtilConst.UI_TEST))
        
        switch.clickCliTab()
        switch.cli.setCliText("end")
        switch.cli.setCliText("show running-config")
        
        switch.cli.textCheckPoint("hostname newName", start='show running-config')
        switch.cli.setCliText(" ")
        switch.cli.setCliText(" ")
        switch.cli.setCliText(" ")
        switch.cli.setCliText(" ")
        switch.close()
        
def mergeConfig():
    for i, switch in enumerate([switch0, switch1, switch2, switch3, switch4, switch5]):
        switch.select()
        switch.cli.setCliText("conf t")
        switch.cli.setCliText("hostname Test")
        switch.cli.setCliText("end")
        switch.cli.setCliText("show run")
        switch.cli.textCheckPoint("hostname Test", start='show run')
        switch.cli.setCliText(" ")
        switch.cli.setCliText(" ")
        switch.cli.setCliText(" ")
        switch.cli.setCliText(" ")
        switch.clickConfigTab()
        switch.config.settings.mergeButton()
        switch.config.settings.fileDialog.cancelButton()
        switch.config.settings.mergeRunningConfig(util.getFilePath(paths[i], UtilConst.UI_TEST))
        
        switch.clickCliTab()
        switch.cli.setCliText("show run")
        switch.cli.textCheckPoint("hostname newName", start='show run')
        switch.close()