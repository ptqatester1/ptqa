from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router

from API.Utility.Util import Util
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst
from API.MenuBar.Options.ViewCommandLog.ViewCommandLogConst import ViewCommandLogConst

util = Util()
options = Options()

r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 100, 200, "Router0")

def main():
    util.init()
    createTopology()
    editOptionsSetting()
    checkpoint1()
    editOptionsSetting()
    checkpoint2()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    util.clickOnSimulation()
    util.clickOnRealtime()

def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickButton(InterfaceConst.ENABLE_LOGGING)
    util.close(OptionsConst.OPTIONS_DIALOG)
    options.selectOptionsItem(OptionsConst.VIEW_COMMAND_LOG)
    
def checkpoint1():
    snooze(5)
    r0.select()
    r0.clickCliTab()
    r0.cli.startConsole()
    r0.cli.setCliText("en")
    util.clickButton(ViewCommandLogConst.COMMAND_LOG_UPDATE_BUTTON)
    snooze(2)
    test.compare(findObject(ViewCommandLogConst.COMMAND_LOG_LIST).rowCount, 0)
    
def checkpoint2():
    r0.select()
    r0.cli.setCliText("exit")
    util.clickButton(ViewCommandLogConst.COMMAND_LOG_UPDATE_BUTTON)
    snooze(2)
    test.compare(findObject(ViewCommandLogConst.COMMAND_LOG_LIST).rowCount, 1)