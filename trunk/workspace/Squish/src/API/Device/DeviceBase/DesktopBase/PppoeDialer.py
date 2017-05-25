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
	def failureMsgbox(self):
		try:
			return findObject(self.objName(DesktopConst.pppoeDialer.FAILURE_MSG_BOX))
		except LookupError, e:
			return False
		
	def failureMsgOkButton(self):
		Util().clickButton(self.objName(DesktopConst.pppoeDialer.FAILURE_OK))

	def connectedMsgbox(self):
		try:
			return findObject(self.objName(DesktopConst.pppoeDialer.CONNECTED_MSG_BOX))
		except LookupError, e:
			return False
		
	def connectedMsgOkButton(self):
		Util().clickButton(self.objName(DesktopConst.pppoeDialer.CONNECTED_OK))

class PppoeDialerCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.popups = PopupWarnings(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.popups.updateName(squishName)
	
	def failureMessage(self, message):
		Util().textCheckPoint(self.objName(DesktopConst.pppoeDialer.FAILURE_LABEL), message)

class PppoeDialer(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.popups = PopupWarnings(self)
		self.check = PppoeDialerCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.popups.updateName(squishName)
		self.check.updateName(squishName)
		
	def username(self, username):
		Util().setText(self.objName(DesktopConst.pppoeDialer.USERNAME), username)

	def password(self, password):
		Util().setText(self.objName(DesktopConst.pppoeDialer.PASSWORD), password)

	def connectButton(self):
		Util().clickButton(self.objName(DesktopConst.pppoeDialer.CONNECT_BUTT))

	def close(self):
		Util().clickButton(self.objName(DesktopConst.pppoeDialer.CLOSE_BUTT))

	def connect(self, username, password):
		self.username(username)
		self.password(password)
		self.connectButton()
		snooze(5)
		if self.popups.failureMsgbox:
			self.popups.failureMsgOkButton()
		