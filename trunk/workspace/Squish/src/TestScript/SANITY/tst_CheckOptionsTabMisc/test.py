##Chris Allen
##Sanity check to make sure that all the options tabs are there and functioning

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.PreferencesConst import PreferencesConst as pConst
from API.MenuBar.Options.Preferences.Miscellaneous.MiscellaneousConst import MiscellaneousConst as mConst
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst

util = Util()
opt = Options()

def main():
    check()

def cleanup():
    resetDefaults()
    
def check():
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(pConst.TAB_BAR, pConst.MISCELLANEOUS)
    util.clickButton(mConst.PROMPT)
    util.clickButton(mConst.AUTO_CLEAR_EVENT_LIST)
    util.clickButton(mConst.AUTO_VIEW_PREVIOUS_EVENTS)
    util.clickButton(mConst.ENABLE_SCREEN_READER_SUPPORT)
    util.clickButton(mConst.ENABLE_SCREEN_READER_SUPPORT_OK)
    util.clickButton(mConst.DEVICE_DIALOG_TASKBAR)
    test.passes("All objects clickable")
    
def resetDefaults():
    if(object.exists(OptionsConst.PREFERENCES_WINDOW)):
        util.close(OptionsConst.PREFERENCES_WINDOW)
    util.init()
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(pConst.TAB_BAR, pConst.MISCELLANEOUS)
    util.clickButton(mConst.PROMPT)
    if(findObject(mConst.ENABLE_SCREEN_READER_SUPPORT).checked):
        util.clickButton(mConst.ENABLE_SCREEN_READER_SUPPORT)
        util.clickButton(mConst.ENABLE_SCREEN_READER_SUPPORT_OK)
    if(findObject(mConst.DEVICE_DIALOG_TASKBAR).checked):
        util.clickButton(mConst.DEVICE_DIALOG_TASKBAR)
    test.log("Cleanup Finished")