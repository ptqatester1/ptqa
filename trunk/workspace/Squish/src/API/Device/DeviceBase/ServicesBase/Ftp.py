##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *
import object

class FtpCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def on(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.ftp.ON), checked)
	
	def off(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.ftp.OFF), checked)
	
	def writeCheckbox(self, checked):
		Util().isChecked(self.objName(ServicesConst.ftp.WRITE_CHKBOX), checked)
	
	def readCheckbox(self, checked):
		Util().isChecked(self.objName(ServicesConst.ftp.READ_CHKBOX), checked)
	
	def deleteCheckbox(self, checked):
		Util().isChecked(self.objName(ServicesConst.ftp.DELETE_CHKBOX), checked)
	
	def renameCheckbox(self, checked):
		Util().isChecked(self.objName(ServicesConst.ftp.RENAME_CHKBOX), checked)
	
	def listCheckbox(self, checked):
		Util().isChecked(self.objName(ServicesConst.ftp.LIST_CHKBOX), checked)
	
	def username(self, username):
		Util().textCheckPoint(self.objName(ServicesConst.ftp.USERNAME_EDIT), username)
	
	def password(self, password):
		Util().textCheckPoint(self.objName(ServicesConst.ftp.PASSWORD_EDIT), password)

	def addButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.ftp.USER_ADD_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
	
	def saveButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.ftp.USER_SAVE_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
	
	def removeUserButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.ftp.USER_REMOVE_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')

class Ftp(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = FtpCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def on(self):
		Util().clickButton(self.objName(ServicesConst.ftp.ON))
	
	def off(self):
		Util().clickButton(self.objName(ServicesConst.ftp.OFF))
	
	def username(self, username):
		Util().setText(self.objName(ServicesConst.ftp.USERNAME_EDIT), username)
	
	def password(self, password):
		Util().setText(self.objName(ServicesConst.ftp.PASSWORD_EDIT), password)
	
	def checkbox(self, checkbox, checked = None):
		if checked == None:
			Util().click(checkbox)
		elif checked == True:
			if not checkbox.checked:
				Util().click(checkbox)
		elif checked == False:
			if checkbox.checked:
				Util().click(checkbox)
		else:
			raise ValueError('Must be None, True, or False')
	def writeCheckbox(self, checked = None):
		self.checkbox(findObject(self.objName(ServicesConst.ftp.WRITE_CHKBOX)), checked)
	
	def readCheckbox(self, checked = None):
		self.checkbox(findObject(self.objName(ServicesConst.ftp.READ_CHKBOX)), checked)
	
	def deleteCheckbox(self, checked = None):
		self.checkbox(findObject(self.objName(ServicesConst.ftp.DELETE_CHKBOX)), checked)
	
	def renameCheckbox(self, checked = None):
		self.checkbox(findObject(self.objName(ServicesConst.ftp.RENAME_CHKBOX)), checked)
	
	def listCheckbox(self, checked = None):
		self.checkbox(findObject(self.objName(ServicesConst.ftp.LIST_CHKBOX)), checked)
	
	def addButton(self):
		Util().clickButton(self.objName(ServicesConst.ftp.USER_ADD_BUTT))
	
	def saveButton(self):
		Util().clickButton(self.objName(ServicesConst.ftp.USER_SAVE_BUTT))
	
	def removeUserButton(self):
		Util().clickButton(self.objName(ServicesConst.ftp.USER_REMOVE_BUTT))
	
	@property
	def userTableName(self):
		return self.objName(ServicesConst.ftp.USER_LIST)
	
	@property
	def userTable(self):
		return findObject(self.userTableName)
	
	@property
	def fileTableName(self):
		return self.objName(ServicesConst.ftp.FILE_LIST)
	
	@property
	def fileTable(self):
		return findObject(self.fileTableName)
	
	def removeFileButton(self):
		Util().clickButton(self.objName(ServicesConst.ftp.FILE_REMOVE_BUTT))
	
	def selectUser(self, username):
		Util().clickItem(self.userTable, username)

	def selectFile(self, filename):
		for fileItem in object.children(self.fileTable):
			try:
				nametext = fileItem.text
			except AttributeError, e:
				continue
			if nametext == filename:
				Util().click(fileItem)
				return
		raise ValueError('Unable to find file: ' + filename)

	def addUser(self, username, password, **permissions):
		'''Permissions are write, read, delete, rename, list
		example:
			addUser('someUser', 'somePassword', ['read', 'write', 'delete'])'''
		self.username(username)
		self.password(password)
		for permit in permissions:
			if 'write' in permissions:
				self.writeCheckbox(permissions['write'])
			if 'read' in permissions:
				self.readCheckbox(permissions['read'])
			if 'delete' in permissions:
				self.deleteCheckbox(permissions['delete'])
			if 'rename' in permissions:
				self.deleteCheckbox(permissions['rename'])
			if 'list' in permissions:
				self.listCheckbox(permissions['list'])
		self.addButton()
	
	def editUser(self, username, newUsername, password = None, permissions = None):
		self.selectUser(username)
		if newUsername:
			self.username(newUsername)
		if password:
			self.password(password)
		if not permissions == None:
			if 'write' in permissions:
				self.writeCheckbox(True)
			else:
				self.writeCheckbox(False)
			if 'read' in permissions:
				self.readCheckbox(True)
			else:
				self.readCheckbox(False)
			if 'delete' in permissions:
				self.deleteCheckbox(True)
			else:
				self.deleteCheckbox(False)
			if 'rename' in permissions:
				self.deleteCheckbox(True)
			else:
				self.deleteCheckbox(False)
			if 'list' in permissions:
				self.listCheckbox(True)
			else:
				self.listCheckbox(False)
				
	def removeUser(self, username):
		self.selectUser(username)
		self.removeUserButton()
	
	def removeFile(self, filename):
		self.selectFile(filename)
		self.removeFileButton()
		