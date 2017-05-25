##Chris Allen

class InfoTab:
    SELECT_TEMPLATE_COMBO = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_3.cbTemplates'
    SCRIPT_MODULE_GENERAL_INFO_GOTO_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_4.btnGeneral'
    SCRIPT_ENGINE_FILES_GOTO_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_6.btnSE'
    CUSTOM_INTERFACE_FILES_GOTO_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_7.btnCI'
    DATA_STORE_GOTO_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_10.btnDS'
    SAVE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_9.btnSave'
    EXPORT_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_9.btnExport'
    TRANSLATE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_9.btnTranslate'
    STOP_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_8.btnStart'
    START_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_8.btnStart'
    DEBUG_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_8.btnDebug'
    WARNING_POPUP_DIALOG = ':Activity_Wizard.m_contents.ScriptingInterface.Packet Tracer'
    WARNING_POPUP_YES_BUTTON = ':Activity_Wizard.m_contents.ScriptingInterface.Packet Tracer.qt_msgbox_buttonbox.Yes'
    WARNING_POPUP_NO_BUTTON = ':Activity_Wizard.m_contents.ScriptingInterface.Packet Tracer.qt_msgbox_buttonbox.No'
    
class GeneralTabInfo:
    NAME = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox.txtName'
    ID = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox.txtId'
    VERSION = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox.txtVersion'
    AUTHOR = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox.txtAuthor'
    CONTACT = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox.txtContact'
    DESCRIPTION = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox.txtDescription'
    
class GeneralTabPublisherSigning:
    BROWSE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox_5.btnSign'
    CLEAR_BUTTON = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox_5.btnClearSign'

class GeneralTabPassword:
    PASSWORD = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox_2.txtPassword'
    CONFIRM_PASSWORD = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox_2.txtConfirmedPassword'
    ENABLE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox_2.btnEnablePass'
    DISABLE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupBox_2.btnDisablePass'
    
class GeneralTabStartup:
    ON_STARTUP_RADIO = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupStartup.radioOnStartup'
    ON_DEMAND_RADIO = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupStartup.radioOnDemand'
    DISABLED_RADIO = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupStartup.radioDisabled'
    
class GeneralTabSecurityPrivileges:
    APPLICATION_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkApplication'
    ACTIVITY_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkActivity'
    FILE_OPERATIONS_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkFile'
    CHANGE_USER_INTERFACE_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkUi'
    MULTIUSER_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkMultiuser'
    IPC_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkIpc'
    GET_NETWORK_INFO_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkGetNetwork'
    CHANGE_NETWORK_INFO_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkChangeNetwork'
    SIMULATION_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkSimulation'
    USER_PREFERENCES_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkPreferences'
    MISC_UI_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkMisc'
    ALLOW_OPENING_FILE_EVEN_IF_SECURITY_PRIVILEGES_NOT_GRANTED_CHECKBOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges.chkOpenIfDenied'
    GROUP_BOX = '.tabs.qt_tabwidget_stackedwidget.generalTab.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.groupPrivileges'

class GeneralTab:
    info = GeneralTabInfo
    publisherSigning = GeneralTabPublisherSigning
    password = GeneralTabPassword
    startup = GeneralTabStartup
    securityPrivileges = GeneralTabSecurityPrivileges
    SIGN_SCRIPT_RESIGN_AND_EDIT = 'Activity_Wizard.m_contents.ScriptingInterface.Sign Script?.qt_msgbox_buttonbox.Resign and Edit'
    SIGN_SCRIPT_READ_ONLY = 'Activity_Wizard.m_contents.ScriptingInterface.Sign Script?.qt_msgbox_buttonbox.Read Only'
    SIGN_SCRIPT_EDIT_UNSIGNED = 'Activity_Wizard.m_contents.ScriptingInterface.Sign Script?.qt_msgbox_buttonbox.Edit Unsigned'
    
