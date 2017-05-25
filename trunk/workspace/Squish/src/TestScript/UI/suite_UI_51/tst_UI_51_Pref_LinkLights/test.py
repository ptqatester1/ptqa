from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst

util = Util()
options = Options()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 200, "PC1")

def main():
    util.init()
    createTopology()
    editOptionsSetting()
    editOptionsSetting()

def createTopology():
    pc0.create()
    pc1.create()
    pc0.connect(pc1, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickButton(InterfaceConst.SHOW_LINK_LIGHTS)
    util.close(OptionsConst.OPTIONS_DIALOG)