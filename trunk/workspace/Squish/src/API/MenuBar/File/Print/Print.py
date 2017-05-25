#****************************************
#@author: Pam Vinco, Thi Nguyen
#@summary: Print handles the Print window
#****************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.Print.PrintConst import PrintConst
from API.MenuBar.File.Save.Save import Save

filemenu = File()
save = Save()

class Print(SquishSyntax):
    #Prints to file selected Item
    def printToFile(self, p_filePath):
        filemenu.selectFileItem(FileConst.PRINT)
        self.commonPrintToFile(p_filePath)
    def printToPrinter(self, p_obj):
        filemenu.selectFileItem(FileConst.PRINT)
        self.commonPrintToPrinter(p_obj)
    def printCancel(self):
        filemenu.selectFileItem(FileConst.PRINT)
        self.commonPrintCancel()
    def commonPrintToFile(self, p_filePath):
        self.clickButton(PrintConst.PRINT_TO_FILE)
        save.saveFile(p_filePath)
    def commonPrintToPrinter(self, p_obj):
        filemenu.selectFileItem(FileConst.PRINT)
        self.clickButton(p_obj)
        self.clickButton(PrintConst.CONFIRM_PRINT)
    def commonPrintCancel(self):
        filemenu.selectFileItem(FileConst.PRINT)
        self.close(PrintConst.PRINT_DIALOG_WINDOW)        