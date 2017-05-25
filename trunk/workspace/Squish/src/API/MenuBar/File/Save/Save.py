#*******************************************
#@author: Pam Vinco
#@summary: Save handles the Save File window
#*******************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.File.Save.SaveConst import SaveConst
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst
from squish import *
import object
filemenu = File()

class Save(SquishSyntax):
    #@summary: Saves a file to p_filepath
    #@param p_filePath: File path to save to
    def saveFile(self, p_filePath):
        filemenu.selectFileItem(FileConst.SAVE)
        snooze(2)
        self.commonSaveFile(p_filePath)
        
    #@summary: Save as to exisiting file
    #@param p_filePath: File path to save to
    def saveAsExistingFile(self, p_filePath):
        filemenu.selectFileItem(FileConst.SAVE_AS)
        snooze(2)
        self.commonSaveAsExistingFile(p_filePath)
        
    #@summary: Saves a file as a new file
    #@param p_filePath: File path to save to
    def saveAs(self, p_filePath):
        filemenu.selectFileItem(FileConst.SAVE_AS)
        snooze(2)
        self.commonSaveAs(p_filePath)

    #@summary: Saves a PKZ as a new file
    #@param p_filePath: File path to save to
    #@param p_addFilePathList: ["P:\ptqa\trunk\workspace\Squish\Pkt_Pka_ForTesting\Brad\JPEG.jpeg", "P:\ptqa\trunk\workspace\Squish\Pkt_Pka_ForTesting\Brad\file2.pkt"]
    def saveAsPkz(self, p_filePath, p_addFilePathList):
        filemenu.selectFileItem(FileConst.SAVE_AS_PKZ)
        snooze(2)
        self.setText(SaveConst.SAVE_FILE_NAME, p_filePath)
        self.clickButton(SaveConst.CONFIRM_SAVE_FILE)
        for path in p_addFilePathList:
            self.addPkz(path)
        self.clickButton(SaveConst.PKZ_SELECT_FILES_OK_BUTT)
        
    def saveAsExsistingPkz(self, p_filePath, p_addFilePathList):
        filemenu.selectFileItem(FileConst.SAVE_AS_PKZ)
        snooze(2)
        self.setText(SaveConst.SAVE_FILE_NAME, p_filePath)
        self.clickButton(SaveConst.CONFIRM_SAVE_FILE)
        for path in p_addFilePathList:
            self.addPkz(path)
        self.clickButton(SaveConst.PKZ_SELECT_FILES_OK_BUTT)
        self.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)


    def addPkz(self, p_filePath):
        self.clickButton(SaveConst.PKZ_SELECT_FILES_ADD_BUTT)
        self.typeText(SaveConst.PKZ_ADD_DIALOG_FILENAME_EDIT, p_filePath)
        self.clickButton(SaveConst.PKZ_ADD_DIALOG_OPEN_BUTT)
        
    #@summary: Saves a file to p_filepath
    #@param p_filePath: File path to save to        
    def saveExistingFile(self):
        filemenu.selectFileItem(FileConst.SAVE)


        
    #@summary: Saves a file to p_filepath
    #@param p_filePath: File path to save to        
    def saveOverwriteSelf(self, p_filePath):
        filemenu.selectFileItem(FileConst.SAVE)
        snooze(2)
        self.commonSaveOverwrite(p_filePath)
   
    #@summary: Saves a file to p_filepath
    #@param p_filePath: File path to save to    
    #@param p_newfilePath: new file name      
    def saveNoOverwrite(self, p_filePath, p_newfilePath):
        filemenu.selectFileItem(FileConst.SAVE)
        snooze(2)
        self.commonSaveNoOverwrite(p_filePath, p_newfilePath)

    #@summary: this function will be called by other SaveFile function
    #@param p_filePath: File path to save to        
    def commonSaveFile(self, p_filePath):
        self.setText(SaveConst.SAVE_FILE_NAME, p_filePath)
        snooze(2)
        self.clickButton(SaveConst.CONFIRM_SAVE_FILE)

    #@summary: this function will be called by other SaveFile function
    #@param p_filePath: File path to save to        
    def commonSaveAsExistingFile(self, p_filePath):
        self.setText(SaveConst.SAVE_FILE_NAME, p_filePath)
        snooze(2)
        if object.exists(SaveConst.CONFIRM_SAVE_FILE):
            self.clickButton(SaveConst.CONFIRM_SAVE_FILE)
            snooze(1)
            self.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)

    #@summary: this function will be called by other SaveFile function
    #@param p_filePath: File path to save to        
    def commonSaveAs(self, p_filePath):
        self.setText(SaveConst.SAVE_FILE_NAME, p_filePath)
        self.clickButton(SaveConst.CONFIRM_SAVE_FILE)
        snooze(1)
        self.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_NO)

    #@summary: this function will be called by other SaveExistingFile function
    #@param p_filePath: File path to save to        
    def commonSaveExistingFile(self):
        snooze(1)
        self.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
            
    #@summary: this function will be called by other SaveOverwrite function
    #@param p_filePath: File path to save to      
    def commonSaveOverwriteNew(self, p_filePath):
        self.setText(SaveConst.SAVE_FILE_NAME, p_filePath)
        self.clickButton(SaveConst.CONFIRM_SAVE_FILE)
        snooze(1)
        self.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)

    #@summary: this function will be called by other SaveOverwrite function
    #@param p_filePath: File path to save to      
    def commonSaveOverwrite(self, p_filePath):
        self.clickButton(SaveConst.CONFIRM_SAVE_FILE)
        snooze(1)
        self.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    #@summary: this function will be called by other SaveNoOverwrite function
    #@param p_filePath: File path to save to 
    #@param p_newfilePath: new file name   
    def commonSaveNoOverwrite(self, p_filePath, p_newfilePath):
        self.setText(SaveConst.SAVE_FILE_NAME, p_filePath)
        self.clickButton(SaveConst.CONFIRM_SAVE_FILE)
        snooze(1)
        self.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_NO)
        snooze(2)
        filemenu.selectFileItem(FileConst.SAVE)
        self.setText(SaveConst.SAVE_FILE_NAME, p_newfilePath)
        snooze(2)
        self.clickButton(SaveConst.CONFIRM_SAVE_FILE)        