#**************************************************************************
#@author: Tuan Hoang
#@summary: HelpConst contains the common constants used in Help menu
#**************************************************************************
class ViewConst:
    MENU_BAR = ":CAppWindowBase.m_pMenubar"
    VIEW_MENU = ":CAppWindowBase.m_pMenubar.View Menu"
    SHOW_VIEWPORT = "Show Viewport"
    VIEWPORT_HBAR = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Viewport.Viewport.qt_scrollarea_hcontainer.QScrollBar1"
    VIEWPORT_VBAR = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Viewport.Viewport.qt_scrollarea_vcontainer.QScrollBar1"
    class Zoom:
        ZOOM_MENU = ":CAppWindowBase.m_pMenubar.View Menu.menuZoom"
        ZOOM_IN = "Zoom In"
        ZOOM_OUT = "Zoom Out"
        ZOOM_RESET = "Zoom Reset"
    class Toolbar:
        TOOLBAR_MENU = ":CAppWindowBase.m_pMenubar.View Menu.menuToolbar"
        MAIN_TOOLBAR = "Main Toolbar"
        MAIN_TOOLBAR_OBJECT = ":menuToolbar.Main Toolbar"
        RIGHT_TOOLBAR = "Right Toolbar"
        BOTTOM_TOOLBAR = "Bottom Toolbar"