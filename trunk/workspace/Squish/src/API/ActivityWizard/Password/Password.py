##Chris Allen

from API.Utility.Util import Util
from API.ActivityWizard.Password.PasswordConst import PasswordConst

class Password:
    def __init__(self):
        self.util = Util()
    
    def password(self, password):
        self.util.setText(PasswordConst.PASSWORD_TEXTFIELD, password)
    
    def confirmPassword(self, password):
        self.util.setText(PasswordConst.CONFIRM_TEXTFIELD, password)
    
    def enablePasswordButton(self):
        self.util.clickButton(PasswordConst.ENABLE_PASSWORD)
    
    def disablePasswordButton(self):
        self.util.clickButton(PasswordConst.DISABLE_PASSWORD)
    
    def setActivityPassword(self, password):
        self.password(password)
        self.confirmPassword(password)
        self.enablePasswordButton()