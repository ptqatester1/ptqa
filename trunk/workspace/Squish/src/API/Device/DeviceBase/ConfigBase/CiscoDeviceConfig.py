from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config as ConfigBase
from API.Device.DeviceBase.ConfigBase.CiscoDeviceConfigConst import ConfigConst
from squish import *
import object
from API.Device.DeviceBase.ConfigBase.ConfigBase import (SerialInterface, SerialInterfaceCheck,
														 WiredInterface, WiredInterfaceCheck,
														 SwitchInterface, SwitchInterfaceCheck,
														 WirelessRouterInterface, WirelessRouterInterfaceCheck,
														 CellularInterface, CellularInterfaceCheck,
														 TxRingLimit, TxRingLimitCheck)
														 

class FileDialog(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def filename(self, filename):
		Util().setText(self.objName(ConfigConst.settings.STARTUP_CONF_LOAD_FILE_EDITOR), filename)
	
	def openButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_LOAD_OK))
	
	def saveButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_EXPORT_OK))
	
	def cancelButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_LOAD_CANCEL))
	
class PopupWarnings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def eraseStartupConfigYesButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.NVRAM_ERASE_OK))
	
	def eraseStartupConfigNoButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.NVRAM_ERASE_CANCEL))
	
	def configurationLoadedSuccessfullyOkButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_SAVE_SUCCESSFUL_OK))
	
	def configurationSavedSuccessfullyOkButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_SAVE_SUCCESSFUL_OK))

	def configurationMergedSuccessfullyOkButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_SAVE_SUCCESSFUL_OK))
	
	@property
	def fileAlreadyExistsDialog(self):
		try:
			return findObject(self.objName(ConfigConst.settings.FILE_ALREADY_EXISTS_DIALOG))
		except LookupError, e:
			return False
	
	def fileAlreadyExistsYesButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_LOAD_OVERWRITE_OK))
	
	def fileAlreadyExistsNoButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_LOAD_OVERWRITE_CANCEL))

class CiscoGlobalSettingsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def displayName(self, name):
		Util().textCheckPoint(self.objName(ConfigConst.settings.DISPLAY_NAME_EDIT), name)

	def hostname(self, hostname):
		Util().textCheckPoint(self.objName(ConfigConst.settings.HOSTNAME_EDIT), hostname)
		
	def exportRunningConfigFilename(self, filename):
		Util().textCheckPoint(self.objName(ConfigConst.settings.STARTUP_CONF_LOAD_FILE_EDITOR), filename)

class CiscoGlobalSettings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.fileDialog = FileDialog(self)
		self.popups = PopupWarnings(self)
		self.check = CiscoGlobalSettingsCheck(self)
		None
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.fileDialog.updateName(squishName)
		self.popups.updateName(squishName)
		self.check.updateName(squishName)
		
	def displayName(self, name):
		Util().setText(self.objName(ConfigConst.settings.DISPLAY_NAME_EDIT), name)

	def hostname(self, hostname):
		Util().setText(self.objName(ConfigConst.settings.HOSTNAME_EDIT), hostname)

	def eraseButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.NVRAM_ERASE_BUTT))
	
	def saveButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.NVRAM_SAVE_BUTT))
	
	def loadButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_LOAD_BUTT))

	
	def exportStartupConfigButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.STARTUP_CONF_EXPORT_BUTT))
	
	def exportRunningConfigButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.RUNNING_CONF_EXPORT_BUTT))
	
	def mergeButton(self):
		Util().clickButton(self.objName(ConfigConst.settings.RUNNING_CONF_MERGE_BUTT))

	def eraseNvram(self):
		self.eraseButton()
		self.popups.eraseStartupConfigYesButton()
	
	def loadStartupConfig(self, filename):
		self.loadButton()
		self.fileDialog.filename(filename)
		self.fileDialog.openButton()
		self.popups.configurationLoadedSuccessfullyOkButton()
	
	def exportStartupConfig(self, filename):
		self.exportStartupConfigButton()
		self.fileDialog.filename(filename)
		self.fileDialog.saveButton()
		snooze(2)
		if self.popups.fileAlreadyExistsDialog:
			self.popups.fileAlreadyExistsYesButton()
		self.popups.configurationSavedSuccessfullyOkButton()
	
	def exportRunningConfig(self, filename):
		self.exportRunningConfigButton()
		self.fileDialog.filename(filename)
		self.fileDialog.saveButton()
		if self.popups.fileAlreadyExistsDialog:
			self.popups.fileAlreadyExistsYesButton()
		self.popups.configurationSavedSuccessfullyOkButton()
	
	def mergeRunningConfig(self, filename):
		self.mergeButton()
		self.fileDialog.filename(filename)
		self.fileDialog.openButton()
		self.popups.configurationMergedSuccessfullyOkButton()

	def asaTextCheckPoint(self, p_searchText, p_occurrenceNum = -1, **kwargs):
		Util().textCheckPoint(self.objName(ConfigConst.EQUIVALENT_ASA_COMMANDS_VIEW), p_searchText, p_occurrenceNum, **kwargs)
		
