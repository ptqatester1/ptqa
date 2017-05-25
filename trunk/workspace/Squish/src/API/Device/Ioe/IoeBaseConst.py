##Chris Allen

from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import GlobalSettings, Interface
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import PhysicalConst as PhysicalBaseConst

class Modules(object):
	MODULE_BASE = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_menuCfgScrollView.qt_scrollarea_viewport.QWidget1.QFrame1.'
	NETWORK_MODULE_SLOT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget1'
	IOE_MODULE_SLOT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget2'
	POWER_SLOT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CModuleContainer1.CModuleTarget2'
	IOE_MODULE_SLOT_BASE = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget'
	PT_IOE_NM_1CE  =  ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_menuCfgScrollView.qt_scrollarea_viewport.QWidget1.QFrame1.PT-IOE-NM-1CE" 
	PT_IOE_NM_1CFE =  ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_menuCfgScrollView.qt_scrollarea_viewport.QWidget1.QFrame1.PT-IOE-NM-1CFE"
	PT_IOE_NM_1CGE =  ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_menuCfgScrollView.qt_scrollarea_viewport.QWidget1.QFrame1.PT-IOE-NM-1CGE" 
	PT_IOE_NM_1W   =  ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_menuCfgScrollView.qt_scrollarea_viewport.QWidget1.QFrame1.PT-IOE-NM-1W"
	PT_IOE_POWER_ADAPTER   =  ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_menuCfgScrollView.qt_scrollarea_viewport.QWidget1.QFrame1.PT-IOE-POWER-ADAPTER"
	PT_IOE_CUSTOM_IO   =  ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_menuCfgScrollView.qt_scrollarea_viewport.QWidget1.QFrame1.PT-IOE-CUSTOM-IO"
	
class PhysicalConst(PhysicalBaseConst):
	modules = Modules
	POWER_BLOCK = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CModuleContainer1.CModuleTarget15'#this is the block that connects to the device
	POWER_BLOCK_CONTAINER = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.CModuleListButton1'#This is where the power block gets dragged away fromt he device to
	POWER_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CModuleContainer1.CModuleTarget3"
	None

class Settings(GlobalSettings):
	SERIAL_NUMBER = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.m_serialNumber'
	NONE_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.m_IoEServerGroupBox.m_noIoeServer'
	HOME_GATEWAY_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.m_IoEServerGroupBox.m_lanServer'
	REMOTE_SERVER_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.m_IoEServerGroupBox.m_remoteServer'
	SERVER_ADDRESS_EDIT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.m_IoEServerGroupBox.m_serverAddress'
	USER_NAME_EDIT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.m_IoEServerGroupBox.m_username'
	PASSWORD_EDIT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.m_IoEServerGroupBox.m_password'
	CONNECT_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CUniversalGlobalSettings.m_IoEServerGroupBox.m_reconnectRegistration'

class Files:
	UP_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.m_upBtn'
	TABLE = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.m_fileManagerTable'
	NEW_DIRECTORY_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.m_newDirBtn'
	NEW_FILE_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.m_newFileBtn'
	IMPORT_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.m_importBtn'
	NEW_DIRECTORY_LINE_EDIT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.Packet Tracer.QLineEdit1'
	NEW_DIRECTORY_OK_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.Packet Tracer.QDialogButtonBox1.OK'
	NEW_DIRECTORY_CANCEL_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.Packet Tracer.QDialogButtonBox1.Cancel'
	NEW_FILE_LINE_EDIT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.Packet Tracer.QLineEdit1'
	NEW_FILE_OK_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.Packet Tracer.QDialogButtonBox1.OK'
	NEW_FILE_CANCEL_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.Packet Tracer.QDialogButtonBox1.Cancel'
	IMPORT_LINE_EDIT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.QFileDialog.fileNameEdit'
	IMPORT_OPEN_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.QFileDialog.buttonBox.Open'
	IMPORT_CANCEL_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.QFileDialog.buttonBox.Cancel'
	FILE_PATH = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.m_pathLabel'
	ERROR_CREATING_FILE_DIALOG = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.New File'
	ERROR_CREATING_FILE_OK_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.New File.qt_msgbox_buttonbox.OK'
	ERROR_CREATING_DIRECTORY_DIALOG = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.New Directory'
	ERROR_CREATING_DIRECTORY_OK_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.New Directory.qt_msgbox_buttonbox.OK'
	FILE_MANAGER_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManagerEdit.m_fileManagerBtn'
	SAVE_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManagerEdit.m_saveBtn'
	FILE_EDITOR_TEXT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManagerEdit.m_pageContent'
	DELETE_YES_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.Delete File.qt_msgbox_buttonbox.Yes'
	DELETE_NO_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseDeviceFileManager.Delete File.qt_msgbox_buttonbox.No'
	
