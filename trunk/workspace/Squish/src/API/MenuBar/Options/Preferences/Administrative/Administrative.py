##Chris Allen

from API.Utility.Util import Util
from API.MenuBar.Options.Preferences.Administrative.AdministrativeConst import AdministrativeConst

class PopupWarnings:
    def __init__(self):
        self.util = Util()
        
    @property
    def optionsSuccessfullySavedDialog(self):
        try:
            return findObject(AdministrativeConst.WRITE_SUCCESSFUL_DIALOG)
        except LookupError, e:
            return False
    
    def optionsSuccessfullySavedOkButton(self):
        self.util.clickButton(AdministrativeConst.WRITE_SUCCESSFUL_DIALOG_OK)
        
class FileDialog:
    def __init__(self):
        self.util = Util()
    
    def filename(self, filename):
        self.util.setText(AdministrativeConst.FILENAME_EDIT, filename)
    
    def chooseButton(self):
        self.util.clickButton(AdministrativeConst.CHOOSE_BUTTON)
    
    def cancelButton(self):
        self.util.clickButton(AdministrativeConst.CANCEL_BUTTON)
    
    def save(self, filename):
        self.filename(filename)
        self.chooseButton()


class InterfaceLocking:
    def __init__(self):
        self.util = Util()
    
    @property
    def interfaceLockingGroupbox(self):
        err()
    
    def checkItem(self, checkboxName, checked = None):
        checkbox = None
        for checkboxItem in object.children(self.interfaceLockingGroupbox):
            if checkboxItem.text == checkboxName:
                checkbox = checkboxItem
        if not checkbox:
            raise ValueError('Could not find checkbox: ' + checkboxName)
        self.util.checkbox(checkbox, checked)

class Administrative:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
        self.fileDialog = FileDialog()
        self.interfaceLocking = InterfaceLocking()
    
    def password(self, password):
        self.util.setText(AdministrativeConst.PASSWORD_EDIT, password)
    
    def confirm(self, password):
        self.util.setText(AdministrativeConst.CONFIRM_EDIT, password)
    
    def enablePasswordButton(self):
        self.util.clickButton(AdministrativeConst.ENABLE_PASSWORD_BUTTON)
    
    def disablePasswordButton(self):
        self.util.clickButton(AdministrativeConst.DISABLE_PASSWORD_BUTTON)
    
    def writeButton(self):
        self.util.clickButton(AdministrativeConst.WRITE_BUTTON)
    
    def userFolder(self, filename):
        self.util.setText(AdministrativeConst.USER_FOLDER_EDIT, filename)
    
    def browseButton(self):
        self.util.clickButton(AdministrativeConst.USER_FOLDER_BROWSE_BUTTON)
        
    def enablePassword(self, password):
        self.password(password)
        self.confirm(password)
        self.enablePasswordButton()
    
    def writeOptions(self):
        self.writeButton()
        if self.popups.optionsSuccessfullySavedDialog:
            self.popups.optionsSuccessfullySavedOkButton()