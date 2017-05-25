##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.ServicesBase.ServicesBase import Dhcpv6
from API.Device.DeviceBase.ServicesBase.ServicesBase import Services as ServicesBase
from API.Device.COServer.COServerConst import COServerConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from squish import *

def err(msg = ''):
	raise NotImplementedError(msg)

class DhcpCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def ip(self, ip):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.DHCP_IP), ip)
	
	def subnet(self, subnet):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.DHCP_SUBNET_MASK), subnet)
	
	def startIp1(self, octet1):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.DHCP_EDIT_START_IP_1), octet1)
	
	def startIp2(self, octet2):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.DHCP_EDIT_START_IP_2), octet2)
	
	def startIp3(self, octet3):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.DHCP_EDIT_START_IP_3), octet3)
	
	def startIp4(self, octet4):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.DHCP_EDIT_START_IP_4), octet4)
	
	def maxUsers(self, max):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.DHCP_EDIT_MAX_USER), max)
	
	def dnsServer(self, dnsServer):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.DHCP_DNS), dnsServer)
	
	def ipAddressRange1(self, octet1):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.IP_ADDRESS_RANGE_1), octet1)
	
	def ipAddressRange2(self, octet2):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.IP_ADDRESS_RANGE_2), octet2)
	
	def ipAddressRange3(self, octet3):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.IP_ADDRESS_RANGE_3), octet3)
	
	def ipAddressRange4(self, octet4):
		Util().textCheckPoint(self.objName(COServerConst.services.dhcp.IP_ADDRESS_RANGE_4), octet4)
	
	def saveButton(self):
		err()
	
	
	def cancelButton(self):
		err()
	

class Dhcp(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = DhcpCheck(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def startIp(self, lastOctet):
		Util().setText(self.objName(COServerConst.services.dhcp.DHCP_EDIT_START_IP_4), lastOctet)
	
	def maxUsers(self, max):
		Util().setText(self.objName(COServerConst.services.dhcp.DHCP_EDIT_MAX_USER), max)
	
	def dnsServer(self, dnsServer):
		Util().setText(self.objName(COServerConst.services.dhcp.DHCP_DNS))
	
	def saveButton(self):
		Util().clickButton(self.objName(COServerConst.services.dhcp.DHCP_ADD_SAVE_BUTT))
	
	def cancelButton(self):
		Util().clickButton(self.objName(COServerConst.services.dhcp.DHCP_CANCEL_BUTT))

class CellCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def item(self, item, value):
		''' item = "0/0"'''
		Util().textCheckPoint(self.objName(COServerConst.services.cellTower.DEVICE_LIST + ".item_" + item), value)
	
class CellTower(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = CellCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def refreshButton(self):
		Util().clickButton(self.objName(COServerConst.services.cellTower.REFRESH_BUTT))
	
	def clickItem(self, item):
		Util().clickItem(self.objName(COServerConst.services.cellTower.LIST), item)
	
class PapChapCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def interface(self, interface, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(COServerConst.services.papChap.INTERFACE), **kwargs)
		else:
			Util().textCheckPoint(self.objName(COServerConst.services.papChap.INTERFACE), interface, textProperty='currentText')
		
	def username(self, username, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(COServerConst.services.papChap.USER_NAME), **kwargs)
		else:
			Util().textCheckPoint(self.objName(COServerConst.services.papChap.USER_NAME), username)
	
	def password(self, password, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(COServerConst.services.papChap.PASSWORD), **kwargs)
		else:
			Util().textCheckPoint(self.objName(COServerConst.services.papChap.PASSWORD), password)

class PapChap(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = PapChapCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def interface(self, interface):
		Util().clickItem(self.objName(COServerConst.services.papChap.INTERFACE), interface)
	
	def pap(self):
		Util().clickButton(self.objName(COServerConst.services.papChap.PAP))
	
	def chap(self):
		Util().clickButton(self.objName(COServerConst.services.papChap.CHAP))
	
	def username(self, username):
		Util().setText(self.objName(COServerConst.services.papChap.USER_NAME), username)
	
	def password(self, password):
		Util().setText(self.objName(COServerConst.services.papChap.PASSWORD), password)
	
	def addButton(self):
		Util().clickButton(self.objName(COServerConst.services.papChap.ADD_BUTT))
	
	def saveButton(self):
		Util().clickButton(self.objName(COServerConst.services.papChap.SAVE_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(COServerConst.services.papChap.REMOVE_BUTT))
	
	def add(self, username, password, papOrChap = 'pap', interface = 'Backbone'):
		self.interface(interface)
		self.username(username)
		self.password(password)
		if papOrChap.lower() == 'pap':
			self.pap()
		elif papOrChap.lower() == 'chap':
			self.chap()
		else:
			raise ValueError('Should pass either pap or chap for papOrChap')
		self.addButton()
	
	@property
	def userTable(self):
		return findObject(self.objName(COServerConst.services.papChap.LIST))

	def selectUser(self, username):
		for i in range(self.userTable.rowCount):
			table = self.objName(COServerConst.services.papChap.LIST)
			usernameField = findObject(table + '.item_' + str(i) + '/0')
			passwordField = findObject(table + '.item_' + str(i) + '/1')
			if usernameField.text == username:
				Util().click(usernameField)
				return
		raise ValueError('Could not find username: ' + username)
	
	def remove(self, username):
		self.selectUser(username)
		self.removeButton()

class Services(ServicesBase):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.dhcp = Dhcp(self)
		self.dhcpv6 = Dhcpv6(self)
		self.cellTower = CellTower(self)
		self.papChap = PapChap(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.dhcp.updateName(squishName)
		self.dhcpv6.updateName(squishName)
		self.cellTower.updateName(squishName)
		self.papChap.updateName(squishName)