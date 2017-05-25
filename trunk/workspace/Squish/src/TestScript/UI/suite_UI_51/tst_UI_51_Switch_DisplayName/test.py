from API.ComponentBox import ComponentBoxConst

from API.Device.Switch.Switch import Switch
from API.Device.Router.Router import Router

from API.Device.Bridge.Bridge import Bridge

from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Physical.test import createTopology
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.Open.OpenConst import OpenConst
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
fileMenu = File()
def main():
    util.init()
    createTopology()
    setDisplayName()


    
def setDisplayName():
    switch0.select()
    switch0.clickConfigTab()
    switch0.config.settings.displayName("SWITCH_2950_24")
    switch0.close()
    util.clickOnWorkspace(switch0.x, switch0.y+30)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "SWITCH_2950_24")

    switch1.select()
    switch1.clickConfigTab()
    switch1.config.settings.displayName("SWITCH_2950T")
    util.clickOnWorkspace(switch1.x, switch1.y+30)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "SWITCH_2950T") 

    util.clickOnWorkspace(switch2.x, switch2.y)
    switch2.updateName()
    switch2.clickConfigTab()
    switch2.config.settings.displayName("SWITCH_2960")
    util.clickOnWorkspace(switch2.x, switch2.y+30)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "SWITCH_2960")    

    util.clickOnWorkspace(switch3.x, switch3.y)
    switch3.updateName()
    switch3.clickConfigTab()
    switch3.config.settings.displayName("SWITCH_3560_24PS")
    util.clickOnWorkspace(switch3.x, switch3.y+40)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "SWITCH_3560_24PS")

    util.clickOnWorkspace(switch4.x, switch4.y)
    switch4.updateName()
    switch4.clickConfigTab()
    switch4.config.settings.displayName("SWITCH_PT")
    util.clickOnWorkspace(switch4.x, switch4.y+30)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "SWITCH_PT")

    util.clickOnWorkspace(switch5.x, switch5.y)
    switch5.updateName()
    switch5.clickConfigTab()
    switch5.config.settings.displayName("SWITCH_PT_EMPTY")
    util.clickOnWorkspace(switch5.x, switch5.y+30)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "SWITCH_PT_EMPTY")

    util.clickOnWorkspace(bridge0.x, bridge0.y)
    bridge0.updateName()
    bridge0.clickConfigTab()
    bridge0.config.settings.displayName("BRIDGE_PT")
    util.clickOnWorkspace(bridge0.x, bridge0.y+30)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "BRIDGE_PT")

      

