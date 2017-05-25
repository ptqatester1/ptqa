from API.MenuBar.File.File import File
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.Switch.Switch import Switch
from API.Utility import UtilConst
from API.Device.Bridge.Bridge import Bridge
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar

util = Util()
editMenu = Edit()
commonToolsBar = CommonToolsBar()
fileMenu = File()
 
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

switches = [Switch0, Switch1, Switch2, Switch3, Switch4, Switch5]
copySwitches = [CopySwitch0, CopySwitch1, CopySwitch2, CopySwitch3, CopySwitch4, CopySwitch5]

def main():
    util.init()
    createTopology()
    changeHostname()
    copyPaste_deviceOnWorkspace()
    checkpoint()

def createTopology():
    for sw in switches + [Bridge0]:
        sw.create()
    util.fastForwardTime()
    
def changeHostname():
    for sw in switches:
        sw.select()
        sw.clickConfigTab()
        sw.config.settings.hostname("SwitchCopy")
        sw.config.selectInterface('VLAN Database')
        sw.config.vlan.addVlan("SwitchCopy", "100")
        sw.close()
    
def copyPaste_deviceOnWorkspace():
    util.selectObjectsOnWorkspace(Switch0.x, Switch0.y)
    util.selectObjectsOnWorkspace(Switch1.x, Switch1.y)
    util.selectObjectsOnWorkspace(Switch2.x, Switch2.y)
    util.selectObjectsOnWorkspace(Switch3.x, Switch3.y)
    util.selectObjectsOnWorkspace(Switch4.x, Switch4.y)
    util.selectObjectsOnWorkspace(Switch5.x, Switch5.y)
    util.selectObjectsOnWorkspace(Bridge0.x, Bridge0.y)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+C>")
    snooze(1)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+V>")
    
def checkpoint():
    for i, sw in enumerate(copySwitches):
        sw.select()
        sw.clickConfigTab()
        sw.config.settings.check.hostname("SwitchCopy")
        if sw is CopySwitch5:
            sw.config.settings.check.displayName('CopyMultilayer Switch0')
        else:
            sw.config.settings.check.displayName("CopySwitch%s"%(i,))
        sw.config.selectInterface('VLAN Database')
        sw.config.vlan.removeVlanNumber('100')
        sw.cli.textCheckPoint("no vlan 100")
        sw.close()

    CopyBridge0.select()
    CopyBridge0.clickConfigTab()
    CopyBridge0.config.settings.check.displayName("CopyBridge0")