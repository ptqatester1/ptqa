##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from squish import *
import object

class PopupWarnings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	@property
	def duplicateFirewallRuleDialog(self):
		try:
			return findObject(self.objName(DesktopConst.firewall.popups.DUPLICATE_FIREWALL_RULE_DIALOG))
		except LookupError, e:
			return False
	
	def duplicateFirewallRuleText(self, text):
		Util().textCheckPoint(self.objName(DesktopConst.firewall.popups.DUPLICATE_FIREWALL_RULE_TEXT), text)
	
	def duplicateFirewallRuleOkButton(self):
		Util().clickButton(self.objName(DesktopConst.firewall.popups.DUPLIACTE_FIREWALL_RULE_OK_BUTTON))
	
	@property
	def invalidRemotePortDialog(self):
		try:
			return findObject(self.objName(DesktopConst.firewall.popups.INVALID_REMOTE_PORT_DIALOG))
		except LookupError, e:
			return False
	
	def invalidRemotePortText(self, text):
		Util().textCheckPoint(self.objName(DesktopConst.firewall.popups.INVALID_REMOTE_PORT_TEXT), text)
	
	def invalidRemotePortOkButton(self):
		Util().clickButton(self.objName(DesktopConst.firewall.popups.INVALID_REMOTE_PORT_OK_BUTTON))

class Firewallv6Check(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def interface(self, interface, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewallv6.INTERFACE_DROPDOWN), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.firewallv6.INTERFACE_DROPDOWN), interface, textProperty='currentText')

	def on(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewallv6.SERVICE_RADIO_ON), **kwargs)
		else:
			Util().clickButton(self.objName(DesktopConst.firewallv6.SERVICE_RADIO_ON))

	def off(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewallv6.SERVICE_RADIO_OFF), **kwargs)
		else:
			Util().clickButton(self.objName(DesktopConst.firewallv6.SERVICE_RADIO_OFF))

	def action(self, action, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewallv6.ACTION_DROPDOWN), **kwargs)
		else:
			Util().clickItem(self.objName(DesktopConst.firewallv6.ACTION_DROPDOWN), action)

	def protocol(self, protocol, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewallv6.PROTOCOL_DROPDOWN), **kwargs)
		else:
			Util().clickItem(self.objName(DesktopConst.firewallv6.PROTOCOL_DROPDOWN), protocol)

	def remoteIp(self, remoteIp, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewallv6.REMOTE_IP_EDIT), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.firewallv6.REMOTE_IP_EDIT), remoteIp)

	def remoteWildcardMask(self, remoteWildcardMask, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewallv6.REMOTE_MASK_EDIT), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.firewallv6.REMOTE_MASK_EDIT), remoteWildcardMask)

	def remotePort(self, remotePort, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewallv6.REMOTE_PORT_EDIT), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.firewallv6.REMOTE_PORT_EDIT), remotePort)

	def localPort(self, localPort, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewallv6.LOCAL_PORT_EDIT), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.firewallv6.LOCAL_PORT_EDIT), localPort)

	def addButton(self, **kwargs):
		Util().checkProperty(self.objName(DesktopConst.firewallv6.ADD_FIREWALL_BUTT), **kwargs)

	def saveButton(self, **kwargs):
		Util().checkProperty(self.objName(DesktopConst.firewallv6.SAVE_FIREWALL_BUTT), **kwargs)

	def removeButton(self, **kwargs):
		Util().checkProperty(self.objName(DesktopConst.firewallv6.REMOVE_FIREWALL_BUTT), **kwargs)

	def _tableTextCheckPoint(self, row, col, text):
		Util().textCheckPoint(self.tableName + '.item_%s/%s'%(row, col), text)
	
	@property
	def tableName(self):
		return self.objName(DesktopConst.firewallv6.ENTRIES_TABLE)
	
	@property
	def table(self):
		return findObject(self.tableName)
		
	def tableActionAt(self, row, action):
		self._tableTextCheckPoint(row, 0, action)
	
	def tableProtocolAt(self, row, protocol):
		self._tableTextCheckPoint(row, 1, protocol)
		
	def tableRemoteIpAt(self, row, ip):
		self._tableTextCheckPoint(row, 2, ip)
	
	def tableRemotePortAt(self, row, port):
		self._tableTextCheckPoint(row, 3, port)
	
	def tableLocalPortAt(self, row, port):
		self._tableTextCheckPoint(row, 4, port)
		
