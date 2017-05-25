#**************************************************************************
#@author: Pam Vinco
#@summary: Edit handles the Edit menu
#**************************************************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.Edit.EditConst import EditConst

class Edit(SquishSyntax):
    #@summary: Selects p_item from the Edit menu
    #@param p_item: Copy, Paste, Undo
    def selectEditItem(self, p_item):
        self.activateItem(EditConst.MENU_BAR, "Edit")
        self.activateItem(EditConst.EDIT_MENU, p_item)