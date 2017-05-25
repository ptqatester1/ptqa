#*************************************************************
#@author: Pam Vinco, Thi Nguyen
#@summary: MainToolbar handles tools found in the Main Toolbar
#*************************************************************
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.MenuBar.File.Open.Open import Open
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.File.New.New import New
from API.MenuBar.File.Save.Save import Save
from API.MenuBar.File.Print.Print import Print
from API.Utility import UtilConst
from API.SquishSyntax import SquishSyntax
from squish import *

class PopupWarnings:
    def __init__(self):
        self.squishSyntax = SquishSyntax()
    
    @property
    def useAsAnswerNetworkDialog(self):
        try:
            return findObject(MainToolbarConst.USE_AS_ANSWER_NETWORK_PROMPT)
        except LookupError, e:
            return False
    
    def useAsAnswerNetworkYesButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.USE_AS_ANSWER_NETWORK_YES)
    
    def useAsAnswerNetworkNoButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.USE_AS_ANSWER_NETWORK_NO)
    
    def useAsAnswerNetworkCancelButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.USE_AS_ANSWER_NETWORK_CANCEL)
    
    def passwordDialog(self):
        try:
            return findObject(MainToolbarConst.ACTIVITY_WIZARD_PASSWORD_DIALOG)
        except LookupError, e:
            return False
    
    def passwordEdit(self, password):
        self.squishSyntax.setText(MainToolbarConst.ACTIVITY_WIZARD_PASSWORD, password)
    
    def passwordOkButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.ACTIVITY_WIZARD_PASSWORD_OK)
    
    def passwordCancelButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.ACTIVITY_WIZARD_PASSWORD_CANCEL)

class MainToolbar:
    #@summary: A null function to initialize SquishSyntax
    def __init__(self):
        self.squishSyntax = SquishSyntax()
        self.open = Open()
        self.new = New()
        self.save = Save()
        self.Print = Print()#Python 2.x does not allow me to overwrite the print function
        self.popups = PopupWarnings()
    
    def saveAs(self, filename):
        self.save.saveAs(filename)
    
    def newButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.NEW)
    
    def openButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.OPEN)
    
    def saveButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.SAVE)
    
    def printButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.PRINT)
    
    def activityWizardButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    
    def copyButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.COPY)
    
    def pasteButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.PASTE)
    
    def undoButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.UNDO)
    
    def redoButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.REDO)
        
    def zoomInButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.ZOOM_IN)
    
    def zoomResetButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.ZOOM_RESET)
    
    def zoomOutButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.ZOOM_OUT)
        
    def paletteButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.PALETTE)
    
    def customDevicesButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.CUSTOM_DEVICES)
    
    def networkDescriptionButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.NETWORK_DESCRIPTION)
    
    def contentsButton(self):
        self.squishSyntax.clickButton(MainToolbarConst.CONTENTS)
    
    def openFile(self, p_filePath):
        self.openButton()
        self.open.commonOpenFile(p_filePath)
        
    def openFileSave(self, p_savefilePath, p_openfilePath):
        self.openButton()
        self.open.openFileSave(p_savefilePath, p_openfilePath)
        
    def openFileSaveOverwrite(self, p_openfilePath, p_savefilePath = None):
        self.openButton()
        if p_savefilePath:
            self.squishSyntax.clickButton(OpenConst.SAVE_NETWORK_PROMPT_YES)
            self.save.commonSaveAsExistingFile(p_savefilePath)
        self.open.commonOpenFile(p_openfilePath)
        
    def openFileNoSave(self, p_filePath):
        self.openButton()
        self.open.commonOpenFileNoSave(p_filePath)
        
    def newSave(self, p_filePath):
        self.newButton()
        self.new.commonNewSave(p_filePath)
    
    def newNoSave(self):
        self.newButton()
        self.new.commonNewNoSave()
    
    def newCancel(self):
        self.newButton()
        self.new.commonNewCancel()
        
    def printToFile(self, p_obj, p_filePath):
        self.printButton()
        self.Print.commonPrintToFile(p_filePath)
        
    def printToPrinter(self, p_obj):
        self.printButton()
        self.Print.commonPrintToPrinter(p_obj)
        
    def printCancel(self):
        self.printButton()
        self.Print.commonPrintCancel()  
        
    def saveFile(self, p_filePath):
        self.saveButton()
        self.save.commonSaveFile(p_filePath)
        
    def saveExistingFile(self):
        self.saveButton()
        
    def saveAsExistingFile(self, p_filePath):
        self.save.saveAsExistingFile(p_filePath)
        
    def saveOverwrite(self, p_filePath):
        self.saveButton()
        self.save.commonSaveOverwrite(p_filePath)
        
    def saveNoOverwrite(self, p_filePath, p_newfilePath):
        self.saveButton()
        self.save.commonSaveNoOverwrite(p_filePath, p_newfilePath)
        
    def activityWizard(self, useNetwork = True, **kwargs):
        self.activityWizardButton()
        if 'password' in kwargs:
            self.popups.passwordEdit(kwargs['password'])
            self.popups.passwordOkButton()
        if self.popups.useAsAnswerNetworkDialog:
            if useNetwork == None:
                self.popups.useAsAnswerNetworkCancelButton()
            elif useNetwork == True:
                self.popups.useAsAnswerNetworkYesButton()
            elif useNetwork == False:
                self.popups.useAsAnswerNetworkNoButton()
            else:
                raise ValueError('useNetwork should be None, True, or False')
            
    def activityWizardUseNetwork(self):
        self.activityWizard(useNetwork=True)
        
    def activityWizardDontUseNetwork(self):
        self.activityWizard(useNetwork=False)
        
    def addNetworkDescription(self, p_description):
        self.networkDescriptionButton()
        self.squishSyntax.setText(MainToolbarConst.NETWORK_DESCRIPTION_TEXT, p_description)