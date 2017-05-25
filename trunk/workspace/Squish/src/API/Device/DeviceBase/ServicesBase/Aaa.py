##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *

class ClientTableItem:
	def __init__(self, name, ip, type, key, objectName):
		self.name = name
		self.ip = ip
		self.type = type
		self.key = key
		self.clientNameSquishObjectName = objectName

class AaaNetworkConfigurationCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def clientName(self, clientName):
		Util().textCheckPoint(self.objName(ServicesConst.aaa.HOST_EDIT), clientName)
	
	def clientIp(self, clientIp):
		Util().textCheckPoint(self.objName(ServicesConst.aaa.HOST_IP_EDIT), clientIp)
	
	def secret(self, secret):
		Util().textCheckPoint(self.objName(ServicesConst.aaa.SHARED_SECRET), secret)
	
	def serverType(self, serverType):
		Util().textCheckPoint(self.objName(ServicesConst.aaa.TYPE_VALUE), serverType, textProperty='currentText')
	
	def addButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.aaa.ADD_CLIENT_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
		
	def saveButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.aaa.SAVE_CLIENT_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
		
	def removeButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.aaa.REMOVE_CLIENT_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
		
	@property
	def clientTableName(self):
		return self.objName(ServicesConst.aaa.CLIENT_TABLE)
	
	@property
	def clientTable(self):
		return findObject(self.clientTableName)

