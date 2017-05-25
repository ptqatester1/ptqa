##Chris Allen
##Sanity check to make sure that all the options tabs are there and functioning

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.PreferencesConst import PreferencesConst as pConst
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst as iConst
from API.MenuBar.Options.Preferences.Administrative.AdministrativeConst import AdministrativeConst as aConst

import os

util = Util()
opt = Options()

adminCheckBoxList = [aConst.INTERFACE_TAB, aConst.HIDE_TAB, aConst.CUSTOM_INTERFACES_TAB, aConst.MULTIUSER_MENU,
                     aConst.IPC_MENU, aConst.SCRIPTING_MENU, aConst.MISC_TAB]

def main():
    util.init()
    openPreferences()
    checkAdministrativeTabButtons()
    
def cleanup():
    resetDefaults()
    test.log("Cleanup Finished")
    
def openPreferences():
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    
def checkAdministrativeTabButtons():
    util.clickTab(pConst.TAB_BAR, pConst.ADMINISTRAVTIVE)
    for item in adminCheckBoxList:
        util.clickButton(item)
    
    util.setText(aConst.PASSWORD_EDIT, "password")
    util.setText(aConst.CONFIRM_EDIT, "password")
    util.clickButton(aConst.ENABLE_PASSWORD_BUTTON)
    util.close(OptionsConst.PREFERENCES_WINDOW)
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(pConst.TAB_BAR, pConst.ADMINISTRAVTIVE)
    if(object.exists(aConst.PASSWORD_DIALOG)):
        util.setText(aConst.PASSWORD_DIALOG, "password")
        util.clickButton(aConst.PASSWORD_DIALOG_OK)
        test.passes("Password was enabled")
    else:
        test.fail("The password is not enabled")
    util.clickButton(aConst.DISABLE_PASSWORD_BUTTON)
    if(findObject(aConst.PASSWORD_EDIT).text == "" and findObject(aConst.CONFIRM_EDIT).text == ""):
        test.passes("The password is now disabled")
    else:
        test.fail("Password did not get disabled")
        
    util.clickButton(aConst.WRITE_BUTTON)
    if(object.exists(aConst.WRITE_SUCCESSFUL_DIALOG)):
        util.clickButton(aConst.WRITE_SUCCESSFUL_DIALOG_OK)
        test.passes("Write button works")
    else:
        test.fail("Write does not work")
    None
    
def resetDefaults():
    util.clickTab(pConst.TAB_BAR, pConst.ADMINISTRAVTIVE)
    for item in adminCheckBoxList:
        if(findObject(item).checked):
            util.clickButton(item)
    util.clickButton(aConst.DISABLE_PASSWORD_BUTTON)
    util.clickButton(aConst.WRITE_BUTTON)
    util.clickButton(aConst.WRITE_SUCCESSFUL_DIALOG_OK)
    util.close(OptionsConst.PREFERENCES_WINDOW)