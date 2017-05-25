##Chris Allen

from API.Device.DeviceBase.DeviceBase import SquishObjectName

class IoeIde:
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
