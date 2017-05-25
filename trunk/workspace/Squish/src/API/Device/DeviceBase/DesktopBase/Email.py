##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from squish import *

class ConfigureMailCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def name(self, name, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.email.ConfigureMail.NAME), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.email.ConfigureMail.NAME), name)

	def email(self, email, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.email.ConfigureMail.EMAIL), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.email.ConfigureMail.EMAIL), email)

	def incomingServer(self, incomingServer, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.email.ConfigureMail.INCOMING_MAIL_SERVER), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.email.ConfigureMail.INCOMING_MAIL_SERVER), incomingServer)

	def outgoingServer(self, outgoingServer, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.email.ConfigureMail.OUTGOING_MAIL_SERVER), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.email.ConfigureMail.OUTGOING_MAIL_SERVER), outgoingServer)

	def username(self, username, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.email.ConfigureMail.USERNAME), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.email.ConfigureMail.USERNAME), username)

	def password(self, password, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.email.ConfigureMail.PASSWORD), **kwargs)
		else:
			Util().setText(self.objName(DesktopConst.email.ConfigureMail.PASSWORD), password)

	def save(self, **kwargs):
		Util().checkProperty(self.objName(DesktopConst.email.ConfigureMail.SAVE_BUTT), **kwargs)

	def clear(self, **kwargs):
		Util().checkProperty(self.objName(DesktopConst.email.ConfigureMail.CLEAR_BUTT), **kwargs)

	def reset(self, **kwargs):
		Util().checkProperty(self.objName(DesktopConst.email.ConfigureMail.RESET_BUTT), **kwargs)

class ConfigureMail(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = ConfigureMailCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def name(self, name):
		Util().setText(self.objName(DesktopConst.email.ConfigureMail.NAME), name)

	def email(self, email):
		Util().setText(self.objName(DesktopConst.email.ConfigureMail.EMAIL), email)

	def incomingServer(self, incomingServer):
		Util().setText(self.objName(DesktopConst.email.ConfigureMail.INCOMING_MAIL_SERVER), incomingServer)

	def outgoingServer(self, outgoingServer):
		Util().setText(self.objName(DesktopConst.email.ConfigureMail.OUTGOING_MAIL_SERVER), outgoingServer)

	def username(self, username):
		Util().setText(self.objName(DesktopConst.email.ConfigureMail.USERNAME), username)

	def password(self, password):
		Util().setText(self.objName(DesktopConst.email.ConfigureMail.PASSWORD), password)

	def save(self):
		Util().clickButton(self.objName(DesktopConst.email.ConfigureMail.SAVE_BUTT))

	def clear(self):
		Util().clickButton(self.objName(DesktopConst.email.ConfigureMail.CLEAR_BUTT))

	def reset(self):
		Util().clickButton(self.objName(DesktopConst.email.ConfigureMail.RESET_BUTT))
		
	def close(self):
		Util().clickButton(self.objName(DesktopConst.email.ConfigureMail.CLOSE_BUTT))

	def newAccount(self, name, email, incomingServer, outgoingServer, username, password):
		if name:
			self.name(name)
		if email:
			self.email(email)
		if incomingServer:
			self.incomingServer(incomingServer)
		if outgoingServer:
			self.outgoingServer(outgoingServer)
		if username:
			self.username(username)
		if password:
			self.password(password)
		self.save()

class MailBrowser(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	@property
	def tableName(self):
		return self.objName(DesktopConst.email.MAIL_TABLE)
	
	@property
	def tableObject(self):
		return findObject(self.tableName)
	
	def composeButton(self):
		Util().clickButton(self.objName(DesktopConst.email.COMPOSE_BUTT))
		
	def checkStatus(self, message):
		Util().textCheckPoint(self.objName(DesktopConst.email.STATUS_LABEL), message)

	def replyButton(self):
		Util().clickButton(self.objName(DesktopConst.email.REPLY_BUTT))

	def receiveButton(self):
		Util().clickButton(self.objName(DesktopConst.email.RECEIVE_BUTT))

	def deleteButton(self):
		Util().clickButton(self.objName(DesktopConst.email.DELETE_BUTT))

	def configureMailButton(self):
		Util().clickButton(self.objName(DesktopConst.email.CONFIGURE_BUTT))

	def selectMessage(self, msg_from = None, msg_subject = None, row = None):
		if not (msg_from == None or msg_subject == None or row == None):
			raise ValueError('Must provide at least one argument')
		if not row == None:
			Util().click(self.tableName + '.item_%s/0'%(row,))
		else:
			raise NotImplementedError

	def selectMessageFrom(self, messageFrom):
		self.selectMessage(messageFrom, 'from')
		
	def selectMessageSubject(self, messageSubject):
		self.selectMessage(messageSubject, 'subject')

	def selectMessageReceived(self, messageReceived):
		self.selectMessage(messageReceived, 'received')

	def cancelSendReceiveButton(self):
		Util().clickButton(self.objName(DesktopConst.email.CANCEL_SEND_RECEIVE))

class Compose(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def composeButton(self):
		Util().clickButton(self.objName(DesktopConst.email.COMPOSE_BUTT))
		
	def email(self, emailAddress):
		Util().setText(self.objName(DesktopConst.email.Compose.TO), emailAddress)

	def subject(self, subject):
		Util().setText(self.objName(DesktopConst.email.Compose.SUBJECT), subject)

	def body(self, body):
		Util().setText(self.objName(DesktopConst.email.Compose.CONTENT_EDIT), body)

	def sendButton(self):
		Util().clickButton(self.objName(DesktopConst.email.Compose.SEND_BUTT))

	def close(self):
		Util().clickButton(self.objName(DesktopConst.email.Compose.CLOSE_BUTT))

	def newEmail(self, emailAddress, subject, body):
		self.composeButton()
		self.email(emailAddress)
		self.subject(subject)
		self.body(body)
		self.sendButton()

class Reply(Compose, SquishObjectName):
	def __init__(self, parent):
		super(Reply, self).__init__(parent)
		None

class Message(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		
	def updateName(self, squishName):
		self.squishName = squishName
		
	def checkFrom(self, fromEmail):
		Util().textCheckPoint(self.objName(DesktopConst.email.Message.FROM), fromEmail)
		
	def checkTo(self, toEmail):
		Util().textCheckPoint(self.objName(DesktopConst.email.Message.TO), toEmail)
		
	def checkSubject(self, subject):
		Util().textCheckPoint(self.objName(DesktopConst.email.Message.SUBJECT), subject)
		
	def checkBody(self, body):
		Util().textCheckPoint(self.objName(DesktopConst.email.Message.BODY), body)
		
class Email(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.reply = Reply(self)
		self.compose = Compose(self)
		self.configure = ConfigureMail(self)
		self.mailBrowser = MailBrowser(self)
		self.message = Message(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.reply.updateName(squishName)
		self.compose.updateName(squishName)
		self.configure.updateName(squishName)
		self.mailBrowser.updateName(squishName)
		self.message.updateName(squishName)
	
	def close(self):
		Util().close(self.objName(DesktopConst.email.MAIN_WINDOW))
