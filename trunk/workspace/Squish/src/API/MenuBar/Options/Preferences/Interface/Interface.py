##Chris Allen

from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst
from API.Utility.Util import Util
from squish import *
import object

class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def fileAlreadyExistsDialog(self):
        try:
            return findObject(InterfaceConst.SAVE_LOG_DIALOG)
        except LookupError, e:
            return False
        
    def fileAlreadyExistsYesButton(self):
        self.util.clickButton(InterfaceConst.SAVE_LOG_DIALOG_YES)
        
    def fileAlreadyExistsNoButton(self):
        self.util.clickButton(InterfaceConst.SAVE_LOG_DIALOG_NO)
    
    @property
    def overwriteDialog(self):
        try:
            return findObject(InterfaceConst.OVERWRITE_FILE_DIALOG)
        except LookupError, e:
            return False
    
    def overwriteYesButton(self):
        self.util.clickButton(InterfaceConst.OVERWRITE_FILE_DIALOG_YES)
    
    def overwriteNoButton(self):
        self.util.clickButton(InterfaceConst.OVERWRITE_FILE_DIALOG_NO)
    
    @property
    def changeLanguageDialog(self):
        try:
            return findObject(InterfaceConst.CHANGE_LANGUAGE_POPUP_DIALOG)
        except LookupError, e:
            return False
    
    def changeLanguageOkButton(self):
        self.util.clickButton(InterfaceConst.CHANGE_LANGUAGE_OK)

class FileDialog:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
    
    def filename(self, filename):
        self.util.setText(InterfaceConst.EXPORT_LOG_DIALOG_FILENAME_EDIT, filename)
    
    def saveButton(self):
        self.util.clickButton(InterfaceConst.EXPORT_LOG_DIALOG_OK)
    
    def cancelButton(self):
        self.util.clickButton(InterfaceConst.EXPORT_LOG_DIALOG_CANCEL)
    
    def save(self, filename, overwrite = True):
        self.filename(filename)
        self.saveButton()
        if self.popups.fileAlreadyExistsDialog:
            self.popups.fileAlreadyExistsYesButton()
        if self.popups.overwriteDialog:
            self.popups.overwriteYesButton()

class Interface:
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
        self.popups = PopupWarnings()
    
    def checkItem(self, checkboxName, checked = None):    
        checkbox = None
        for item in self.checkboxes:
            try:
                if item.text == checkboxName:
                    checkbox = item
            except AttributeError, e:
                continue
        if not checkbox:
            raise ValueError('Could not find checkbox named: ' + checkboxName)
        if checked == None:
            self.util.click(checkbox)
        elif checked == True:
            if not checkbox.checked:
                self.util.click(checkbox)
        elif checked == False:
            if checkbox.checked:
                self.util.click(checkbox)
        else:
            raise ValueError('checked must be None, True, or False')
    
    def checkItems(self, checkboxName, *moreCheckboxes, **kwargs):
        checked = None
        if 'checked' in kwargs:
            checked = kwargs['checked']
        for item in (checkboxName,) + moreCheckboxes:
            self.checkItem(item, checked)
    
    def enableLogging(self, checked = None):
        checkbox = findObject(InterfaceConst.ENABLE_LOGGING)
        if checked == None:
            self.util.click(checkbox)
        elif checked == True:
            if not checkbox.checked:
                self.util.click(checkbox)
        elif checked == False:
            if checkbox.checked:
                self.util.click(checkbox)
        else:
            raise ValueError('checked must be None, True, or False')
    
    def exportLogButton(self):
        self.util.clickButton(InterfaceConst.EXPORT_LOG_BUTTON)
    
    def changeLanguageButton(self):
        self.util.clickButton(InterfaceConst.CHANGE_LANGUAGE_BUTTON)
    
    @property
    def languageTable(self):
        return findObject(InterfaceConst.LANGUAGE_BOX)
        
    def selectLanguage(self, language):
        for item in object.children(self.languageTable):
            try:
                if item.text == language:
                    self.util.click(item)
                    return
            except AttributeError, e:
                pass
        raise ValueError('Could not find language file: ' + language)
    
    
    def exportLog(self, filename):
        self.exportLogButton()
        self.fileDialog.save(filename, overwrite=True)

    def changeLanguage(self, p_ptlFileName):
        self.selectLanguage(language)
        self.changeLanguageButton()
        if self.popups.changeLanguageDialog:
            self.popups.changeLanguageOkButton()
    
    @property
    def checkboxes(self):
        groupbox = findObject(InterfaceConst.CHECKBOX_SECTION)
        return [child for child in object.children(groupbox) if 'text' in object.properties(child)]
                
    @property
    def checked(self):
        checkboxes = self.checkboxes
        checkedItems = []
        for checkbox in checkboxes:
            if checkbox.checked:
                checkedItems.append(checkbox)
        return checkedItems
    
    @property
    def unchecked(self):
        checkboxes = self.checkboxes
        checkedItems = []
        for checkbox in checkboxes:
            if not checkbox.checked:
                checkedItems.append(checkbox)
        return checkedItems
    