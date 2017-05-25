from API.Utility.Util import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.UserProfile.UserProfileConst import UserProfileConst
from API.MenuBar.File.File import File
from API.MenuBar.Options.UserProfile.UserProfile import UserProfile
from API.Utility.Util import Util
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.File.FileConst import FileConst
optionsMenu = Options()
util = Util()
userProfile = UserProfile()
fileMenu = File()
def main():
    util.init()
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.CANCEL_OPEN_FILE)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+Shift+U>")
    snooze(2)
    if (object.exists(UserProfileConst.NAME_EDIT)):
        test.passes("User Profile window found")
    else:
        test.fail("User Profile window not found")
    
    userProfile.setUserProfile("UserProfile", "UserProfile", "UserProfile", UserProfileConst.CANCEL_BUTT)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+Shift+U>")
    userProfile.setUserProfile("UserProfile", "UserProfile", "UserProfile")
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.CANCEL_OPEN_FILE)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+Shift+U>")
    snooze(2)
    test.compare(findObject(":CAppWindowBase.CBaseUserProfileDialog.m_nameLE").text, "UserProfile")
    test.compare(findObject(":CAppWindowBase.CBaseUserProfileDialog.m_emailLE").text, "UserProfile")
    test.compare(findObject(":CAppWindowBase.CBaseUserProfileDialog.m_addInfoTE").plainText, "UserProfile")