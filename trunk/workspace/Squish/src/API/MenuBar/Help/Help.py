#**************************************************************************
#@author: Tuan Hoang
#@summary: Help handles the Help menu
#**************************************************************************
from API.MenuBar.Help.HelpConst import HelpConst
from API.SquishSyntax import SquishSyntax

class Help(SquishSyntax):
    #@summary: Selects p_item from the Help menu
    #@param p_item: Contents, Tutorials, or About
    def selectHelpItem(self, p_item):
        self.activateItem(HelpConst.MENU_BAR, "Options")
        self.activateItem(HelpConst.HELP, p_item)