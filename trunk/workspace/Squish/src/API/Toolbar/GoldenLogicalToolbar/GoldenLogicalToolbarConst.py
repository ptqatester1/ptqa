#**************************************************************************
#@author: Tuan Hoang
#@summary: GoldenLogicalToolbarConst contains the common constants used in
#@         the Logical Workspace Toolbar
#**************************************************************************
class GoldenLogicalToolbarConst:
    ROOT = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar.CurrentClusterBtn"
    NEW_CLUSTER = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar.CreateClusterBtn"
    MOVE_OBJECT = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar.MoveBtn"
    SET_TILED_BACKGROUND = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar.SetBGImageBtn"
    VIEWPORT = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar.MiniCanvasBtn"
    LOGICAL_TOOLBAR = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar"
    SELECT_BACKGROUND_IMAGE_FILE_TYPE_COMBO = ":CBaseSetBGImageDlgClass.QFileDialog.fileTypeCombo"

    #Cluster
    CLUSTER_BACK = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar.BackBtn"
    CLUSTER_CURRENT_CLUSTER = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar.CurrentClusterBtn"
    CLUSTER_CURRENT_CLUSTER_LABEL = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar.m_curClusterNameLbl"
    CLUSTER_INFO_DIALOG = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Cluster Info"
    CLUSTER_INFO_DIALOG_OK = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.Cluster Info.qt_msgbox_buttonbox.OK"
    CLUSTER_NAME_EDIT = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.editClusterName.CNoteEdit1"

    #Viewport
    VIEWPORT_WINDOW = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Viewport.Viewport"
    VIEWPORT_BACK_ONE_LEVEL = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Viewport.Viewport.QToolButton1"
    VIEWPORT_DEVICE_LIST = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Viewport.CDevNameListWid.m_DevNameListWidget"     
    
    #Set Tiled Background
    SELECT_BACKGROUND_IMAGE_DIALOG_BTN = ":CAppWindowBase.centralwidget.m_PLFrame.CBaseLogicalToolbar.SetBGImageBtn"
    SELECT_BACKGROUND_IMAGE_DIALOG = ":CBaseSetBGImageDlgClass"
    SELECT_BACKGROUND_IMAGE_TAB_BAR = ":CBaseSetBGImageDlgClass.tabWidget2.qt_tabwidget_tabbar"
    SELECT_BACKGROUND_BACKGROUND_IMAGE_TAB = "Background Image"
    SELECT_BACKGROUND_CLUSTER_ICON_TAB = "Cluster Icon"
    
    SELECT_BACKGROUND_IMAGE_BROWSE = ":CBaseSetBGImageDlgClass.mainTabWidget.qt_tabwidget_stackedwidget.backgroundImagetab.m_browseBtn"
    SELECT_BACKGROUND_IMAGE_FILE_NAME_EDIT = ":CBaseSetBGImageDlgClass.QFileDialog.fileNameEdit"
    SELECT_BACKGROUND_IMAGE_FILE_OPEN = ":CBaseSetBGImageDlgClass.QFileDialog.buttonBox.Open"
    SELECT_BACKGROUND_IMAGE_FILE_CANCEL = ":CBaseSetBGImageDlgClass.QFileDialog.buttonBox.Cancel"
    SELECT_BACKGROUND_IMAGE_LIST = ":CBaseSetBGImageDlgClass.tabWidget2.qt_tabwidget_stackedwidget.backgroundImagetab.m_BGImageTableWidget"
    SELECT_BACKGROUND_IMAGE_ORIGINAL_IMAGE_RADIO = ":CBaseSetBGImageDlgClass.mainTabWidget.qt_tabwidget_stackedwidget.backgroundImagetab.gb_imageOptions.chkTiledView_2"
    SELECT_BACKGROUND_IMAGE_TILED_CHECKBOX = ":CBaseSetBGImageDlgClass.tabWidget2.qt_tabwidget_stackedwidget.backgroundImagetab.gb_imageOptions.chkTiledView"
    SELECT_BACKGROUND_IMAGE_RESET = ":CBaseSetBGImageDlgClass.tabWidget2.qt_tabwidget_stackedwidget.backgroundImagetab.m_clearBtn"
    SELECT_BACKGROUND_IMAGE_APPLY = ":CBaseSetBGImageDlgClass.mainTabWidget.qt_tabwidget_stackedwidget.backgroundImagetab.m_applyBtn"
    
    #Move
    MOVE_DROPDOWN = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CLogicalWorkspace1.QMenu1"