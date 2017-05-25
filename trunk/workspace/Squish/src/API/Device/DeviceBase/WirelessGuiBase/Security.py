##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.WirelessGuiBase.ConstantsHelper import ConstantsHelper

class Firewall(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

class Security:
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.firewall = Firewall(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.firewall.updateName(self.squishName)