from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import Interface, AlgorithmSettings, PopupsConst

class GlobalSettings:
	DISPLAY_NAME_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_displayNameEdit"
	HOSTNAME_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_IOSHostnameEdit"
	NVRAM_ERASE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_nvramEraseBtn"
	NVRAM_ERASE_OK = ":Erase the startup-config file?.qt_msgbox_buttonbox.Yes"
	NVRAM_ERASE_CANCEL = ":Erase the startup-config file?.qt_msgbox_buttonbox.No"
	NVRAM_SAVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_nvramSaveBtn"
	STARTUP_CONF_LOAD_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_loadStartButton"
	STARTUP_CONF_LOAD_OK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.QFileDialog.buttonBox.Open"
	STARTUP_CONF_LOAD_CANCEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.QFileDialog.buttonBox.Cancel"
	STARTUP_CONF_LOAD_FILE_EDITOR = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.QFileDialog.fileNameEdit"
	FILE_ALREADY_EXISTS_DIALOG = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.QFileDialog.Save Configuration'
	STARTUP_CONF_LOAD_OVERWRITE_OK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.QFileDialog.Save Configuration.qt_msgbox_buttonbox.Yes"
	STARTUP_CONF_LOAD_OVERWRITE_CANCEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.Save Configuration.qt_msgbox_buttonbox.No"
	
	STARTUP_CONF_EXPORT_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_saveStartButton"
	STARTUP_CONF_EXPORT_OK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.QFileDialog.buttonBox.Save"
	#STARTUP_CONF_EXPORT_OK = ":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.buttonBox.Open"
	STARTUP_CONF_EXPORT_CANCEL = ":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.buttonBox.Cancel"
	STARTUP_CONF_EXPORT_FILE_EDITOR = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.fileNameEdit"
	STARTUP_CONF_EXPORT_OVERWRITE_OK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.Save Configuration.qt_msgbox_buttonbox.Yes"
	STARTUP_CONF_EXPORT_OVERWRITE_CANCEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.Save Configuration.qt_msgbox_buttonbox.No"
	STARTUP_CONF_SAVE_SUCCESSFUL_DIALOG = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.Packet Tracer"
	STARTUP_CONF_SAVE_SUCCESSFUL_LABEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.Packet Tracer.qt_msgbox_label"
	STARTUP_CONF_SAVE_SUCCESSFUL_OK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.Packet Tracer.qt_msgbox_buttonbox.OK"
	
	RUNNING_CONF_MERGE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_loadRunButton"
	RUNNING_CONF_MERGE_OK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.buttonBox.Open"
	RUNNING_CONF_MERGE_CANCEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.buttonBox.Cancel"
	RUNNING_CONF_MERGE_FILE_EDITOR = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.fileNameEdit"
	
	RUNNING_CONF_EXPORT_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_saveRunButton"
	RUNNING_CONF_EXPORT_OK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.buttonBox.Save"
	RUNNING_CONF_EXPORT_CANCEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.buttonBox.Cancel"
	RUNNING_CONF_EXPORT_FILE_EDITOR = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.fileNameEdit"
	RUNNING_CONF_EXPORT_OVERWRITE_OK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.Save Configuration.qt_msgbox_buttonbox.Yes"
	RUNNING_CONF_EXPORT_OVERWRITE_CANCEL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.QFileDialog.Save Configuration.qt_msgbox_buttonbox.No"
	
	SERVER_ADDRESS = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_editServerIP"
	
class Routing:
	NETWORK_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterStaticCfg.m_networkEdit"
	NETMASK_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterStaticCfg.m_maskEdit"
	NEXTHOP_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterStaticCfg.m_nextHopEdit"
	ADD_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterStaticCfg.m_addButton"
	REMOVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterStaticCfg.m_removeButton"
	LISTVIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterStaticCfg.m_networkTableWidget"
	RIP_NETWORK_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterRipCfg.m_networkEdit"
	RIP_ADD_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterRipCfg.m_addButton"
	RIP_REMOVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterRipCfg.m_removeButton"
	RIP_LISTVIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CBaseRouterRipCfg.m_networkListView"
	
class Switching:
	VLAN_NAME_LBL = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_vlanNameLabel'
	VLAN_NUM_LBL = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_vlanNumberLabel'
	VLAN_NAME_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_vlanNameEdit"
	VLAN_NUM_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_vlanNumberEdit"
	VLAN_ADD_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_addButton"
	VLAN_REMOVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_removeButton"
	VLAN_TABLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_vlanTable"
	VLAN_TABLE_3560 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_vlanTable"
	VLAN_NAME_EDIT_3560 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_vlanNameEdit"
	VLAN_NUM_EDIT_3560 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_vlanNumberEdit"
	VLAN_ADD_BUTT_3560 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_addButton"
	VLAN_REMOVE_BUTT_3560 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCiscoDeviceVlanConfig.m_removeButton"
	
class ConfigConst:
	settings = GlobalSettings
	algorithmSettings = AlgorithmSettings
	routing = Routing
	vlan = Switching
	interface = Interface
	popups = PopupsConst
	EQUIVALENT_IOS_COMMANDS = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCommandLine1'
	EQUIVALENT_ASA_COMMANDS_VIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.m_eqPlaceHolder"