class ConfigConst:
	settings = Settings
	files = Files
	interface = Interface
	None

class Programming(object):
	PROGRAMMING_WEBVIEW = '.c_physicalTab.qt_tabwidget_stackedwidget.m_programmingTab.m_programmingWebView.'
	#PROGRAMMING_WEBVIEW = '.c_physicalTab.qt_tabwidget_stackedwidget.m_customHtmlTab.m_customWebView.'
	WEBVIEW_BODY = PROGRAMMING_WEBVIEW + 'DOCUMENT.HTML1.BODY1'
	SCRIPT_LIST				= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV1.SELECT1'
	BLINK_JS				= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV1.SELECT1.OPTION1'
	FIRST_JS				= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV1.SELECT1.OPTION1'
	MAIN_JS					= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV1.SELECT1.OPTION2'
	OPEN_BUTTON				= WEBVIEW_BODY + '.DIV1.DIV2.DIV1.BUTTON1'
	ADD_BUTTON				= WEBVIEW_BODY + '.DIV1.DIV2.DIV1.BUTTON2'
	REMOVE_BUTTON			= WEBVIEW_BODY + '.DIV1.DIV2.DIV1.BUTTON3'
	RENAME_BUTTON			= WEBVIEW_BODY + '.DIV1.DIV2.DIV1.BUTTON4'
	#RELOAD_BUTTON			= WEBVIEW_BODY + '.DIV1.DIV2.DIV1.BUTTON5'
	RUN_BUTTON				= WEBVIEW_BODY + '.DIV1.DIV2.DIV2.BUTTON2'
	STOP_BUTTON				= WEBVIEW_BODY + '.DIV1.DIV2.DIV2.BUTTON2'
	CLEAR_OUTPUTS_BUTTON	= WEBVIEW_BODY + '.DIV1.DIV2.DIV2.BUTTON4'
	SCRIPT_TEXT_AREA		= WEBVIEW_BODY + ''
	OUTPUT_TEXT_AREA		= WEBVIEW_BODY + '.DIV3.DIV3.TEXTAREA1'
	SCRIPT_NAME_LABEL		= WEBVIEW_BODY + '.DIV1.SPAN1'
	NEW_PROJECT_NAME		= WEBVIEW_BODY + 'DIV9.DIV2.INPUT1'
	NEW_PROJECT_TYPE		= WEBVIEW_BODY + 'DIV9.DIV2.DIV1.SELECT1'
	CREATE_PROJECT_BUTTON	= WEBVIEW_BODY + 'DIV9.DIV3.DIV1.BUTTON1'
	
	RELOAD_BUTTON 	= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV3.DIV1.BUTTON1'
	COPY_BUTTON 	= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV3.DIV1.BUTTON2'
	PASTE_BUTTON 	= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV3.DIV1.BUTTON3'
	UNDO_BUTTON 	= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV3.DIV1.BUTTON4'
	REDO_BUTTON 	= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV3.DIV1.BUTTON5'
	FIND_BUTTON 	= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV3.DIV1.BUTTON6'
	REPLACE_BUTTON 	= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV3.DIV1.BUTTON7'
	ZOOM_IN_BUTTON 	= WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV3.DIV1.BUTTON8'
	ZOOM_OUT_BUTTON = WEBVIEW_BODY + '.DIV3.DIV1.DIV1.DIV3.DIV1.BUTTON9'
	None
	
class ShortcutButtons(object):
	BOLD = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Bold"
	ITALIC = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Italic"
	UNDERLINE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Underline"
	STRIKETHROUGH = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Strikethrough"
	ALIGN_LEFT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Align Left"
	ALIGN_CENTER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Align Center"
	ALIGN_RIGHT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Align Right"
	ALIGN_JUSTIFY = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Align Justify"
	DECREASE_INDENT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Decrease Indent"
	INCREASE_INDENT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Increase Indent"
	NUMBERED_LIST = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Numbered List"
	BULLETED_LIST = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Bulleted List"
	INSERT_IMAGE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Insert Image"
	CREATE_LINK = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Create Link"
	INSERT_HTML = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.formatToolBar.Insert HTML"

	NEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.standardToolBar.New"
	OPEN = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.standardToolBar.Open"
	SAVE = ''
	UNDO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.standardToolBar.Undo"
	REDO = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.standardToolBar.Redo"
	PASTE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.standardToolBar.Paste"
	CUT = ""
	COPY = ""
	ZOOM_SLIDER = ""
	ZOOM_IN = ""
	ZOOM_OUT = ""

