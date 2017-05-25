##Chris Allen

FIRST_PART = '.c_physicalTab.qt_tabwidget_stackedwidget.'
LINKSYS_MIDDLE_PART = 'm_guiTab'
PC_MIDDLE_PART = 'm_DeskTopTab.scrollArea.qt_scrollarea_viewport.desktopScrollAreaWidgetContents.CDesktopApplet1.CWorkstationWebBrowserBase'
LAST_PART = '.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseLinkSysGUI.'

class WirelessTabsConst:	
	BASIC_WIRELESS_SETTINGS_TAB = 'Basic Wireless Settings'
	WIRELESS_SECURITY_TAB = 'Wireless Security'
	WIRELESS_MAC_FILTER_TAB = 'Wireless MAC Filter'
	ADVANCED_WIRELESS_SETTINGS_TAB = 'Advanced Wireless Settings'
	
class ApplicationsAndGamingTabsConst:
	SINGLE_PORT_FORWARDING_TAB = 'Single Port Forwarding'
	DMZ_TAB = 'DMZ'

class AdministrationTabsConst:
	MANAGEMENT_TAB = 'Management'
	FACTORY_DEFAULTS_TAB = 'Factory Defaults'
	FIRMWARE_UPGRADE_TAB = 'Firmware Upgrade'
	
class StatusTabsConst:
	ROUTER_TAB = 'Router'
	LOCAL_NETWORK_TAB = 'Local Network '
	WIRELESS_NETWORK_TAB = 'Wireless Network '

class TabsConst:
	wireless = WirelessTabsConst
	applicationsAndGaming = ApplicationsAndGamingTabsConst
	admininstration = AdministrationTabsConst
	status = StatusTabsConst
	TAB_HEADER = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'm_TabHeader'
	PC_TAB_HEADER = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'm_TabHeader'
	
	SETUP_TAB = 'Setup'
	WIRELESS_TAB = 'Wireless'
	SECURITY_TAB = 'Security'
	ACCESS_RESTRICTIONS_TAB = 'Access\xe2\x80\xa8Restrictions'#PT is unicode and these are the chars for a line break used
	APPLICATIONS_AND_GAMING_TAB = 'Applications\xe2\x80\xa8& Gaming'
	ADMINISTRATION_TAB = 'Administration'
	STATUS_TAB = 'Status'

class InternetConst:
	MAIN_VIEW_AREA = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel'
	CONNECTION_TYPE_COMBO = 	MAIN_VIEW_AREA + '.comboConnectionType'
	CONNECTION_TYPE_COMBO = 	MAIN_VIEW_AREA + '.comboConnectionType'
	CONNECTION_TYPE_DROPDOWN =	MAIN_VIEW_AREA + '.comboConnectionType'
	EDIT_STATIC_IP_1 =	 		MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPOne'
	EDIT_STATIC_IP_1 = 			MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPOne'
	EDIT_STATIC_IP_2 = 			MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPTwo'
	EDIT_STATIC_IP_3 = 			MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPThree'
	EDIT_STATIC_IP_4 = 			MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPFour'
	EDIT_STATIC_MASK_1 = 		MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticMaskOne'
	EDIT_STATIC_MASK_2 = 		MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticMaskTwo'
	EDIT_STATIC_MASK_3 = 		MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticMaskThree'
	EDIT_STATIC_MASK_4 = 		MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticMaskFour'
	EDIT_STATIC_GATEWAY_1 = 	MAIN_VIEW_AREA + '.frameStaticIP.m_editGatewayOne'
	EDIT_STATIC_GATEWAY_2 = 	MAIN_VIEW_AREA + '.frameStaticIP.m_editGatewayTwo'
	EDIT_STATIC_GATEWAY_3 = 	MAIN_VIEW_AREA + '.frameStaticIP.m_editGatewayThree'
	EDIT_STATIC_GATEWAY_4 = 	MAIN_VIEW_AREA + '.frameStaticIP.m_editGatewayFour'
	EDIT_STATIC_DNS1_1 = 		MAIN_VIEW_AREA + '.frameStaticIP.m_editDNS1One'
	EDIT_STATIC_DNS1_2 = 		MAIN_VIEW_AREA + '.frameStaticIP.m_editDNS1Two'
	EDIT_STATIC_DNS1_3 = 		MAIN_VIEW_AREA + '.frameStaticIP.m_editDNS1Three'
	EDIT_STATIC_DNS1_4 = 		MAIN_VIEW_AREA + '.frameStaticIP.m_editDNS1Four'
	PASSWORD = 					MAIN_VIEW_AREA + '.framePPPoE.m_passwdEdit'
	USERNAME = 					MAIN_VIEW_AREA + '.framePPPoE.m_userNameEdit'
	SERVICE_NAME = 				MAIN_VIEW_AREA + '.framePPPoE.m_serviceNameEdit'
	HOSTNAME_LABEL = MAIN_VIEW_AREA + '.frameDHCP.labelHostName'
	CONNECTED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.framePPPoE.m_connectRadioBtn'
	TIME_EDIT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.framePPPoE.m_timeEdit'
	KEEP_ALIVE_BTN = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.framePPPoE.m_keepAliveRadioBtn'
	ALIVE_EDIT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.framePPPoE.m_aliveEdit'


	PC_MAIN_VIEW_AREA = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel'
	PC_CONNECTION_TYPE_COMBO = 	PC_MAIN_VIEW_AREA + '.comboConnectionType'
	PC_CONNECTION_TYPE_COMBO = 	PC_MAIN_VIEW_AREA + '.comboConnectionType'
	PC_CONNECTION_TYPE_DROPDOWN =	PC_MAIN_VIEW_AREA + '.comboConnectionType'
	PC_EDIT_STATIC_IP_1 =	 		PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPOne'
	PC_EDIT_STATIC_IP_1 = 			PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPOne'
	PC_EDIT_STATIC_IP_2 = 			PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPTwo'
	PC_EDIT_STATIC_IP_3 = 			PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPThree'
	PC_EDIT_STATIC_IP_4 = 			PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticIPFour'
	PC_EDIT_STATIC_MASK_1 = 		PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticMaskOne'
	PC_EDIT_STATIC_MASK_2 = 		PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticMaskTwo'
	PC_EDIT_STATIC_MASK_3 = 		PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticMaskThree'
	PC_EDIT_STATIC_MASK_4 = 		PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editStaticMaskFour'
	PC_EDIT_STATIC_GATEWAY_1 = 	PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editGatewayOne'
	PC_EDIT_STATIC_GATEWAY_2 = 	PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editGatewayTwo'
	PC_EDIT_STATIC_GATEWAY_3 = 	PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editGatewayThree'
	PC_EDIT_STATIC_GATEWAY_4 = 	PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editGatewayFour'
	PC_EDIT_STATIC_DNS1_1 = 		PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editDNS1One'
	PC_EDIT_STATIC_DNS1_2 = 		PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editDNS1Two'
	PC_EDIT_STATIC_DNS1_3 = 		PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editDNS1Three'
	PC_EDIT_STATIC_DNS1_4 = 		PC_MAIN_VIEW_AREA + '.frameStaticIP.m_editDNS1Four'
	PC_PASSWORD = 					PC_MAIN_VIEW_AREA + '.framePPPoE.m_passwdEdit'
	PC_USERNAME = 					PC_MAIN_VIEW_AREA + '.framePPPoE.m_userNameEdit'
	PC_SERVICE_NAME = 				PC_MAIN_VIEW_AREA + '.framePPPoE.m_serviceNameEdit'
	PC_HOSTNAME_LABEL = PC_MAIN_VIEW_AREA + '.frameDHCP.labelHostName'
	PC_CONNECTED_RADIO = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.framePPPoE.m_connectRadioBtn'
	PC_TIME_EDIT = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.framePPPoE.m_timeEdit'
	PC_KEEP_ALIVE_BTN = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.framePPPoE.m_keepAliveRadioBtn'
	PC_ALIVE_EDIT = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.framePPPoE.m_aliveEdit'

	
