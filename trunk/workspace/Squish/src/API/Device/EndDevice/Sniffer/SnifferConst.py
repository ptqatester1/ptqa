##Chris Allen

from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import PhysicalConst

class GuiConst:
	SERVICE_ON_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_ServiceOn'
	SERVICE_OFF_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_ServiceOff'
	PORT_0_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_port0'
	PORT_1_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_port1'
	PORT_LABEL = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.label'
	BUFFER_SIZE_SLIDER = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_horizontalSlider'
	BUFFER_SIZE_LABEL = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_bufferSizeText'
	PACKET_LIST = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_eventListView'
	PACKET_INFORMATION_WINDOW = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_pduScrollArea'
	CLEAR_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_clearAllBtn'
	EDIT_FILTERS_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_eventListFiltersBtnGroup.m_editFiltersBtn'
	SHOW_ALL_NONE_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_eventListFiltersBtnGroup.m_showAllBtn'
	CURRENT_FILTERS_TEXT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_eventListFiltersBtnGroup.m_filtersLbl'
	PacketInformation = ':CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.m_pduScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.CPDUHeaderTemplate1.'
	
class EditFiltersConst:
	#This is the base for each tab
	EDIT_FILTERS_MENU_IPV4 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.FilterMenu.filterTabs.qt_tabwidget_stackedwidget.ipv4Table'
	EDIT_FILTERS_MENU_IPV6 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.FilterMenu.filterTabs.qt_tabwidget_stackedwidget.ipv6Table'
	EDIT_FILTERS_MENU_MISC = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.FilterMenu.filterTabs.qt_tabwidget_stackedwidget.miscTable'
	
	EDIT_FILTERS_TABBAR = ":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CSnifferSerivce.FilterMenu.filterTabs.qt_tabwidget_tabbar"
	
	IPV6_FILTERS_TAB = "IPv6"
	IP_FILTERS_TAB = "IPv4"
	MISC_FILTERS_TAB = "Misc"

class SnifferConst:
	gui = GuiConst
	editFilters = EditFiltersConst
	None