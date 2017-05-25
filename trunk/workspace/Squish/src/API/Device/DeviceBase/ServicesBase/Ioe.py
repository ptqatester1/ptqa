##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *

class Ioe(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def on(self):
		Util().clickButton(self.objName(ServicesConst.ioe.ON))
	
	def off(self):
		Util().clickButton(self.objName(ServicesConst.ioe.OFF))
	
	def delteButton(self):
		Util().clickButton(self.objName(ServicesConst.ioe.DELETE))
	
	@property
	def tableName(self):
		return self.objName(ServicesConst.ioe.TABLE)
	
	@property
	def table(self):
		return findObject(self.tableName)
	
	def selectRow(self, row):
		Util().click(findObject(self.tableName + '.item_%s/0'%(row,)))
	
	def deleteRow(self, row):
		self.selectRow(row)
		self.delteButton()
		