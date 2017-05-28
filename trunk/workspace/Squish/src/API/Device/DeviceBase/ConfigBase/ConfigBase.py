##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ConfigBase.ConfigItems.Interfaces import *
from squish import *
from __builtin__ import object as Object

class ConfigBaseCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		
	def updateName(self, squishName):
		self.squishName = squishName
	
	def dhcp(self, checked = True):
		Util().isChecked(self.objName(ConfigConst.settings.DHCP_RADIO), checked)

	def static(self, checked = True):
		Util().isChecked(self.objName(ConfigConst.settings.STATIC_RADIO), checked)
		
	def displayName(self, name):
		Util().textCheckPoint(self.objName(ConfigConst.settings.DISPLAY_NAME_EDIT), name)
		
	def gateway(self, gateway):
		Util().textCheckPoint(self.objName(ConfigConst.settings.GATEWAY_EDIT), gateway)
		
	def dns(self, dns):
		Util().textCheckPoint(self.objName(ConfigConst.settings.DNS_EDIT), dns)
	
	def dhcpv6(self, checked = True):
		Util().isChecked(self.objName(ConfigConst.settings.DHCP_RADIO_IPV6), checked)

	def autoconfig(self, checked = True):
		Util().isChecked(self.objName(ConfigConst.settings.AUTO_CONFIG_RADIO), checked)

	def staticv6(self, checked = True):
		Util().isChecked(self.objName(ConfigConst.settings.STATIC_RADIO_IPV6), checked)
	
	def gatewayv6(self, gatewayv6):
		Util().textCheckPoint(self.objName(ConfigConst.settings.IPV6_GATEWAY), gatewayv6)

	def dnsv6(self, dnsv6):
		Util().textCheckPoint(self.objName(ConfigConst.settings.IPV6_DNS_EDIT), dnsv6)
	
	def displayCLI(self, p_searchText, p_occurrenceNum = -1, **kwargs):
		Util().textCheckPoint(self.objName(ConfigConst.DISPLAY_CLI), p_searchText, p_occurrenceNum, **kwargs)

	def asaTextCheckPoint(self, p_searchText, p_occurrenceNum = -1, **kwargs):
		Util().textCheckPoint(self.objName(ConfigConst.EQUIVALENT_ASA_COMMANDS_VIEW), p_searchText, p_occurrenceNum, **kwargs)
		
class GlobalSettings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = ConfigBaseCheck(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def displayName(self, name):
		Util().setText(self.objName(ConfigConst.settings.DISPLAY_NAME_EDIT), name)

	def dhcp(self):
		Util().clickButton(self.objName(ConfigConst.settings.DHCP_RADIO))

	def static(self):
		Util().clickButton(self.objName(ConfigConst.settings.STATIC_RADIO))

	def gateway(self, gateway):
		Util().setText(self.objName(ConfigConst.settings.GATEWAY_EDIT), gateway)
		
	def dns(self, dns):
		Util().setText(self.objName(ConfigConst.settings.DNS_EDIT), dns)
		
	def dhcpv6(self):
		Util().clickButton(self.objName(ConfigConst.settings.DHCP_RADIO_IPV6))

	def autoconfig(self):
		Util().clickButton(self.objName(ConfigConst.settings.AUTO_CONFIG_RADIO))

	def staticv6(self):
		Util().clickButton(self.objName(ConfigConst.settings.STATIC_RADIO_IPV6))

	def gatewayv6(self, gatewayv6):
		Util().setText(self.objName(ConfigConst.settings.IPV6_GATEWAY), gatewayv6)

	def dnsv6(self, dnsv6):
		Util().setText(self.objName(ConfigConst.settings.IPV6_DNS_EDIT), dnsv6)
		
	def serverAddress(self, serverAddress):
		Util().setText(self.objName(ConfigConst.settings.SERVER_ADDRESS), serverAddress)

class AlgorithmSettingsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
			
	def updateName(self, squishName):
		self.squishName = squishName
	
	def globalSettings(self, checked=True, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ConfigConst.algorithmSettings.GLOBAL_SETTINGS_CHECKBOX), kwargs['property'], kwargs['value'])
		else:
			Util().isChecked(self.objName(ConfigConst.algorithmSettings.GLOBAL_SETTINGS_CHECKBOX), checked)
				
	def halfOpenSessionMultiplier(self, multiplier, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ConfigConst.algorithmSettings.HALF_OPEN_SESSION_MULTIPLIER_EDIT), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(ConfigConst.algorithmSettings.HALF_OPEN_SESSION_MULTIPLIER_EDIT), multiplier, **kwargs)

	def maxConnections(self, max, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ConfigConst.algorithmSettings.MAX_CONNECTIONS_EDIT), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(ConfigConst.algorithmSettings.MAX_CONNECTIONS_EDIT), max, **kwargs)

	def maxOpen(self, max, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ConfigConst.algorithmSettings.MAX_OPENED_SESSIONS_EDIT), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(ConfigConst.algorithmSettings.MAX_OPENED_SESSIONS_EDIT), max, **kwargs)

	def maxRetransmission(self, max, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ConfigConst.algorithmSettings.MAX_RETRANSMISSION_TIMEOUT_EDIT), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(ConfigConst.algorithmSettings.MAX_RETRANSMISSION_TIMEOUT_EDIT), max, **kwargs)
	
	def stormControlMultiplierLabel(self, text, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ConfigConst.algorithmSettings.STORM_CONTROL_LBL), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(ConfigConst.algorithmSettings.STORM_CONTROL_LBL), text, **kwargs)