class DhcpReservationConst:
	#Append with 0/0, 0/1. Depending on which item from the table you need
	CLIENT_TABLE = ':CBaseDhcpReservation.m_middlePanel.tableDHCPClient'
	PC_CLIENT_TABLE = ':CBaseDhcpReservation.m_middlePanel.tableDHCPClient'
	CLIENT_TABLE_ITEM = ':CBaseDhcpReservation.m_middlePanel.tableDHCPClient.item_'
	ADD_CLIENT_BUTTON = ':CBaseDhcpReservation.m_middlePanel.btnAddClientFromDhcp'
	MANUALLY_ADDING_CLIENT_TABLE = ':CBaseDhcpReservation.m_middlePanel.tableManualClient'
	MANUALLY_ADDING_CLIENT_CELL_1 = ':CBaseDhcpReservation.m_middlePanel.tableManualClient.qt_scrollarea_viewport.CTableCellLineEdit3.m_inputLine'
	MANUALLY_ADDING_CLIENT_IP_4 = ':CBaseDhcpReservation.m_middlePanel.tableManualClient.qt_scrollarea_viewport.CTableCellIPEdit2.m_octetFour'
	MANUALLY_ADDING_CLIENT_MAC = ':CBaseDhcpReservation.m_middlePanel.tableManualClient.qt_scrollarea_viewport.CTableCellLineEdit4.m_inputLine'
	MANUALLY_ADDING_CLIENT_ADD_BUTTON = ':CBaseDhcpReservation.m_middlePanel.tableManualClient.qt_scrollarea_viewport.CDhcpClientTableCellWidget1.btnDelete'
	CLIENTS_ALREADY_RESERVED_TABLE = ':CBaseDhcpReservation.m_middlePanel.tableReserved'
	SAVE_SETTINGS_BUTTON = ':CBaseDhcpReservation.m_middlePanel.frame1.btnSave'
	CANCEL_CHANGES_BUTTON = ':CBaseDhcpReservation.m_middlePanel.frame1.btnCancel'
	CLOSE_BUTTON = ':CBaseDhcpReservation.m_middlePanel.frame1.btnClose'
	REFRESH_BUTTON = ':CBaseDhcpReservation.m_middlePanel.frame1.btnRefresh'

