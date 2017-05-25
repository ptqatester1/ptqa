from API.ComponentBox import ComponentBoxConst

from API.Device.Switch.Switch import Switch
from API.Device.Router.Router import Router

from API.Device.Bridge.Bridge import Bridge
from API.Utility.Util import Util
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Physical.test import createTopology

#Function initialization
util = Util()

#Device initialization
Switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 200, "Switch0")
Switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 200, 200, "Switch1")
Switch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 300, 200, "Switch2")
Switch3 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 400, 200, "Multilayer Switch0")
Switch4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 500, 200, "Switch3")
Switch5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 600, 200, "Switch4")
bridge0 = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 700, 200, "Bridge0")

switches = [Switch0, Switch1, Switch2, Switch3, Switch4, Switch5] 

def main():
    util.init()
    createTopology()
    addVlan()
    removeVlan()

def addVlan():
    for switch in switches:
        switch.select()
        switch.clickConfigTab()
        switch.config.selectInterface('VLAN Database')
        switch.config.vlan.addVlan("SwitchCopy", "100")
        switch.cli.textCheckPoint("name SwitchCopy")
        switch.cli.textCheckPoint("vlan 100")
        switch.close()

def removeVlan():
    for switch in switches:
        switch.select()
        switch.clickConfigTab()
        switch.config.selectInterface('VLAN Database')
        switch.config.vlan.removeVlanNumber('100')
        switch.cli.textCheckPoint("no vlan 100")
        switch.close()