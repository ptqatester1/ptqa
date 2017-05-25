#######################
#@author: Pamela Vinco
#######################
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.View.View import View
from API.MenuBar.View.ViewConst import ViewConst
from API.Utility.Util import Util
from API.Utility import UtilConst

#Function initialization
util = Util()
viewMenu = View()

def main():
    util.init()
    view_zoomIn()
    view_zoomReset()
    view_zoomOut()
    view_toolbarMain()
    view_toolbarRight()
    view_toolbarBottom()
    
def view_zoomIn():
    #Select Zoom In from the View Menu and check that the vertical scrollbar on the workspace changes value
    viewMenu.selectViewZoomItem(ViewConst.Zoom.ZOOM_IN)
    zoomedIn = findObject(UtilConst.WORKSPACE_SCROLL_VBAR)
    if(zoomedIn.maximum >= 1750):
        test.passes("Zoom In works")
    else:
        test.fail("Zoom In is not working properly")

def view_zoomReset():
    #Select Zoom Reset from the View Menu and check that the vertical scrollbar on the workspace changes value
    viewMenu.selectViewZoomItem(ViewConst.Zoom.ZOOM_RESET)
    zoomReset = findObject(UtilConst.WORKSPACE_SCROLL_VBAR)
    if(zoomReset.maximum >= 1550 and zoomReset.maximum <= 1650):
        test.passes("Zoom Reset works")
    else:
        test.fail("Zoom Reset is not working properly")
        
def view_zoomOut():
    #Select Zoom Out from the View Menu and check that the vertical scrollbar on the workspace changes value
    viewMenu.selectViewZoomItem(ViewConst.Zoom.ZOOM_OUT)
    zoomedOut = findObject(UtilConst.WORKSPACE_SCROLL_VBAR)
    if(zoomedOut.maximum <= 1400):
        test.passes("Zoom Out works")
    else:
        test.fail("Zoom Out is not working properly")
        
def view_toolbarMain():
    #Select the Main Toolbar from View Menu and check that it gets hidden
    viewMenu.selectViewToolbarItem(ViewConst.Toolbar.MAIN_TOOLBAR)
    test.compare(findObject(MainToolbarConst.MAIN_TOOLBAR).visible, False)
    viewMenu.selectViewToolbarItem(ViewConst.Toolbar.MAIN_TOOLBAR)
    
def view_toolbarRight():
    #Select the Right Toolbar from View Menu and check that it gets hidden
    viewMenu.selectViewToolbarItem(ViewConst.Toolbar.RIGHT_TOOLBAR)
    test.compare(findObject(CommonToolsBarConst.COMMON_TOOLS_BAR).visible, False)
    viewMenu.selectViewToolbarItem(ViewConst.Toolbar.RIGHT_TOOLBAR)

def view_toolbarBottom():
    #Select the Bottom Toolbar from View Menu and check that it gets hidden
    viewMenu.selectViewToolbarItem(ViewConst.Toolbar.BOTTOM_TOOLBAR)
    test.compare(findObject(ComponentBoxConst.NETWORK_COMPONENT_BOX).visible, False)
    viewMenu.selectViewToolbarItem(ViewConst.Toolbar.BOTTOM_TOOLBAR)