class NetworkConst:
	dhcpReservation = DhcpReservationConst
	MAIN_VIEW_AREA = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel'
	EDIT_IP_1 = 			MAIN_VIEW_AREA + '.frameDHCP.m_editIPOne'
	EDIT_IP_2 = 			MAIN_VIEW_AREA + '.frameDHCP.m_editIPTwo'
	EDIT_IP_3 = 			MAIN_VIEW_AREA + '.frameDHCP.m_editIPThree'
	EDIT_IP_4 = 			MAIN_VIEW_AREA + '.frameDHCP.m_editIPFour'
	MASK_COMBO = 			MAIN_VIEW_AREA + '.frameDHCP.comboMask'
	MASK_DROPDOWN = 		MAIN_VIEW_AREA + '.frameDHCP.comboMask.QComboBoxPrivateContainer1.QComboBoxListView1'
	DHCP_RADIO_ENABLE =		MAIN_VIEW_AREA + '.frameDHCP.grpBtnRadioDHCP.radioDHCPEnable'
	DHCP_RADIO_DISABLE = 	MAIN_VIEW_AREA + '.frameDHCP.grpBtnRadioDHCP.radioDHCPDisable'
	EDIT_START_IP = 		MAIN_VIEW_AREA + '.frameDHCP.m_editStartIP'
	EDIT_MAX_USER = 		MAIN_VIEW_AREA + '.frameDHCP.m_editMaxUsers'
	SAVE_BUTT = 			MAIN_VIEW_AREA + '.frame.btnSave'
	CANCEL_BUTT = 			MAIN_VIEW_AREA + '.btnCancel'
	START_IP_RANGE = 		MAIN_VIEW_AREA + '.frameDHCP.lblStartIpRange'
	START_IP_LABEL = 		MAIN_VIEW_AREA + '.frameDHCP.labelfirstIP'
	END_IP_RANGE = 			MAIN_VIEW_AREA + '.frameDHCP.lblEndIpRange'
	EDIT_STATIC_DNS1_1 = 	MAIN_VIEW_AREA + '.frameDHCP.m_editStaticDNS1One'
	EDIT_STATIC_DNS1_2 = 	MAIN_VIEW_AREA + '.frameDHCP.m_editStaticDNS1Two'
	EDIT_STATIC_DNS1_3 = 	MAIN_VIEW_AREA + '.frameDHCP.m_editStaticDNS1Three'
	EDIT_STATIC_DNS1_4 = 	MAIN_VIEW_AREA + '.frameDHCP.m_editStaticDNS1Four'
	DHCP_RESERVATION_BUTT = MAIN_VIEW_AREA + '.frameDHCP.btnDHCPReservation'
	LABEL = MAIN_VIEW_AREA + '.frameDHCP.labelDHCP'

	PC_MAIN_VIEW_AREA = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel'
	PC_EDIT_IP_1 = 			PC_MAIN_VIEW_AREA + '.frameDHCP.m_editIPOne'
	PC_EDIT_IP_2 = 			PC_MAIN_VIEW_AREA + '.frameDHCP.m_editIPTwo'
	PC_EDIT_IP_3 = 			PC_MAIN_VIEW_AREA + '.frameDHCP.m_editIPThree'
	PC_EDIT_IP_4 = 			PC_MAIN_VIEW_AREA + '.frameDHCP.m_editIPFour'
	PC_MASK_COMBO = 			PC_MAIN_VIEW_AREA + '.frameDHCP.comboMask'
	PC_MASK_DROPDOWN = 		PC_MAIN_VIEW_AREA + '.frameDHCP.comboMask.QComboBoxPrivateContainer1.QComboBoxListView1'
	PC_DHCP_RADIO_ENABLE =		PC_MAIN_VIEW_AREA + '.frameDHCP.grpBtnRadioDHCP.radioDHCPEnable'
	PC_DHCP_RADIO_DISABLE = 	PC_MAIN_VIEW_AREA + '.frameDHCP.grpBtnRadioDHCP.radioDHCPDisable'
	PC_EDIT_START_IP = 		PC_MAIN_VIEW_AREA + '.frameDHCP.m_editStartIP'
	PC_EDIT_MAX_USER = 		PC_MAIN_VIEW_AREA + '.frameDHCP.m_editMaxUsers'
	PC_SAVE_BUTT = 			PC_MAIN_VIEW_AREA + '.frame.btnSave'
	PC_CANCEL_BUTT = 			PC_MAIN_VIEW_AREA + '.btnCancel'
	PC_START_IP_RANGE = 		PC_MAIN_VIEW_AREA + '.frameDHCP.lblStartIpRange'
	PC_START_IP_LABEL = 		PC_MAIN_VIEW_AREA + '.frameDHCP.labelfirstIP'
	PC_END_IP_RANGE = 			PC_MAIN_VIEW_AREA + '.frameDHCP.lblEndIpRange'
	PC_EDIT_STATIC_DNS1_1 = 	PC_MAIN_VIEW_AREA + '.frameDHCP.m_editStaticDNS1One'
	PC_EDIT_STATIC_DNS1_2 = 	PC_MAIN_VIEW_AREA + '.frameDHCP.m_editStaticDNS1Two'
	PC_EDIT_STATIC_DNS1_3 = 	PC_MAIN_VIEW_AREA + '.frameDHCP.m_editStaticDNS1Three'
	PC_EDIT_STATIC_DNS1_4 = 	PC_MAIN_VIEW_AREA + '.frameDHCP.m_editStaticDNS1Four'
	PC_DHCP_RESERVATION_BUTT = PC_MAIN_VIEW_AREA + '.frameDHCP.btnDHCPReservation'
	PC_LABEL = PC_MAIN_VIEW_AREA + '.frameDHCP.labelDHCP'
	
