##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.WirelessGuiBase.WirelessGuiBaseConst import WirelessGuiConst
from API.Device.DeviceBase.WirelessGuiBase.ConstantsHelper import ConstantsHelper
from squish import *
import object 

class Management(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def routerPassword(self, password):
		Util().setText(self.objName(WirelessGuiConst.administration.management.ROUTER_PASSWORD_EDIT), password)
	
	def reenterPassword(self, password):
		Util().setText(self.objName(WirelessGuiConst.administration.management.PC_REENTER_PASSWORD_EIDT), password)
		
	def backupConfigurationButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.BACKUP_CONFIGURATIONS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.PC_BACKUP_CONFIGURATIONS_BUTTON))
	
	def restoreConfigurationButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.RESTORE_CONFIGURATIONS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.PC_RESTORE_CONFIGURATIONS_BUTTON))

	def remoteManagementEnabled(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.REMOTE_MANAGEMENT_ENABLED_RADIO))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.PC_REMOTE_MANAGEMENT_ENABLED_RADIO))

	def remoteManagementDisabled(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.REMOTE_MANAGEMENT_DISABLED_RADIO))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.PC_REMOTE_MANAGEMENT_DISABLED_RADIO))

	def saveSettingsButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.SAVE_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.PC_SAVE_SETTINGS_BUTTON))

	def cancelChangesButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.CANCEL_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.management.PC_CANCEL_SETTINGS_BUTTON))

	def setPassword(self, password):
		self.routerPassword(password)
		self.reenterPassword(password)

	def directory(self, directory):
		Util().clickItem(self.objName(WirelessGuiConst.administration.management.BACKUP_DIRECTORY), directory)
		Util().clickButton(self.objName(WirelessGuiConst.administration.management.BACKUP_CONFIG_OK))
					
class FactoryDefaults(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def restoreFactoryDefaultsButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.factoryDefaults.RESTORE_FACTORY_DEFAULTS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.factoryDefaults.PC_RESTORE_FACTORY_DEFAULTS_BUTTON))
	
	def restoreOkButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.factoryDefaults.WARNING_DIALOG_OK_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.factoryDefaults.PC_WARNING_DIALOG_OK_BUTTON))
	
	def restoreCancelButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.factoryDefaults.WARNING_DIALOG_CANCEL_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.factoryDefaults.PC_WARNING_DIALOG_CANCEL_BUTTON))

class FirmwareUpgradeBrowse(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	@property
	def listName(self):
		return self.objName(WirelessGuiConst.administration.firmwareUpgrade.browse.LIST)
	
	@property
	def listObject(self):
		try:
			return findObject(self.listName)
		except LookupError, e:
			return False
	
	def _getFirmwareObject(self, name):
		for i in range(self.listObject.topLevelItemCount):
			for child in object.children(findObject('%s.item_%s/0'%(self.listName, i))):
				try:
					if name in str(child.text):
						return child
				except AttributeError, e:
					continue
		raise ValueError('Unable to find file :%s'%(name,))
			
	def okButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.browse.OK_BUTTON))
	
	def cancelButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.browse.CANCEL_BUTTON))
	
	def selectFirmware(self, name):
		Util().clickItem(self.objName(WirelessGuiConst.administration.firmwareUpgrade.browse.LIST), name)
		#Util().click(self._getFirmwareObject(name))

class FirmwareUpgradeCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def progress(self, percent):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.administration.firmwareUpgrade.PROGRESS_BAR_PERCENT), percent)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.administration.firmwareUpgrade.PC_PROGRESS_BAR_PERCENT), percent)

class FirmwareUpgrade(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.browse = FirmwareUpgradeBrowse(self)
		self.check = FirmwareUpgradeCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.browse.updateName(squishName)
		self.check.updateName(squishName)
	
	def filenameEdit(self, filename):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.administration.firmwareUpgrade.FILE_EDIT), filename)
		else:
			Util().setText(self.objName(WirelessGuiConst.administration.firmwareUpgrade.PC_FILE_EDIT), filename)
		
	def browseButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.BROWSE_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.PC_BROWSE_BUTTON))

	def startUpgradeButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.START_TO_UPGRADE_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.PC_START_TO_UPGRADE_BUTTON))
		
	def saveSettingsButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.SAVE_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.PC_SAVE_SETTINGS_BUTTON))

	def cancelChangesButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.CANCEL_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.administration.firmwareUpgrade.PC_CANCEL_SETTINGS_BUTTON))

	def upgrade(self, name):
		self.browseButton()
		self.browse.selectFirmware(name)
		self.browse.okButton()
		self.startUpgradeButton()
		

class Administration:
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.isRouter = parent.isRouter
		self.management = Management(self)
		self.factoryDefaults = FactoryDefaults(self)
		self.firmwareUpgrade = FirmwareUpgrade(self)
		self.firmwareUpgradeBrowse = FirmwareUpgradeBrowse(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.management.updateName(self.squishName)
		self.factoryDefaults.updateName(self.squishName)
		self.firmwareUpgrade.updateName(self.squishName)
		self.firmwareUpgradeBrowse.updateName(squishName)