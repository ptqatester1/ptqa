##Chris Allen
##Sanity check to make sure that all the options tabs are there and functioning

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.PreferencesConst import PreferencesConst as pConst
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst as iConst
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst

util = Util()
opt = Options()

tabList = [pConst.INTERFACE, pConst.ADMINISTRAVTIVE, pConst.HIDE, pConst.FONT, pConst.MISCELLANEOUS, pConst.CUSTOM_INTERFACES, pConst.PUBLISHERS]
intCheckBoxList = [iConst.SHOW_ANIMATION, iConst.PLAY_SOUND, iConst.SHOW_DEVICE_MODEL_LABEL, iConst.SHOW_DEVICE_NAME_LABEL,
                   iConst.ALWAYS_SHOW_PORT_LABEL, iConst.DISABLE_AUTO_CABLE, iConst.SHOW_LINK_LIGHTS, iConst.PLAY_TELEPHONY_SOUND,
                   iConst.SHOW_QOS_STAMPS, iConst.ENABLE_CABLE_LENGTH_EFFECTS, iConst.USE_CLI_AS_DEFAULT_TAB,
                   iConst.ENABLE_LOGGING]

r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 100, "Router1")

def main():
    util.init()
    resetDefaults()
    openPreferences()
    checkAllTabsClickable()
    checkInterfaceTabButtons()

def cleanup():
    resetDefaults()
    test.log("Cleanup Finished")
    
def openPreferences():
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    
def checkAllTabsClickable():
    for item in tabList:
        util.clickTab(pConst.TAB_BAR, item)
    None
    
def checkInterfaceTabButtons():
    util.clickTab(pConst.TAB_BAR, pConst.INTERFACE)
    for item in intCheckBoxList:
        util.clickButton(item)
    util.clickButton(iConst.ALWAYS_SHOW_PORT_LABEL)
    util.clickButton(iConst.SHOW_PORT_LABELS_ON_MOUSEOVER)
    
    util.clickButton(iConst.EXPORT_LOG_BUTTON)
    util.clickButton(iConst.EXPORT_LOG_DIALOG_CANCEL)
    
    util.clickButton(iConst.CHANGE_LANGUAGE_BUTTON)
    util.clickButton(iConst.CHANGE_LANGUAGE_OK)
    util.close(OptionsConst.PREFERENCES_WINDOW)
    
    ##Check that auto-cable does not work and CLI is the default tab
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r1.model, r1.x, r1.y)
    util.clickButton(ComponentBoxConst.DeviceType.CONNECTION)
    util.clickButton(ComponentBoxConst.Connection.CONN_AUTO)
    if(object.exists(UtilConst.AUTOCONNECT_LOCKED_MESSAGE)):
        util.clickButton(UtilConst.AUTOCONNECT_LOCKED_MESSAGE_OK)
        test.passes("The auto connect feature is disabled")
    else:
        test.fail("The auto connect feature is still active")
    r0.select()
    
    ##If the following if statement is false it will cause a script error
    if(findObject(r0.squishName + RouterConst.DeviceBaseConst.Cli.CLI_CONSOLE).visible):
        test.passes("The cli tab is default")
    else:
        test.fail("The cli tab is not default")
    None

def resetDefaults():
    if(object.exists(OptionsConst.PREFERENCES_WINDOW)):
        util.close(OptionsConst.PREFERENCES_WINDOW)
    util.init()
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(pConst.TAB_BAR, pConst.INTERFACE)
    def setChecked(p_checkBox):
        if not(findObject(p_checkBox).checked):
            util.clickButton(p_checkBox)
    def unCheck(p_checkBox):
        if(findObject(p_checkBox).checked):
            util.clickButton(p_checkBox)
    
    setChecked(iConst.SHOW_ANIMATION)
    setChecked(iConst.SHOW_DEVICE_NAME_LABEL)
    setChecked(iConst.SHOW_LINK_LIGHTS)
    setChecked(iConst.SHOW_QOS_STAMPS)
    setChecked(iConst.SHOW_PORT_LABELS_ON_MOUSEOVER)
    setChecked(iConst.ENABLE_CABLE_LENGTH_EFFECTS)
    setChecked(iConst.ENABLE_LOGGING)
    
    unCheck(iConst.PLAY_SOUND)
    unCheck(iConst.SHOW_DEVICE_MODEL_LABEL)
    unCheck(iConst.ALWAYS_SHOW_PORT_LABEL)
    unCheck(iConst.DISABLE_AUTO_CABLE)
    unCheck(iConst.PLAY_TELEPHONY_SOUND)
    unCheck(iConst.USE_CLI_AS_DEFAULT_TAB)
    
    util.close(OptionsConst.PREFERENCES_WINDOW)
    None