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
    setHostName()
    
def setHostName():
    switch0.select()
    switch0.clickConfigTab()
    switch0.config.settings.hostname("SWITCH_2950_24")
    switch0.clickCliTab()
    switch0.cli.textCheckPoint("SWITCH_2950_24\(config\)#")
    switch1.updateName()
    switch1.clickConfigTab()
    switch1.config.settings.hostname("SWITCH_2950T")
    switch1.clickCliTab()
    switch1.cli.textCheckPoint("SWITCH_2950T\(config\)#")
    util.clickOnWorkspace(switch2.x, switch2.y)
    switch2.updateName()
    switch2.clickConfigTab()
    switch2.config.settings.hostname("SWITCH_2960")
    switch2.clickCliTab()
    switch2.cli.textCheckPoint("SWITCH_2960\(config\)#")
    util.clickOnWorkspace(switch3.x, switch3.y)
    switch3.updateName()
    switch3.clickConfigTab()
    switch3.config.settings.hostname("SWITCH_3560_24PS")
    switch3.clickCliTab()
    switch3.cli.textCheckPoint("SWITCH_3560_24PS\(config\)#")
    util.clickOnWorkspace(switch4.x, switch4.y)
    switch4.updateName()
    switch4.clickConfigTab()
    switch4.config.settings.hostname("SWITCH_PT")
    switch4.clickCliTab()
    switch4.cli.textCheckPoint("SWITCH_PT\(config\)#")
    util.clickOnWorkspace(switch5.x, switch5.y)
    switch5.updateName()
    switch5.clickConfigTab()
    switch5.config.settings.hostname("SWITCH_PT_EMPTY")
    switch5.clickCliTab()
    switch5.cli.textCheckPoint("SWITCH_PT_EMPTY\(config\)#")