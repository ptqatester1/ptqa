#************************************
#@author: Pam Vinco
#@summary: File handles the File Menu
#************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.File.FileConst import FileConst
from squish import *

class File(SquishSyntax):
    #@summary: Selects p_item from the File menu
    #@param p_item: New, Open, Save, Save As..., Print..., Exit
    def selectFileItem(self, p_item):
        self.activateItem(FileConst.MENU_BAR, "File")
        self.activateItem(FileConst.FILE_MENU, p_item)