class StaticRouting(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def network(self, network):
		Util().setText(self.objName(ConfigConst.routing.NETWORK_EDIT), network)

	def mask(self, mask):
		Util().setText(self.objName(ConfigConst.routing.NETMASK_EDIT), mask)

	def nextHop(self, nextHop):
		Util().setText(self.objName(ConfigConst.routing.NEXTHOP_EDIT), nextHop)
		

	def addButton(self):
		Util().clickButton(self.objName(ConfigConst.routing.ADD_BUTT))

	@property
	def routingTableName(self):
		return self.objName(ConfigConst.routing.LISTVIEW)

	@property
	def routingTable(self):
		return findObject(self.routingTableName)
		
	def selectRouteInTable(self, route):
		for routeItem in object.children(self.routingTable):
			if 'text' in object.properties(routeItem):
				if route in str(routeItem.text):
					Util().click(routeItem)
					return routeItem
		raise ValueError('Unable to find route ' + route)
		
	def removeButton(self):
		Util().clickButton(self.objName(ConfigConst.routing.REMOVE_BUTT))
	
	def selectRow(self, row):
		Util().click(self.routingTableName + '.item_%s/0'%(row,))
	
	def removeRow(self, row):
		self.selectRow(row)
		self.removeButton()

	def removeRoute(self, network, mask, nextHop):
		if '.' in mask:
			mask = str(sum([bin(int(x)).count('1') for x in mask.split('.')]))#Convert to CIDR notation
		fullRoute = network + '/' + mask + ' via ' + nextHop
		self.selectRouteInTable(fullRoute)
		self.removeButton()
		
	def addRoute(self, network, mask, nextHop):
		self.network(network)
		self.mask(mask)
		self.nextHop(nextHop)
		self.addButton()

class RipRoutingCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		
	def updateName(self, squishName):
		self.squishName = squishName
		
	def network(self, network, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(ConfigConst.routing.RIP_NETWORK_EDIT), **kwargs)
		else:
			Util().setText(self.objName(ConfigConst.routing.RIP_NETWORK_EDIT), network)

	def addButton(self, **kwargs):
		Util().checkProperty(self.objName(ConfigConst.routing.RIP_ADD_BUTT), **kwargs)

		
class RipRouting(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = RipRoutingCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def network(self, network):
		Util().setText(self.objName(ConfigConst.routing.RIP_NETWORK_EDIT), network)

	def addButton(self):
		Util().clickButton(self.objName(ConfigConst.routing.RIP_ADD_BUTT))

	@property
	def routingTableName(self):
		return self.objName(ConfigConst.routing.RIP_LISTVIEW)

	@property
	def routingTable(self):
		return findObject(self.routingTableName)

	def selectRouteInTable(self, route):
		for routeItem in object.children(self.routingTable):
			if 'text' in object.properties(routeItem):
				if route in str(routeItem.text):
					Util().click(routeItem)
					return routeItem
		raise ValueError('Unable to find route ' + route)

	def removeButton(self):
		Util().clickButton(self.objName(ConfigConst.routing.RIP_REMOVE_BUTT))

	def selectRow(self, row):
		Util().click(self.routingTableName + '.item_%s/0'%(row,))
	
	def removeRow(self, row):
		self.selectRow(row)
		self.removeButton()
	
	def removeRouteInTable(self, route):
		self.selectRouteInTable(route)
		self.removeButton()

	def addRoute(self, network):
		self.network(network)
		self.addButton()

class Routing:
	def __init__(self, parent):
		self.squishName = parent.squishName			
		self.rip = RipRouting(self)
		self.static = StaticRouting(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.rip.updateName(self.squishName)
		self.static.updateName(self.squishName)
	
class VlanCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	@property
	def vlanTableObjectName(self):
		return self.objName(ConfigConst.vlan.VLAN_TABLE)
	
	@property
	def vlanTable(self):
		return findObject(self.vlanTableObjectName)
	
	def vlanTableName(self, name, number):
		'''Checks if the vlan with name of (name) is (number)
		name: String (name of the vlan being checked)
		number: String (number that is expected to correspond with vlan name (name)
		'''
		for i in range(self.vlanTable.rowCount):
			rowInfo = [self.vlanTableObjectName + '.item_%s/0'%(i,), self.vlanTableObjectName + '.item_%s/1'%(i,)]
			if findObject(rowInfo[1]).text == name:
				Util().textCheckPoint(rowInfo[0], number)
				break
		raise ValueError("Could not find vlan name %s"%(name))
	
	def vlanTableNumber(self, number, name):
		'''Checks if the vlan with number of (number) is (name)
		number: String (number of the vlan being checked)
		name: String (name that is expected to correspond with vlan number (number)
		'''
		for i in range(self.vlanTable.rowCount):
			rowInfo = [self.vlanTableObjectName + '.item_%s/0'%(i,), self.vlanTableObjectName + '.item_%s/1'%(i,)]
			if findObject(rowInfo[0]).text == number:
				Util().textCheckPoint(rowInfo[1], name)
				break
		raise ValueError("Could not find vlan number %s"%(number))
	
	def vlanTableRow(self, name, number, row):
		'''Checks if the vlan at row (row) is (number) (name)
		number: String || None (number that is expected to correspond to the vlan at row (row))
		name: String || None (name that is  expected to correspond to the vlan at row (row))
		row: String || Int (Row of the vlan to be checked)
		'''
		if not (name or number):
			raise ValueError('Must include a name or number to check')
		rowInfo = [self.vlanTableObjectName + '.item_%s/0'%(row,), self.vlanTableObjectName + '.item_%s/1'%(row,)]
		if number:
			Util().textCheckPoint(rowInfo[0], number)
		if name:
			Util().textCheckPoint(rowInfo[1], name)
			
	def vlanNumber(self, number, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(ConfigConst.vlan.VLAN_NUM_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(ConfigConst.vlan.VLAN_NUM_EDIT), number)

	def vlanName(self, name, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(ConfigConst.vlan.VLAN_NAME_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(ConfigConst.vlan.VLAN_NAME_EDIT), name)


class VlanDatabase(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = VlanCheck(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def vlanNumber(self, number):
		Util().setText(self.objName(ConfigConst.vlan.VLAN_NUM_EDIT), number)

	def vlanName(self, name):
		Util().setText(self.objName(ConfigConst.vlan.VLAN_NAME_EDIT), name)

	def addButton(self):
		Util().clickButton(self.objName(ConfigConst.vlan.VLAN_ADD_BUTT))

	def removeButton(self):
		try:
			findObject(self.objName(ConfigConst.vlan.VLAN_REMOVE_BUTT))
			Util().clickButton(self.objName(ConfigConst.vlan.VLAN_REMOVE_BUTT))
		except LookupError, e:
			findObject(self.objName(ConfigConst.vlan.VLAN_REMOVE_BUTT_3560))
			Util().clickButton(self.objName(ConfigConst.vlan.VLAN_REMOVE_BUTT_3560))

	@property
	def vlanTableName(self):
		try:
			findObject(self.objName(ConfigConst.vlan.VLAN_TABLE))
			return self.objName(ConfigConst.vlan.VLAN_TABLE)
		except LookupError, e:
			findObject(self.objName(ConfigConst.vlan.VLAN_TABLE_3560))
			return self.objName(ConfigConst.vlan.VLAN_TABLE_3560)
	
	@property
	def vlanTable(self):
		return findObject(self.vlanTableName)

	def selectVlan(self, vlan, nameOrNumber):
		if nameOrNumber == 'name':
			Util().clickItem(self.vlanTable, vlan)
		elif nameOrNumber == 'number':
			Util().clickItem(self.vlanTable, vlan)
		else:
			raise ValueError('Should be name or number')

	def selectVlanNumberInTable(self, number):
		self.selectVlan(number, 'number')

	def selectVlanNameInTable(self, name):
		self.selectVlan(name, 'name')
	
	def selectVlanRow(self, row):
		Util().click(self.vlanTableName + '.item_%s/0'%(row,))

	def addVlan(self, name, number):
		self.vlanName(name)
		self.vlanNumber(number)
		self.addButton()

	def removeVlanName(self, name):
		self.selectVlanNameInTable(name)
		self.removeButton()
	
	def removeVlanNumber(self, number):
		self.selectVlanNumberInTable(number)
		self.removeButton()
	
	def removeRow(self, row):
		self.selectVlanRow(row)
		self.removeButton()
		
class EthernetCheck(WiredInterfaceCheck, TxRingLimitCheck):
	None

class Ethernet(WiredInterface, TxRingLimit):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = EthernetCheck(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	None

class Interface:
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.ethernet = Ethernet(self)
		self.switch = SwitchInterface(self)
		self.modem = WiredInterface(self)
		self.serial = SerialInterface(self)
		self.wireless = WirelessRouterInterface(self)
		self.cell = CellularInterface(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.ethernet.updateName(squishName)
		self.modem.updateName(squishName)
		self.serial.updateName(squishName)
		self.wireless.updateName(squishName)
		self.cell.updateName(squishName)
		self.switch.updateName(squishName)

class EquivalentIosCommands(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	@property
	def text(self):
		return str(findObject(self.objName(ConfigConst.EQUIVALENT_IOS_COMMANDS)))
	
	def textCheckPoint(self, p_searchText, p_occurrenceNum = -1, **kwargs):
		if object.exists(self.objName(ConfigConst.EQUIVALENT_IOS_COMMANDS)):
			Util().textCheckPoint(self.objName(ConfigConst.EQUIVALENT_IOS_COMMANDS), p_searchText, p_occurrenceNum, **kwargs)
		elif object.exists(self.objName(ConfigConst.EQUIVALENT_ASA_COMMANDS_VIEW)):
			Util().textCheckPoint(self.objName(ConfigConst.EQUIVALENT_ASA_COMMANDS_VIEW), p_searchText, p_occurrenceNum, **kwargs)
		else:
			err()

class Config(ConfigBase):
	def __init__(self, parent):
		self.squishName = parent.squishName
		super(Config, self).__init__(self)
		self.squishName = parent.squishName
		self.settings = CiscoGlobalSettings(self)
		self.routing = Routing(self)
		self.vlan = VlanDatabase(self)
		self.interface = Interface(self)
		self.equivalentIosCommands = EquivalentIosCommands(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.settings.updateName(self.squishName)
		self.algorithmSettings.updateName(self.squishName)
		self.routing.updateName(self.squishName)
		self.vlan.updateName(self.squishName)
		self.interface.updateName(self.squishName)
		self.equivalentIosCommands.updateName(self.squishName)