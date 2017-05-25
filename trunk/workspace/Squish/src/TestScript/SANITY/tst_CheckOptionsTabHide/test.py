##Chris Allen
##Sanity check to make sure that all the options tabs are there and functioning

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.PreferencesConst import PreferencesConst as pConst
from API.MenuBar.Options.Preferences.Hide.HideConst import HideConst as hConst
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst

util = Util()
opt = Options()

hideBoxList = [hConst.HIDE_PHYSICAL_TAB, hConst.HIDE_CONFIG_TAB, hConst.HIDE_CLI_TAB, hConst.HIDE_DESKTOP_TAB,
               hConst.HIDE_GUI_TAB, hConst.HIDE_GUI_TAB_WIRELESS_WIRED, hConst.HIDE_HTML_TAB_WIRELESS_WIRED]

r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")


def main():
    util.init()
    hideAll()
    check()
        
def cleanup():
    resetDefaults()
    test.log("Cleanup Finished")
    
def hideAll():
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(pConst.TAB_BAR, pConst.HIDE)
    for item in hideBoxList:
        util.clickButton(item)
    None
    
def check():
    util.close(OptionsConst.PREFERENCES_WINDOW)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    r0.select()
    if(object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        test.passes("All tabs are hidden")
    else:
        test.fail("Not all tabs are hidden")
    None
    
def resetDefaults():
    if(object.exists(OptionsConst.PREFERENCES_WINDOW)):
        util.close(OptionsConst.PREFERENCES_WINDOW)
    util.init()
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(pConst.TAB_BAR, pConst.HIDE)
    for item in hideBoxList:
        if(findObject(item).checked):
            util.clickButton(item)
    util.close(OptionsConst.PREFERENCES_WINDOW)