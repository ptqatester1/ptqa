#****************************************
#@author: Pam Vinco, Thi Nguyen
#@summary: New handles creating new files
#****************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.MenuBar.File.New.NewConst import NewConst
from API.MenuBar.File.Save.Save import Save
from API.ActivityWizard.Exit.ExitConst import ExitConst
import object
from squish import *
save = Save()
filemenu = File()

class PopupWarnings:
    def __init__(self):
        self.sq = SquishSyntax()
    
    def saveNetworkDialog(self):
        try:
            return findObject(NewConst.SAVE_NETWORK_PROMPT)
        except LookupError, e:
            return False
    
    def saveNetworkYesButton(self):
        self.sq.clickButton(NewConst.SAVE_NETWORK_PROMPT_YES)
    
    def saveNetworkNoButton(self):
        self.sq.clickButton(NewConst.SAVE_NETWORK_PROMPT_NO)
    
    def saveNetworkCancelButton(self):
        self.sq.clickButton(NewConst.SAVE_NETWORK_PROMPT_CANCEL)

class New(SquishSyntax):
    def __init__(self):
        self.popups = PopupWarnings()
        
    def newSave(self, p_filePath):
        filemenu.selectFileItem(FileConst.NEW)
        self.commonNewSave(p_filePath)
        
    def newNoSave(self):
        filemenu.selectFileItem(FileConst.NEW)
        snooze(1)
        self.commonNewNoSave()
        
    def newCancel(self):
        filemenu.selectFileItem(FileConst.NEW)
        self.commonNewCancel()
    
    def commonNewSave(self, p_filePath):
    	snooze(1)
        self.clickButton(NewConst.SAVE_NETWORK_PROMPT_YES)
        snooze(1)
        save.SaveFile(p_filePath)

    def commonNewNoSave(self):
    	snooze(1)
        if ( object.exists(NewConst.SAVE_NETWORK_PROMPT_NO)):
            self.clickButton(NewConst.SAVE_NETWORK_PROMPT_NO)
        if (object.exists(ExitConst.EXIT_DIALOG_YES)):
            self.clickButton(ExitConst.EXIT_DIALOG_YES)
        
    def commonNewCancel(self):
    	snooze(1)
        self.clickButton(NewConst.SAVE_NETWORK_PROMPT_CANCEL)    
        