##Chris Allen

from API.Utility.Util import Util
from API.ActivityWizard.Save.SaveConst import SaveConst
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from squish import *

def err(msg = ''): raise NotImplementedError(msg)

class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def overwriteDialog(self):
        try:
            return findObject(SaveConst.OVERWRITE_FILE_PROMPT)
        except LookupError, e:
            return False
    
    def overwriteYesButton(self):
        self.util.click(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    
    def overwriteNoButton(self):
        self.util.click(SaveConst.OVERWRITE_FILE_PROMPT_NO)

class PkzSelectFilesDialog:
    def __init__(self):
        self.util = Util()
    
    def filename(self, filename):
        err()
    
    def openButton(self):
        err()
    
    def cancelButton(self):
        err()

class AddPkzFilesDialog:
    def __init__(self):
        self.util = Util()
        self.fileDialog = PkzSelectFilesDialog()
    
    def addButton(self):
        err()
    
    def removeButton(self):
        err()
    
    def okButton(self):
        err()
    
    def cancelButton(self):
        err()
    
    @property
    def fileList(self):
        err()
        
    def selectFile(self):
        err()

class CommonCartridgeDialog:
    def __init__(self):
        self.util = Util()
    
    def packagePath(self, path):
        err()
    
    def enableWikiPageSupport(self, checked = True):
        err()
    
    def wikiPageName(self, wikiPage):
        err()
    
    def packageCaption(self, caption):
        err()
    
    def packageDescription(self, desc):
        err()
    
    def importTagsButton(self):
        err()
    
    def exportButton(self):
        err()
    
    def cancelButton(self):
        err()
        

class FileDialog:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
    
    @property
    def dialogWindow(self):
        try:
            return findObject(SaveConst.SAVE_DIALOG)
        except LookupError, e:
            return False
    
    def filename(self, filename):
        self.util.setText(SaveConst.SAVE_FILE_NAME, filename)
    
    def saveButton(self):
        self.util.clickButton(SaveConst.SAVE_DIALOG_OK)
    
    def cancelButton(self):
        self.util.clickButton(SaveConst.SAVE_DIALOG_CANCEL)
    
    def save(self, filename, overwrite):
        self.filename(filename)
        self.saveButton()
        if self.popups.overwriteDialog:
            if overwrite:
                self.popups.overwriteYesButton()
            else:
                self.popups.overwriteNoButton()
        

class Save:
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
        self.popups = PopupWarnings()
        self.pkzDialog = AddPkzFilesDialog()
        self.ccDialog = CommonCartridgeDialog()
        
    def saveButton(self):
        self.util.clickButton(ActivityWizardConst.SAVE)
    
    def saveAsButton(self):
        self.util.clickButton(ActivityWizardConst.SAVE_AS)
    
    def saveAsPkzButton(self):
        self.util.clickButton(ActivityWizardConst.SAVE_AS_PKZ)
    
    def exportAsCCButton(self):
        self.util.clickButton(ActivityWizardConst.SAVE_AS_CC)
        
    def savefile(self, filename, overwrite = True):
        self.saveButton()
        if self.fileDialog.dialogWindow:
            self.fileDialog.save(filename, overwrite)
        
    
    def saveAs(self, filename, overwrite = True):
        self.saveAsButton()
        self.fileDialog.save(filename, overwrite)
    
    def saveAsPkz(self, filename):
        '''Currently this function only handles the standard case of
        Press the save as pkz button
        Enter the filename
        if the file exists overwrite it
        Press ok at the add files dialog'''
        self.saveAsPkzButton()
        self.fileDialog.save(filename, overwrite=True)
        self.pkzDialog.okButton()
    
    def exportAsCC(self, filename, packagePath, wikiPageName, packageCaption, packageDescription):
        self.exportAsCCButton()
        self.fileDialog.save(filename, overwrite=True)
        self.pkzDialog.okButton()
        self.ccDialog.packagePath(packagePath)
        self.ccDialog.wikiPageName(wikiPageName)
        self.ccDialog.packageCaption(packageCaption)
        self.ccDialog.packageDescription(packageDescription)
        self.ccDialog.exportButton()