class Firewallv6(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = Firewallv6Check(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)

	def interace(self, interface):
		Util().clickItem(self.objName(DesktopConst.firewallv6.INTERFACE_DROPDOWN), interface)

	def on(self):
		Util().clickButton(self.objName(DesktopConst.firewallv6.SERVICE_RADIO_ON))

	def off(self):
		Util().clickButton(self.objName(DesktopConst.firewallv6.SERVICE_RADIO_OFF))

	def action(self, action):
		Util().clickItem(self.objName(DesktopConst.firewallv6.ACTION_DROPDOWN), action)

	def protocol(self, protocol):
		Util().clickItem(self.objName(DesktopConst.firewallv6.PROTOCOL_DROPDOWN), protocol)

	def remoteIpv6(self, remoteIpv6):
		Util().setText(self.objName(DesktopConst.firewallv6.REMOTE_IP_EDIT), remoteIpv6)

	def subnetMask(self, subnetMask):
		Util().setText(self.objName(DesktopConst.firewallv6.REMOTE_MASK_EDIT), subnetMask)

	def remotePort(self, remotePort):
		Util().setText(self.objName(DesktopConst.firewallv6.REMOTE_PORT_EDIT), remotePort)

	def localPort(self, localPort):
		Util().setText(self.objName(DesktopConst.firewallv6.LOCAL_PORT_EDIT), localPort)

	def addButton(self):
		Util().clickButton(self.objName(DesktopConst.firewallv6.ADD_FIREWALL_BUTT))

	def saveButton(self):
		Util().clickButton(self.objName(DesktopConst.firewallv6.SAVE_FIREWALL_BUTT))

	def removeButton(self):
		Util().clickButton(self.objName(DesktopConst.firewallv6.REMOVE_FIREWALL_BUTT))

	@property
	def tableName(self):
		return self.objName(DesktopConst.firewallv6.ENTRIES_TABLE)
	
	@property
	def tableObject(self):
		try:
			return findObject(self.tableName)
		except LookupError, e:
			return False

	def selectRule(self, action = None, protocol = None, remoteIpv6 = None,
				   subnetMask = None, remotePort = None,
				   localPort = None, row=None):
		'''Will select a rule that matches all of the provided parameters. It is not required
		to provide all the parameters but it will need to be enough to be specific. For example
		if two rules have the action allow then another parameter will need to be provided to 
		distinguish between the two otherwise the first match will be chosen'''
		if not row == None:
			Util().click(self.tableName + '.item_%s/0'%(row,))
		else:
			raise NotImplementedError('Selecting by options other than row has not been implemented yet')

	def removeRule(self, **kwargs):
		if not kwargs:
			raise ValueError('Must provide parameters of action, protocol, remoteIpv6, subnetMask, remotePort, and/or localPort')
		self.selectRule(**kwargs)
		self.removeButton()

	def addRule(self, action, protocol, remoteIpv6, subnetMask, remotePort = None, localPort = None):
		self.action(action)
		self.protocol(protocol)
		self.remoteIpv6(remoteIpv6)
		self.subnetMask(subnetMask)
		if remotePort:
			self.remotePort(remotePort)
		if localPort:
			self.localPort(localPort)
		self.addButton()

	def editRule(self, newAction = None, newProtocol = None, newRemoteIpv6 = None,
				 newSubnetMask = None, newRemotePort = None,
				 newLocalPort = None, **kwargs):
		if not kwargs:
			raise ValueError('Must provide parameters of action, protocol, remoteIpv6, subnetMask, remotePort, and/or localPort')
		self.selectRule(**kwargs)
		if newAction:
			self.action(newAction)
		if newProtocol:
			self.protocol(newProtocol)
		if newRemoteIpv6:
			self.remoteIpv6(newRemoteIpv6)
		if newSubnetMask:
			self.subnetMask(newSubnetMask)
		if newRemotePort:
			self.remotePort(newRemotePort)
		if newLocalPort:
			self.localPort(newLocalPort)
		self.saveButton()

	def close(self):
		Util().clickButton(self.objName(DesktopConst.firewallv6.CLOSE_BUTT))