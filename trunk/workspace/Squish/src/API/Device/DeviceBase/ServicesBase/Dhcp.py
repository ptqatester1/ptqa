##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *

class PopupWarnings:
	def __init__(self):
		self.util = Util()
	
	@property
	def informationDialog(self):
		try:
			return findObject(ServicesConst.dhcp.CANNOT_MODIFY_POPUP)
		except LookupError, e:
			return False
		
	def informationOkButton(self):
		self.util.clickButton(ServicesConst.dhcp.CANNOT_MODIFY_POPUP_OK)

class DhcpCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.util = Util()
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	@property
	def dhcpTableName(self):
		return self.objName(ServicesConst.dhcp.LIST_VIEW)
	
	def _textCheckPoint(self, text, row, column, **kwargs):
		cell = findObject(self.dhcpTableName + '.item_%s/%s'%(row, column))
		self.util.textCheckPoint(cell, text, **kwargs)
	
	def tablePoolName(self, name, row):
		self._textCheckPoint(name, row, 0)
	
	def tableGateway(self, gateway, row, **kwargs):
		self._textCheckPoint(gateway, row, 1, **kwargs)
	
	def tableDns(self, dns, row, **kwargs):
		self._textCheckPoint(dns, row, 2, **kwargs)
	
	def tableIp(self, ip, row, **kwargs):
		self._textCheckPoint(ip, row, 3, **kwargs)
	
	def tableSubnet(self, subnet, row, **kwargs):
		self._textCheckPoint(subnet, row, 4, **kwargs)
	
	def tableMax(self, max, row, **kwargs):
		self._textCheckPoint(max, row, 5, **kwargs)
	
	def tableTftp(self, tftp, row, **kwargs):
		self._textCheckPoint(tftp, row, 6, **kwargs)
	
	def interface(self, interfaceName):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.INTERFACE_COMBO), interfaceName, textProperty='currentText')
	
	def on(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.dhcp.ON), checked)
		
	def off(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.dhcp.OFF), checked)
	
	def poolName(self, poolName):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.POOL_NAME_EDIT), poolName)
	
	def gateway(self, gateway):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.GATEWAY), gateway)
	
	def dns(self, dns):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.DNS), dns)
	
	def start_ip_1(self, ip1):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.START_IP_1), ip1)
	
	def start_ip_2(self, ip2):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.START_IP_2), ip2)
		
	def start_ip_3(self, ip3):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.START_IP_3), ip3)
		
	def start_ip_4(self, ip4):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.START_IP_4), ip4)
	
	def start_subnet_1(self, sub1):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.SUBNET_MASK_1), sub1)
	
	def start_subnet_2(self, sub2):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.SUBNET_MASK_2), sub2)
	
	def start_subnet_3(self, sub3):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.SUBNET_MASK_3), sub3)
	
	def start_subnet_4(self, sub4):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.SUBNET_MASK_4), sub4)
	
	def maxUsers(self, maxUsers):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.MAX_USER), maxUsers)
	
	def tftpServer(self, tftpServer):
		Util().textCheckPoint(self.objName(ServicesConst.dhcp.TFTP_SERVER_EDIT), tftpServer)
	
	def addButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.dhcp.ADD_NEW_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')

	def saveButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.dhcp.ADD_SAVE_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
	
	def removeButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.dhcp.ADD_REMOVE_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')

