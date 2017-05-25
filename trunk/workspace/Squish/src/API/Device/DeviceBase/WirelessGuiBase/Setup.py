##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.WirelessGuiBase.WirelessGuiBaseConst import WirelessGuiConst
from API.Device.DeviceBase.WirelessGuiBase.ConstantsHelper import ConstantsHelper
from squish import *
import object

class InternetConnectionTypeDhcp:
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

class InternetConnectionTypeStaticCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def ip_octave_1(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_1), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_1), ip, **kwargs)
			
	def ip_octave_2(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_2), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_2), ip, **kwargs)
			
	
	def ip_octave_3(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_3), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_3), ip, **kwargs)
			
	def ip_octave_4(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_4), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_4), ip, **kwargs)
			
	
	def ip(self, ip, **kwargs):
		ipList = ip.split('.')
		self.ip_octave_1(ipList[0], **kwargs)
		self.ip_octave_2(ipList[1], **kwargs)
		self.ip_octave_3(ipList[2], **kwargs)
		self.ip_octave_4(ipList[3], **kwargs)
	
	def mask_octave_1(self, mask, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_1), mask)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_1), mask)
			
	
	def mask_octave_2(self, mask, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_2), mask)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_2), mask)
			
	def mask_octave_3(self, mask, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_3), mask)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_3), mask)
	
	def mask_octave_4(self, mask, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_4), mask)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_4), mask)

	def subnet(self, subnet, **kwargs):
		subnetList = subnet.split('.')
		self.mask_octave_1(subnetList[0], **kwargs)
		self.mask_octave_2(subnetList[1], **kwargs)
		self.mask_octave_3(subnetList[2], **kwargs)
		self.mask_octave_4(subnetList[3], **kwargs)
	
	def gateway_octave_1(self, gateway, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_1), gateway, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_1), gateway, **kwargs)
	
	def gateway_octave_2(self, gateway, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_2), gateway, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_2), gateway, **kwargs)
	
	def gateway_octave_3(self, gateway, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_3), gateway, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_3), gateway, **kwargs)
	
	def gateway_octave_4(self, gateway, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_4), gateway, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_4), gateway, **kwargs)
			
		
	def gateway(self, gateway, **kwargs):
		gatewayList = gateway.split('.')
		self.gateway_octave_1(gatewayList[0], **kwargs)
		self.gateway_octave_2(gatewayList[1], **kwargs)
		self.gateway_octave_3(gatewayList[2], **kwargs)
		self.gateway_octave_4(gatewayList[3], **kwargs)
		
	def dns1_octave_1(self, dns, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_1), dns, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_1), dns, **kwargs)
	
	def dns1_octave_2(self, dns, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_2), dns, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_2), dns, **kwargs)
	
	def dns1_octave_3(self, dns, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_3), dns, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_3), dns, **kwargs)

	def dns1_octave_4(self, dns, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_4), dns, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_4), dns, **kwargs)
			
	def dns1(self, dns1, **kwargs):
		dnsList = dns1.split('.')
		self.dns1_octave_1(dnsList[0], **kwargs)
		self.dns1_octave_2(dnsList[1], **kwargs)
		self.dns1_octave_3(dnsList[2], **kwargs)
		self.dns1_octave_4(dnsList[3], **kwargs)
		
		
