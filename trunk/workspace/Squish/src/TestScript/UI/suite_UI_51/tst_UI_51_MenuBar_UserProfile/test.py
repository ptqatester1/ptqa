from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.UserProfile.UserProfileConst import UserProfileConst
from API.MenuBar.Options.UserProfile.UserProfile import UserProfile
from API.Utility.Util import Util
optionsMenu = Options()
util = Util()
userProfile = UserProfile()

def main():
    util.init()
    snooze(5)
    optionsMenu.selectOptionsItem(OptionsConst.USER_PROFILE)
    if (object.exists(UserProfileConst.NAME_EDIT)):
        test.passes("User Profile window found")
    else:
        test.fail("User Profile window not found")
    
    userProfile.setUserProfile("UserProfile", "UserProfile", "UserProfile", UserProfileConst.CANCEL_BUTT)
    optionsMenu.selectOptionsItem(OptionsConst.USER_PROFILE)
    test.compare(findObject(":CAppWindowBase.CBaseUserProfileDialog.m_nameLE").text, "Guest")
    test.compare(findObject(":CAppWindowBase.CBaseUserProfileDialog.m_emailLE").text, "")
    test.compare(findObject(":CAppWindowBase.CBaseUserProfileDialog.m_addInfoTE").plainText, "")
    userProfile.setUserProfile("UserProfile", "UserProfile", "UserProfile")
    optionsMenu.selectOptionsItem(OptionsConst.USER_PROFILE)
    snooze(2)
    test.compare(findObject(":CAppWindowBase.CBaseUserProfileDialog.m_nameLE").text, "UserProfile")
    test.compare(findObject(":CAppWindowBase.CBaseUserProfileDialog.m_emailLE").text, "UserProfile")
    test.compare(findObject(":CAppWindowBase.CBaseUserProfileDialog.m_addInfoTE").plainText, "UserProfile")


