##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *

class EmailCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	def smtpOn(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.email.SMTP_ON), checked)
	
	def smtpOff(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.email.SMTP_OFF), checked)
	
	def pop3On(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.email.POP3_ON), checked)
	
	def pop3Off(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.email.POP3_OFF), checked)
	
	def domainName(self, domainName):
		Util().textCheckPoint(self.objName(ServicesConst.email.DOMAIN_NAME_EDIT), domainName)
	
	def user(self, user):
		Util().textCheckPoint(self.objName(ServicesConst.email.USERNAME_EDIT), user)
	
	def password(self, password):
		Util().textCheckPoint(self.objName(ServicesConst.email.PASSWORD_EDIT), password)
	
	def setButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.email.DOMAIN_NAME_SET_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
	
	def addButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.email.USER_ADD_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
	
	def removeButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.email.USER_REMOVE_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
	
	def changePasswordButton(self, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.email.USER_CHANGE_PASSWORD_BUTT), kwargs['property'], kwargs['value'])
		else:
			raise ValueError('A property and expected value must be specified. Please specify a property')
		
	@property
	def userTable(self):
		return findObject(self.objName(ServicesConst.email.USER_LIST))
	
class Email(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = EmailCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def smtpOn(self):
		Util().clickButton(self.objName(ServicesConst.email.SMTP_ON))
	
	def smtpOff(self):
		Util().clickButton(self.objName(ServicesConst.email.SMTP_OFF))
	
	def pop3On(self):
		Util().clickButton(self.objName(ServicesConst.email.POP3_ON))
	
	def pop3Off(self):
		Util().clickButton(self.objName(ServicesConst.email.POP3_OFF))
	
	def domainName(self, domainName):
		Util().setText(self.objName(ServicesConst.email.DOMAIN_NAME_EDIT), domainName)
	
	def setButton(self):
		Util().clickButton(self.objName(ServicesConst.email.DOMAIN_NAME_SET_BUTT))
	
	def user(self, user):
		Util().setText(self.objName(ServicesConst.email.USERNAME_EDIT), user)
	
	def password(self, password):
		Util().setText(self.objName(ServicesConst.email.PASSWORD_EDIT), password)
	
	def addButton(self):
		Util().clickButton(self.objName(ServicesConst.email.USER_ADD_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(ServicesConst.email.USER_REMOVE_BUTT))
	
	def changePasswordButton(self):
		Util().clickButton(self.objName(ServicesConst.email.USER_CHANGE_PASSWORD_BUTT))
	
	def newPasswordEdit(self, password):
		Util().setText(self.objName(ServicesConst.email.NEW_PASSWORD_EDIT), password)
		
	def newPasswordOkButton(self):
		Util().clickButton(self.objName(ServicesConst.email.NEW_PASSWORD_OK_BUTT))
	
	def newPasswordCancelButton(self):
		Util().clickButton(self.objName(ServicesConst.email.NEW_PASSWORD_CANCEL_BUTT))
	
	def newPasswordSuccessfulOkButton(self):
		Util().clickButton(self.objName(ServicesConst.email.CHANGE_PASSWORD_CONFIRM_BUTT))
	
	@property
	def userTableName(self):
		return self.objName(ServicesConst.email.USER_LIST)
	
	@property
	def userTable(self):
		return findObject(self.userTableName)
	
	def selectUser(self, username):
		Util().clickItem(self.userTable, username)
	
	def addUser(self, username, password):
		self.user(username)
		self.password(password)
		self.addButton()
	
	def removeUser(self, username):
		self.selectUser(username)
		self.removeButton()
	
	def changePassword(self, username, password):
		self.selectUser(username)
		self.changePasswordButton()
		self.newPasswordEdit(password)
		self.newPasswordOkButton()
		self.newPasswordSuccessfulOkButton()
	