class InternetConnectionTypeStatic(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = InternetConnectionTypeStaticCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def ip_ocatve_1(self, ip):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_1), ip)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_1), ip)
	
	def ip_ocatve_2(self, ip):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_2), ip)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_2), ip)
	
	def ip_ocatve_3(self, ip):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_3), ip)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_3), ip)
	
	def ip_ocatve_4(self, ip):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_IP_4), ip)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_IP_4), ip)
	
	def ip(self, ip):
		ipList = ip.split('.')
		self.ip_ocatve_1(ipList[0])
		self.ip_ocatve_2(ipList[1])
		self.ip_ocatve_3(ipList[2])
		self.ip_ocatve_4(ipList[3])
		
	def mask_octave_1(self, mask):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_1), mask)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_1), mask)
	
	def mask_octave_2(self, mask):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_2), mask)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_2), mask)
	
	def mask_octave_3(self, mask):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_3), mask)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_3), mask)
	
	def mask_octave_4(self, mask):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_MASK_4), mask)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_MASK_4), mask)
	
	def subnet(self, subnet):
		subnetList = subnet.split('.')
		self.mask_octave_1(subnetList[0])
		self.mask_octave_2(subnetList[1])
		self.mask_octave_3(subnetList[2])
		self.mask_octave_4(subnetList[3])
		
	def gateway_octave_1(self, gateway):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_1), gateway)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_1), gateway)
	
	def gateway_octave_2(self, gateway):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_2), gateway)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_2), gateway)

	def gateway_octave_3(self, gateway):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_3), gateway)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_3), gateway)

	def gateway_octave_4(self, gateway):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_GATEWAY_4), gateway)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_GATEWAY_4), gateway)

	def gateway(self, gateway):
		gatewayList = gateway.split('.')
		self.gateway_octave_1(gatewayList[0])
		self.gateway_octave_2(gatewayList[1])
		self.gateway_octave_3(gatewayList[2])
		self.gateway_octave_4(gatewayList[3])
	
	def dns1_octave_1(self, dns):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_1), dns)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_1), dns)
	
	def dns1_octave_2(self, dns):	
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_2), dns)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_2), dns)
	
	def dns1_octave_3(self, dns):	
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_3), dns)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_3), dns)

	def dns1_octave_4(self, dns):	
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.EDIT_STATIC_DNS1_4), dns)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_EDIT_STATIC_DNS1_4), dns)
	
	def dns1(self, dns1):
		dnsList = dns1.split('.')
		self.dns1_octave_1(dnsList[0])
		self.dns1_octave_2(dnsList[1])
		self.dns1_octave_3(dnsList[2])
		self.dns1_octave_4(dnsList[3])
		
	def dns2(self, dns2):
		err()
	
	def dns3(self, dns3):
		err()
	
	def hostname(self, hostname):
		err()
	
class InternetConnectionTypePppoe(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = InternetConnectionTypePppoeCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def username(self, username):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.USERNAME), username)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_USERNAME), username)
	
	def password(self, password):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PASSWORD), password)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_PASSWORD), password)
	
	def serviceName(self, serviceName):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.SERVICE_NAME), serviceName)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.internet.PC_SERVICE_NAME), serviceName)
		
class InternetConnectionTypePppoeCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	def username(self, username, **kwargs):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.USERNAME), username, **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_USERNAME), username, **kwargs)
	
	def password(self, password, **kwargs):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PASSWORD), password, **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_PASSWORD), password, **kwargs)
	
	def serviceName(self, serviceName, **kwargs):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.SERVICE_NAME), serviceName, **kwargs)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.internet.PC_SERVICE_NAME), serviceName, **kwargs)

class InternetSetupCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	def connectionType(self, connectionType, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.CONNECTION_TYPE_DROPDOWN), **kwargs)
			else:
				Util().clickItem(self.objName(WirelessGuiConst.setup.internet.CONNECTION_TYPE_COMBO), connectionType)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.setup.internet.PC_CONNECTION_TYPE_DROPDOWN), **kwargs)
			else:
				Util().clickItem(self.objName(WirelessGuiConst.setup.internet.PC_CONNECTION_TYPE_COMBO), connectionType)
			
class InternetSetup(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.dhcp = InternetConnectionTypeDhcp(self)
		self.static = InternetConnectionTypeStatic(self)
		self.pppoe = InternetConnectionTypePppoe(self)
		self.check = InternetSetupCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.dhcp.updateName(squishName)
		self.static.updateName(squishName)
		self.pppoe.updateName(squishName)
		self.check.updateName(squishName)
	
	def connectionType(self, connectionType):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.setup.internet.CONNECTION_TYPE_COMBO), connectionType)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.setup.internet.PC_CONNECTION_TYPE_COMBO), connectionType)

class RouterIpCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def ip_edit_1(self, ip):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_IP_1), ip)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_1), ip)
	
	def ip_edit_2(self, ip):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_IP_2), ip)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_2), ip)
	
	def ip_edit_3(self, ip):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_IP_3), ip)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_3), ip)
	
	def ip_edit_4(self, ip):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_IP_4), ip)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_4), ip)
	
	def ip(self, ip):
		ipList = ip.split('.')
		self.ip_edit_1(ipList[0])
		self.ip_edit_2(ipList[1])
		self.ip_edit_3(ipList[2])
		self.ip_edit_4(ipList[3])
	
	def subnet(self, subnet):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.MASK_COMBO), subnet, textProperty='currentText')
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_MASK_COMBO), subnet, textProperty='currentText')

