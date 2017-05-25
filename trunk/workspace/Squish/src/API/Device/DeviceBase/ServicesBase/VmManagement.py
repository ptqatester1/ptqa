##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *

class VmManagement(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def on(self):
		Util().clickButton(self.objName(ServicesConst.vmManagement.ON_BUTTON))
	
	def off(self):
		Util().clickButton(self.objName(ServicesConst.vmManagement.OFF_BUTTON))
	
	def start(self):
		Util().clickButton(self.objName(ServicesConst.vmManagement.START_BUTTON))
	
	def stop(self):
		Util().clickButton(self.objName(ServicesConst.vmManagement.STOP_BUTTON))
	