class AlgorithmSettings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = AlgorithmSettingsCheck(self)
			
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)

	def globalSettings(self, checked=None):
		'''If None is passed the checkbox will be toggled
		True or False can be passed as arguments which will choose the checkbox state'''
		if checked == None:
			Util().click(self.objName(ConfigConst.algorithmSettings.GLOBAL_SETTINGS_CHECKBOX))
		else:
			checkbox = findObject(self.objName(ConfigConst.algorithmSettings.GLOBAL_SETTINGS_CHECKBOX))
			if checked == True:
				if not checkbox.checked:
					Util().click(self.objName(ConfigConst.algorithmSettings.GLOBAL_SETTINGS_CHECKBOX))
			elif checked == False:
				if checkbox.checked:
					Util().click(self.objName(ConfigConst.algorithmSettings.GLOBAL_SETTINGS_CHECKBOX))
			else:
				raise ValueError('Parameter should be None, True, or False')
				
	def halfOpenSessionMultiplier(self, multiplier):
		Util().setText(self.objName(ConfigConst.algorithmSettings.HALF_OPEN_SESSION_MULTIPLIER_EDIT), multiplier)

	def maxConnections(self, max):
		Util().setText(self.objName(ConfigConst.algorithmSettings.MAX_CONNECTIONS_EDIT), max)

	def maxOpen(self, max):
		Util().setText(self.objName(ConfigConst.algorithmSettings.MAX_OPENED_SESSIONS_EDIT), max)

	def maxRetransmission(self, max):
		Util().setText(self.objName(ConfigConst.algorithmSettings.MAX_RETRANSMISSION_TIMEOUT_EDIT), max)

	def stormControlMultiplier(self, multiplier):
		Util().setText(self.objName(ConfigConst.algorithmSettings.STORM_CONTROL_MULTIPLIER_EDIT), multiplier)

class Interface:
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.wired = WiredInterface(self)
		self.wireless = WirelessInterface(self)
		self.cellular = CellularInterface(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		for interface in [self.wired, self.wireless, self.cellular]:
			interface.updateName(self.squishName)

class ConfigPopupWarnings(SquishObjectName):
	def __init__(self, parent):
		self.util = Util()
		self.squishName = parent.squishName
		
	def updateName(self, squishName):
		self.squishName = squishName
		
	@property
	def deviceMustBePoweredOnDialog(self):
		try:
			return findObject(ConfigConst.popups.ERROR_MESSAGE_DIALOG)
		except LookupError, e:
			return False
	
	def deviceMustBePoweredOnOkButton(self):
		self.util.clickButton(ConfigConst.popups.ERROR_MESSAGE_OK_BUTTON)
		
	def deviceBootingOkButton(self):
		self.util.clickButton(ConfigConst.popups.DEVICE_BOOTING_POPUP_OK)

class Config(SquishObjectName, Object):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.settings = GlobalSettings(self)
		self.algorithmSettings = AlgorithmSettings(self)
		self.interface = Interface(self)
		self.check = ConfigBaseCheck(self)
		self.popups = ConfigPopupWarnings(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.settings.updateName(self.squishName)
		self.algorithmSettings.updateName(self.squishName)
		self.interface.updateName(self.squishName)
		self.check.updateName(self.squishName)
	
	@property
	def interfaceListName(self):
		return self.objName(".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.m_menuCfgScrollView.qt_scrollarea_viewport.scrollAreaWidget.QFrame1")
	
	@property
	def interfaceListObject(self):
		return findObject(self.interfaceListName)
	
	def getInterfaceObject(self, p_interface):
		obj = self.interfaceListName + "." + p_interface
		return findObject(obj)
	
	def selectInterface(self, p_interface):
		'''Select which part of the config to interact with
		pc.config.selectInterface('Settings')'''
		obj = self.getInterfaceObject(p_interface)
		Util().clickButton(obj)
		snooze(1)