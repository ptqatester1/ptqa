#**************************************************************************
#@author: Thi Nguyen
#@summary: IPCConst contains the common constants used in IPC
#**************************************************************************
class IPCConst:
    IPC_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu.extensionsIPCAction"
    CONFIGURE_APPS = "Configure Apps ..."
    ACTIVE_APPS = "Show Active Apps ..."
    OPTION = "Options ..."
    LOG = "Log ..."
    class Configure_Apps:
        TAB_BAR = ".tabWidget.qt_tabwidget_tabbar"
        SETTING_TAB = "Settings"
        DESCRIPTION_TAB = "Description"
        SECURITY_TAB = "Security"
        SAVE_BUTT = ".m_saveBtn"
        OK_BUTT = ".m_okBtn"
        CANCEL_BUTT = ".m_cancelBtn"
        REMOVE_BUTT = ".groupBox_5.m_removeBtn"
        APPS_LIST = ".groupBox_5.m_cepList"
        LAUNCH_BUTT = ".groupBox_5.m_launchBtn"
        ADD_BUTT = ".groupBox_5.m_addBtn"
        class Apps_List:
            ADD_APPS_FILENAME_EDIT = ".QFileDialog.fileNameEdit"
            ADD_APPS_FILENAME_CANCEL_BUTT = ".QFileDialog.buttonBox.Cancel"
            ADD_APPS_FILENAME_OPEN_BUTT = ".QFileDialog.buttonBox.Open"
            ADD_APPS_FILENAME_CANCEL_BUTT = ".QFileDialog.buttonBox.Cancel"
            
        class Security:
            APPLICATION_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_applicationCB"
            ACTIVITY_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_activityCB"
            FILE_OPERATION_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_fileOperationsCB"
            UI_INTERACTION_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_UIInteractionCB"
            MULTIUSER_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_multiuserCB"
            IPC_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_IPCCB"
            NETWORK_INFO_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_getNetworkInfoCB"
            CHANGE_NETWORK_INFO_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_changeNetworkInfoCB"
            SIMULATION_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_simulationCB"
            USR_PREFERENCES_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_userPreferencesCB"
            MISC_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_3.m_securityGrpbox.m_miscCB"

        class Setting:
            ON_DEMAND_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_2.m_startupGrpbox.m_onDemandRB"
            DISABLE_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_2.m_startupGrpbox.m_disabledRB"
            ON_STARTUP_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_2.m_startupGrpbox.m_onStartupRB"
            ALWAYS_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_2.m_savingGrpbox.m_alwaysRB"
            PROMPT_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_2.m_savingGrpbox.m_promptRB"
            NEVER_CHKBOX = ".tabWidget.qt_tabwidget_stackedwidget.tab_2.m_savingGrpbox.m_neverRB"
            
    class Active_Apps:
        DISCONNECT_BUTT = ".m_disconnectBtn"
        APPS_LIST = ".m_activeTW"
        CANCEL_BUTT =".m_cancelBtn"
    class Options:
        PORT_NUM_EDIT = ".m_editPortNumber"
        START_LISTENING_BUTT = ".m_btnStartListening"
        STOP_LISTENING_BUTT = ".m_btnStopListening"
        ALLOW_REMOTE_APPLICATIONS_CHKBOX = ".chkAllowRemoteApps"
        ALWAYS_LISTEN_ON_START_CHKBOX = ".m_chkListenStartup"
        OK_BUTT = ".m_btnOK"
        CANCEL_BUTT = ".m_btnCancel"
    class Log:
        IPC_LOG =  ".m_txtMessage"
        CLEAR_BUTT = ".btnClear"
        CLOSE_BUTT = ".btnClose"
        