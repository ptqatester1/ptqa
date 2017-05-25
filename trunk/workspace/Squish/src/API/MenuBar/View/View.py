#**************************************************************************
#@author: Pam Vinco
#@summary: View handles the View menu
#**************************************************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.View.ViewConst import ViewConst

class View(SquishSyntax):
    #@summary: Selects p_item from the View menu
    #@param p_item: Copy, Paste, Undo
    def selectViewItem(self, p_item):
        self.activateItem(ViewConst.MENU_BAR, "View")
        self.activateItem(ViewConst.VIEW_MENU, p_item)
        
    def selectViewToolbarItem(self, p_item):
        self.activateItem(ViewConst.MENU_BAR, "View")
        self.activateItem(ViewConst.VIEW_MENU, "Toolbars")
        self.activateItem(ViewConst.Toolbar.TOOLBAR_MENU, p_item)
        
    def selectViewZoomItem(self, p_item):
        self.activateItem(ViewConst.MENU_BAR, "View")
        self.activateItem(ViewConst.VIEW_MENU, "Zoom")
        self.activateItem(ViewConst.Zoom.ZOOM_MENU, p_item)