class ScriptEngineTab:
    SCRIPT_LIST = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.listFiles'
    SCRIPT_TEXT = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.textEditor'
    ADD_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnAdd'
    REMOVE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnRemove'
    RENAME_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnRename'
    IMPORT_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnImport'
    IMPORT_DIR_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnImportDir'
    EXPORT_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnExport'
    RUN_FILE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnReloadFile'
    STOP_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnStart'
    START_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnStart'
    DEBUG_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnDebug'
    FILE_DIALOG_OPEN = ".tabs.qt_tabwidget_stackedwidget.CScriptEditor1.QFileDialog.buttonBox.Open"
    FILE_DIALOG_NAME_EDIT = ".tabs.qt_tabwidget_stackedwidget.CScriptEditor1.QFileDialog.fileNameEdit"
    ENTER_SCRIPT_ID_DIALOG = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.Enter Script ID'
    ENTER_SCRIPT_ID_FILENAME = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.Enter Script ID.QLineEdit1'
    ENTER_SCRIPT_ID_OK_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.Enter Script ID.QDialogButtonBox1.OK'
    ENTER_SCRIPT_ID_CANCEL_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.Enter Script ID.QDialogButtonBox1.Cancel'
    EXPORT_SCRIPT_CANCEL_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.QFileDialog.buttonBox.Cancel'
    EXPORT_IMPORT_FILE_WINDOW = ':Activity_Wizard.m_contents.ScriptingInterface.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.QFileDialog'
    EXPORT_FILE_SAVE_BTN = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.QFileDialog.buttonBox.Save'
    EXPORT_FILE_OVERWRITE_YES_BTN = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.QFileDialog.Export Script File.qt_msgbox_buttonbox.Yes'
    EXPORT_FILE_OVERWRITE_MESSAGE = ':Activity_Wizard.m_contents.ScriptingInterface.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.QFileDialog.Export Script File'
    REMOVE_SCRIPT_YES_BTN = '.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.Packet Tracer.qt_msgbox_buttonbox.Yes'

class CustomInterfacesTab:
    INTERFACE_LIST = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.listFiles'
    INTERFACE_TEXT = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.textEditor'
    ADD_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnAdd'
    REMOVE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnRemove'
    RENAME_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnRename'
    IMPORT_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnImport'
    IMPORT_DIR_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnImportDir'
    EXPORT_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnExport'
    RUN_FILE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnReloadFile'
    STOP_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnStart'
    START_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnStart'
    DEBUG_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CCustomInterfaceEditor1.btnDebug'

class DataStoreTab:
    DATA_STORE_LIST = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.listFiles'
    DATA_STORE_TEXT = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.textEditor'
    ADD_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnAdd'
    REMOVE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnRemove'
    RENAME_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnRename'
    IMPORT_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnImport'
    IMPORT_DIR_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnImportDir'
    EXPORT_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnExport'
    RUN_FILE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnReloadFile'
    STOP_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnStart'
    START_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnStart'
    DEBUG_BUTTON = '.tabs.qt_tabwidget_stackedwidget.CDataStoreEditor1.btnDebug'


class DebuggerBasic:
    DIALOG_WINDOW = '.m_simpleDebugWidget'
    SWITCH_TO_FULL_DEBUGGER_BUTTON = '.m_simpleDebugWidget.m_switchToFullBtn'
    OUTPUT_FIELD = '.m_simpleDebugWidget.m_debugTE'
    INPUT_FIELD = '.m_simpleDebugWidget.cmd'

class DebuggerAdvanced:
    PLAY_BUTTON = '.QMainWindow1.qtscriptdebugger_standardToolBar.Continue'

class Debugger:
    basic = DebuggerBasic
    advanced = DebuggerAdvanced
    
