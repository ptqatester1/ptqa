##Chris Allen

from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import PhysicalConst
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import GlobalSettings
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import Dhcpv6

class Settings(GlobalSettings):
	DOMAIN_NAME_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_domainNameEdit"
	PROVIDER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.mainScrollArea.qt_scrollarea_viewport.mainScrollAreaContents.m_providerEdit"

class Dhcp:	
	DHCP_IP = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_IpAddress"
	DHCP_SUBNET_MASK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editSubnet"
	DHCP_DNS = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_DNSEdit"
	DHCP_EDIT_START_IP_1 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editStartIPOne"
	DHCP_EDIT_START_IP_2 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editStartIPTwo"
	DHCP_EDIT_START_IP_3 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editStartIPThree"
	DHCP_EDIT_START_IP_4 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editStartIPFour"
	DHCP_EDIT_MAX_USER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editMaxUsers"
	DHCP_ADD_SAVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editButton"
	DHCP_CANCEL_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_cancelButton"
	IP_ADDRESS_RANGE_1 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editStartIPOne'
	IP_ADDRESS_RANGE_2 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editStartIPTwo'
	IP_ADDRESS_RANGE_3 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editStartIPThree'
	IP_ADDRESS_RANGE_4 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editStartIPFour'
	"BaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CRouterServiceDhcpClass.m_editStartIPFour"


class Backbone:
	TITLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_title"
	DHCP_RADIO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPSettingsGroupBox.m_ipv4RadioDHCP"
	STATIC_RADIO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPSettingsGroupBox.m_ipv4RadioStatic"
	IP_ADDRESS_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPSettingsGroupBox.m_ipAddrEdit"
	SUBNET_MASK_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPSettingsGroupBox.m_subnetEdit"
	GATEWAY_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPSettingsGroupBox.m_gatewayEdit"
	DNS_SERVER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPSettingsGroupBox.m_DNSEdit"
	
class Cell_Tower:
	TITLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_title"
	IP_ADDRESS_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPSettingsGroupBox.m_ipAddrEdit"
	SUBNET_MASK_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPSettingsGroupBox.m_subnetEdit"
	IPv6_ADDRESS_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPv6SettingsGroupBox.m_ipv6AddrEdit"
	IPv6_SUBNET_MASK_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPv6SettingsGroupBox.m_ipv6MaskEdit"
	IPv6_LINK_LOCAL_ADDRESS_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.grpIPv6SettingsGroupBox.m_linkLocalAddrEdit"

class Interfaces:
	backbone = Backbone
	cellTower = Cell_Tower

class ConfigConst:
	interface = Interfaces
	settings = Settings
	
class CellTower:
	ON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceCellTowerClass.m_cellTowerOn"
	OFF = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceCellTowerClass.m_cellTowerOff"
	REFRESH_BUTT = ":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceCellTowerClass.m_refresh"
	LIST = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceCellTowerClass.m_cellTowerList"
	ITEM1 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceCellTowerClass.m_cellTowerList.item_0/0"
	DEVICE_LIST = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceCellTowerClass.m_cellDeivceList"
	TOWER_LIST = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceCellTowerClass.m_cellTowerList"
	
class PapChap:
	INTERFACE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServicePapChapClass.m_interfaceComboBox"
	PAP = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServicePapChapClass.m_papOn"
	CHAP = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServicePapChapClass.m_chapOn"
	USER_NAME = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServicePapChapClass.m_usernameEdit"
	PASSWORD = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServicePapChapClass.m_passwordEdit"
	ADD_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServicePapChapClass.m_addNewButton"
	SAVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServicePapChapClass.m_editButton"
	REMOVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServicePapChapClass.m_removeButton"
	LIST = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServicePapChapClass.m_usernamePwListView"
	
class ServicesConst:
	dhcp = Dhcp
	dhcpv6 = Dhcpv6
	cellTower = CellTower
	papChap = PapChap

class COServerConst:
	config = ConfigConst
	physical = PhysicalConst
	services = ServicesConst

'''		
	DHCP_V6_ON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_Dhcpv6On"
	DHCP_V6_OFF = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_Dhcpv6Off"
	DHCP_V6_POOL_LIST = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_dhcpv6PoolComboBox"
	DHCP_V6_DOMAIN = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_dhcpv6DomainName"
	DHCP_V6_DNS = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_dhcpv6Dns"
	DHCP_V6_CREATE_POOL_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_ipv6DhcpPoolAddButton"
	DHCP_V6_REMOVE_POOL_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_ipv6DhcpPoolRemoveButton"
	DHCP_V6_PREFIX_CREATE_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_ipv6DhcpPrefixAddButton"
	DHCP_V6_PREFIX_EDIT_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_ipv6DhcpPoolEditButton"
	DHCP_V6_PREFIX_REMOVE_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_ipv6DhcpPrefixRemoveButton"
	DHCP_V6_PREFIX_TABLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_Dhcpv6PoolTable"
	DHCP_V6_PREFIX_ITEM = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.m_dhcpv6PoolGroupBox.m_Dhcpv6PoolTable.item_"
	DHCP_V6_LOCAL_CREATE_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.groupBox_2.m_ipv6DhcpLocalPoolAddButton"
	DHCP_V6_LOCAL_EDIT_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.groupBox_2.m_ipv6LocalPoolEditButton"
	DHCP_V6_LOCAL_REMOVE_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.groupBox_2.m_ipv6DhcpLocalPoolRemoveButton"
	DHCP_V6_LOCAL_TABLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.groupBox_2.m_Dhcpv6LocalPoolTable"
	DHCP_V6_LOCAL_ITEM = ".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.CServerServiceDhcpv6.groupBox_2.m_Dhcpv6LocalPoolTable.item_"
	
class DHCP_V6_Pool_Config: 
	POOL_NAME = ":CServerServiceDhcpv6PoolConfig.m_poolName"
	VALID_LIFETIME = ":CServerServiceDhcpv6PoolConfig.groupBox_2.m_prefixValidLifetime"
	PREFERRED_LIFETIME = ":CServerServiceDhcpv6PoolConfig.groupBox_2.m_prefixPreferredLifetime"
	LOCAL_POOL_NAME = ":CServerServiceDhcpv6PoolConfig.groupBox.m_localPool"
	VALID_POOL_LIFETIME = ":CServerServiceDhcpv6PoolConfig.groupBox.m_poolValidTime"
	PREFERRED_POOL_LIFETIME = ":CServerServiceDhcpv6PoolConfig.groupBox.m_poolPreferredTime"
	SAVE_BUTTON = ":CServerServiceDhcpv6PoolConfig.m_saveButton"
	CANCEL_BUTTON = ":CServerServiceDhcpv6PoolConfig.m_cancelButton" 

class IPv6_Pool_Config:
	IPV6_POOL_NAME = ":CServerServiceDhcpv6LocalPoolConfig.m_localPoolName"
	IPV6_POOL_PREFIX_ADD = ":CServerServiceDhcpv6LocalPoolConfig.m_localPoolPrefix"
	IPV6_POOL_PREFIX_SUB = ":CServerServiceDhcpv6LocalPoolConfig.m_localPoolPrefixLength"
	IPV6_POOL_PREFIX_LENGTH = ":CServerServiceDhcpv6LocalPoolConfig.m_localPoolSubPrefixLength"
	SAVE_BUTTON = ":CServerServiceDhcpv6LocalPoolConfig.m_saveButton"
	CANCEL_BUTTON = ":CServerServiceDhcpv6LocalPoolConfig.m_cancelButton"'''