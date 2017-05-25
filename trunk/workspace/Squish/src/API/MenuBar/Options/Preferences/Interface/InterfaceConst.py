#********************************************************************************
#@author: Tuan Hoang
#@summary: InterfaceConst contains the common constants used in the Interface tab
#********************************************************************************
class InterfaceConst:
    PREFERENCES_WINDOW = ":CAppWindowBase.Admin_Opts"
    INTERFACE_WINDOW = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab"
    TAB_BAR = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_tabbar"
    INTERFACE = "Interface"
    
    #Customize User Experience
    CHECKBOX_SECTION = ':CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox'
    SHOW_ANIMATION = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.AnimationGBox"
    PLAY_SOUND = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.SoundGBox"
    SHOW_DEVICE_MODEL_LABEL = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.iTbShowDeviceModelCkBox"
    SHOW_DEVICE_NAME_LABEL = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.HideDeviceLabelGBox"
    ALWAYS_SHOW_PORT_LABEL = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.ShowPortsCB"
    DISABLE_AUTO_CABLE = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.iTbDisableAutoCableCkBox"
    USE_METRIC_SYSTEM = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.UseMetricCB"
    SHOW_LINK_LIGHTS = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.ShowLinkLightsCB"
    PLAY_TELEPHONY_SOUND = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.TelephonySoundGBox"
    SHOW_QOS_STAMPS = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.HideQoSStampCB"
    SHOW_PORT_LABELS_ON_MOUSEOVER = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.DontShowPortsCB"
    ENABLE_CABLE_LENGTH_EFFECTS = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.EnableCableLengthsCB"
    USE_CLI_AS_DEFAULT_TAB = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.UseCliDefaultTab"
    SHOW_CABLE_INFO_POPUP_PHYSICAL_WORKSPACE = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbCustomizeGroupBox.CableInfoPopup"
    #Logging
    ENABLE_LOGGING = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbLogGroupBox.LogEnableCB"
    EXPORT_LOG_BUTTON = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbLogGroupBox.LogExportBtn"
    EXPORT_LOG_DIALOG = ":CAppWindowBase.Admin_Opts.QFileDialog"
    EXPORT_LOG_DIALOG_CLOSE = ""
    EXPORT_LOG_DIALOG_FILENAME_EDIT = ":CAppWindowBase.Admin_Opts.QFileDialog.fileNameEdit"
    EXPORT_LOG_DIALOG_OK = ":CAppWindowBase.Admin_Opts.QFileDialog.buttonBox.Save"
    EXPORT_LOG_DIALOG_CANCEL = ":CAppWindowBase.Admin_Opts.QFileDialog.buttonBox.Cancel"
    
    OVERWRITE_FILE_DIALOG = ":Overwrite File?"
    OVERWRITE_FILE_DIALOG_LABEL = ":Overwrite File?.qt_msgbox_label"
    OVERWRITE_FILE_DIALOG_YES = ":Overwrite File?.qt_msgbox_buttonbox.Yes"
    OVERWRITE_FILE_DIALOG_NO = ":Overwrite File?.qt_msgbox_buttonbox.No"
    
    SAVE_LOG_DIALOG = ":CAppWindowBase.Admin_Opts.QFileDialog.Save Log File"
    SAVE_LOG_DIALOG_LABEL = ":CAppWindowBase.Admin_Opts.QFileDialog.Save Log File.qt_msgbox_label"
    SAVE_LOG_DIALOG_YES = ":CAppWindowBase.Admin_Opts.QFileDialog.Save Log File.qt_msgbox_buttonbox.Yes"
    SAVE_LOG_DIALOG_NO = ":CAppWindowBase.Admin_Opts.QFileDialog.Save Log File.qt_msgbox_buttonbox.No"
    
    #Language
    LANGUAGE_BOX = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_languageBox.m_langListView"
    CHANGE_LANGUAGE_BUTTON = ":CAppWindowBase.Admin_Opts.m_mainOptionsTabWidget.qt_tabwidget_stackedwidget.m_interfaceTab.m_iTbLangGroupBox.ChangeLangBtn"
    CHANGE_LANGUAGE_POPUP_DIALOG = ':CAppWindowBase.Admin_Opts.Change Language -- Packet Tracer'
    CHANGE_LANGUAGE_OK = ":CAppWindowBase.Admin_Opts.Change Language -- Packet Tracer.qt_msgbox_buttonbox.OK"    