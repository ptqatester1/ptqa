##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst

class DialUpCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	def status(self, status):
		Util().textCheckPoint(self.objName(DesktopConst.dialup.STATUS_MESSAGE), status)

class DialUp(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = DialUpCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def username(self, username):
		Util().setText(self.objName(DesktopConst.dialup.USERNAME_EDIT), username)
	
	def password(self, password):
		Util().setText(self.objName(DesktopConst.dialup.PASSWORD_EDIT), password)
	
	def numbder(self, number):
		Util().setText(self.objName(DesktopConst.dialup.NUM_EDIT), number)
	
	def dialButton(self):
		Util().clickButton(self.objName(DesktopConst.dialup.DIAL_BUTTON))

	def disconnectButton(self):
		Util().clickButton(self.objName(DesktopConst.dialup.DISCONNECT_BUTT))
	
	def dial(self, username, password, number):
		self.username(username)
		self.password(password)
		self.numbder(number)
		self.dialButton()
	
	def close(self):
		Util().clickButton(self.objName(DesktopConst.dialup.CLOSE))