from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.Switch.Switch import Switch

from API.Device.Bridge.Bridge import Bridge

from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst

util = Util()
editMenu = Edit()
commonToolsBar = CommonToolsBar() 

#first row
CopySwitch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 100, 50, "CopySwitch0")
CopySwitch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 200, 50, "CopySwitch1")
CopySwitch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 300, 50, "CopySwitch2")
CopySwitch3 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 400, 50, "CopySwitch3")
CopySwitch4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 500,  50, "CopySwitch4")
CopySwitch5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 600, 50, "CopyMultiLayer Switch0")
CopyBridge0 = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 700, 50, "CopyBridge0")

Switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 100, 100 , "Switch0")
Switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 200, 100 , "Switch1")
Switch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 300, 100 , "Switch2")
Switch3 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 400, 100 , "Switch3")
Switch4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 500, 100 , "Switch4")
Switch5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 600, 100 , "MultiLayer Switch0")
Bridge0 = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 700, 100, "Bridge0")

def main():
    util.init()
    copyPaste_deviceOnWorkspace()

def copyPaste_deviceOnWorkspace():
    for sw in [Switch0, Switch1, Switch2, Switch3, Switch4, Switch5, Bridge0]:
        sw.create()    
        
    util.clickOnSimulation()
    util.clickOnRealtime()
    
    for sw in [Switch0, Switch1, Switch2, Switch3, Switch4, Switch5, Bridge0]:
        sw.select()
        sw.clickConfigTab()
        if not sw is Bridge0:
            sw.config.settings.hostname("SwitchCopy")
            sw.config.selectInterface('VLAN Database')
            sw.config.vlan.addVlan("SwitchCopy", "100")
        sw.close()
        
    for sw in [Switch0, Switch1, Switch2, Switch3, Switch4, Switch5, Bridge0]:
        util.selectObjectsOnWorkspace(sw.x, sw.y)
    util.clickButton(MainToolbarConst.COPY)
    util.clickButton(MainToolbarConst.PASTE)
    
    for i, sw in enumerate([CopySwitch0, CopySwitch1, CopySwitch2, CopySwitch3, CopySwitch4, CopySwitch5, CopyBridge0]):
        sw.select()
        sw.clickConfigTab()
        if not sw is CopyBridge0:
            sw.config.settings.check.hostname("SwitchCopy")
            if sw is CopySwitch5:
                sw.config.settings.check.displayName('CopyMultilayer Switch0')
            else:
                sw.config.settings.check.displayName("CopySwitch%s"%(i,))
            sw.config.selectInterface('VLAN Database')
            sw.config.vlan.removeVlanName('SwitchCopy')
            sw.cli.textCheckPoint("no vlan 100")       
        else:
            sw.config.settings.check.displayName("CopyBridge0")
        sw.close()