class AaaNetworkConfiguration(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = AaaNetworkConfigurationCheck(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def clientName(self, clientName):
		Util().setText(self.objName(ServicesConst.aaa.HOST_EDIT), clientName)
	
	def clientIp(self, clientIp):
		Util().setText(self.objName(ServicesConst.aaa.HOST_IP_EDIT), clientIp)
	
	def secret(self, secret):
		Util().setText(self.objName(ServicesConst.aaa.SHARED_SECRET), secret)
	
	def serverType(self, serverType):
		Util().clickItem(self.objName(ServicesConst.aaa.TYPE_VALUE), serverType)
	
	def addButton(self):
		Util().clickButton(self.objName(ServicesConst.aaa.ADD_CLIENT_BUTT))
	
	def saveButton(self):
		Util().clickButton(self.objName(ServicesConst.aaa.SAVE_CLIENT_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(ServicesConst.aaa.REMOVE_CLIENT_BUTT))
	
	@property
	def clientTableName(self):
		return self.objName(ServicesConst.aaa.CLIENT_TABLE)
	
	@property
	def clientTable(self):
		return findObject(self.clientTableName)
	
	def getClientRow(self, name, ip = None, type = None, key = None):
		for i in range(self.clientTable.rowCount):
			matched = True
			rowName = findObject(self.clientTableName + '.item_' + str(i) + '/0')
			rowIp = findObject(self.clientTableName + '.item_' + str(i) + '/1')
			rowType = findObject(self.clientTableName + '.item_' + str(i) + '/2')
			rowKey = findObject(self.clientTableName + '.item_' + str(i) + '/3')
			if name:
				if not name == rowName.text:
					matched = False
			if ip:
				if not ip == rowIp.text:
					matched = False
			if type:
				if not type == rowType.text:
					matched = False
			if key:
				if not key == rowKey.text:
					matched = False
			if matched:
				return ClientTableItem(rowName, rowIp, rowType, rowKey, self.clientTableName + '.item_%s/0'%(i,))
		
	def rowObjectAt(self, row):
		rowName = findObject(self.clientTableName + '.item_%s/0'%(row,))
		rowIp = findObject(self.clientTableName + '.item_%s/1'%(row,))
		rowType = findObject(self.clientTableName + '.item_%s/2'%(row,))
		rowKey = findObject(self.clientTableName + '.item_%s/3'%(row,))
		return ClientTableItem(rowName, rowIp, rowType, rowKey, self.clientTableName + '.item_%s/0'%(row,))
		
	def selectClient(self, name, ip = None, type = None, key = None):
		client = self.getClientRow(name, ip, type, key)
		Util().click(client.name)
	
	def selectRow(self, row):
		Util().click(self.clientTableName + '.item_%s/0'%(row,))
	
	def addClient(self, clientName, clientIp, secret, serverType = None):
		self.clientName(clientName)
		self.clientIp(clientIp)
		self.secret(secret)
		if serverType:
			self.serverType(serverType)
		self.addButton()
	
	def editClient(self, clientName, newClientName = None, clientIp = None, secret = None, serverType = None):
		self.selectClient(clientName)
		if newClientName:
			self.clientName(newClientName)
		if clientIp:
			self.clientIp(clientIp)
		if secret:
			self.secret(secret)
		if serverType:
			self.serverType(serverType)
		self.saveButton()
	
	def removeClient(self, clientName, clientIp, serverType):
		self.selectClient(clientName)
		self.removeButton()

class UserTableItem:
	def __init__(self, username, password, objectName):
		self.username = username
		self.password = password
		self.usernameSquishObjectName = objectName

class AaaUserSetupCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def username(self, username):
		Util().textCheckPoint(self.objName(ServicesConst.aaa.USERNAME_EDIT), username)
	
	def password(self, password):
		Util().textCheckPoint(self.objName(ServicesConst.aaa.PASSWORD_EDIT), password)
	
	def addButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.aaa.USER_ADD_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
		
	def saveButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.aaa.USER_SAVE_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
		
	def removeButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.aaa.USER_REMOVE_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
	
	@property
	def userTableName(self):
		return self.objName(ServicesConst.aaa.USER_TABLE)
	
	@property
	def userTable(self):
		return findObject(self.userTableName)
	
class AaaUserSetup(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = AaaUserSetupCheck(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def username(self, username):
		Util().setText(self.objName(ServicesConst.aaa.USERNAME_EDIT), username)
	
	def password(self, password):
		Util().setText(self.objName(ServicesConst.aaa.PASSWORD_EDIT), password)
	
	def addButton(self):
		Util().clickButton(self.objName(ServicesConst.aaa.USER_ADD_BUTT))
	
	def saveButton(self):
		Util().clickButton(self.objName(ServicesConst.aaa.USER_SAVE_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(ServicesConst.aaa.USER_REMOVE_BUTT))
	
	@property
	def userTableName(self):
		return self.objName(ServicesConst.aaa.USER_TABLE)
	
	@property
	def userTable(self):
		return findObject(self.userTableName)
	
	def getUserRow(self, username, password = None):
		for i in range(self.userTable.rowCount):
			matched = True
			rowUsername = findObject(self.userTableName + '.item_' + str(i) + '/0')
			rowPassword = findObject(self.userTableName + '.item_' + str(i) + '/1')
			if username:
				if not username == rowUsername.text:
					matched = False
			if password:
				if not password == rowPassword.text:
					matched = False
			if matched:
				return UserTableItem(rowUsername, rowPassword, self.userTableName + str(i) + '/0')
			
	def selectUser(self, username, password = None):
		user = self.getUserRow(username, password)
		Util().click(user.username)
	
	def selectRow(self, row):
		Util().click(self.userTableName + '.item_%s/0'%(row,))
		
	def rowObjectAt(self, row):
		rowUsername = findObject(self.userTableName + '.item_%s/0'%(row,))
		rowPassword = findObject(self.userTableName + '.item_%s/1'%(row,))
		return UserTableItem(rowUsername, rowPassword, self.userTableName + '.item_%s/0'%(row,))
	
	def addUser(self, username, password):
		self.username(username)
		self.password(password)
		self.addButton()
	
	def editUser(self, username, newUsername = None, password = None):
		self.selectUser(username)
		if newUsername:
			self.username(newUsername)
		if password:
			self.password(password)
		self.saveButton()
	
	def removeUser(self, username):
		self.selectUser(username)
		self.removeButton()
		
class AaaCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	def on(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.aaa.ON), checked)
	
	def off(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.aaa.OFF), checked)
	
	def radiusPort(self, port):
		Util().textCheckPoint(self.objName(ServicesConst.aaa.RADIUS_PORT_EDIT), port)
		

class Aaa(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = AaaCheck(self)
		self.networkConfiguration = AaaNetworkConfiguration(self)
		self.userSetup = AaaUserSetup(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		self.networkConfiguration.updateName(squishName)
		self.userSetup.updateName(squishName)
		
	def on(self):
		Util().clickButton(self.objName(ServicesConst.aaa.ON))
	
	def off(self):
		Util().clickButton(self.objName(ServicesConst.aaa.OFF))
	
	def radiusPort(self, port):
		Util().setText(self.objName(ServicesConst.aaa.RADIUS_PORT_EDIT), port)
		