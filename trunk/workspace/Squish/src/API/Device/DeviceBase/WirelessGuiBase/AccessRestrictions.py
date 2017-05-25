##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.WirelessGuiBase.WirelessGuiBaseConst import WirelessGuiConst
from API.Device.DeviceBase.WirelessGuiBase.ConstantsHelper import ConstantsHelper
from squish import *
import object

class EditFiltersDialog(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	def editIp(self, ip, num):
		'''ip: String (last octet of the IP)
		   num: Int (Which ip to edit)'''
		err()
	
	def editRange(self, number, ip):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.EDIT_LIST_BUTTON))
		Util().setText(WirelessGuiConst.accessRestrictions.EDIT_IP + number, ip)
		Util().clickButton(WirelessGuiConst.accessRestrictions.EDIT_LIST_SAVE_BUTT)
		Util().clickButton(WirelessGuiConst.accessRestrictions.EDIT_LIST_CLOSE_BUTT)
		
	def saveSettingsButton(self):
		err()
	
	def cancelChangesButton(self):
		err()
	
	def closeButton(self):
		err()
		
class AccessRestrictionsCheck(ConstantsHelper):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.isRouter = parent.isRouter

	def updateName(self, squishName):
		self.squishName = squishName
	
	def accessPolicy(self, policyNumber, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.accessRestrictions.ACCESS_POLICY_DROPDOWN), **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.accessRestrictions.ACCESS_POLICY_DROPDOWN), policyNumber, textProperty='currentText', **kwargs)
	
	def deleteThisEntryButton(self, **kwargs):
		Util().checkProperty(self.objName(WirelessGuiConst.accessRestrictions.DELETE_THIS_ENTRY_BUTTON), **kwargs)
	
	def policyName(self, policyName, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.accessRestrictions.EDIT_POLICY_NAME), **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.accessRestrictions.EDIT_POLICY_NAME), policyName, **kwargs)
	
	def enabled(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.accessRestrictions.ENABLED_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.accessRestrictions.ENABLED_RADIO), checked)
	
	def disabled(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.accessRestrictions.DISABLED_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.accessRestrictions.DISABLED_RADIO), checked)
	
	def editListButton(self, **kwargs):
		Util().checkProperty(self.objName(WirelessGuiConst.accessRestrictions.EDIT_LIST_BUTTON), **kwargs)
		
	def deny(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.accessRestrictions.DENY_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.accessRestrictions.DENY_RADIO), checked)
	
	def allow(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.accessRestrictions.ALLOW_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.accessRestrictions.ALLOW_RADIO), checked)
	
	@property
	def applicationsList(self):
		return findObject(self.objName(WirelessGuiConst.accessRestrictions.APPLICATIONS_LIST))
	
	@property
	def blockedList(self):
		return findObject(self.objName(WirelessGuiConst.accessRestrictions.BLOCKED_LIST))

class AccessRestrictions(ConstantsHelper):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.isRouter = parent.isRouter
		self.editFilters = EditFiltersDialog(self)
		self.check = AccessRestrictionsCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.editFilters.updateName(squishName)
		self.check.updateName(squishName)
	
	def accessPolicy(self, policyNumber):
		policyNumber = str(policyNumber)
		if not '(' in policyNumber:
			policyNumber = policyNumber + '()'
		Util().clickItem(self.objName(WirelessGuiConst.accessRestrictions.ACCESS_POLICY_DROPDOWN), policyNumber)
	
	def delteThisEntryButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.DELETE_THIS_ENTRY_BUTTON))
	
	def policyName(self, policyName):
		Util().setText(self.objName(WirelessGuiConst.accessRestrictions.EDIT_POLICY_NAME), policyName)
	
	def enabled(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.ENABLED_RADIO))
	
	def disabled(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.DISABLED_RADIO))
	
	def editListButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.EDIT_LIST_BUTTON))
		
	def deny(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.DENY_RADIO))
	
	def allow(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.ALLOW_RADIO))
	
	@property
	def applicationsList(self):
		return findObject(self.objName(WirelessGuiConst.accessRestrictions.APPLICATIONS_LIST))
	
	@property
	def blockedList(self):
		return findObject(self.objName(WirelessGuiConst.accessRestrictions.BLOCKED_LIST))
	
	def selectApplicationItem(self, protocol):
		for child in object.children(self.applicationsList):
			if 'text' in object.properties(child):
				if protocol in str(child.text):
					Util().click(child)
					return
		raise ValueError('Unable to find protocol: ' + protocol)
	
	def selectBlockedListItem(self, protocol):
		for child in object.children(self.blockedList):
			if 'text' in object.properties(child):
				if protocol in str(child.text):
					Util().click(child)
					return
		raise ValueError('Unable to find protocol: ' + protocol)
	
	def leftButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.LEFT_BUTTON))
	
	def rightButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.RIGHT_BUTTON))
	
	def addToBlockedList(self, protocol):
		self.selectApplicationItem(protocol)
		self.rightButton()
	
	def removeFromBlockedList(self, protocol):
		self.selectBlockedListItem(protocol)
		self.leftButton()
	
	def saveSettingsButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.SAVE_SETTINGS_BUTTON))
	
	def cancelChangesButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.accessRestrictions.CANCEL_SETTINGS_BUTTON))
	
	def appliedPC(self, p_ipAddressTupleList):
		self.editListButton()
		for ipTuplet in p_ipAddressTupleList:
			Util().setText(WirelessGuiConst.accessRestrictions.EDIT_IP + ipTuplet[0], ipTuplet[1])
		Util().clickButton(WirelessGuiConst.accessRestrictions.EDIT_LIST_SAVE_BUTT)
		Util().clickButton(WirelessGuiConst.accessRestrictions.EDIT_LIST_CLOSE_BUTT)
	
	#@summary: set administration password
	#@param p_policyNum: text show on the combo box
	#@param p_policyName: name of the policy that you'd like to name	 
	#@param p_status: self.objName(WirelessGuiConst.accessRestrictions.ENABLE_RADIO or
	#				self.objName(WirelessGuiConst.accessRestrictions.DISABLE_RADIO
	#@param p_ipAddressTupleList: {("1","8"),("2","10")} 1 is the position, 8 is the host address 
	#@param p_restriction: self.objName(WirelessGuiConst.accessRestrictions.DENY_RADIO or
	#					self.objName(WirelessGuiConst.accessRestrictions.ALLOW_RADIO  
	#p_blockedApps: {"HTTPS(443-443)", "POP3(110-110)"}
	def createPolicy(self, p_policyNum, p_policyName, p_status, p_ipAddressTupleList, p_restriction = None, p_blockedApps = None):
		self.accessPolicy(p_policyNum)
		self.policyName(p_policyName)
		if p_status == 'enable':
			self.enabled()
		elif p_status == 'disable':
			self.disabled()
		self.appliedPC(p_ipAddressTupleList)
		if p_restriction == 'allow':
			self.allow()
		elif p_restriction == 'deny':
			self.deny()
		for item in p_blockedApps:
			self.addToBlockedList(item)
		self.saveSettingsButton()