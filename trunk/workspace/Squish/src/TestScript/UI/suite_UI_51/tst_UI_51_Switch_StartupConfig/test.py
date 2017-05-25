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

paths = ["UI17_Switch_startup-config.txt", "UI17_Switch0_startup-config.txt", "UI17_Switch0_startup-config.txt",
         "UI17_Switch0_startup-config.txt", "UI17_Switch0_startup-config.txt", "UI17_Switch0_startup-config.txt"]

def main():
    util.init()
    createTopology()
    exportStartupConfig()
    loadStartUpConfig()
    
def exportStartupConfig():
    for i, switch in enumerate([switch0, switch1, switch2, switch3, switch4, switch5]):
        switch.select()
        switch.clickConfigTab()
        switch.config.settings.hostname('newName')
        
        switch.config.settings.saveButton()
        switch.config.settings.exportStartupConfigButton()
        switch.config.settings.fileDialog.cancelButton()
        switch.config.settings.exportStartupConfig(util.getFilePath(paths[i], UtilConst.UI_TEST))
        
        switch.config.settings.eraseNvram()
        
        switch.clickCliTab()
        switch.cli.setCliText("show startup-config")
        switch.cli.textCheckPoint("startup-config is not present")
        switch.close()

def loadStartUpConfig():
    for i, switch in enumerate([switch0, switch1, switch2, switch3, switch4, switch5]):
        switch.select()
        switch.clickConfigTab()
        switch.config.settings.loadButton()
        switch.config.settings.fileDialog.cancelButton()
        switch.config.settings.loadStartupConfig(util.getFilePath(paths[i], UtilConst.UI_TEST))

        switch.clickCliTab()
        switch.cli.setCliText("show startup-config")
        switch.cli.textCheckPoint("hostname newName", start='show startup-config')
        switch.close()