class RouterIp(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = RouterIpCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def ip(self, ip):
		ipList = ip.split('.')
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_IP_1), ipList[0])
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_IP_2), ipList[1])
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_IP_3), ipList[2])
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_IP_4), ipList[3])
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_1), ipList[0])
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_2), ipList[1])
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_3), ipList[2])
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_4), ipList[3])
		
	def ip1(self, ip):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_IP_1), ip)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_1), ip)
		
	def ip2(self, ip):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_IP_2), ip)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_2), ip)

	def ip3(self, ip):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_IP_3), ip)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_3), ip)
		
	def ip4(self, ip):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_IP_4), ip)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_IP_4), ip)
		
	def subnet(self, subnet):
		if self.isRouter:
			dropdown = findObject(self.objName(WirelessGuiConst.setup.network.MASK_COMBO))
			for i in range(dropdown.count):
				currentItem = findObject(self.objName(WirelessGuiConst.setup.network.MASK_COMBO + '.item_' + str(i) + '/0'))
				if currentItem.text == subnet:
					dropdown.setCurrentIndex(i)
					return
			raise ValueError('Unable to find subnet: ' + subnet)
		else:
			dropdown = findObject(self.objName(WirelessGuiConst.setup.network.PC_MASK_COMBO))
			for i in range(dropdown.count):
				currentItem = findObject(self.objName(WirelessGuiConst.setup.network.PC_MASK_COMBO + '.item_' + str(i) + '/0'))
				if currentItem.text == subnet:
					dropdown.setCurrentIndex(i)
					return
			raise ValueError('Unable to find subnet: ' + subnet)
		
class DhcpReservationCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	@property
	def clientsAlreadyReservedTableName(self):
		if self.isRouter:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.CLIENTS_ALREADY_RESERVED_TABLE)
		else:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_CLIENTS_ALREADY_RESERVED_TABLE)
	
	@property
	def clientsAlreadyReservedTable(self):
		return findObject(self.clientsAlreadyReservedTableName)
	
	def clientsAlreadyReservedNameAtRow(self, row, name):
		Util().textCheckPoint(self.objName(self.clientsAlreadyReservedTableName + '.item_%s/0'%(row,)), name)
	
	def clientsAlreadyReservedIpAtRow(self, row, ip):
		Util().textCheckPoint(self.objName(self.clientsAlreadyReservedTableName + '.item_%s/1'%(row,)), ip)
	
	def clientsAlreadyReservedMacAtRow(self, row, mac):
		Util().textCheckPoint(self.objName(self.clientsAlreadyReservedTableName + '.item_%s/2'%(row,)), mac)
	
	@property
	def dhcpClientTableName(self):
		if self.isRouter:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.CLIENT_TABLE)
		else:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_CLIENT_TABLE)
	
	def dhcpClientNameAtRow(self, row, name):
		Util().textCheckPoint(self.dhcpClientTableName + '.item_%s/0'%(row,), name)
	
	def dhcpClientInterfaceAtRow(self, row, interface):
		Util().textCheckPoint(self.dhcpClientTableName + '.item_%s/1'%(row,), interface)
	
	def dhcpClientIpAtRow(self, row, ip):
		Util().textCheckPoint(self.dhcpClientTableName + '.item_%s/2'%(row,), ip)
	
	def dhcpClientMacAtRow(self, row, mac):
		Util().textCheckPoint(self.dhcpClientTableName + '.item_%s/3'%(row,), mac)
	
	def dhcpClientIsSelectedAtRow(self, row, checked=True):
		Util().checkProperty(self.dhcpClientTableName + '.item_%s/4'%(row,), property='selected', value=checked)
	
class DhcpReservation(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = DhcpReservationCheck(self)
	def updateName(self, squishName):
		self.squishName = squishName
	
	@property
	def dhcpClientTableName(self):
		if self.isRouter:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.CLIENT_TABLE)
		else:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_CLIENT_TABLE)
	
	def selectDhcpClientAtRow(self, row):
		Util().click(self.dhcpClientTableName + '.item_%s/4'%(row,))
	
	def addClientButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.ADD_CLIENT_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_ADD_CLIENT_BUTTON))

	@property
	def manuallyAddingClientTableName(self):
		if self.isRouter:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.MANUALLY_ADDING_CLIENT_TABLE)
		else:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_MANUALLY_ADDING_CLIENT_TABLE) 
	
	def clientName(self, name):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.dhcpReservation.MANUALLY_ADDING_CLIENT_CELL_1), name)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_MANUALLY_ADDING_CLIENT_CELL_1), name)
	
	def clientIp(self, ip):
		ip = ip.split('.')[-1]#Get the last octet if full ip provided
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.dhcpReservation.MANUALLY_ADDING_CLIENT_IP_4), ip)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_MANUALLY_ADDING_CLIENT_IP_4), ip)
	
	def clientMac(self, mac):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.dhcpReservation.MANUALLY_ADDING_CLIENT_MAC), mac)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_MANUALLY_ADDING_CLIENT_MAC), mac)
	
	def addButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.MANUALLY_ADDING_CLIENT_ADD_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_MANUALLY_ADDING_CLIENT_ADD_BUTTON))
	
	@property
	def clientsAlreadyReservedTableName(self):
		if self.isRouter:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.CLIENTS_ALREADY_RESERVED_TABLE)
		else:
			return self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_CLIENTS_ALREADY_RESERVED_TABLE)
	
	@property
	def clientsAlreadyReservedTable(self):
		return findObject(self.clientsAlreadyReservedTableName)
	
	def clientsAlreadyReservedRemoveAtRow(self, row):
		obj = ':CBaseDhcpReservation.m_middlePanel.tableReserved.qt_scrollarea_viewport.CDhcpClientTableCellWidget%s.btnDelete'%(row+1)
		Util().click(obj)
		
	def saveSettingsButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.SAVE_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_SAVE_SETTINGS_BUTTON))
	
	def cancelChangesButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.CANCEL_CHANGES_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_CANCEL_CHANGES_BUTTON))
	
	def closeButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.CLOSE_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_CLOSE_BUTTON))
	
	def refreshButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.REFRESH_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.dhcpReservation.PC_REFRESH_BUTTON))
		
class DhcpServerSettingsCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def enabled(self, checked=True):
		if self.isRouter:
			Util().isChecked(self.objName(WirelessGuiConst.setup.network.DHCP_RADIO_ENABLE), checked)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.setup.network.PC_DHCP_RADIO_ENABLE), checked)
	
	def disabled(self, checked=True):
		if self.isRouter:
			Util().isChecked(self.objName(WirelessGuiConst.setup.network.DHCP_RADIO_DISABLE), checked)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.setup.network.PC_DHCP_RADIO_DISABLE), checked)
	
	def startIp(self, startIp):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_START_IP), startIp)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_START_IP), startIp)
	
	def maxUsers(self, maxUser):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_MAX_USER), maxUser)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_MAX_USER), maxUser)
	
	def dns1_1(self, dns):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_1), dns)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_1), dns)
	
	def dns1_2(self, dns):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_2), dns)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_2), dns)
	
	def dns1_3(self, dns):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_3), dns)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_3), dns)
	
	def dns1_4(self, dns):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_4), dns)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_4), dns)
	
	def staticDns1(self, dns):
		dnsList = dns.split('.')
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_1), dnsList[0])
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_2), dnsList[1])
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_3), dnsList[2])
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_4), dnsList[3])
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_1), dnsList[0])
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_2), dnsList[1])
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_3), dnsList[2])
			Util().textCheckPoint(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_4), dnsList[3])

class DhcpServerSettings(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.dhcpReservation = DhcpReservation(self)
		self.check = DhcpServerSettingsCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.dhcpReservation.updateName(squishName)
		self.check.updateName(squishName)
	
	def enabled(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.DHCP_RADIO_ENABLE))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.PC_DHCP_RADIO_ENABLE))
	
	def disabled(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.DHCP_RADIO_DISABLE))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.PC_DHCP_RADIO_DISABLE))
	
	def startIp(self, startIp):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_START_IP), startIp)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_START_IP), startIp)
	
	def maxUsers(self, maxUser):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_MAX_USER), maxUser)
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_MAX_USER), maxUser)
		
	def staticDns1(self, dns):
		dnsList = dns.split('.')
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_1), dnsList[0])
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_2), dnsList[1])
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_3), dnsList[2])
			Util().setText(self.objName(WirelessGuiConst.setup.network.EDIT_STATIC_DNS1_4), dnsList[3])
		else:
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_1), dnsList[0])
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_2), dnsList[1])
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_3), dnsList[2])
			Util().setText(self.objName(WirelessGuiConst.setup.network.PC_EDIT_STATIC_DNS1_4), dnsList[3])
		
	def dhcpReservationButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.DHCP_RESERVATION_BUTT))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.setup.network.PC_DHCP_RESERVATION_BUTT))
			
class NetworkSetup(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.routerIp = RouterIp(self)
		self.dhcpServerSettings = DhcpServerSettings(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.routerIp.updateName(squishName)
		self.dhcpServerSettings.updateName(squishName)

class BasicSetup(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.internetSetup = InternetSetup(self)
		self.networkSetup = NetworkSetup(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.internetSetup.updateName(squishName)
		self.networkSetup.updateName(squishName)
	
	def saveSettingsButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.setup.SAVE_SETTINGS_BUTTON))
	
	def cancelChangesButton(self):
		Util().clickButton(self.objName(WirelessGuiConst.setup.CANCEL_SETTINGS_BUTTON))

class Setup:
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.basicSetup = BasicSetup(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.basicSetup.updateName(squishName)