#*******************************************************#
#@Author: Chris Allen                                   #
#*******************************************************#

from API.Device.Ioe.IoeBaseConst import IoeBaseConst
from API.Device.DeviceBase import PhysicalBase

class Physical(PhysicalBase):
	def __init__(self):
		self.squishName = ""

	def updateName(self, p_squishName):
		self.squishName = p_squishName
		super(Physical, self).updateName(self.squishName)
		
	def removePower(self):
		self.dragAndDrop(
						self.squishName + IoeBaseConst.physical.POWER_BLOCK,
						5, 5,
						self.squishName + IoeBaseConst.physical.POWER_BLOCK_CONTAINER,
						5, 5)
	def addPower(self):
		self.dragAndDrop(
						self.squishName + IoeBaseConst.physical.POWER_BLOCK_CONTAINER,
						5, 5,
						self.squishName + IoeBaseConst.physical.POWER_BLOCK,
						5, 5)