##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.WirelessGuiBase.WirelessGuiBaseConst import WirelessGuiConst
from API.Device.DeviceBase.WirelessGuiBase.ConstantsHelper import ConstantsHelper

class RouterCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		
	def updateName(self, squishName):
		self.squishName = squishName
		
	def dns1(self, dns):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.DNS1), dns)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_DNS1), dns)

	def dns2(self, dns):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.DNS2), dns)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_DNS2), dns)
		
	def dns3(self, dns):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.DNS3), dns)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_DNS3), dns)

	def firmwareVersion(self, version):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.FIRMWARE_VERSION), version)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_FIRMWARE_VERSION), version)

	
	def currentTime(self, time):
		err()
	
	def internetMacAddress(self, mac):
		err()
	
	def hostName(self, hostname):
		err()
	
	def domainName(self, domainName):
		err()
	
	def connectionType(self, type):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.CONNECTION_TYPE), type)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_CONNECTION_TYPE), type)
	
	def internetIpAddress(self, ip):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.INTERNET_IP_ADDRESS), ip)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_INTERNET_IP_ADDRESS), ip)
	
	def subnetMask(self, subnet):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.SUBNET), subnet)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_SUBNET), subnet)
	
	def defaultGateway(self, gateway):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.GATEWAY), gateway)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_GATEWAY), gateway)
		
	def loginStatus(self, status):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.LOGIN_STATUS), status)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_LOGIN_STATUS), status)
	
	def mtu(self, mtu, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.status.router.MTU_TEXT), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.MTU_TEXT), mtu, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.status.router.PC_MTU_TEXT), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.status.router.PC_MTU_TEXT), mtu, **kwargs)
			
	def dhcpLeaseTime(self, time):
		err()
	

class Router(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = RouterCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def ipAddressReleaseButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.IP_ADDRESS_RELEASE_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.PC_IP_ADDRESS_RELEASE_BUTTON))
	
	def ipAddressRenewButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.IP_ADDRESS_RENEW_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.PC_IP_ADDRESS_RENEW_BUTTON))

	def disconnect(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.DISCONNECT_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.PC_DISCONNECT_BUTTON))
		
	def connect(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.CONNECT_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.PC_CONNECT_BUTTON))
	
	def refreshButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.REFRESH_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.status.router.PC_REFRESH_BUTTON))

class LocalNetwork(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def dhcpClientButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.status.localNetwork.DHCP_CLIENT_TABLE_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.status.localNetwork.PC_DHCP_CLIENT_TABLE_BUTTON))

class WirelessNetwork(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = WirelessNetworkCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)

class WirelessNetworkCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	def radioBand(self, band):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.wirelessNetwork.RADIO_BAND), band)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.wirelessNetwork.PC_RADIO_BAND), band)

	def standardChannel(self, channel):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.wirelessNetwork.RADIO_BAND), channel)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.status.wirelessNetwork.PC_RADIO_BAND), channel)
				
class Status:
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.router = Router(self)
		self.localNetwork = LocalNetwork(self)
		self.wirelessNetwork = WirelessNetwork(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.router.updateName(self.squishName)
		self.localNetwork.updateName(self.squishName)
		self.wirelessNetwork.updateName(self.squishName)