class SetupConst:
	internet = InternetConst
	network = NetworkConst
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.frame.btnSave'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseSetup.m_middlePanel.frame.btnSave'
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseSetup.m_middlePanel.frame.btnCancel'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseSetup.m_middlePanel.frame.btnCancel'
	
class BasicWirelessSettingsConst:
	MAIN_VIEW_AREA = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSettings.m_middlePanel'
	LEFT_PANEL_LABEL = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSettings.m_leftPanel.label1_2_3'
	SETTINGS_EDIT_FRAME = MAIN_VIEW_AREA + '.mainConfigFrame'
	VERTICAL_LAYOUT = SETTINGS_EDIT_FRAME + '.verticalLayout'
	MODE_COMBO = SETTINGS_EDIT_FRAME + '.comboMode'
	SSID_EDIT = SETTINGS_EDIT_FRAME + '.m_editSSID'
	RADIO_BAND = SETTINGS_EDIT_FRAME + '.comboBand'
	WIDE_CHANNEL_COMBO = SETTINGS_EDIT_FRAME + '.comboWChannel'
	STANDARD_CHANNEL_COMBO = SETTINGS_EDIT_FRAME + '.comboSChannel'
	SSID_BROADCAST_ENABLED = SETTINGS_EDIT_FRAME + '.grpBtnSSIDBroadcast.radioBroadcastEnabled'
	SSID_BROADCAST_DISABLED = SETTINGS_EDIT_FRAME + '.grpBtnSSIDBroadcast.radioBroadcastDisabled'
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSettings.m_middlePanel.bottomPurpleFrame.btnSave'
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSettings.m_middlePanel.bottomPurpleFrame.btnCancel'

	PC_MAIN_VIEW_AREA = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseWirelessSettings.m_middlePanel'
	PC_LEFT_PANEL_LABEL = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseWirelessSettings.m_leftPanel.label1_2_3'
	PC_SETTINGS_EDIT_FRAME = PC_MAIN_VIEW_AREA + '.mainConfigFrame'
	PC_VERTICAL_LAYOUT = PC_SETTINGS_EDIT_FRAME + '.verticalLayout'
	PC_MODE_COMBO = PC_SETTINGS_EDIT_FRAME + '.comboMode'
	PC_SSID_EDIT = PC_SETTINGS_EDIT_FRAME + '.m_editSSID'
	PC_RADIO_BAND = PC_SETTINGS_EDIT_FRAME + '.comboBand'
	PC_WIDE_CHANNEL_COMBO = PC_SETTINGS_EDIT_FRAME + '.comboWChannel'
	PC_STANDARD_CHANNEL_COMBO = PC_SETTINGS_EDIT_FRAME + '.comboSChannel'
	PC_SSID_BROADCAST_ENABLED = PC_SETTINGS_EDIT_FRAME + '.grpBtnSSIDBroadcast.radioBroadcastEnabled'
	PC_SSID_BROADCAST_DISABLED = PC_SETTINGS_EDIT_FRAME + '.grpBtnSSIDBroadcast.radioBroadcastDisabled'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseWirelessSettings.m_middlePanel.bottomPurpleFrame.btnSave'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CBaseWirelessSettings.m_middlePanel.bottomPurpleFrame.btnCancel'

class WirelessSecurityWepConst:
	ENCRYPTION_COMBO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWEP.comboEncryption'
	PC_ENCRYPTION_COMBO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWEP.comboEncryption'
		
	KEY1_EDIT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWEP.m_editKey1'
	PC_KEY1_EDIT = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWEP.m_editKey1'

class WirelessSecurityWpaPersonalConst:
	ENCRYPTION_COMBO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAPersonal.comboWPAPerEncryption'
	PC_ENCRYPTION_COMBO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAPersonal.comboWPAPerEncryption'
	
	PASSPRHASE_EDIT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAPersonal.m_editWPAPerPass'
	PC_PASSPRHASE_EDIT = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAPersonal.m_editWPAPerPass'

class WirelessSecurityWpaEnterpriseConst:
	ENCRYPTION_COMBO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.comboWPAEntEncryption'
	PC_ENCRYPTION_COMBO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.comboWPAEntEncryption'
	
	RADIUS_SERVER_IP1 = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntRADIUSServerOne'
	PC_RADIUS_SERVER_IP1 = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntRADIUSServerOne'
	
	RADIUS_SERVER_IP2 = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntRADIUSServerTwo'
	PC_RADIUS_SERVER_IP2 = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntRADIUSServerTwo'
	
	RADIUS_SERVER_IP3 = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntRADIUSServerThree'
	PC_RADIUS_SERVER_IP3 = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntRADIUSServerThree'
	
	RADIUS_SERVER_IP4 = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntRADIUSServerFour'
	PC_RADIUS_SERVER_IP4 = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntRADIUSServerFour'
	
	SHARED_SECRET = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntSharedSecret'
	PC_SHARED_SECRET = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frameWPAEnterprise.m_editWPAEntSharedSecret'
	