class Dhcp(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = DhcpCheck(self)
		self.popups = PopupWarnings()
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def interface(self, interfaceName):
		Util().clickItem(self.objName(ServicesConst.dhcp.INTERFACE_COMBO), interfaceName)
		
	def on(self):
		Util().clickButton(self.objName(ServicesConst.dhcp.ON))
		
	def off(self):
		Util().clickButton(self.objName(ServicesConst.dhcp.OFF))
	
	def poolName(self, poolName):
		Util().setText(self.objName(ServicesConst.dhcp.POOL_NAME_EDIT), poolName)
	
	def gateway(self, gateway):
		Util().setText(self.objName(ServicesConst.dhcp.GATEWAY), gateway)
	
	def dns(self, dns):
		Util().setText(self.objName(ServicesConst.dhcp.DNS), dns)
	
	def start_ip_1(self, ip1):
		Util().setText(self.objName(ServicesConst.dhcp.START_IP_1), ip1)
	
	def start_ip_2(self, ip2):
		Util().setText(self.objName(ServicesConst.dhcp.START_IP_2), ip2)
		
	def start_ip_3(self, ip3):
		Util().setText(self.objName(ServicesConst.dhcp.START_IP_3), ip3)
		
	def start_ip_4(self, ip4):
		Util().setText(self.objName(ServicesConst.dhcp.START_IP_4), ip4)
	
	def start_subnet_1(self, sub1):
		Util().setText(self.objName(ServicesConst.dhcp.SUBNET_MASK_1), sub1)
	
	def start_subnet_2(self, sub2):
		Util().setText(self.objName(ServicesConst.dhcp.SUBNET_MASK_2), sub2)
	
	def start_subnet_3(self, sub3):
		Util().setText(self.objName(ServicesConst.dhcp.SUBNET_MASK_3), sub3)
	
	def start_subnet_4(self, sub4):
		Util().setText(self.objName(ServicesConst.dhcp.SUBNET_MASK_4), sub4)
	
	def ip(self, ip):
		address = ip.split('.')
		self.start_ip_1(address[0])
		self.start_ip_2(address[1])
		self.start_ip_3(address[2])
		self.start_ip_4(address[3])
	
	def subnet(self, subnet):
		address = subnet.split('.')
		self.start_subnet_1(address[0])
		self.start_subnet_2(address[1])
		self.start_subnet_3(address[2])
		self.start_subnet_4(address[3])
	
	def maxUsers(self, maxUsers):
		Util().setText(self.objName(ServicesConst.dhcp.MAX_USER), maxUsers)
	
	def tftpServer(self, tftpServer):
		Util().setText(self.objName(ServicesConst.dhcp.TFTP_SERVER_EDIT), tftpServer)
	
	def addButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcp.ADD_NEW_BUTT))
	
	def saveButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcp.ADD_SAVE_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcp.ADD_REMOVE_BUTT))
	
	@property
	def dhcpTableName(self):
		return self.objName(ServicesConst.dhcp.LIST_VIEW)
	
	@property
	def dhcpTable(self):
		return findObject(self.dhcpTableName)
	
	def selectRow(self, row):
		Util().clickItem(self.dhcpTable, row +"/0")
		
	def selectPool(self, poolName):
		Util().clickItem(self.dhcpTable, poolName)
	
	def add(self, poolName, gateway, dns, ip, subnet, maxUsers = '512', tftpServer = None, interfaceName = None):
		if interfaceName:
			self.interface(interfaceName)
		if poolName:
			self.poolName(poolName)
		if gateway:
			self.gateway(gateway)
		if dns:
			self.dns(dns)
		if ip:
			self.ip(ip)
		if subnet:
			self.subnet(subnet)
		if maxUsers:
			self.maxUsers(maxUsers)
		if tftpServer:
			self.tftpServer(tftpServer)
		self.addButton()
	
	def edit(self, poolName, newPoolName = None, gateway = None, dns = None, ip = None, subnet = None, maxUsers = None, tftpServer = None):
		self.selectPool(poolName)
		if newPoolName:
			self.poolName(newPoolName)
		if gateway:
			self.gateway(gateway)
		if dns:
			self.dns(dns)
		if ip:
			self.ip(ip)
		if subnet:
			self.subnet(subnet)
		if maxUsers:
			self.maxUsers(maxUsers)
		if tftpServer:
			self.tftpServer(tftpServer)
		self.saveButton()
	
	def remove(self, poolName):
		self.selectPool(poolName)
		self.removeButton()
		