#**************************************************************************
#@author: Pam Vinco
#@summary: Edit handles the Edit menu
#**************************************************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.Tools.ToolsConst import ToolsConst

class Tools(SquishSyntax):
    #@summary: Selects p_item from the Edit menu
    #@param p_item: Copy, Paste, Undo
    def selectToolsItem(self, p_item):
        self.activateItem(ToolsConst.MENU_BAR, "Tools")
        self.activateItem(ToolsConst.TOOLS_MENU, p_item)