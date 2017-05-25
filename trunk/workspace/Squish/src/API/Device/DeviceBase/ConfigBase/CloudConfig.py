##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config as ConfigBase
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.Cloud.CloudConst import CloudConst
from squish import *

def err(msg = ''):
	raise NotImplementedError(msg)

class SettingsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def displayName(self, displayName):
		Util().textCheckPoint(self.objName(CloudConst.config.settings.DISPLAY_NAME_EDIT), displayName)

class Settings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = SettingsCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def displayName(self, displayName):
		Util().setText(self.objName(CloudConst.config.settings.DISPLAY_NAME_EDIT), displayName)

class TvSettings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def filenameEdit(self, filename):
		Util().setText(self.objName(CloudConst.config.tvSettings.TV_IMAGE_PATH_EDIT), filename)
	
	def browseFilesButton(self):
		Util().clickButton(self.objName(CloudConst.config.tvSettings.TV_IMAGE_BROWSE_BUTT))
	
	def addButton(self):
		Util().clickButton(self.objName(CloudConst.config.tvSettings.TV_IMAGE_ADD_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(CloudConst.config.tvSettings.TV_IMAGE_REMOVE_BUTT))

class FrameRelay(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def fromPort(self, fromPort):
		Util().clickItem(self.objName(CloudConst.config.connections.frameRelay.SRC_PORT_COMBO), fromPort)
	
	def fromSublink(self, fromSublink):
		Util().clickItem(self.objName(CloudConst.config.connections.frameRelay.SRC_SUBLINK_COMBO), fromSublink)
	
	def toPort(self, toPort):
		Util().clickItem(self.objName(CloudConst.config.connections.frameRelay.DST_PORT_COMBO), toPort)
	
	def toSublink(self, toSublink):
		Util().clickItem(self.objName(CloudConst.config.connections.frameRelay.DST_SUBLINK_COMBO), toSublink)
	
	def addButton(self):
		Util().clickButton(self.objName(CloudConst.config.connections.frameRelay.CONNECTIONS_ADD_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(CloudConst.config.connections.frameRelay.CONNECTIONS_REMOVE_BUTT))
	
	def add(self, fromPort, fromSublink, toPort, toSublink):
		self.fromPort(fromPort)
		self.fromSublink(fromSublink)
		self.toPort(toPort)
		self.toSublink(toSublink)
		self.addButton()
		
	@property
	def frameRelayTableName(self):
		return self.objName(CloudConst.config.connections.frameRelay.TABLE)
	
	@property
	def frameRelayTable(self):
		return findObject(self.frameRelayTableName)
	
	def selectFrameRelay(self, fromPort, fromSublink, toPort, toSublink):
		err('Add in code to choose based off of the parameters. Possible to shorten parameter list. Need to check.')
	
	def selectRow(self, row):
		Util().click(self.frameRelayTableName + '.item_%s/0'%(row,))
	
	def removeRow(self, row):
		self.selectRow(row)
		self.removeButton()
	
	def remove(self, fromPort, fromSublink, toPort, toSublink):
		self.selectFrameRelay(fromPort, fromSublink, toPort, toSublink)
		self.removeButton()

class DslCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def fromPort(self, expected):
		Util().textCheckPoint(self.objName(CloudConst.config.connections.dsl.SRC_PORT_COMBO), expected, textProperty='currentText')
	
	def toPort(self, expected):
		Util().textCheckPoint(self.objName(CloudConst.config.connections.dsl.DST_PORT_COMBO), expected, textProperty='currentText')

	def rowCount(self, expected):
		if self.objName(self.squishName + CloudConst.config.connections.dsl.CONNECTION_VIEW).rowCount == expected:
			test.passes("Passed")
		else:
			test.fail("Failed")

class Dsl(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = DslCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)

	def fromPort(self, fromPort):
		Util().clickItem(self.objName(CloudConst.config.connections.dsl.SRC_PORT_COMBO), fromPort)
	
	def toPort(self, toPort):
		Util().clickItem(self.objName(CloudConst.config.connections.dsl.DST_PORT_COMBO), toPort)
	
	def addButton(self):
		Util().clickButton(self.objName(CloudConst.config.connections.dsl.CONNECTIONS_ADD_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(CloudConst.config.connections.dsl.CONNECTIONS_REMOVE_BUTT))
	
	@property
	def dslTableName(self):
		return self.objName(CloudConst.config.connections.dsl.TABLE)
	
	@property
	def dslTable(self):
		return findObject(self.dslTableName)
	
	def selectMapping(self, fromPort, toPort):
		err('Add in code for selecting an item in the table')
	
	def add(self, fromPort, toPort):
		self.fromPort(fromPort)
		self.toPort(toPort)
		self.addButton()
	
	def selectRow(self, row):
		Util().click(self.dslTableName + '.item_%s/0'%(row,))
	
	def removeRow(self, row):
		self.selectRow(row)
		self.removeButton()
	
	def remove(self, fromPort, toPort):
		self.selectMapping(fromPort, toPort)
		self.removeButton()

class CableCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def fromPort(self, expected):
		Util().textCheckPoint(self.objName(CloudConst.config.connections.cable.SRC_PORT_COMBO), expected, textProperty='currentText')
	
	def toPort(self, expected):
		Util().textCheckPoint(self.objName(CloudConst.config.connections.cable.DST_PORT_COMBO), expected, textProperty='currentText')

class Cable(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = CableCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def fromPort(self, fromPort):
		Util().clickItem(self.objName(CloudConst.config.connections.cable.SRC_PORT_COMBO), fromPort)
	
	def toPort(self, toPort):
		Util().clickItem(self.objName(CloudConst.config.connections.cable.DST_PORT_COMBO), toPort)
	
	def addButton(self):
		Util().clickButton(self.objName(CloudConst.config.connections.cable.CONNECTIONS_ADD_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(CloudConst.config.connections.cable.CONNECTIONS_REMOVE_BUTT))
	@property
	def cableTableName(self):
		return self.objName(CloudConst.config.connections.cable.TABLE)
	
	@property
	def cableTable(self):
		return findObject(self.cableTableName)
	
	def selectMapping(self, fromPort, toPort):
		err()
	
	def add(self, fromPort, toPort):
		self.fromPort(fromPort)
		self.toPort(toPort)
		self.addButton()
	
	def selectRow(self, row):
		Util().click(self.cableTableName + '.item_%s/0'%(row,))
	
	def removeRow(self, row):
		self.selectRow(row)
		self.removeButton()
	
	def remove(self, fromPort, toPort):
		self.selectMapping(fromPort, toPort)
		self.removeButton()
		
class Connections:
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.frameRelay = FrameRelay(self)
		self.dsl = Dsl(self)
		self.cable = Cable(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.frameRelay.updateName(squishName)
		self.dsl.updateName(squishName)
		self.cable.updateName(squishName)

class Serial(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def portStatus(self, checked = None):
		checkbox = findObject(self.objName(CloudConst.config.interface.serial.PORT_STATUS_CHECKBOX))
		if checked == None:
			Util().click(checkbox)
		elif checked == True:
			if not checkbox.checked:
				Util().click(checkbox)
		elif checked == False:
			if checkbox.checked:
				Util().click(checkbox)
		else:
			raise ValueError('checked must be None, True, or False')
	
	def lmi(self, lmi = 'Cisco'):
		'''LMI can be Cisco, ANSI, or Q933a'''
		if not lmi.capitalize() in ['Cisco', 'ANSI', 'Q933a']:
			raise ValueError('LMI can be Cisco, ANSI, or Q933a')
		Util().clickItem(self.objName(CloudConst.config.interface.serial.LMI_DROPDOWN), lmi)
	
	def dlci(self, dlci):
		Util().setText(self.objName(CloudConst.config.interface.serial.DLCI_NUM_EDIT), str(dlci))
	
	def name(self, name):
		Util().setText(self.objName(CloudConst.config.interface.serial.DLCI_NAME_EDIT), name)
	
	def addButton(self):
		Util().clickButton(self.objName(CloudConst.config.interface.serial.DLCI_ADD_BUTTON))
	
	def removeButton(self):
		Util().clickButton(self.objName(CloudConst.config.interface.serial.DLCI_REMOVE_BUTTON))
	
	@property
	def dlciTableName(self):
		return self.objName(CloudConst.config.interface.serial.DLCI_TABLE)
	
	@property
	def dlciTable(self):
		return findObject(self.dlciTableName)
	
	def selectDlci(self, dlci = None, name = None):
		if name == None and dlci == None:
			raise ValueError('Must provide name, dlci, or both')
		for i in range(self.dlciTable.topLevelItemCount):
			dlciColumn = findObject(self.dlciTableName + '.item_%s/0'%(i,))
			nameColumn = findObject(self.dlciTableName + '.item_%s/1'%(i,))
			if name and dlci:
				if name == nameColumn.text and dlci == dlciColumn.text:
					Util().click(dlciColumn)
					return
			elif name:
				if name == nameColumn.text:
					Util().click(dlciColumn)
					return
			elif dlci:
				if dlci == dlciColumn.text:
					Util().click(dlciColumn)
					return
		raise ValueError('Unable to find row with given name and dlci')
	
	def add(self, dlci, name, lmi = 'Cisco'):
		self.lmi(lmi)
		self.dlci(dlci)
		self.name(name)
		self.addButton()
	
	def remove(self, dlci, name):
		self.selectDlci(dlci, name)
		self.removeButton()

class ModemCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def phoneNumber(self, phoneNumber):
		Util().textCheckPoint(self.objName(CloudConst.config.interface.modem.PHONE_NUMBER_EDIT), phoneNumber)

class Modem(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = ModemCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def phoneNumber(self, phoneNumber):
		Util().setText(self.objName(CloudConst.config.interface.modem.PHONE_NUMBER_EDIT), phoneNumber)

class Ethernet(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def cable(self):
		Util().clickButton(self.objName(CloudConst.config.interface.ethernet.CABLE_RADIO))
	
	def dsl(self):
		Util().clickButton(self.objName(CloudConst.config.interface.ethernet.DSL_RADIO))

class Coax(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

class Interface:	
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.serial = Serial(self)
		self.modem = Modem(self)
		self.ethernet = Ethernet(self)
		self.coax = Coax(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.serial.updateName(squishName)
		self.modem.updateName(squishName)
		self.ethernet.updateName(squishName)
		self.coax.updateName(squishName)

class Config(ConfigBase):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.settings = Settings(self)
		self.tvSettings = TvSettings(self)
		self.connections = Connections(self)
		self.interface = Interface(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.settings.updateName(squishName)
		self.tvSettings.updateName(squishName)
		self.connections.updateName(squishName)
		self.interface.updateName(squishName)