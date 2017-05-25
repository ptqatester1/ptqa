##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.WirelessGuiBase.ConstantsHelper import ConstantsHelper
from API.Device.DeviceBase.WirelessGuiBase.WirelessGuiBaseConst import WirelessGuiConst
from squish import *
import object

class Tabs(ConstantsHelper):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.isRouter = parent.isRouter
		
	def updateName(self, squishName):
		self.squishName = squishName

	#@summary: select what tab on the GUI to go to
	#@param p_guiTab: LinksysRouterConst.Gui.SETUP_TAB
	def selectTabHeader(self, p_guiTab):
		if self.isRouter:
			scrollbar = findObject(self.objName(WirelessGuiConst.VERTICAL_SCROLLBAR))
		else:
			scrollbar = findObject(self.objName(WirelessGuiConst.PC_VERTICAL_SCROLLBAR))
		scrollbar.setValue(0)
		if self.isRouter:
			header = findObject(self.objName(WirelessGuiConst.tabs.TAB_HEADER))
		else:
			header = findObject(self.objName(WirelessGuiConst.tabs.PC_TAB_HEADER))
		document = header.document
		regex = QRegExp("^" + p_guiTab + "$")
		#test.log(regex.pattern())
		textCursor = document.find(regex, 0)
		rect = header.cursorRect(textCursor)
		top = rect.top()
		bottom = rect.bottom()
		left = rect.left()
		right = rect.right()
		x = left - 10#Slight offset
		y = top + 5
		Util().click_x_y(header, x, y)
		
	def setup(self):
		self.selectTabHeader(WirelessGuiConst.tabs.SETUP_TAB)
	
	def wireless(self):
		self.selectTabHeader(WirelessGuiConst.tabs.WIRELESS_TAB)
	
	def basicWirelessSettings(self):
		self.wireless()
		self.selectTabHeader(WirelessGuiConst.tabs.wireless.BASIC_WIRELESS_SETTINGS_TAB)
	
	def wirelessSecurity(self):
		self.wireless()
		self.selectTabHeader(WirelessGuiConst.tabs.wireless.WIRELESS_SECURITY_TAB)
	
	def wirelessMacFilter(self):
		self.wireless()
		self.selectTabHeader(WirelessGuiConst.tabs.wireless.WIRELESS_MAC_FILTER_TAB)
	
	def advancdedWirelessSettings(self):
		self.wireless()
		self.selectTabHeader(WirelessGuiConst.tabs.wireless.ADVANCED_WIRELESS_SETTINGS_TAB)
	
	def security(self):
		self.selectTabHeader(WirelessGuiConst.tabs.SECURITY_TAB)
	
	def accessRestrictions(self):
		self.selectTabHeader(WirelessGuiConst.tabs.ACCESS_RESTRICTIONS_TAB)
	
	def applicationsAndGaming(self):
		self.selectTabHeader(WirelessGuiConst.tabs.APPLICATIONS_AND_GAMING_TAB)
	
	def singlePortForwarding(self):
		self.applicationsAndGaming()
		self.selectTabHeader(WirelessGuiConst.tabs.applicationsAndGaming.SINGLE_PORT_FORWARDING_TAB)
	
	def dmz(self):
		self.applicationsAndGaming()
		self.selectTabHeader(WirelessGuiConst.tabs.applicationsAndGaming.DMZ_TAB)
	
	def administration(self):
		self.selectTabHeader(WirelessGuiConst.tabs.ADMINISTRATION_TAB)
	
	def management(self):
		self.administration()
		self.selectTabHeader(WirelessGuiConst.tabs.admininstration.MANAGEMENT_TAB)
	
	def facotryDefaults(self):
		self.administration()
		self.selectTabHeader(WirelessGuiConst.tabs.admininstration.FACTORY_DEFAULTS_TAB)
	
	def firmwareUpgrade(self):
		self.administration()
		self.selectTabHeader(WirelessGuiConst.tabs.admininstration.FIRMWARE_UPGRADE_TAB)
		
	def status(self):
		self.selectTabHeader(WirelessGuiConst.tabs.STATUS_TAB)
	
	def router(self):
		self.status()
		self.selectTabHeader(WirelessGuiConst.tabs.status.ROUTER_TAB)
	
	def localNetwork(self):
		self.status()
		self.selectTabHeader(WirelessGuiConst.tabs.status.LOCAL_NETWORK_TAB)
	
	def wirelessNetwork(self):
		self.status()
		self.selectTabHeader(WirelessGuiConst.tabs.status.WIRELESS_NETWORK_TAB)