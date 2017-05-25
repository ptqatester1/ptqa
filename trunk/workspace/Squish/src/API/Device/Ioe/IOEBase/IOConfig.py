#*******************************************************#
#@Author: Chris Allen                                   #
#*******************************************************#

from API.Utility.Util import Util
from API.Device.Ioe.IoeBaseConst import IoeBaseConst
from API.Device.DeviceBase.DeviceBase import DeviceBase, SquishObjectName
from squish import *
import test

class IOConfigCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.util = Util()
		
	def updateName(self, p_squishName):
		self.squishName = p_squishName
	
	def analogSlots(self, slots, **kwargs):
		spinbox = self.objName(IoeBaseConst.ioConfig.ANALOG_SLOTS_SPINBOX)
		if 'property' in kwargs:
			Util().checkProperty(spinbox, **kwargs)
		else:
			Util().textCheckPoint(spinbox, slots, **kwargs)

class IOConfig(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.util = Util()
		self.check = IOConfigCheck(self)
		
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		self.check.updateName(p_squishName)
	
	def selectAdapter(self, p_adapter):
		self.util.click(IoeBaseConst.ioConfig.NETWORK_ADAPTER_DROPDOWN)
		self.util.clickItem(IoeBaseConst.ioConfig.NETWORK_ADAPTER_DROPDOWN, p_adapter)
		None
	
#	def addDigitalSlots(self, p_numberOfSlotsToAdd = 1):
#		None
#	
#	def removeDigitalSlots(self, p_numberOfSlotsToRemove = 1):
#		None
#	
#	def addAnalogSlots(self, p_numberOfSlotsToAdd = 1):
#		None
#	
#	def removeAnalogSlots(self, p_numberOfSlotsToRemove = 1):
#		None
#	
	def setDigitalSlots(self, p_number):
		p_number = str(p_number)
		self.util.setText(IoeBaseConst.ioConfig.DIGITAL_SLOTS_SPINBOX, p_number)
		None
	
	def setAnalogSlots(self, p_number):
		p_number = str(p_number)
		self.util.setText(self.objName(IoeBaseConst.ioConfig.ANALOG_SLOTS_SPINBOX), p_number)
		None
	
	def endDevice(self):
		self.util.clickButton(IoeBaseConst.ioConfig.USAGE_END_DEVICE)
	
	def sensor(self):
		self.util.clickButton(IoeBaseConst.ioConfig.USAGE_SENSOR)