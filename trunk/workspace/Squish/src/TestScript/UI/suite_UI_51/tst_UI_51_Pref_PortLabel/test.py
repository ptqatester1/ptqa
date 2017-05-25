from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router
from API.Utility.Util import Util
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst

util = Util()
options = Options()

r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 100, 200, "Router0")
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 100, 300, "Router1")

def main():
    util.init()
    createTopology()
    editOptionsSetting()
    checkpoint1()
    editOptionsSetting()
    checkpoint2()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r1.model, r1.x, r1.y)
    util.connect(r1.x, r1.y, r0.x, r0.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickButton(InterfaceConst.ALWAYS_SHOW_PORT_LABEL)
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def checkpoint1():
    None
    
def checkpoint2():
    None