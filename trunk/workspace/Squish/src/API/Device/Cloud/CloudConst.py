##Chris Allen

from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import PhysicalConst
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import GlobalSettings
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import Interface

class TVSettings:
	TV_SETTINGS = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.m_menuCfgScrollView.qt_scrollarea_viewport.scrollAreaWidget.QFrame1.TV Settings"
	TV_IMAGE_PATH_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudImageSettings.m_imgSettingsgroupBox.m_imagePathlineEdit"
	TV_IMAGE_BROWSE_PATH_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudImageSettings.QFileDialog.fileNameEdit"
	TV_IMAGE_PATH_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudImageSettings.m_imgSettingsgroupBox.m_imagePathlineEdit"
	TV_IMAGE_BROWSE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudImageSettings.m_imgSettingsgroupBox.m_browseImageBtn"
	TV_IMAGE_BROWSE_OPEN_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudImageSettings.QFileDialog.buttonBox.Open"
	TV_IMAGE_ADD_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudImageSettings.m_imgSettingsgroupBox.m_addBtn"
	TV_IMAGE_REMOVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudImageSettings.m_imgSettingsgroupBox.m_removeBtn"
	TV_IMAGE_LIST = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudImageSettings.m_imgSettingsgroupBox.m_imageListWidget"


class FrameRelay:
	SRC_PORT_COMBO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_srcPortBox"
	SRC_SUBLINK_COMBO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_srcSublinkBox"
	DST_PORT_COMBO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_dstPortBox"
	DST_SUBLINK_COMBO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_dstSublinkBox"
	CONNECTIONS_ADD_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_addButton"
	CONNECTIONS_REMOVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_removeButton"
	CONNECTION_VIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_connectionView"
	CONNECTION_VIEW_HEADER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_connectionView.QHeaderView2"
	CONNECTION_VIEW_HEADER_SRC_PORT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_connectionView.QHeaderView2.HeaderViewItem1"
	CONNECTION_VIEW_HEADER_SRC_SUBLINK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_connectionView.QHeaderView2.HeaderViewItem2"
	CONNECTION_VIEW_HEADER_DST_PORT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_connectionView.QHeaderView2.HeaderViewItem3"
	CONNECTION_VIEW_HEADER_DST_SUBLINK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_connectionView.QHeaderView2.HeaderViewItem4"
	CONNECTION_VIEW_TEXT_HEADER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.textLabel1"    
	TABLE = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudConnectionsBase.m_connectionView'
	
class Dsl:
	SRC_PORT_COMBO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudDSLConnectionsBase.m_srcPortBox"
	DST_PORT_COMBO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudDSLConnectionsBase.m_dstPortBox"
	CONNECTIONS_ADD_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudDSLConnectionsBase.m_addButton"
	CONNECTIONS_REMOVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudDSLConnectionsBase.m_removeButton"
	CONNECTION_VIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudDSLConnectionsBase.m_connectionView"
	CONNECTION_VIEW_HEADER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudDSLConnectionsBase.m_connectionView.QHeaderView2"
	TABLE = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudDSLConnectionsBase.m_connectionView'

class Cable:
	SRC_PORT_COMBO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudCableConnectionsBase.m_srcPortBox"
	DST_PORT_COMBO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudCableConnectionsBase.m_dstPortBox"
	CONNECTIONS_ADD_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudCableConnectionsBase.m_addButton"
	CONNECTIONS_REMOVE_BUTT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudCableConnectionsBase.m_removeButton"
	CONNECTION_VIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudCableConnectionsBase.m_connectionView"
	CONNECTION_VIEW_HEADER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudCableConnectionsBase.m_connectionView.QHeaderView2"
	TABLE = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CCloudCableConnectionsBase.m_connectionView'

class Connections:
	frameRelay = FrameRelay
	dsl = Dsl
	cable = Cable
	FRAME_RELAY = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.m_menuCfgScrollView.qt_scrollarea_viewport.scrollAreaWidget.QFrame1.Frame Relay"
	DSL = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.m_menuCfgScrollView.qt_scrollarea_viewport.scrollAreaWidget.QFrame1.DSL"
	CABLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.m_menuCfgScrollView.qt_scrollarea_viewport.scrollAreaWidget.QFrame1.Cable"
	
class Serial:
	PORT_STATUS_CHECKBOX = Interface.PORT_STATUS_CHECKBOX
	LMI_DROPDOWN = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_lmiBox"
	DLCI_NUM_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_dlciBox"
	DLCI_NAME_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_dlciNameBox"
	DLCI_ADD_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_addButton"
	DLCI_REMOVE_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_removeButton"
	DLCI_TABLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_mapView"
	DLCI_TABLE_HEADER_1 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_mapView.QHeaderView1.HeaderViewItem1"
	DLCI_TABLE_HEADER_2 = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_mapView.QHeaderView1.HeaderViewItem2"
	
class Modem:
	TITLE = Interface.TITLE
	PHONE_NUMBER_EDIT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_phoneNumEdit'

class Ethernet:
	TITLE = Interface.TITLE
	CABLE_RADIO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_cableRadioButton"
	DSL_RADIO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.m_dslRadioButton"
	
class Coaxial:
	TITLE = Interface.TITLE

class Interfaces:
	serial = Serial
	modem = Modem
	ethernet = Ethernet
	coax = Coaxial

class Config:
	settings = GlobalSettings
	tvSettings = TVSettings
	connections = Connections
	interface = Interfaces

class CloudConst:
	physical = PhysicalConst
	config = Config
	None