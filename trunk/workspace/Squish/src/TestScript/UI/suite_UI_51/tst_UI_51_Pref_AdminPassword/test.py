######################
#@author: Pamela Vinco
######################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Administrative.AdministrativeConst import AdministrativeConst
from API.MenuBar.Options.Preferences.Administrative.Administrative import Administrative
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst

util = Util()
options = Options()
admin = Administrative()

def main():
    util.init()
    editOptionsSetting()
    checkpoint1()
    checkpoint2()
    resetOptionsSetting()
    checkpoint3()
    
def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    options.clickTab(AdministrativeConst.TAB_BAR, "Administrative")
    snooze(2)

    admin.enablePassword("cisco")
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def checkpoint1():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    options.clickTab(AdministrativeConst.TAB_BAR, "Administrative")
    util.clickButton(AdministrativeConst.PASSWORD_DIALOG_CANCEL)
    snooze(2)
    if (object.exists(AdministrativeConst.PASSWORD_DIALOG)):
        test.fail("Password window found")
    else:
        test.passes("Password window not found")

def checkpoint2():
    options.clickTab(AdministrativeConst.TAB_BAR, "Administrative")
    snooze(2)
    if (object.exists(AdministrativeConst.PASSWORD_DIALOG)):
        test.passes("Password window found")
    else:
        test.fail("Password window not found")
    util.setText(AdministrativeConst.PASSWORD_DIALOG, "cisco")
    util.clickButton(AdministrativeConst.PASSWORD_DIALOG_OK)

def resetOptionsSetting():
    util.clickButton(AdministrativeConst.DISABLE_PASSWORD_BUTTON)
    util.close(OptionsConst.OPTIONS_DIALOG)

def checkpoint3():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    options.clickTab(AdministrativeConst.TAB_BAR, "Administrative")
    snooze(2)
    if (object.exists(AdministrativeConst.PASSWORD_DIALOG)):
        test.fail("Password window found")
    else:
        test.passes("Password window not found")
