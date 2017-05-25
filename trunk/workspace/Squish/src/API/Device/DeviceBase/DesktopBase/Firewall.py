##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst

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

class FirewallCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def interface(self, interface, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewall.INTERFACE_DROPDOWN), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.firewall.INTERFACE_DROPDOWN), interface, textProperty='currentText')

	def on(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewall.SERVICE_RADIO_ON), **kwargs)
		else:
			Util().clickButton(self.objName(DesktopConst.firewall.SERVICE_RADIO_ON))

	def off(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewall.SERVICE_RADIO_OFF), **kwargs)
		else:
			Util().clickButton(self.objName(DesktopConst.firewall.SERVICE_RADIO_OFF))

	def action(self, action, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewall.ACTION_DROPDOWN), **kwargs)
		else:
			Util().clickItem(self.objName(DesktopConst.firewall.ACTION_DROPDOWN), action)

	def protocol(self, protocol, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewall.PROTOCOL_DROPDOWN), **kwargs)
		else:
			Util().clickItem(self.objName(DesktopConst.firewall.PROTOCOL_DROPDOWN), protocol)

	def remoteIp(self, remoteIp, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewall.REMOTE_IP_EDIT), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.firewall.REMOTE_IP_EDIT), remoteIp)

	def remoteWildcardMask(self, remoteWildcardMask, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewall.REMOTE_MASK_EDIT), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.firewall.REMOTE_MASK_EDIT), remoteWildcardMask)

	def remotePort(self, remotePort, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewall.REMOTE_PORT_EDIT), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.firewall.REMOTE_PORT_EDIT), remotePort)

	def localPort(self, localPort, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.firewall.LOCAL_PORT_EDIT), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.firewall.LOCAL_PORT_EDIT), localPort)

	def addButton(self, **kwargs):
		Util().checkProperty(self.objName(DesktopConst.firewall.ADD_FIREWALL_BUTT), **kwargs)

	def saveButton(self, **kwargs):
		Util().checkProperty(self.objName(DesktopConst.firewall.SAVE_FIREWALL_BUTT), **kwargs)

	def removeButton(self, **kwargs):
		Util().checkProperty(self.objName(DesktopConst.firewall.REMOVE_FIREWALL_BUTT), **kwargs)

	def _tableTextCheckPoint(self, row, col, text):
		Util().textCheckPoint(self.tableName + '.item_%s/%s'%(row, col), text)
	
	@property
	def tableName(self):
		return self.objName(DesktopConst.firewall.FIREWALL_ENTRIES_TABLE)
	
	@property
	def table(self):
		return findObject(self.tableName)
		
	def tableActionAt(self, row, action):
		self._tableTextCheckPoint(row, 0, action)
	
	def tableProtocolAt(self, row, protocol):
		self._tableTextCheckPoint(row, 1, protocol)
		
	def tableRemoteIpAt(self, row, ip):
		self._tableTextCheckPoint(row, 2, ip)
	
	def tableRemoteWildCardAt(self, row, mask):
		self._tableTextCheckPoint(row, 3, mask)
	
	def tableRemotePortAt(self, row, port):
		self._tableTextCheckPoint(row, 4, port)
	
	def tableLocalPortAt(self, row, port):
		self._tableTextCheckPoint(row, 5, port)
		
class Firewall(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = FirewallCheck(self)
		self.popups = PopupWarnings(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		self.popups.updateName(squishName)

	def interface(self, interface):
		Util().clickItem(self.objName(DesktopConst.firewall.INTERFACE_DROPDOWN), interface)

	def on(self):
		Util().clickButton(self.objName(DesktopConst.firewall.SERVICE_RADIO_ON))

	def off(self):
		Util().clickButton(self.objName(DesktopConst.firewall.SERVICE_RADIO_OFF))

	def action(self, action):
		Util().clickItem(self.objName(DesktopConst.firewall.ACTION_DROPDOWN), action)

	def protocol(self, protocol):
		Util().clickItem(self.objName(DesktopConst.firewall.PROTOCOL_DROPDOWN), protocol)

	def remoteIp(self, remoteIp):
		Util().setText(self.objName(DesktopConst.firewall.REMOTE_IP_EDIT), remoteIp)

	def remoteWildcardMask(self, remoteWildcardMask):
		Util().setText(self.objName(DesktopConst.firewall.REMOTE_MASK_EDIT), remoteWildcardMask)

	def remotePort(self, remotePort):
		Util().setText(self.objName(DesktopConst.firewall.REMOTE_PORT_EDIT), remotePort)

	def localPort(self, localPort):
		Util().setText(self.objName(DesktopConst.firewall.LOCAL_PORT_EDIT), localPort)

	def addButton(self):
		Util().clickButton(self.objName(DesktopConst.firewall.ADD_FIREWALL_BUTT))

	def saveButton(self):
		Util().clickButton(self.objName(DesktopConst.firewall.SAVE_FIREWALL_BUTT))

	def removeButton(self):
		Util().clickButton(self.objName(DesktopConst.firewall.REMOVE_FIREWALL_BUTT))

	def selectRule(action = None, protocol = None, remoteIp = None,
				   remoteWildcardMask = None, remotePort = None,
				   localPort = None):
		'''Will select a rule that matches all of the provided parameters. It is not required
		to provide all the parameters but it will need to be enough to be specific. For example
		if two rules have the action allow then another parameter will need to be provided to 
		distinguish between the two otherwise the first match will be chosen'''
		err()

	def selectRow(self, row):
		'''Select row on the firewall table entries. Ex. 0/0'''
		Util().clickItem(self.objName(DesktopConst.firewall.FIREWALL_ENTRIES_TABLE), row)
		
	def removeRule(self, **kwargs):
		if not kwargs:
			raise ValueError('Must provide parameters of action, protocol, remoteIp, remoteWildcardMask, remotePort, and/or localPort')
		self.selectRule(**kwargs)
		self.removeButton()

	def addRule(self, action, protocol, remoteIp, remoteWildcardMask, remotePort = None, localPort = None):
		self.action(action)
		self.protocol(protocol)
		self.remoteIp(remoteIp)
		self.remoteWildcardMask(remoteWildcardMask)
		if remotePort:
			self.remotePort(remotePort)
		if localPort:
			self.localPort(localPort)
		self.addButton()

	def editRule(self, newAction = None, newProtocol = None, newRemoteIp = None,
				 newRemoteWildcardMask = None, newRemotePort = None,
				 newLocalPort = None, **kwargs):
		if not kwargs:
			raise ValueError('Must provide parameters of action, protocol, remoteIp, remoteWildcardMask, remotePort, and/or localPort')
		self.selectRule(**kwargs)
		if newAction:
			self.action(newAction)
		if newProtocol:
			self.protocol(newProtocol)
		if newRemoteIp:
			self.remoteIp(newRemoteIp)
		if newRemoteWildcardMask:
			self.remoteWildcardMask(newRemoteWildcardMask)
		if newRemotePort:
			self.remotePort(newRemotePort)
		if newLocalPort:
			self.localPort(newLocalPort)
		self.saveButton()
	
	def close(self):
		Util().clickButton(self.objName(DesktopConst.firewall.CLOSE_BUTT))
