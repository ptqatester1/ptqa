##Chris Allen
from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from squish import *

class TftpService(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName

	def setDirectory(self, p_directoryPath):
		dirPath = p_directoryPath.split("_")
		print dirPath
		Util().clickButton(self.objName(DesktopConst.tftpService.BROWSE_BUTTON))
		snooze(1)
		for i in range(0, len(dirPath)-1):	  
			Util().doubleClickItem(self.objName(DesktopConst.tftpService.BROWSE_LIST), dirPath[i])
		Util().clickItem(self.objName(DesktopConst.tftpService.BROWSE_LIST), dirPath[-1])
		Util().clickButton(self.objName(DesktopConst.tftpService.BROWSE_OK_BUTTON))