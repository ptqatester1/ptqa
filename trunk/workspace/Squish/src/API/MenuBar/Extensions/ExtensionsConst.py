#*******************************************************************************
#@author: Tuan Hoang
#@summary: ExtensionsConst contains the common constants used in Extensions menu
#*******************************************************************************
class ExtensionsConst:
    MENU_BAR = ":CAppWindowBase.m_pMenubar"
    EXTENSIONS = "Extensions"
    EXTENSIONS_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu"
    EXTENSIONS_IPC_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu.extensionsIPCAction"
    EXTENSIONS_SCRIPTING_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu.menu_Scripting"
    EXTENSION_MULTIUSER_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu.extensionsMUAction"
    ENVIRONMENT_OPTIONS = "Environment Options..."
    CLEAR_TERMINAL_AGENT = "Clear Terminal Agent"
    WAN_MULTIUSER_AGENT = "WAN Multiuser Agent"
    LAN_MULTIUSER_AGENT = "LAN Multiuser Agent"
    PT_UPDATER = "PT Updater"
    ACTIVITY_WIZARD = "Activity Wizard ..."
    UPNP_MULTIUSER = "UPnP Multiuser"
    MULTIUSER = "Multiuser"
    IPC = "IPC"
    SCRIPTING = "Scripting"
    AUTO_TEAM_CLIENT_CREATOR = "Auto Team Client Creator"
    MARVEL = 'Marvel'
    
    class ClearTerminalAgent:
        CLEAR_TERMINAL_AGENT_WINDOW = ":Terminal"
        
    class WANMultiuserAgent:
        WAN_MULTIUSER_AGENT_WINDOW = ":WAN Multiuser Agent"
        
    class LANMultiuserAgent:
        LAN_MULTIUSER_AGENT_WINDOW = ":LAN Multiuser Agent"
        
    class PTUpdater:
        PT_UPDATER_WINDOW = ""
    
    class Multiuser:
        MULTI_USER_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu.extensionsMUAction"
        LISTEN = "Listen ..."
        PORT_VISIBILITY = "Port Visibility ..."
        SAVE_OFFLINE = "Save Offline Copy As ..."
        OPTIONS = "Options ..."  
        
        class Listen:
            LISTEN_WINDOW = ":CAppWindowBase.CBaseMUListenDlg"
            PORT_NUM_EDIT = ":CAppWindowBase.CBaseMUListenDlg.m_editPortNumber"
            PASSWORD_EDIT = ":CAppWindowBase.CBaseMUListenDlg.m_editpasswd"
            ACCEPT_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBox.m_alwaysAccept"
            DENY_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBox.m_alwaysDeny"
            PROMPT_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBox.m_prompt"
            NEW_RN_ACCEPT_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBoxNewRN.radioAlwaysAcceptNewRN"
            NEW_RN_DENY_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBoxNewRN.radioAlwaysDenyNewRN"
            NEW_RN_PROMPT_CHKBOX = ":CAppWindowBase.CBaseMUListenDlg.groupBoxNewRN.radioAlwaysPromptNewRN"
            STOP_LISTEN_BUTT = ":CAppWindowBase.CBaseMUListenDlg.m_btnStartListening"
            OK_BUTT = ":CAppWindowBase.CBaseMUListenDlg.m_btnOk"
            CANCEL_BUTT = ":CAppWindowBase.CBaseMUListenDlg.m_btnCancel"
            
        class Port_Visibility:
            PORT_VISIBILITY_WINDOW = ":CAppWindowBase.Dialog"
            NETWORK_TREE_VIEW = ":CAppWindowBase.Dialog.portTreeView"
            OK_BUTT = ":CAppWindowBase.Dialog.btnOK"
            CANCEL_BUTT = ":CAppWindowBase.Dialog.btnCancel"
            
        class Options:
            OPTIONS_WINDOW = ":CBaseMUOptoinsDlg"
            REMOTE_SAVING_CHKBOX = ":CBaseMUOptoinsDlg.chkAllowRemoteSaving"
            DEPTH_EDIT = ":CBaseMUOptoinsDlg.m_editDepth"
            LISTEN_CHKBOX = ":CBaseMUOptoinsDlg.chkAlwaysListen"
            ALLOW_PEERS_CHKBOX = ":CBaseMUOptoinsDlg.chkAllowPeers"
            FWD_BROADCAST_CHKBOX = ":CBaseMUOptoinsDlg.chkAllowBroadcast"
            OK_BUTT = ":CBaseMUOptoinsDlg.m_btnOK"
            CANCEL_BUTT = ":CBaseMUOptoinsDlg.m_btnCancel"
        
        class Save_OffLine:
            SAVE_OFFLINE_WINDOW = ":CAppWindowBase.QFileDialog"
            FILE_NAME_EDIT = ":CAppWindowBase.QFileDialog.fileNameEdit"
            SAVE_BUTT = ":CAppWindowBase.QFileDialog.buttonBox.Save"
            CANCEL_BUTT = ":CAppWindowBase.QFileDialog.buttonBox.Cancel"
            
    class Ipc:
        IPC_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu.extensionsIPCAction"
        CONFIGURE_APPS = "Configure Apps ..."
        ACTIVE_APPS = "Show Active Apps ..."
        OPTIONS = "Options ..."
        LOG = "Log ..."
        
        class Configure_Apps:
            CONFIGURE_APPS_WINDOW = ":BaseCEPListDialog"
            TAB_BAR = ".tabWidget.qt_tabwidget_tabbar"
            SETTING_TAB = "Settings"
            DESCRIPTION_TAB = "Description"
            SECURITY_TAB = "Security"
            SAVE_BUTT = ".m_saveBtn"
            OK_BUTT = ":BaseCEPListDialog.m_okBtn"
            CANCEL_BUTT = ".m_cancelBtn"
            REMOVE_BUTT = ".groupBox_5.m_removeBtn"
            APPS_LIST = ".groupBox_5.m_cepList"
            LAUNCH_BUTT = ".groupBox_5.m_launchBtn"
            ADD_BUTT = ".groupBox_5.m_addBtn"
            
        class Active_Apps:
            ACTIVE_APPS_WINDOW = ":BaseCEPActiveDialog"
            DISCONNECT_BUTT = ".m_disconnectBtn"
            APPS_LIST = ".m_activeTW"
            CANCEL_BUTT = ":BaseCEPActiveDialog.m_cancelBtn"
        
        class Options:
            OPTIONS_WINDOW = ":CBaseOptionsDialog"
            PORT_NUM_EDIT = ".m_editPortNumber"
            START_LISTENING_BUTT = ".m_btnStartListening"
            STOP_LISTENING_BUTT = ".m_btnStopListening"
            ALLOW_REMOTE_APPLICATIONS_CHKBOX = ".chkAllowRemoteApps"
            ALWAYS_LISTEN_ON_START_CHKBOX = ".m_chkListenStartup"
            OK_BUTT = ".m_btnOK"
            CANCEL_BUTT = ":CBaseOptionsDialog.m_btnCancel"
        
        class Log:
            LOG_WINDOW = ":CBaseCEPMessageDlg"
            IPC_LOG =  ".m_txtMessage"
            CLEAR_BUTT = ".btnClear"
            CLOSE_BUTT = ":CBaseCEPMessageDlg.btnClose"
            
    class Scripting:
        SCRIPTING_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu.menu_Scripting"
        CONFIGURE_PT_SCRIPT_MODULES = "Configure PT Script Modules ..."
        NEW_PT_SCRIPT_MODULE = "New PT Script Module ..."
        EDIT_FILE_SCRIPT_MODULE = "Edit File Script Module ..."
        CONFIGURE_GLOBAL_CUSTOM_INTERFACES = "Configure Global Custom Interfaces ..."
        CONFIGURE_FILE_CUSTOM_INTERFACES = "Configure File Custom Interfaces ..."
        class Configure_PT_Script_Modules:
            CONFIGURE_PT_SCRIPT_MODULE_WINDOW = ":BaseCEPListDialog"
            TAB_BAR = ":BaseCEPListDialog.tabWidget.qt_tabwidget_tabbar"
            SETTING_TAB = "Settings"
            DESCRIPTION_TAB = "Description"
            SECURITY_TAB = "Security"
            OK_BUTT = "Configure PT Script Modules.m_okBtn"
            OK_BUTT2 = ":ScriptingInterface.Packet Tracer.qt_msgbox_buttonbox.OK"
            CANCEL_BUTT = ":ScriptingInterface.QFileDialog.buttonBox.Cancel"
            YES_BUTT = ":ScriptingInterface.Cisco Packet Tracer.qt_msgbox_buttonbox.Yes"
            SCRIPT_LIST = ":BaseCEPListDialog..groupBox_5.m_cepList"
            REMOVE_BUTT = ":BaseCEPListDialog.groupBox_5.m_newBtnFrame.m_newBtn"
            ADD_BUTT = ":BaseCEPListDialog.groupBox_5.m_addBtn"
            NEW_BUTT = ":BaseCEPListDialog.groupBox_5.m_removeBtn"
            STOP_BUTT = ":BaseCEPListDialog.groupBox_5.m_launchBtn"
            START_BUTT = ":BaseCEPListDialog.groupBox_5.m_launchBtn"
            EDIT_BUTT = ":BaseCEPListDialog.groupBox_5.m_editBtn"
            class Add_Script_Dialog:
                ADD_SCRIPT_FILENAME_EDIT = ":BaseCEPListDialog.QFileDialog.fileNameEdit"
                ADD_SCRIPT_FILENAME_OPEN_BUTT = ":BaseCEPListDialog.QFileDialog.buttonBox.Open"
                ADD_SCRIPT_FILENAME_CANCEL_BUTT = ":BaseCEPListDialog.QFileDialog.buttonBox.Cancel"
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
                ON_DEMAND_CHKBOX = ":BaseCEPListDialog.tabWidget.qt_tabwidget_stackedwidget.tab_2.m_startupGrpbox.m_onDemandRB"
                DISABLE_CHKBOX = ":BaseCEPListDialog.tabWidget.qt_tabwidget_stackedwidget.tab_2.m_startupGrpbox.m_disabledRB"
                ON_STARTUP_CHKBOX = ":BaseCEPListDialog.tabWidget.qt_tabwidget_stackedwidget.tab_2.m_startupGrpbox.m_onStartupRB"
                ALWAYS_CHKBOX = ""
                PROMPT_CHKBOX = ""
                NEVER_CHKBOX = ""
        class New_PT_Script_Module:
            NEW_PT_SCRIPT_MODULE_WINDOW = ":ScriptingInterface"
            CONFIRM_EXIT_YES = ":ScriptingInterface.Packet Tracer.qt_msgbox_buttonbox.Yes"
        class Edit_File_Script_Module:
            EDIT_FILE_SCRIPT_MODULE_WINDOW = ":ScriptingInterface"
        class Configure_Global_Custom_Interfaces:
            CONFIGURE_GLOBAL_CUSTOM_INTERFACES_WINDOW = ":CAppWindowBase.Admin_Opts"
        class Configure_File_Custom_Interfaces:
            CONFIGURE_FILE_CUSTOM_INTERFACES_WINDOW = ":ConfigCustomInterfaces" 
                       