class FormatMenu(object):
	STYLE = ''
	ALIGN = ''
	BOLD = ''
	ITALIC = ''
	UNDERLINE = ''
	STRIKETHROUGH = ''
	INCREASE_INDENT = ''
	DECREASE_INDENT = ''
	NUMBERED_LIST = ''
	BULLETED_LIST = ''
	FONT_NAME = ''
	FONT_SIZE = ''
	TEXT_COLOR = ''
	BACKGROUND_COLOR = ''

class EditMenu(object):
	UNDO = ''
	REDO = ''
	CUT = ''
	COPY = ''
	PASTE = ''
	SELECT_ALL = ''
	INSERT_IMAGE = ''
	CREATE_LINK = ''

class Menu(object):
	EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.menubar.menu_Edit.Edit"
	FORMAT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.menubar.menuF_ormat.Format"
	editMenu = EditMenu
	formatMenu = FormatMenu

class ThingEditorPropterties(object):
	COMPONENT_NAME = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.BaseSubComponent.m_componentName'
	REMOVE_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.BaseSubComponent.m_removeComponent'
	NONE_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.BaseSubComponent.m_slotMappingGB.m_noneRB'
	DIGITAL_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.BaseSubComponent.m_slotMappingGB.m_digitalRB'
	ANALOG_RADIO = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.BaseSubComponent.m_slotMappingGB.m_analogRB'
	SLOT_DROPDOWN = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.BaseSubComponent.m_slotMappingGB.m_slotNum'
	NEW_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.Form.m_newBtn'
	ADD_COMPONENT_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.m_addComponentBtn'
	OPEN_IMAGE_NAME = ".c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.BaseSubComponent.QFileDialog.fileNameEdit"
	OPEN_IMAGE_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.propertiesTab.m_subComponentScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.BaseSubComponent.QFileDialog.buttonBox.Open"

class ThingEditorLayout(object):
	BRING_ITEM_FORWARD_BUTTON = ''
	SEND_ITEM_BACK_BUTTON = ''
	CYCLE_SELECTED_IMAGE_BUTTON = ''
	GRAPHICS_VIEW = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.layoutTab.QGraphicsView1'

class ThingEditorRules(object):
	ADD_BUTTON = ''
	REMOVE_BUTTON = ''
	TABLE = '.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.rulesTab.m_rulesTable'
	SUB_COMPONENT_HEADER = ''
	SLOT_VALUE_HEADER = ''
	IMAGE_HEADER = ''
	COMPONENT_DROPDOWN = ''
	SLOT_VALUE_SPINBOX_START = ''
	SLOT_VALUE_SPINBOX_STOP = ''
	SLOT_VALUE_DROPDOWN = ''
	IMAGE_DROPDOWN = ''
	RULE_NUMBER_COLUMN = ':CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_stackedwidget.rulesTab.m_rulesTable.QHeaderView1.HeaderViewItem'


class Specifications(object):
	shortCutButtons = ShortcutButtons
	menu = Menu
	MAIN_WEBVIEW = '.c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.centralwidget.webView'
	EDIT_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.m_editSpecificationsBtn'
	TEXT_AREA = '.c_physicalTab.qt_tabwidget_stackedwidget.m_specificationsTab.MainWindow.centralwidget.webView.DOCUMENT.HTML1.BODY1'
	ADVANCED_BUTTON = ':CBaseDeviceWidgetClass.m_advancedBtn'

class ThingEditor(object):
	Layout = ThingEditorLayout
	Properties = ThingEditorPropterties
	Rules = ThingEditorRules
	TAB = ':CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_thingEditorTab.BaseThingEditor.m_thingEditor.qt_tabwidget_tabbar'
	None


class IOConfig(object):
	NETWORK_ADAPTER_DROPDOWN = '.c_physicalTab.qt_tabwidget_stackedwidget.m_ioTab.m_networkAdapterCB'
	DIGITAL_SLOTS_SPINBOX = '.c_physicalTab.qt_tabwidget_stackedwidget.m_ioTab.m_digitalSlotsSB.qt_spinbox_lineedit'
	ANALOG_SLOTS_SPINBOX = '.c_physicalTab.qt_tabwidget_stackedwidget.m_ioTab.m_analogSlotsSB.qt_spinbox_lineedit'
	USB_PORTS_SPINBOX = '.c_physicalTab.qt_tabwidget_stackedwidget.m_ioTab.m_usbPortsSB.qt_spinbox_lineedit'
	USAGE_END_DEVICE = ':CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_ioTab.m_usageEndDeviceRadio'
	USAGE_SENSOR = ':CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_ioTab.m_usageSensorRadio'
	
class IoeBaseConst(object):
	specifications = Specifications
	config = ConfigConst
	physical = PhysicalConst
	thingEditor = ThingEditor
	programming = Programming
	ioConfig = IOConfig
	ADVANCED_BUTTON = '.m_advancedBtn'
	TAB_BAR = '.c_physicalTab.qt_tabwidget_tabbar'