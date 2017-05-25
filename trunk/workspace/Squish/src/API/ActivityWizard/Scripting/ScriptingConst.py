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
    DEBUG_BUTTON = '.tabs.qt_tabwidget_stackedwidget.infoTab.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.groupBox_8.btnDebug'

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

class GeneralTab:
    info = GeneralTabInfo
    publisherSigning = GeneralTabPublisherSigning
    password = GeneralTabPassword
    startup = GeneralTabStartup
    securityPrivileges = GeneralTabSecurityPrivileges

class ScriptEnginTab:
    SCRIPT_LIST = '.tabs.qt_tabwidget_stackedwidget.Form.listFiles'
    SCRIPT_TEXT = '.tabs.qt_tabwidget_stackedwidget.Form.textEditor'
    ADD_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnAdd'
    REMOVE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnRemove'
    RENAME_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnRename'
    IMPORT_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnImport'
    IMPORT_DIR_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnImportDir'
    EXPORT_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnExport'
    RUN_FILE_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnReloadFile'
    STOP_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnStart'
    START_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnStart'
    DEBUG_BUTTON = '.tabs.qt_tabwidget_stackedwidget.Form.btnDebug'

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

class Tabs:
    INFO = '.tabs.qt_tabwidget_tabbar.TabItem1'
    GENREAL = '.tabs.qt_tabwidget_tabbar.TabItem2'
    SCRIPT_ENGIN = '.tabs.qt_tabwidget_tabbar.TabItem3'
    CUSTOM_INTERFACE = '.tabs.qt_tabwidget_tabbar.TabItem4'
    DATA_STORE = '.tabs.qt_tabwidget_tabbar.TabItem5'

class ScriptingConst:
    info = '.tabs.qt_tabwidget_tabbar.TabItem1'
    general = '.tabs.qt_tabwidget_tabbar.TabItem2'
    scriptEngin = '.tabs.qt_tabwidget_tabbar.TabItem3'
    customInterfaces = '.tabs.qt_tabwidget_tabbar.TabItem4'
    dataStore = '.tabs.qt_tabwidget_tabbar.TabItem5'
