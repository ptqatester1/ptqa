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
	def vpnIsConnectedDialog(self): 
		try:
			return findObject(self.objName(DesktopConst.vpn.VPN_IS_CONNECTED_DIALOG))
		except LookupError, e:
			return False
	
	@property
	def vpnIsConnectedText(self):
		return str(findObject(self.objName(DesktopConst.vpn.VPN_IS_CONNECTED_TEXT)).text)
	
	def vpnIsConnectedOkButton(self):
		Util().clickButton(self.objName(DesktopConst.vpn.OK_BUTT))
		
	@property
	def connectionTimeOutDialog(self):
		'''This is the same dialog box name as the vpnIsConnectedDialog but with a different text label
		This property should still be called when using connectionTimeOut though in case the dialog box
		changes in the future and also for clarity when reading the test script'''
		return self.vpnIsConnectedDialog
	
	@property
	def connectionTimeOutText(self):
		return self.vpnIsConnectedText
	
	def connectionTimeOutOkButton(self):
		'''Same as connectionTimeOutDialog this should be called when it times out even though the button
		is the same as vpnIsConnectedOkButton'''
		self.vpnIsConnectedOkButton()
	
	
	@property
	def errorMessageDialog(self):
		try:
			return findObject(self.objName(DesktopConst.vpn.ERROR_MESSAGE_DIALOG))
		except LookupError, e:
			return False
	
	def errorMessageOkButton(self):
		Util().clickButton(self.objName(DesktopConst.vpn.ERROR_MESSAGE_OK_BUTTON))

class VpnCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def popupLabel(self, text):
		Util().textCheckPoint(self.objName(DesktopConst.vpn.MSGBOX_LABEL), text)
	
	def groupName(self, groupName):
		Util().textCheckPoint(self.objName(DesktopConst.vpn.GROUP_NAME), groupName)

	def groupKey(self, groupKey):
		Util().textCheckPoint(self.objName(DesktopConst.vpn.GROUP_KEY), groupKey)

	def hostIp(self, hostIp):
		Util().textCheckPoint(self.objName(DesktopConst.vpn.HOST_IP), hostIp)

	def username(self, username):
		Util().textCheckPoint(self.objName(DesktopConst.vpn.USERNAME), username)

	def password(self, password):
		Util().textCheckPoint(self.objName(DesktopConst.vpn.PASSWORD), password)
	
	def clientIpLabel(self, ip):
		Util().textCheckPoint(self.objName(DesktopConst.vpn.CLIENT_IP_LABEL), ip)
	
class Vpn(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.popups = PopupWarnings(self)
		self.check = VpnCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.popups.updateName(squishName)
		self.check.updateName(squishName)
		
	def groupName(self, groupName):
		Util().setText(self.objName(DesktopConst.vpn.GROUP_NAME), groupName)

	def groupKey(self, groupKey):
		Util().setText(self.objName(DesktopConst.vpn.GROUP_KEY), groupKey)

	def hostIp(self, hostIp):
		Util().setText(self.objName(DesktopConst.vpn.HOST_IP), hostIp)

	def username(self, username):
		Util().setText(self.objName(DesktopConst.vpn.USERNAME), username)

	def password(self, password):
		Util().setText(self.objName(DesktopConst.vpn.PASSWORD), password)

	def connectButton(self):
		Util().clickButton(self.objName(DesktopConst.vpn.CONNECT_BUTT))

	def disconnectButton(self):
		Util().clickButton(self.objName(DesktopConst.vpn.DISCONNECT_BUTT))
		
	def errorOkButton(self):
		raise NotImplementedError

	def connectedOkButton(self):
		Util().clickButton(self.objName(DesktopConst.vpn.OK_BUTT))
	
	def close(self):
		Util().clickButton(self.objName(DesktopConst.vpn.CLOSE_BUTT))

	def connectVpn(self, groupName = None, groupKey = None, hostIp = None, username = None, password = None):
		if groupName:
			self.groupName(groupName)
		if groupKey:
			self.groupKey(groupKey)
		if hostIp:
			self.hostIp(hostIp)
		if username:
			self.username(username)
		if password:
			self.password(password)
		self.connectButton()
		#raise NotImplementedError('Need to add error handling')