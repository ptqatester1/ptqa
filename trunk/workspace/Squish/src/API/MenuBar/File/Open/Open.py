#*******************************************
#@author: Pam Vinco, Thi Nguyen
#@summary: Open handles the Open File window
#*******************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.File.FileConst import FileConst 
from API.MenuBar.File.File import File
from API.MenuBar.File.Save.Save import Save
from squish import *
import object
import os

#Function initialization
filemenu = File()
save = Save()

class PopupWarnings:
    def __init__(self):
        self.sq = SquishSyntax()
    
    def saveNetworkDialog(self):
        try:
            return findObject(OpenConst.SAVE_NETWORK_PROMPT)
        except LookupError, e:
            return False
    
    def saveNetworkYesButton(self):
        self.sq.clickButton(OpenConst.SAVE_NETWORK_PROMPT_YES)
    
    def saveNetworkNoButton(self):
        self.sq.clickButton(OpenConst.SAVE_NETWORK_PROMPT_NO)
    
    def saveNetworkCancelButton(self):
        self.sq.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)

class Open(SquishSyntax):
    def __init__(self):
        self.popups = PopupWarnings()

    def openFile(self, p_filePath):
        filemenu.selectFileItem(FileConst.OPEN)
        self.commonOpenFile(p_filePath)
        
    def openFileSave(self, p_savefilePath, p_openfilePath):
        filemenu.selectFileItem(FileConst.OPEN)
        self.commonOpenFileSave(p_savefilePath, p_openfilePath)
        
    def openFileNoSave(self, p_filePath):
        filemenu.selectFileItem(FileConst.OPEN)
        self.commonOpenFileNoSave(p_filePath)
        
    def openSamples(self, p_filePath):
        filemenu.selectFileItem(FileConst.OPEN_SAMPLES)
        self.commonOpenFile(p_filePath)
        if (object.exists(OpenConst.UPDATE_IOE_DEVICES)):
            self.clickButton(OpenConst.UPDATE_IOE_DEVICES_YES)
        
    def openSamplesSave(self, p_savefilePath, p_openfilePath):
        filemenu.selectFileItem(FileConst.OPEN_SAMPLES)
        self.commonOpenFileSave(p_savefilePath, p_openfilePath)
        
    def openSamplesNoSave(self, p_filePath):
        filemenu.selectFileItem(FileConst.OPEN_SAMPLES)
        self.commonOpenFileNoSave(p_filePath)
        
    def commonOpenFile(self, p_filePath):
        if(os.name =='posix'):
            snooze(1)
        snooze(5)
        self.setText(OpenConst.OPEN_FILE_NAME, p_filePath)
        snooze(1)
        self.clickButton(OpenConst.CONFIRM_OPEN_FILE)
        if(os.name =='posix'):
            snooze(5)
            
    def commonOpenFileSave(self, p_savefilePath, p_openfilePath):
        snooze(1)
        self.clickButton(OpenConst.SAVE_NETWORK_PROMPT_YES)
        snooze(1)
        save.SaveFile(p_savefilePath)
        self.setText(OpenConst.OPEN_FILE_NAME, p_openfilePath)
        self.clickButton(OpenConst.CONFIRM_OPEN_FILE)
        
    def commonOpenFileNoSave(self, p_filePath):
        snooze(1)
        self.clickButton(OpenConst.SAVE_NETWORK_PROMPT_NO)
        snooze(1)
        self.setText(OpenConst.OPEN_FILE_NAME, p_filePath)
        snooze(1)
        self.clickButton(OpenConst.CONFIRM_OPEN_FILE)        