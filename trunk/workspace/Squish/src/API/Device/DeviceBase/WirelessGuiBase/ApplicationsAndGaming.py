##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.WirelessGuiBase.WirelessGuiBaseConst import WirelessGuiConst
from API.Device.DeviceBase.WirelessGuiBase.ConstantsHelper import ConstantsHelper
from squish import *
import object

class SinglePortForwardingCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def enabledCheckbox(self, rowNum, checked = True, **kwargs):
		try:
			checkbox = findObject(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.CHECKBOX_BASE +str(rowNum)))
		except LookupError, e:
			test.log('Unable to find checkbox at row ' + str(rowNum), str(e))
			raise
		if 'property' in kwargs:
			Util().checkProperty(checkbox, **kwargs)
		else:
			Util().isChecked(checkbox, checked)
	
	def applicationName(self, rowNum, application, **kwargs):
		'''protocol: String - (Application Name)
		   rowNum: Int - (Rows 1-5 are the drop downs. The others are line edits.'''
		if float(rowNum) <= 5:
			obj = self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.APPLICATION_NAME_DROPDOWN_BASE + str(rowNum))
		else:
			obj = self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.APPLICATION_NAME_EDIT_BASE + str(rowNum - 5))
		if 'property' in kwargs:
			Util().checkProperty(obj, **kwargs)
		else:
			if float(rowNum) <= 5:
				Util().textCheckPoint(obj, application, textProperty='currentText', **kwargs)
			else:
				Util().textCheckPoint(obj, application, **kwargs)
				
	def externalPort(self, rowNum, port, **kwargs):
		'''Numbering starts at 1 then internal port is an additional 1.
		The 6th row (1,2,3,4,5,6) would be (6 - 5 = 1). (1 * 2 = 2). (2 - 1 = 1). And so forth.
		'''
		row = ((rowNum-5)*2)-1
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.EXTERNAL_PORT_BASE + str(row)), **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.EXTERNAL_PORT_BASE + str(row)), port)
	
	def internalPort(self, rowNum, port, **kwargs):
		row = ((rowNum-5)*2)
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.EXTERNAL_PORT_BASE + str(row)), **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.INTERNALE_PORT_BASE + str(row)), port)
	
	def protocol(self, rowNum, protocol, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.PROTOCOL_BASE + str(rowNum - 5)), **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.PROTOCOL_BASE + str(rowNum - 5)), protocol, textProperty='currentText', **kwargs)
	
	def ip(self, rowNum, ip, **kwargs):
		if rowNum <= 5:
			obj = self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.IP_EDIT_BASE + str(rowNum)) + '.QLineEdit1'
		else:
			obj = self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.IP_EDIT_BASE_2 + str(rowNum - 5))
		if 'property' in kwargs:
			Util().checkProperty(obj, **kwargs)
		else:
			Util().textCheckPoint(obj, ip, **kwargs)

class SinglePortForwarding(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = SinglePortForwardingCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def enabledCheckbox(self, rowNum, checked = None):
		try:
			checkbox = findObject(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.CHECKBOX_BASE +str(rowNum)))
		except LookupError, e:
			test.log('Unable to find checkbox at row ' + str(rowNum), str(e))
			raise
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
	
	def applicationName(self, rowNum, application):
		'''protocol: String - (Application Name)
		   rowNum: Int - (Rows 1-5 are the drop downs. The others are line edits.'''
		if float(rowNum) <= 5:
			Util().clickItem(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.APPLICATION_NAME_DROPDOWN_BASE + str(rowNum)), application)
		else:
			Util().setText(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.APPLICATION_NAME_EDIT_BASE + str(rowNum - 5)), application)
		
	def externalPort(self, rowNum, port):
		row = ((rowNum-5)*2)-1
		Util().setText(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.EXTERNAL_PORT_BASE + str(row)), port)
	
	def internalPort(self, rowNum, port):
		row = ((rowNum-5)*2)
		Util().setText(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.INTERNALE_PORT_BASE + str(row)), port)
	
	def protocol(self, rowNum, protocol):
		if not protocol in ['TCP', 'UDP', 'Both']:
			raise ValueError('protocol must be TCP, UDP, or Both')
		Util().clickItem(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.PROTOCOL_BASE + str(rowNum - 5)), protocol)
	
	def ip(self, rowNum, ip):
		if rowNum <= 5:
			Util().setText(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.IP_EDIT_BASE + str(rowNum)) + '.QLineEdit1', ip.split('.')[-1])
		else:
			Util().setText(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.IP_EDIT_BASE_2 + str(rowNum - 5)), ip.split('.')[-1])
			
	
	def addApplication(self, rowNum, application, protocol, ip, checked = None, externalPort = None, internalPort = None):
		self.applicationName(rowNum, application)
		if float(rowNum) > 5:
			if externalPort:
				self.externalPort(rowNum, externalPort)
			if internalPort:
				self.internalPort(rowNum, internalPort)
		if protocol:
			self.protocol(rowNum, protocol)
		self.ip(rowNum, ip)
		self.enabledCheckbox(rowNum, checked)
		
	def saveSettingsButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.SAVE_SETTINGS_BUTTON))
	
	def cancelChangesButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.applicationAndGaming.portForwarding.CANCEL_SETTINGS_BUTTON))

class DmzCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	def enabled(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.applicationAndGaming.dmz.ENABLED_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.applicationAndGaming.dmz.ENABLED_RADIO), checked)
	
	def disabled(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.applicationAndGaming.dmz.DISABLED_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.applicationAndGaming.dmz.DISABLED_RADIO), checked=True)
	
	def ipAddress(self, ip, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.applicationAndGaming.dmz.DST_IP_ADDRESS_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.applicationAndGaming.dmz.DST_IP_ADDRESS_EDIT), ip)
	
	def ipLabel(self, ip, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(WirelessGuiConst.applicationAndGaming.dmz.DST_IP_LABEL), **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.applicationAndGaming.dmz.DST_IP_LABEL), ip)
	
class Dmz(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = DmzCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def enabled(self):
		Util().clickButton(self.objName(WirelessGuiConst.applicationAndGaming.dmz.ENABLED_RADIO))
	
	def disabled(self):
		Util().clickButton(self.objName(WirelessGuiConst.applicationAndGaming.dmz.DISABLED_RADIO))
	
	def ipAddress(self, ip):
		Util().setText(self.objName(WirelessGuiConst.applicationAndGaming.dmz.DST_IP_ADDRESS_EDIT), ip.split('.')[-1])
	
	def saveSettingsButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.applicationAndGaming.dmz.SAVE_SETTINGS_BUTTON))
	
	def cancelChangesButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.applicationAndGaming.dmz.CANCEL_SETTINGS_BUTTON))

class ApplicationsAndGaming(ConstantsHelper):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.isRouter = parent.isRouter
		self.singlePortFowarding = SinglePortForwarding(self)
		self.dmz = Dmz(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.singlePortFowarding.updateName(squishName)
		self.dmz.updateName(squishName)