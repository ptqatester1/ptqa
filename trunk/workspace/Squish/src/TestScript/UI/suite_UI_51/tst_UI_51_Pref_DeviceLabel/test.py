from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst

util = Util()
options = Options()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    editOptionsSetting()
    checkpoint2()
    editOptionsSetting()

def createTopology():
    pc0.create()
    
def checkpoint1():
    None

def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickButton(InterfaceConst.SHOW_DEVICE_NAME_LABEL)
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def checkpoint2():
    None