class Tabs:
    TABBAR = '.tabs.qt_tabwidget_tabbar'
    INFO = '.tabs.qt_tabwidget_tabbar.TabItem1'
    GENREAL = '.tabs.qt_tabwidget_tabbar.TabItem2'
    SCRIPT_ENGIN = '.tabs.qt_tabwidget_tabbar.TabItem3'
    CUSTOM_INTERFACE = '.tabs.qt_tabwidget_tabbar.TabItem4'
    DATA_STORE = '.tabs.qt_tabwidget_tabbar.TabItem5'

class ScriptingConst:
    info = InfoTab
    general = GeneralTab
    scriptEngine = ScriptEngineTab
    customInterfaces = CustomInterfacesTab
    dataStore = DataStoreTab
    debugger = Debugger
    tabs = Tabs
    
    ADD_BUTT = ":BaseCEPListDialog.groupBox_5.m_addBtn"
    OK_BUTT = ":BaseCEPListDialog.m_okBtn"
    SCRIPT_LIST = ":BaseCEPListDialog..groupBox_5.m_cepList"
    REMOVE_BUTT = ":BaseCEPListDialog.groupBox_5.m_removeBtn"
    NEW_BUTT = ":BaseCEPListDialog.groupBox_5.m_newBtnFrame.m_newBtn"
    STOP_BUTT = ":BaseCEPListDialog.groupBox_5.m_launchBtn"
    START_BUTT = ":BaseCEPListDialog.groupBox_5.m_launchBtn"
    EDIT_BUTT = ":BaseCEPListDialog.groupBox_5.m_editBtn"

    class Add_Script_Dialog:
        ADD_SCRIPT_FILENAME_EDIT = ":BaseCEPListDialog.QFileDialog.fileNameEdit"
        ADD_SCRIPT_FILENAME_OPEN_BUTT = ":BaseCEPListDialog.QFileDialog.buttonBox.Open"
        ADD_SCRIPT_FILENAME_CANCEL_BUTT = ":BaseCEPListDialog.QFileDialog.buttonBox.Cancel"

'''
#**************************************************************************
#@author: Alex Leung
#@summary: IPCConst contains the common constants used in IPC
#**************************************************************************
class ScriptingConst:
    SCRIPTING_MENU = ":CAppWindowBase.m_pMenubar.Extensions Menu.menu_Scripting"
    CONFIGURE_PT_SCRIPT_MODULES = "Configure PT Script Modules ..."
    NEW_PT_SCRIPT_MODULE = "New PT Script Module ..."
    EDIT_PT_SCRIPT_MODULE = "Edit File Script Module ..."
    CONFIGURE_GLOBAL_CUSTOM_INTERFACES = "Configure Global Custom Interfaces ..."
    CONFIGURE_FILE_CUSTOM_INTERFACES = "Configure File Custom Interfaces ..."
    class FileScriptModule:
        TAB_BAR = ":ScriptingInterface.tabs.qt_tabwidget_tabbar"
        class ScriptEngine:
            START_STOP_BUTTON = ":ScriptingInterface.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnStart"
            DEBUG_BUTTON = ":ScriptingInterface.tabs.qt_tabwidget_stackedwidget.CScriptEditor1.btnDebug"
        class DebugWindow:
            DEBUG_OUTPUT = ":BaseDebugDialog.m_simpleDebugWidget.m_debugTE"
    class Debugger:
        IOE_DEBUGGER = ':Debug - Internet of Everything'
        FULL_DEBUGGER_BUTTON = '.m_simpleDebugWidget.m_switchToFullBtn'
        DEBUGGER_TEXT = '.m_simpleDebugWidget.m_debugTE'
        
    class Configure_PT_Script_Modules:
        TAB_BAR = ":BaseCEPListDialog.tabWidget.qt_tabwidget_tabbar"
        SETTING_TAB = "Settings"
        DESCRIPTION_TAB = "Description"
        SECURITY_TAB = "Security"
        OK_BUTT = ":BaseCEPListDialog.m_okBtn"
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
    #class New_PT
        
    #class Edit_PT
        
    #class Configure_Global
        
    #class Configure_File
'''