##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.AttributeBase.AttributesBaseConst import AttributesConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from squish import *

class Attributes(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def checkAttribute(self, name, attribute):
		if name == "MTBF":
			Util().textCheckPoint(self. objName(AttributesConst.MTBF), attribute)
			
		elif name == "cost":
			Util().textCheckPoint(self.objName(AttributesConst.COST), attribute)
		
		elif name == "power source":
			Util().textCheckPoint(self.objName(AttributesConst.POWER_SOURCE), attribute)
			
		elif name == "rack units":
			Util().textCheckPoint(self.objName(AttributesConst.RACK_UNITS), attribute)
		
		elif name == "wattage":
			Util().textCheckPoint(self.objName(AttributesConst.WATTAGE), attribute)
		
	def getPropertyValue(self, property):
		table_object_name = self.objName(AttributesConst.PROPERTIES_TABLE)
		table = findObject(table_object_name)
		for i in range(table.rowCount):
			row_name = findObject(table_object_name + '.item_0/0')
			row_value = findObject(table_object_name + '.item_0/1')
			if not row_name.text == property:
				continue
			return row_value.text
		raise  ValueError('No property with name %s found' % (property))
	