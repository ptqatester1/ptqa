from API.MenuBar.Extensions.Multiuser.Multiuser import MultiUser
from API.MenuBar.Extensions.Multiuser.MultiuserConst import MultiuserConst
from API.Utility.Util import Util
MultiUserMenu = MultiUser()
util = Util()


def main():
    util.init()
    multiUserListenWindow()
    multiUserPortVisibilityWindow()
    multiUserOptionWindow()
    multiUserSaveWindow()

def multiUserListenWindow(): 
    snooze(1)
    MultiUserMenu.selectMultiUserItem(MultiuserConst.LISTEN)
    if (object.exists(MultiuserConst.Listen.PORT_NUM_EDIT)):
        test.passes("Listen window found")
    else:
        test.fail("Listen window not found")
    util.clickButton(MultiuserConst.Listen.OK_BUTT)

def multiUserPortVisibilityWindow(): 
    snooze(1)
    MultiUserMenu.selectMultiUserItem(MultiuserConst.PORT_VISIBILITY)
    if (object.exists(MultiuserConst.Port_Visilbility.NETWORK_TREE_VIEW)):
        test.passes("Port_Visilbility window found")
    else:
        test.fail("Port_Visilbility window not found")

    util.clickButton(MultiuserConst.Port_Visilbility.OK_BUTT)
    
def multiUserOptionWindow(): 
    snooze(1)
    MultiUserMenu.selectMultiUserItem(MultiuserConst.OPTION)
    if (object.exists(":CBaseMUOptoinsDlg.chkAllowRemoteSaving")):
        test.passes("Options window found")
    else:
        test.fail("Options window not found")
    util.clickButton(":CBaseMUOptoinsDlg.m_btnOK")
    
def multiUserSaveWindow(): 
    snooze(1)
    MultiUserMenu.selectMultiUserItem(MultiuserConst.SAVE_OFFLINE)
    if (object.exists(MultiuserConst.Save_OffLine.CANCEL_BUTT)):
        test.passes("Save_OffLine window found")
    else:
        test.fail("Save_OffLine window not found")
    util.clickButton(MultiuserConst.Save_OffLine.CANCEL_BUTT)
