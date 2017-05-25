##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.ConfigBase.ConfigBase import AlgorithmSettings
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst
from API.Device.COServer.COServerConst import COServerConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config as ConfigBase
from squish import *

def err(msg = ''):
	raise NotImplementedError(msg)

class SettingsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def displayName(self, displayName):
		Util().textCheckPoint(self.objName(COServerConst.config.settings.DISPLAY_NAME_EDIT), displayName)
	
	def domainName(self, domainName):
		Util().textCheckPoint(self.objName(COServerConst.config.settings.DOMAIN_NAME_EDIT), domainName)

class Settings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = SettingsCheck(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def displayName(self, displayName):
		Util().setText(self.objName(COServerConst.config.settings.DISPLAY_NAME_EDIT), displayName)
	
	def domainName(self, domainName):
		Util().setText(self.objName(COServerConst.config.settings.DOMAIN_NAME_EDIT), domainName)

class BackboneCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def dhcp(self, checked=True):
		Util().isChecked(self.objName(COServerConst.config.interface.backbone.DHCP_RADIO), checked)
	
	def static(self, checked=True):
		Util().isChecked(self.objName(COServerConst.config.interface.backbone.STATIC_RADIO), checked)
	
	def ip(self, ip):
		Util().textCheckPoint(self.objName(COServerConst.config.interface.backbone.IP_ADDRESS_EDIT), ip)
	
	def subnet(self, subnet):
		Util().textCheckPoint(self.objName(COServerConst.config.interface.backbone.SUBNET_MASK_EDIT), subnet)
	
	def dns(self, dns):
		Util().textCheckPoint(self.objName(COServerConst.config.interface.backbone.DNS_SERVER), dns)
	
	def gateway(self, gateway):
		Util().textCheckPoint(self.objName(COServerConst.config.interface.backbone.GATEWAY_EDIT), gateway)
		

class Backbone(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = BackboneCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def dhcp(self):
		Util().clickButton(self.objName(COServerConst.config.interface.backbone.DHCP_RADIO))
	
	def static(self):
		Util().clickButton(self.objName(COServerConst.config.interface.backbone.STATIC_RADIO))
	
	def ip(self, ip):
		Util().setText(self.objName(COServerConst.config.interface.backbone.IP_ADDRESS_EDIT), ip)
	
	def subnet(self, subnet):
		Util().setText(self.objName(COServerConst.config.interface.backbone.SUBNET_MASK_EDIT), subnet)
	
	def dns(self, dns):
		Util().setText(self.objName(COServerConst.config.interface.backbone.DNS_SERVER), dns)
	
	def gateway(self, gateway):
		Util().setText(self.objName(COServerConst.config.interface.backbone.GATEWAY_EDIT), gateway)
		
	def ipconfig(self, ip, subnet, gateway = None, dns = None):
		self.static()
		self.ip(ip)
		self.subnet(subnet)
		if gateway:
			self.gateway(gateway)
		if dns:
			self.dns(dns)
		

class CellTowerCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def ip(self, ip):
		Util().textCheckPoint(self.objName(COServerConst.config.interface.cellTower.IP_ADDRESS_EDIT), ip)
	
	def subnet(self, subnet):
		Util().textCheckPoint(self.objName(COServerConst.config.interface.cellTower.SUBNET_MASK_EDIT), subnet)
	
	def ipv6(self, ipv6):
		Util().textCheckPoint(self.objName(COServerConst.config.interface.cellTower.IPv6_ADDRESS_EDIT), ipv6)
	
	def subnetv6(self, subnetv6):
		Util().textCheckPoint(self.objName(COServerConst.config.interface.cellTower.IPv6_SUBNET_MASK_EDIT), subnetv6)
	
	def linkLocal(self, linkLocal):
		Util().textCheckPoint(self.objName(COServerConst.config.interface.cellTower.IPv6_LINK_LOCAL_ADDRESS_EDIT), linkLocal)
	
	
class CellTower(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = CellTowerCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
class Interface:
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.backbone = Backbone(self)
		self.cellTower = CellTower(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.backbone.updateName(squishName)
		self.cellTower.updateName(squishName)

class Config(ConfigBase):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.settings = Settings(self)
		self.algorithmSettings = AlgorithmSettings(self)
		self.interface = Interface(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.settings.updateName(squishName)
		self.algorithmSettings.updateName(squishName)
		self.interface.updateName(squishName)
		