class WirelessSecurityConst:
	SECURITY_MODE = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.comboMode'
	PC_SECURITY_MODE = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.comboMode'
	wep = WirelessSecurityWepConst
	wpaPersonal = WirelessSecurityWpaPersonalConst
	wpaEnterprise = WirelessSecurityWpaEnterpriseConst
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frame1.btnSave'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frame1.btnSave'
	
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frame1.btnCancel'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessSecurity.m_middlePanel.frame1.btnCancel'

class WirelessMacFilterConst:
	ENABLED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.radioEnable'
	PC_ENABLED_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.radioEnable'
	
	DISABLED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.radioDisabled'
	PC_DISABLED_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.radioDisabled'
	
	PREVENT_PCS_LISTED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.radioPrevent'
	PC_PREVENT_PCS_LISTED_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.radioPrevent'
	
	PERMIT_PCS_LISTS_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.radioPermit'
	PC_PERMIT_PCS_LISTS_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.radioPermit'
	
	MAC_EDIT_BASE = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.m_lineEdit'
	PC_MAC_EDIT_BASE = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.m_lineEdit'
	
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.frame1.btnSave'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.frame1.btnSave'
	
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.frame1.btnCancel'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseWirelessMACFilter.m_middlePanel.frame1.btnCancel'
	
class Administration:
	WIRELESS_AUTHENTICATION_TYPE_COMBO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAdvWirelessSecurity.m_middlePanel.comboAuthType'
	PC_WIRELESS_AUTHENTICATION_TYPE_COMBO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAdvWirelessSecurity.m_middlePanel.comboAuthType'

class WirelessConst:
	basicSettings = BasicWirelessSettingsConst
	wirelessSecurity = WirelessSecurityConst
	macFilters = WirelessMacFilterConst
	administration = Administration
	
class AccessRestrictionsConst:
	ACCESS_POLICY_DROPDOWN = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.comboPolicy'
	PC_ACCESS_POLICY_DROPDOWN = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.comboPolicy'
	
	DELETE_THIS_ENTRY_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnDeletePolicy'
	PC_DELETE_THIS_ENTRY_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnDeletePolicy'
	
	EDIT_POLICY_NAME = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.m_editPolicyName'
	PC_EDIT_POLICY_NAME = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.m_editPolicyName'
	
	ENABLED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxStatus.radioEnabled'
	PC_ENABLED_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxStatus.radioEnabled'
	
	DISABLED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxStatus.radioDisabled'
	PC_DISABLED_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxStatus.radioDisabled'
	
	EDIT_LIST_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnEdit'
	PC_EDIT_LIST_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnEdit'
	
	DENY_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxAccess.radioDeny'
	PC_DENY_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxAccess.radioDeny'
	
	ALLOW_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxAccess.radioAllow'
	PC_ALLOW_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxAccess.radioAllow'
	
	APPLICATIONS_LIST = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.listApplications'
	PC_APPLICATIONS_LIST = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.listApplications'
	
	BLOCKED_LIST = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.listBlockedApplications'
	PC_BLOCKED_LIST = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.listBlockedApplications'
	
	LEFT_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnMoveToAppList'
	PC_LEFT_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnMoveToAppList'
	
	RIGHT_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnMoveToBlockedList'
	PC_RIGHT_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnMoveToBlockedList'
	
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.frame1.btnSave'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.frame1.btnSave'
	
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.frame1.btnCancel'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.frame1.btnCancel'

	EDIT_LIST_WINDOW = ':CBasePCIPListDlg'
	EDIT_IP = ':CBasePCIPListDlg.m_middlePanel.m_editIP'
	EDIT_IP1 = ':CBasePCIPListDlg.m_middlePanel.m_editIP1'
	EDIT_IP2 = ':CBasePCIPListDlg.m_middlePanel.m_editIP2'
	EDIT_IP3 = ':CBasePCIPListDlg.m_middlePanel.m_editIP3'
	EDIT_IP4 = ':CBasePCIPListDlg.m_middlePanel.m_editIP4'
	EDIT_IP5 = ':CBasePCIPListDlg.m_middlePanel.m_editIP5'
	EDIT_IP6 = ':CBasePCIPListDlg.m_middlePanel.m_editIP6'
	EDIT_LIST_SAVE_BUTT = ':CBasePCIPListDlg.m_middlePanel.frame1.btnSave'
	EDIT_LIST_CANCEL_BUTT = ':CBasePCIPListDlg.m_middlePanel.frame1.btnCancel'
	EDIT_LIST_CLOSE_BUTT = ':CBasePCIPListDlg.m_middlePanel.frame1.btnClose'
	DENY_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxAccess.radioDeny'
	PC_DENY_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxAccess.radioDeny'
	
	ALLOW_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxAccess.radioAllow'
	PC_ALLOW_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.grpBoxAccess.radioAllow'
	
	APPLICATION_LIST = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.listApplications'
	PC_APPLICATION_LIST = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.listApplications'
	
	BLOCKED_APPLICATION_LIST = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.listBlockedApplications'
	PC_BLOCKED_APPLICATION_LIST = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.listBlockedApplications'
	
	MOVE_TO_BLOCKED_APPLICATION_BUTT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnMoveToBlockedList'
	PC_MOVE_TO_BLOCKED_APPLICATION_BUTT = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnMoveToBlockedList'
	
	MOVE_TO_APPLICATION_BUTT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnMoveToAppList'
	PC_MOVE_TO_APPLICATION_BUTT = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnMoveToAppList'
	
	SAVE_BUTT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.frame1.btnSave'
	PC_SAVE_BUTT = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.frame1.btnSave'
	
	CANCEL_BUTT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnCancel'
	PC_CANCEL_BUTT = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAccessRestrictions.m_middlePanel.btnCancel'

	
