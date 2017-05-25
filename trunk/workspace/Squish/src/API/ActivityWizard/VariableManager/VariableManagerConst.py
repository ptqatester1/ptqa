#*************************************************************************************
#@author: Tuan Hoang
#@summary: VariableManagerConst contains the common constants used in Variable Manager
#*************************************************************************************
class VariableManagerConst:
    VARIABLE_MANAGER = ":Activity_Wizard.m_navigationBtnGrpBox.VariableManagerBtn"
    TAB_BAR = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_tabbar"
    SHOW_VARIABLE_MANAGER_INTERFACE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.m_varIntroTab.groupBox_3.m_enableVarManCB"
    LABEL_INTRO = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.textLabel1_3_4"
    
    #TAB NAMES
    INTRODUCTION = "Introduction"
    SEEDS = "Seeds"
    NUMBER = "Number"
    STRINGS = "Strings"
    IP_ADDRESSES = "IP Addresses"
    
    #Import/Export shared between all import/export functions
    FILE_DIALOG = ':Activity_Wizard.QFileDialog'
    IMPORT_EXPORT_SAVE_BUTTON = ":Activity_Wizard.QFileDialog.buttonBox.Save"
    IMPORT_EXPORT_OPEN_BUTTON = ":Activity_Wizard.QFileDialog.buttonBox.Open"
    IMPORT_EXPORT_CANCEL_BUTTON = ":Activity_Wizard.QFileDialog.buttonBox.Cancel"
    IMPORT_EXPORT_FILENAME_EDIT = ":Activity_Wizard.QFileDialog.fileNameEdit"
    IMPORT_EXPORT_REPLACE_DIALOG = ":Activity_Wizard.QFileDialog.Export Seeds" 
    IMPORT_EXPORT_REPLACE_FILE_OK = ":Activity_Wizard.QFileDialog.Export Seeds.qt_msgbox_buttonbox.Yes"
    IMPORT_EXPORT_REPLACE_FILE_NO = ":Activity_Wizard.QFileDialog.Export Seeds.qt_msgbox_buttonbox.No"
    
    TABLE_LINE_EDIT_ENDING = '.qt_scrollarea_viewport.QExpandingLineEdit1'#TableName + TABLE_LINE_EDIT_ENDING
    TABLE_COMBO_BOX_ENDING = '.qt_scrollarea_viewport.QComboBox'#TableName + TABLE_COMBO_BOX_ENDING + (COLUMN_NUMBER - 1)
    
    #SEEDS TAB
    SEEDS_TABLE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.SeedsTab.groupBox_4.m_seedTbl"
    SEEDS_ENTRY = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.SeedsTab.groupBox_4.m_seedTbl"
    SEEDS_ENTRY_EDIT = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.SeedsTab.groupBox_4.m_seedTbl.qt_scrollarea_viewport.QExpandingLineEdit1"
    SEEDS_IMPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.SeedsTab.groupBox_4.m_importSeedsBtn"
    SEEDS_EXPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.SeedsTab.groupBox_4.m_exportSeedsBtn"
    
    #NUMBER TAB
    NUMBERS_POOLS_TABLE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_5.m_numberPoolTbl"
    NUMBERS_POOLS_ENTRY = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_5.m_numberPoolTbl"
    NUMBERS_POOLS_EDIT = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_5.m_numberPoolTbl.qt_scrollarea_viewport.QExpandingLineEdit1"
    NUMBERS_POOLS_IMPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_5.m_importNumberPoolsBtn"
    NUMBERS_POOLS_EXPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_5.m_exportNumberPoolsBtn"
    
    NUMBERS_VARIABLES_TABLE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_6.m_numVariableTbl"
    NUMBERS_VARIABLES_ENTRY = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_6.m_numVariableTbl"
    NUMBERS_VARIABLES_EDIT = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_6.m_numVariableTbl.qt_scrollarea_viewport.QExpandingLineEdit1"
    NUMBERS_VARIABLES_POOLNAME_COMBO = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_6.m_numVariableTbl.qt_scrollarea_viewport.QComboBox1"
    NUMBERS_VARIABLES_VALUETYPE_COMBO = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_6.m_numVariableTbl.qt_scrollarea_viewport.QComboBox2"
    NUMBERS_VARIABLES_IMPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_6.m_importNumberVarsBtn"
    NUMBERS_VARIABLES_EXPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.NumberTab.groupBox_6.m_exportNumberVarsBtn"

    #STRINGS TAB
    STRINGS_POOLS_TABLE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_7.m_stringPoolTbl"
    STRINGS_POOLS_TABLE_0_1 = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_7.m_stringPoolTbl.item_0/1"
    STRINGS_POOLS_NAME_BASE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_7.m_stringPoolTbl."
    STRINGS_POOLS_ENTRY = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_7.m_stringPoolTbl"
    STRINGS_POOLS_EDIT = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_7.m_stringPoolTbl.qt_scrollarea_viewport.QExpandingLineEdit1"
    STRINGS_POOLS_IMPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_7.m_importStringPoolsBtn"
    STRINGS_POOLS_EXPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_7.m_exportStringPoolsBtn"
    
    STRINGS_VARIABLES_TABLE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_8.m_strVariableTbl"
    STRINGS_VARIABLES_ENTRY = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_8.m_strVariableTbl"
    STRINGS_VARIABLES_EDIT = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_8.m_strVariableTbl.qt_scrollarea_viewport.QExpandingLineEdit1"
    STRINGS_VARIABLES_POOLNAME_COMBO = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_8.m_strVariableTbl.qt_scrollarea_viewport.QComboBox1"
    STRINGS_VARIABLES_POOLNAME_COMBO_BASE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_8.m_strVariableTbl.qt_scrollarea_viewport.QComboBox"
    STRINGS_VARIABLES_VALUETYPE_COMBO = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_8.m_strVariableTbl.qt_scrollarea_viewport.QComboBox2"
    STRINGS_VARIABLES_IMPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_8.m_importStringVarsBtn"
    STRINGS_VARIABLES_EXPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_8.m_exportStringVarsBtn"
    STRINGS_VARIABLES_SCROLL_BAR = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.StringTab.groupBox_8.m_strVariableTbl.qt_scrollarea_vcontainer.QScrollBar1"
    
    #IP ADDRESSES TAB
    IP_POOLS_TABLE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_9.m_ipPoolTbl"
    IP_POOLS_ENTRY = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_9.m_ipPoolTbl"
    IP_POOLS_EDIT = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_9.m_ipPoolTbl.qt_scrollarea_viewport.QExpandingLineEdit1"
    IP_POOLS_IMPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_9.m_importIpPoolsBtn"
    IP_POOLS_EXPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_9.m_exportIpPoolsBtn"
    
    IP_VARIABLES_TABLE = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_10.m_ipVariableTbl"
    IP_VARIABLES_ENTRY = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_10.m_ipVariableTbl"
    IP_VARIABLES_EDIT = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_10.m_ipVariableTbl.qt_scrollarea_viewport.QExpandingLineEdit1"
    IP_VARIABLES_POOLNAME_COMBO = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_10.m_ipVariableTbl.qt_scrollarea_viewport.QComboBox1"
    IP_VARIABLES_VALUETYPE_COMBO = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_10.m_ipVariableTbl.qt_scrollarea_viewport.QComboBox2"
    IP_VARIABLES_IMPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_10.m_importIpVarsBtn"
    IP_VARIABLES_EXPORT_BUTTON = ":Activity_Wizard.m_contents.VariableManager.m_variableManagerTabs.qt_tabwidget_stackedwidget.IpAddressTab.groupBox_10.m_exportIpVarsBtn"
    
    RANDOM = "Random"
    ELEMENT_POSITION = "Element Position"
    ENTIRE_RANGE = "Entire Range"