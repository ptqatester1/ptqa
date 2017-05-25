#****************************************
#@author: Pam Vinco, Thi Nguyen
#@summary: New handles creating new files
#****************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.MenuBar.File.Exit.ExitConst import ExitConst
from API.MenuBar.File.Save.Save import Save
from squish import *
save = Save()
filemenu = File()

class Exit(SquishSyntax):
    def exitSave(self, p_filePath):
        filemenu.selectFileItem(FileConst.EXIT)
        self.commonExitCancel(p_filePath)
    def exitNoSave(self):
        filemenu.selectFileItem(FileConst.EXIT)
        self.commonExitNoSave()
    def exitCancel(self):
        filemenu.selectFileItem(FileConst.EXIT)
        self.commonExitCancel()
        
    def commonExitSave(self, p_filePath):
    	snooze(1)
        self.clickButton(ExitConst.SAVE_NETWORK_PROMPT_YES)
        save.SaveFile(p_filePath)
    def commonExitNoSave(self):
    	snooze(1)
        self.clickButton(ExitConst.SAVE_NETWORK_PROMPT_NO)
    def commonExitCancel(self):
    	snooze(1)
        self.clickButton(ExitConst.SAVE_NETWORK_PROMPT_CANCEL)
    