class SinglePortForwardingConst:
	APPLICATION_NAME_DROPDOWN_BASE = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_leftPanel.comboApp'
	PC_APPLICATION_NAME_DROPDOWN_BASE = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAppAndGaming.m_leftPanel.comboApp'
	
	TABLE = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList'
	PC_TABLE = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList'
	
	APPLICATION_NAME_EDIT_BASE = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_leftPanel.m_editApp'
	PC_APPLICATION_NAME_EDIT_BASE = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAppAndGaming.m_leftPanel.m_editApp'
	
	EXTERNAL_PORT_BASE = 	FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QLineEdit'
	PC_EXTERNAL_PORT_BASE = 	FIRST_PART + PC_MIDDLE_PART +  LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QLineEdit'
	
	INTERNALE_PORT_BASE = 	FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QLineEdit'
	PC_INTERNALE_PORT_BASE = 	FIRST_PART + PC_MIDDLE_PART +  LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QLineEdit'
	
	PROTOCOL_BASE = 		FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QComboBox'
	PC_PROTOCOL_BASE = 		FIRST_PART + PC_MIDDLE_PART +      LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QComboBox'
	
	IP_EDIT_BASE = 			FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QWidget'#1.QLineEdit'
	PC_IP_EDIT_BASE = 			FIRST_PART + PC_MIDDLE_PART +  LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QWidget'#1.QLineEdit'
	
	IP_EDIT_BASE_2 = 			FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QWidget6.QLineEdit'
	PC_IP_EDIT_BASE_2 = 			FIRST_PART + PC_MIDDLE_PART +  LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QWidget6.QLineEdit'
	
	CHECKBOX_BASE = 		FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QCheckBox'
	PC_CHECKBOX_BASE = 		FIRST_PART + PC_MIDDLE_PART +      LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.qt_scrollarea_viewport.QCheckBox'
	
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame1.btnSave'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame1.btnSave'
	
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame1.btnCancel'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame1.btnCancel'
	
	TABLE_HEADER = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.QHeaderView2'
	PC_TABLE_HEADER = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame.tblAppList.QHeaderView2'

class DmzConst:
	ENABLED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseDMZSettings.m_middlePanel.grpBoxStatus.radioEnable'
	PC_ENABLED_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseDMZSettings.m_middlePanel.grpBoxStatus.radioEnable'
	
	DISABLED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseDMZSettings.m_middlePanel.grpBoxStatus.radioDisable'
	PC_DISABLED_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseDMZSettings.m_middlePanel.grpBoxStatus.radioDisable'
	
	SRC_ANY_IP_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseDMZSettings.m_middlePanel.groupBox.radioSourceIP'
	PC_SRC_ANY_IP_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseDMZSettings.m_middlePanel.groupBox.radioSourceIP'
	
	DST_IP_ADDRESS_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseDMZSettings.m_middlePanel.groupBox_2.radioDestIP'
	PC_DST_IP_ADDRESS_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseDMZSettings.m_middlePanel.groupBox_2.radioDestIP'
	
	DST_IP_ADDRESS_EDIT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseDMZSettings.m_middlePanel.groupBox_2.m_editDestIPOct4'
	PC_DST_IP_ADDRESS_EDIT = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseDMZSettings.m_middlePanel.groupBox_2.m_editDestIPOct4'
	
	DST_IP_LABEL = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseDMZSettings.m_middlePanel.groupBox_2.labelDestIP'
	PC_DST_IP_LABEL = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseDMZSettings.m_middlePanel.groupBox_2.labelDestIP'
	
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseDMZSettings.m_middlePanel.frame1.btnSave'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseDMZSettings.m_middlePanel.frame1.btnSave'
	
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseDMZSettings.m_middlePanel.frame1.btnCancel'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseDMZSettings.m_middlePanel.frame1.btnCancel'
	
class ApplicationsAndGamingConst:
	portForwarding = SinglePortForwardingConst
	dmz = DmzConst

class AdvancedWirelessSettings:
	AUTHENTICATION_TYPE = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAdvWirelessSecurity.m_middlePanel.comboAuthType'
	PC_AUTHENTICATION_TYPE = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CBaseAdvWirelessSecurity.m_middlePanel.comboAuthType'
	
