##Chris Allen

from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import PhysicalConst

class FileEditConst:
	HTML_CONTENT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CServerServiceHttpEdit.m_pageContent'
	FILE_MANAGER_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CServerServiceHttpEdit.m_fileManagerBtn'
	RESET_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CServerServiceHttpEdit.m_resetBtn'
	SAVE_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CServerServiceHttpEdit.m_saveBtn'
	FILE_NAME_EDIT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CServerServiceHttpEdit.m_editPageName'
	
class PopupConst:
	FILE_EDIT_WARNING = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CServerServiceHttpEdit.File Edit Warning'
	FILE_EDIT_WARNING_TEXT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CServerServiceHttpEdit.File Edit Warning.qt_msgbox_label'
	FILE_EDIT_WARNING_YES = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CServerServiceHttpEdit.File Edit Warning.qt_msgbox_buttonbox.Yes'
	FILE_EDIT_WARNING_NO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.CServerServiceHttpEdit.File Edit Warning.qt_msgbox_buttonbox.No'
		
class GuiConst:
	fileEdit = FileEditConst
	popup = PopupConst
	HTTP_ON_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CServerServiceHttp.grpHttp.m_HttpOn'
	HTTP_OFF_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CServerServiceHttp.grpHttp.m_HttpOff'
	HTTPS_ON_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CServerServiceHttp.grpHttps.m_HttpsOn'
	HTTPS_OFF_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CServerServiceHttp.grpHttps.m_HttpsOff'
	FILE_MANAGER_TABLE = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CServerServiceHttp.m_fileManagerTable'
	NEW_FILE_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CServerServiceHttp.m_newFileBtn'
	IMPORT_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CServerServiceHttp.m_importBtn'

class HomeGatewayConst:
	config = ConfigConst
	physical = PhysicalConst
	gui = GuiConst