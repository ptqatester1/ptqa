##Chris Allen

from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst

class IoeMonitor:
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName

	def close(self):
		Util().clickButton(self.objName(DesktopConst.ioemonitor.CLOSE_BUTT))