class ManagementConst:
	ROUTER_PASSWORD_EDIT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CAdminManagementBase.m_middlePanel.m_editPasswd'
	PC_ROUTER_PASSWORD_EDIT = FIRST_PART + PC_MIDDLE_PART + LAST_PART + 'CAdminManagementBase.m_middlePanel.m_editPasswd'
	
	REENTER_PASSWORD_EIDT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CAdminManagementBase.m_middlePanel.m_editConfirmPasswd'
	PC_REENTER_PASSWORD_EIDT = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CAdminManagementBase.m_middlePanel.m_editConfirmPasswd'
	
	REMOTE_MANAGEMENT_ENABLED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CAdminManagementBase.m_middlePanel.grpBtnRemoteMgmt.radioRemoteMgmtEnabled'
	PC_REMOTE_MANAGEMENT_ENABLED_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CAdminManagementBase.m_middlePanel.grpBtnRemoteMgmt.radioRemoteMgmtEnabled'
	
	REMOTE_MANAGEMENT_DISABLED_RADIO = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CAdminManagementBase.m_middlePanel.grpBtnRemoteMgmt.radioRemoteMgmtDisabled'
	PC_REMOTE_MANAGEMENT_DISABLED_RADIO = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CAdminManagementBase.m_middlePanel.grpBtnRemoteMgmt.radioRemoteMgmtDisabled'
	
	BACKUP_CONFIGURATIONS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CAdminManagementBase.m_middlePanel.m_btnBackup'
	PC_BACKUP_CONFIGURATIONS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CAdminManagementBase.m_middlePanel.m_btnBackup'
	
	RESTORE_CONFIGURATIONS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CAdminManagementBase.m_middlePanel.m_btnRestore'
	PC_RESTORE_CONFIGURATIONS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CAdminManagementBase.m_middlePanel.m_btnRestore'
	
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CAdminManagementBase.m_middlePanel.frame1.btnSave'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CAdminManagementBase.m_middlePanel.frame1.btnSave'
	
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CAdminManagementBase.m_middlePanel.frame1.btnCancel'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART +   LAST_PART + 'CAdminManagementBase.m_middlePanel.frame1.btnCancel'

	BACKUP_FILE_NAME_EDIT = ".CBaseFileTreeView.m_editFileName"
	BACKUP_DIRECTORY = ".CBaseFileTreeView.m_DirView"
	BACKUP_CONFIG_OK = ".CBaseFileTreeView.btnOK"
	BACKUP_CONFIG_CANCEL = ".CBaseFileTreeView.btnOK"

class FactoryDefaultsConst:
	RESTORE_FACTORY_DEFAULTS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFactoryDefaults.m_middlePanel.frame.btnRestoreDefaults'
	PC_RESTORE_FACTORY_DEFAULTS_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFactoryDefaults.m_middlePanel.frame.btnRestoreDefaults'
	
	WARNING_DIALOG = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFactoryDefaults.Restore Factory Defaults'
	PC_WARNING_DIALOG = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFactoryDefaults.Restore Factory Defaults'
	
	WARNING_DIALOG_OK_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + '.Restore Factory Defaults.qt_msgbox_buttonbox.OK'
	PC_WARNING_DIALOG_OK_BUTTON = FIRST_PART + PC_MIDDLE_PART +   '.Restore Factory Defaults.qt_msgbox_buttonbox.OK'
	
	WARNING_DIALOG_CANCEL_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + '.Restore Factory Defaults.qt_msgbox_buttonbox.Cancel'
	PC_WARNING_DIALOG_CANCEL_BUTTON = FIRST_PART + PC_MIDDLE_PART +   '.Restore Factory Defaults.qt_msgbox_buttonbox.Cancel'

class FirmwareUpgradeBrowseConst:
	DIALOG = '.CBaseFileTreeView'
	TITLE_LABEL = '.CBaseFileTreeView.labelTitle'
	LIST = '.CBaseFileTreeView.m_DirView'
	OK_BUTTON = '.CBaseFileTreeView.btnOK'
	CANCEL_BUTTON = '.CBaseFileTreeView.btnCancel'

class FirmwareUpgradeConst:
	browse = FirmwareUpgradeBrowseConst
	FILE_EDIT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.m_middlePanel.m_editFileName'
	PC_FILE_EDIT = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.m_middlePanel.m_editFileName'
	
	BROWSE_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.m_middlePanel.btnBrowse'
	PC_BROWSE_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.m_middlePanel.btnBrowse'
	
	START_TO_UPGRADE_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.m_middlePanel.btnStartUpgrade'
	PC_START_TO_UPGRADE_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.m_middlePanel.btnStartUpgrade'
	
	PROGRESS_BAR_PERCENT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.m_middlePanel.progressBar'
	PC_PROGRESS_BAR_PERCENT = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.m_middlePanel.progressBar'
	
	FEATURE_CAN_ONLY_BE_ACCESSED_FROM_PC_OK_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.Firmware Upgrade.qt_msgbox_buttonbox.OK'
	PC_FEATURE_CAN_ONLY_BE_ACCESSED_FROM_PC_OK_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.Firmware Upgrade.qt_msgbox_buttonbox.OK'
	
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.m_middlePanel.frame1.btnSave'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.m_middlePanel.frame1.btnSave'
	
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.m_middlePanel.frame1.btnCancel'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.m_middlePanel.frame1.btnCancel'
	
	SELECT_A_FILE_LABEL = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.m_middlePanel.labelMode'
	PC_SELECT_A_FILE_LABEL = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.m_middlePanel.labelMode'
	
	DO_NOT_INTERRUPT_LABEL = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.m_middlePanel.label_2'
	PC_DO_NOT_INTERRUPT_LABEL = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.m_middlePanel.label_2'
	
	FIRMWARE_WARNING_LABEL = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseFirmwareUpgrade.m_middlePanel.label'
	PC_FIRMWARE_WARNING_LABEL = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseFirmwareUpgrade.m_middlePanel.label'
	
