class DeviceModules:
	'''Create an empty object'''
	def __init__(self):
		self.moduleBase = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget'

class RouterModules:
	def __init__(self):
		None    
	
	@property
	def r2811(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.ROUTER_2811
		m.left = m.moduleBase + '5'
		m.right = DeviceModules()
		m.right.top = DeviceModules()
		m.right.top.left = m.moduleBase + '4'
		m.right.top.right = m.moduleBase + '3'
		m.right.bottom = DeviceModules()
		m.right.bottom.left = m.moduleBase + '2'
		m.right.bottom.right = m.moduleBase + '1'
		return m
	
	@property    
	def r1941(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.ROUTER_1941
		m.left = m.moduleBase + '2'
		m.right = m.moduleBase + '1'
		return m
	
	@property    
	def r1841(self):
		return self.r1941#Same module slots
	
	@property    
	def r2901(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.ROUTER_2901
		m.left = m.moduleBase + '5'
		m.centerLeft = m.moduleBase + '4'
		m.centerRight = m.moduleBase + '3'
		m.right = m.moduleBase + '2'
		return m
	
	@property    
	def rPT(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.ROUTER_PT
		m.slot1 = m.moduleBase + '16'
		m.slot2 = m.moduleBase + '15'
		m.slot3 = m.moduleBase + '14'
		m.slot4 = m.moduleBase + '13'
		m.slot5 = m.moduleBase + '5'
		m.slot6 = m.moduleBase + '5'
		m.slot7 = m.moduleBase + '5'
		m.slot8 = m.moduleBase + '5'
		m.slot9 = m.moduleBase + '5'
		m.slot10 = m.moduleBase + '5'
		m.currentModule10 = m.moduleBase + '1'
		m.currentModule9 = m.moduleBase + '2'
		m.currentModule8 = m.moduleBase + '3'
		m.currentModule7= m.moduleBase + '4'
		m.currentModule6 = m.moduleBase + '5'
		m.currentModule5 = m.moduleBase + '6'
		return m
	
	@property    
	def r2911(self):
		return self.r2901#Same as 2901
	
	@property    
	def r819hgw(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.ROUTER_819HGW
		return m

	@property    
	def r819iox(self):
		return self.r819hgw
	
	@property  
	def r829(self):
		m = DeviceModules()
		m.left = Modules.MODULE_BASE
		return m
	
	@property    
	def r1240(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.ROUTER_1240
		m.left = DeviceModules()
		m.left.top = m.moduleBase + '4'
		m.left.bottom = m.moduleBase + '5'
		m.right = DeviceModules()
		m.right.top = m.moduleBase + '7'
		m.right.bottom = m.moduleBase + '6'
		m.slot0 = m.moduleBase + '9'
		return m
	
	@property    
	def r2620xm(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.ROUTER_2620XM
		m.left = m.moduleBase + '3'
		m.center = m.moduleBase + '2'
		m.right = m.moduleBase + '1'
		return m
	
	@property    
	def r2621xm(self):
		return self.r2620xm

class SwitchModules:
	def __init__(self):
		None    
	
	@property    
	def s2960(self):
		m = DeviceModules()
		m.rommon_button = m.moduleBase
		return m
	
	@property    
	def s_pt(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.SWITCH_PT
		m.slot0 = m.moduleBase + '10'
		m.slot1 = m.moduleBase + '9'
		m.slot2 = m.moduleBase + '8'
		m.slot3 = m.moduleBase + '7'
		m.slot4 = m.moduleBase + '17'
		m.slot5 = m.moduleBase + '16'
		m.slot6 = m.moduleBase + '15'
		m.slot7 = m.moduleBase + '14'
		m.slot8 = m.moduleBase + '13'
		m.slot9 = m.moduleBase + '12'
		return m
		
	@property    
	def s_pt_empty(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.SWITCH_PT_EMPTY
		m.slot0 = m.moduleBase + '10'
		m.slot1 = m.moduleBase + '9'
		m.slot2 = m.moduleBase + '8'
		m.slot3 = m.moduleBase + '7'
		m.slot4 = m.moduleBase + '6'
		m.slot5 = m.moduleBase + '5'
		m.slot6 = m.moduleBase + '4'
		m.slot7 = m.moduleBase + '3'
		m.slot8 = m.moduleBase + '2'
		m.slot9 = m.moduleBase + '1'
		return m
	
	@property    
	def s3560(self):
		return self.s2960
	
	@property    
	def s_ie_2000(self):
		return False#This device has no slots
	
	@property    
	def s_bridge(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.SWITCH_BRIDGE
		m.slot0 = m.moduleBase + '5'
		m.slot1 = m.moduleBase + '4'
		return m

	@property    
	def s2950_24(self):
		return False#This device has no slots
	
	@property    
	def s2950_t(self):
		return False#This device has no slots
	
class HubModules:
	def __init__(self):
		None    
	
	@property    
	def hub(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.HUB
		m.top = DeviceModules()
		m.bottom = DeviceModules()
		m.top.slot0 = m.moduleBase + '9'
		m.top.slot1 = m.moduleBase + '7'
		m.top.slot2 = m.moduleBase + '16'
		m.top.slot3 = m.moduleBase + '14'
		m.top.slot4 = m.moduleBase + '12'
		m.bottom.slot0 = m.moduleBase + '10'
		m.bottom.slot1 = m.moduleBase + '8'
		m.bottom.slot2 = m.moduleBase + '17'
		m.bottom.slot3 = m.moduleBase + '15'
		m.bottom.slot4 = m.moduleBase + '13'
		return m
	
	@property    
	def repeater(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.REPEATER
		m.slot0 = m.moduleBase + '4'
		m.slot1 = m.moduleBase + '5'
		return m
	
	@property    
	def coaxial_splitter(self):
		return False#This device has no slots
	
class WirelessDeviceModules:
	def __init__(self):
		None
	
	@property    
	def ap_pt(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.AP_PT
		m.slot0 = m.moduleBase + '2'
		return m
	
	@property    
	def ap_a(self):
		return self.ap_pt
	
	@property    
	def ap_n(self):
		return self.ap_pt
	
	@property    
	def wireless_router(self):
		return False
	
	@property    
	def home_gateway(self):
		return False
	
	@property    
	def cell_tower(self):
		m = DeviceModules()
		m.power = PowerButtonsConst
		m.slot0 = m.moduleBase
		return m
	
	@property    
	def central_office_server(self):
		m = DeviceModules()
		m.power = PowerButtonsConst
		return m
	
		
class SecurityModules:
	def __init__(self):
		None
	
	@property    
	def asa(self):
		return False

class WanEmulationModules:
	def __init__(self):
		None
	
	@property    
	def cloud_pt(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.CLOUD_PT
		m.top = DeviceModules()
		m.bottom = DeviceModules()
		m.top.slot1 = m.moduleBase + '16'
		m.top.slot2 = m.moduleBase + '15'
		m.top.slot3 = m.moduleBase + '14'
		m.top.slot4 = m.moduleBase + '13'
		m.top.slot5 = m.moduleBase + '12'
		m.bottom.slot1 = m.moduleBase + '10'
		m.bottom.slot2 = m.moduleBase + '9'
		m.bottom.slot3 = m.moduleBase + '19'
		m.bottom.slot4 = m.moduleBase + '18'
		m.bottom.slot5 = m.moduleBase + '17'
		return m
	
	@property    
	def cloud_pt_empty(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.CLOUD_PT_EMPTY
		m.top = DeviceModules()
		m.bottom = DeviceModules()
		m.top.slot0 = m.moduleBase + '5'
		m.top.slot0 = m.moduleBase + '4'
		m.top.slot0 = m.moduleBase + '3'
		m.top.slot0 = m.moduleBase + '2'
		m.top.slot0 = m.moduleBase + '1'
		m.bottom.slot0 = m.moduleBase + '10'
		m.bottom.slot0 = m.moduleBase + '9'
		m.bottom.slot0 = m.moduleBase + '8'
		m.bottom.slot0 = m.moduleBase + '7'
		m.bottom.slot0 = m.moduleBase + '6'
		return m
	
	@property    
	def dsl_modem(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.DSL_MODEM
		m.slot0 = m.moduleBase + '3'
		return m
	
	@property    
	def cable_modem(self):
		return self.dsl_modem
	
class EndDeviceModules:
	def __init__(self):
		None
	
	@property    
	def pc(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.PC
		m.currentModule = m.moduleBase + '1'
		m.slot0 = m.moduleBase
		m.headphone = m.moduleBase + '4'
		m.mic = m.moduleBase + '5'
		return m
	
	@property    
	def laptop(self):
		return self.pc
	
	@property    
	def server(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.SERVER
		m.slot0 = m.moduleBase #top
		m.slot1 = m.moduleBase + '2'#bottom
		return m
	
	@property    
	def printer(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.PRINTER
		m.slot0 = m.moduleBase
		return m
	
	@property    
	def ip_phone(self):
		m = DeviceModules()
		m.power = m.moduleBase
		return m
	
	@property    
	def home_voip(self):
		return False
	
	@property    
	def analog_phone(self):
		return False
	
	@property    
	def tv(self):
		return False
	
	@property    
	def tablet(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.TABLET
		return m
	
	@property    
	def smart_device(self):
		return False
	
	@property    
	def generic_wireless(self):
		return False
	
	@property    
	def generic_wired(self):
		return False
	
	@property    
	def sniffer(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.SNIFFER
		m.slot0 = m.moduleBase + '1'
		m.slot1 = m.moduleBase + '2'
		return m

class IoeDeviceModules:
	def __init__(self):
		None
	
	@property    
	def mcu(self):
		m = DeviceModules()
		m.moduleBase = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.QWidget1.CModuleContainer1.CModuleTarget'
		m.power = m.moduleBase + '3'
		m.powerAdapter = m.moduleBase + '4'
		m.powerSocket = m.moduleBase + '2'
		m.slot0 = m.moduleBase + '1'
		return m
	
	@property    
	def sbc(self):
		return self.mcu

	@property    
	def thing(self):
		m = DeviceModules()
		m.power = PowerButtonsConst.THING
		m.powerAdapter = m.moduleBase + '14'
		m.powerSocket = m.moduleBase + ''
		return m
	
	
'''
Classes related to physical view
'''
class PowerButtonsConst:
	PC = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget5'
	PC_OFF = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget4'
	LAPTOP = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget5'
	SERVER = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget3'		  
	PRINTER = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget2'
	TABLET = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget5'
	SNIFFER = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget5'
	MODEM = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget2'
	
	AP_PT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget2'
	AP_PT_A = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget2'
	AP_PT_N = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget2'
	COSERVER = ':Central Office Server0.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget'
	
	HUB = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget17'
	REPEATER = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget5'
	
	ROUTER_1941 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.PowerButtonModuleTarget'
	ROUTER_2901 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.PowerButtonModuleTarget'
	ROUTER_2911 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.PowerButtonModuleTarget'
	ROUTER_819IOX = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.PowerButtonModuleTarget'
	ROUTER_819HGW = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.CModuleContainer1.PowerButtonModuleTarget'
	ROUTER_4321 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.PowerButtonModuleTarget'
	ROUTER_PT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget17'
	ROUTER_PT_EMPTY = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget11'
	ROUTER_1841 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.PowerButtonModuleTarget'
	ROUTER_2620XM = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget4'
	ROUTER_2621XM = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget4'
	ROUTER_2811 = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget6'
	
	SWITCH_PT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget17'
	SWITCH_PT_EMPTY = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget11'
	SWITCH_BRIDGE = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget5'
	
	CLOUD_PT = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget19'
	CLOUD_PT_EMPTY = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget11'
	DSL_MODEM = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget2'
	CABLE_MODEM = DSL_MODEM
	
	MCU = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget3'
	SBC = MCU
	THING = MCU
	
class Modules:
	router = RouterModules()
	switch = SwitchModules()
	hub = HubModules()
	wireless = WirelessDeviceModules()
	security = SecurityModules()
	wan = WanEmulationModules()
	endDevice = EndDeviceModules()
	ioe = IoeDeviceModules()
	MODULE_LIST = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_moduleListScrollView.qt_scrollarea_viewport.QWidget1.QFrame1'
	MODULE_BASE = DeviceModules().moduleBase
	PC = MODULE_BASE + '3'
	
class CustomizeImageWindow:
	RESET_BUTTON = '.CBaseCustomImage.btnRestore'
	OK_BUTTON = '.CBaseCustomImage.m_okButton'
	OK_BUTTON_LOGICAL = ':CBaseDeviceWidgetClass.Customize Images in Logical and Physical View.m_okButton'
	CANCEL_BUTTON = '.CBaseCustomImage.m_cancelButton'
	BROWSE_BUTTON = '.CBaseCustomImage.btnBrowse'
	OPEN_BUTTON = '.CBaseCustomImage.QFileDialog.buttonBox.Open'
	FILE_NAME = '.CBaseCustomImage.QFileDialog.fileNameEdit'

class PhysicalConst:
	modules = Modules
	customizeImageWindow = CustomizeImageWindow
	powerbuttons = PowerButtonsConst
	PHYSICAL_VIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab"
	TITLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_titleLabel"
	
	#ZOOM
	ZOOM_IN = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_physicalViewButtonFrame.m_plusButton"
	ZOOM_OUT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_physicalViewButtonFrame.m_minusButton"
	ZOOM_ORIGINAL_SIZE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_physicalViewButtonFrame.m_homeButton"
	
	IMAGE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1.qt_scrollarea_viewport.CModuleContainer1"
	IMAGE_AREA = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.QScrollArea1'
	
	#Customize Icon Physical and Logical View
	CUSTOMIZE_ICON_PHYSICAL_VIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_customImagePVButton"
	CURRENT_ICON_PHYSICAL_VIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_customImagePVButton"
	CUSTOMIZE_ICON_LOGICAL_VIEW = ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_customImageLVButton"
	POWER_BUTTON = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.deviceScrollerArea.qt_scrollarea_viewport.CModuleContainer1.CModuleTarget2'
	CURRENT_MODULE_TEXT = ':CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_textInfoConfig'