#######################
#@author: Pamela Vinco
#######################

from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Options import Options
from API.Utility.Util import Util

#Function initialization
util = Util()
optionsMenu = Options()

def main():
    util.init()
    options_preferences()
    options_userProfile()
    options_algorithmSettings()
    options_viewCommandLog()
    
def options_preferences():
    #Select Preferences from Options Menu and check that the Preferences Window appears
    optionsMenu.selectOptionsItem(OptionsConst.PREFERENCES)
    snooze(1)
    if (object.exists(OptionsConst.PREFERENCES_DIALOG)):
        test.passes("Preferences Window found")
        util.close(OptionsConst.PREFERENCES_DIALOG)
    else:
        test.fail("Preferences Window not found")
        
def options_userProfile():
    #Select User Profile from Options Menu and check that the User Profile Window appears
    optionsMenu.selectOptionsItem(OptionsConst.USER_PROFILE)
    snooze(1)
    if (object.exists(OptionsConst.USER_PROFILE_DIALOG)):
        test.passes("User Profile Window found")
        util.close(OptionsConst.USER_PROFILE_DIALOG)
    else:
        test.fail("User Profile Window not found")
    
def options_algorithmSettings():
    #Select Algorithm Settings from Options Menu and check that the Algorithm Settings Window appears
    optionsMenu.selectOptionsItem(OptionsConst.ALGORITHM_SETTINGS)
    snooze(1)
    if (object.exists(OptionsConst.ALGORITHM_SETTINGS_DIALOG)):
        test.passes("Algorithm Settings Window found")
        util.close(OptionsConst.ALGORITHM_SETTINGS_DIALOG)
    else:
        test.fail("Algorithm Settings Window not found")
    
def options_viewCommandLog():
    #Select View Command Log from Option Menu and check that the View  Window appears
    optionsMenu.selectOptionsItem(OptionsConst.VIEW_COMMAND_LOG)
    snooze(1)
    if (object.exists(OptionsConst.VIEW_COMMAND_LOG_DIALOG)):
        test.passes("Command Log Window found")
        util.close(OptionsConst.VIEW_COMMAND_LOG_DIALOG)
    else:
        test.fail("Command Log Window not found")