class AdministrationConst:
	management = ManagementConst
	factoryDefaults = FactoryDefaultsConst
	firmwareUpgrade = FirmwareUpgradeConst
	
class RouterStatusConst:
	INTERNET_IP_ADDRESS = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelIP'
	PC_INTERNET_IP_ADDRESS = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelIP'
	
	IP_ADDRESS_RELEASE_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.m_btnIPRelease'
	PC_IP_ADDRESS_RELEASE_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.m_btnIPRelease'
	
	IP_ADDRESS_RENEW_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.m_btnIPRelease'
	PC_IP_ADDRESS_RENEW_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.m_btnIPRelease'
	
	CONNECTION_TYPE = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelConnType'
	PC_CONNECTION_TYPE = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelConnType'
	
	DNS1 = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelDNS1'
	PC_DNS1 = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelDNS1'
	
	DNS2 = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelDNS2'
	PC_DNS2 = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelDNS2'
	
	DNS3 = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelDNS3'
	PC_DNS3 = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelDNS3'
	
	GATEWAY = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelGateway'
	PC_GATEWAY = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelGateway'
	
	SUBNET = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelSubnet'
	PC_SUBNET = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelSubnet'
	
	LOGIN_STATUS = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelLoginStatus'
	PC_LOGIN_STATUS = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelLoginStatus'
		
	DISCONNECT_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.m_btnPPPoEConnect'
	PC_DISCONNECT_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.m_btnPPPoEConnect'
	
	CONNECT_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.m_btnPPPoEConnect'
	PC_CONNECT_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.m_btnPPPoEConnect'
	
	REFRESH_BUTTON =    FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.frame1.m_btnRefresh'
	PC_REFRESH_BUTTON =    FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.frame1.m_btnRefresh'
	
	MTU_TEXT = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelMTU'
	PC_MTU_TEXT = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelMTU'
	
	FIRMWARE_VERSION = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseRouterStatus.m_middlePanel.labelVersion'
	PC_FIRMWARE_VERSION = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseRouterStatus.m_middlePanel.labelVersion'
	
class LocalNetworkStatusConst:
	DHCP_CLIENT_TABLE_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseLocalNetworkStatus.m_middlePanel.btnDhcpClient'
	PC_DHCP_CLIENT_TABLE_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseLocalNetworkStatus.m_middlePanel.btnDhcpClient'
	
	ROUTER_IP = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseLocalNetworkStatus.m_middlePanel.labelRouterIP'
	PC_ROUTER_IP = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseLocalNetworkStatus.m_middlePanel.labelRouterIP'
	
	DHCP_START_IP = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseLocalNetworkStatus.m_middlePanel.labelStartIP'
	PC_DHCP_START_IP = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseLocalNetworkStatus.m_middlePanel.labelStartIP'
	
	DHCP_END_IP = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseLocalNetworkStatus.m_middlePanel.labelEndIP'
	PC_DHCP_END_IP = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseLocalNetworkStatus.m_middlePanel.labelEndIP'
	
class WirelessNetworkStatusConst:
	RADIO_BAND = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessNetStatus.m_middlePanel.labelBand'
	PC_RADIO_BAND = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseWirelessNetStatus.m_middlePanel.labelBand'
	
	STANDARD_CHANNEL = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessNetStatus.m_middlePanel.labelSChannel'
	PC_STANDARD_CHANNEL = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseWirelessNetStatus.m_middlePanel.labelSChannel'
	
	SECURITY = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseWirelessNetStatus.m_middlePanel.labelSecurity'
	PC_SECURITY = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseWirelessNetStatus.m_middlePanel.labelSecurity'

class StatusConst:
	router = RouterStatusConst
	localNetwork = LocalNetworkStatusConst
	wirelessNetwork = WirelessNetworkStatusConst
	SAVE_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame1.btnSave'
	PC_SAVE_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseAppAndGaming.m_middlePanel.frame1.btnSave'
	
	CANCEL_SETTINGS_BUTTON = FIRST_PART + LINKSYS_MIDDLE_PART + LAST_PART + 'CBaseAppAndGaming.m_middlePanel.frame1.btnCancel'
	PC_CANCEL_SETTINGS_BUTTON = FIRST_PART + PC_MIDDLE_PART + LAST_PART +   'CBaseAppAndGaming.m_middlePanel.frame1.btnCancel'
	
class WirelessGuiConst:
	tabs = TabsConst
	setup = SetupConst
	wireless = WirelessConst
	accessRestrictions = AccessRestrictionsConst
	applicationAndGaming = ApplicationsAndGamingConst
	administration = AdministrationConst
	advancedWirelessSettings = AdvancedWirelessSettings
	status = StatusConst
	VERTICAL_SCROLLBAR = FIRST_PART + 'm_guiTab.QScrollArea1.qt_scrollarea_vcontainer.QScrollBar1'
	PC_VERTICAL_SCROLLBAR = FIRST_PART + 'm_DeskTopTab.scrollArea.qt_scrollarea_viewport.desktopScrollAreaWidgetContents.CDesktopApplet1.CWorkstationWebBrowserBase.QScrollArea1.qt_scrollarea_vcontainer.QScrollBar1'
	None