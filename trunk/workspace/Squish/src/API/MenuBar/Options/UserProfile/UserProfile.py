#**************************************************************************
#@author: Thi Nguyen
#@summary: UerProfile
#******************************
from API.MenuBar.Options.UserProfile.UserProfileConst import UserProfileConst
from API.SquishSyntax import SquishSyntax

class UserProfile(SquishSyntax):
    def setUserProfile(self, p_name = None, p_email = None, p_addInfo = None, p_okOrCancel = UserProfileConst.OK_BUTT):
        if p_name:
            self.setText(UserProfileConst.NAME_EDIT, p_name)
        if p_email:
            self.setText(UserProfileConst.EMAIL_EDIT, p_email)
        if p_addInfo:
            self.setText(UserProfileConst.ADD_INFO_EDIT, p_addInfo)
        self.clickButton(p_okOrCancel)
        
    def closeAndConfirm(self):
        self.clickButton(UserProfileConst.OK_BUTT)
        self.clickButton(UserProfileConst.CONFIRM_RESET_YES)