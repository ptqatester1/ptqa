#******************************************************************************************
#@author: Tuan Hoang
#@summary: AdministrativeConst contains the common constants used in the Administrative Tab
#******************************************************************************************
class AdministrativeConst:
    PREFERENCES_WINDOW = ":CAppWindowBase.Admin_Opts"
    ADMINISTRATIVE_WINDOW = ""
    TAB_BAR = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_tabbar"
    ADMINISTRATIVE = "Administrative"
    
    #Choose Password
    PASSWORD_EDIT = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.m_aTbPassGroupBox.aTbPasswordEdit"
    CONFIRM_EDIT = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.m_aTbPassGroupBox.aTbConfirmEdit"
    ENABLE_PASSWORD_BUTTON = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.m_aTbPassGroupBox.SetPasswordBtn"
    DISABLE_PASSWORD_BUTTON = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.m_aTbPassGroupBox.DisablePasswordBtn"
    
    PASSWORD_DIALOG = ":Password? -- Packet Tracer.QLineEdit1"
    PASSWORD_DIALOG_OK = ":Password? -- Packet Tracer.QDialogButtonBox1.OK"
    PASSWORD_DIALOG_CANCEL = ":Password? -- Packet Tracer.QDialogButtonBox1.Cancel"
    
    #Interface Locking    
    INTERFACE_TAB = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.aTbIntLockingGroupBox.m_aTbIntTabCkBox"
    HIDE_TAB = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.aTbIntLockingGroupBox.m_aTbHideTabCkBox"
    FONT_TAB = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.m_interfaceLockingGB.fontTabCB"
    CUSTOM_INTERFACES_TAB = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.aTbIntLockingGroupBox.m_aTbCustomIntTabCkBox"
    MULTIUSER_MENU = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.aTbIntLockingGroupBox.m_aTbMUMenuCkBox"
    IPC_MENU = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.aTbIntLockingGroupBox.m_aTbIPCMenuCkBox"
    SCRIPTING_MENU = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.aTbIntLockingGroupBox.m_aTbScriptingMenuCkBox"
    MISC_TAB = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.aTbIntLockingGroupBox.m_miscellaneousTabChkBox"
    
    #Write Options to PT Installed Folder
    WRITE_BUTTON = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.m_aTbWriteOptionsGroupBox.aTbWriteButton"
    WRITE_SUCCESSFUL_DIALOG = ":CAppWindowBase.Admin_Opts.Packet Tracer.qt_msgbox_buttonbox"
    WRITE_SUCCESSFUL_DIALOG_OK = ":CAppWindowBase.Admin_Opts.Packet Tracer.qt_msgbox_buttonbox.OK"
    
    #User Folder
    USER_FOLDER_EDIT = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.m_aTbUserFolderGroupBox.m_aTbUserFolderEdit"
    USER_FOLDER_BROWSE_BUTTON = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_adminTab.m_aTbUserFolderGroupBox.aTbBrowseButton"
    
    FILENAME_EDIT = ':CAppWindowBase.Admin_Opts.QFileDialog.fileNameEdit'
    CHOOSE_BUTTON = ':CAppWindowBase.Admin_Opts.QFileDialog.buttonBox.Choose'
    CANCEL_BUTTON = ':CAppWindowBase.Admin_Opts.QFileDialog.buttonBox.Cancel'