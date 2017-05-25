##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *

class SyslogCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	def on(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.syslog.ON), checked)
	
	def off(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.syslog.OFF), checked)
		
	@property
	def tableName(self):
		return self.objName(ServicesConst.syslog.LIST)
	
	def lineEdit(self, line, occurrenceNum = -1):
		Util().textCheckPoint(self.objName(ServicesConst.syslog.LINE_EDIT), line, occurrenceNum)
		
	def time(self, row, time, occurrenceNum):
		Util().textCheckPoint(self.objName(ServicesConst.syslog.LIST) + '.item_%s/0'%(row,), time, occurrenceNum)

	def hostName(self, row, hostName, occurrenceNum):
		Util().textCheckPoint(self.objName(ServicesConst.syslog.LIST) + '.item_%s/1'%(row,), hostName, occurrenceNum)
		
	def message(self, row, message, occurrenceNum=-1):
		Util().textCheckPoint(self.objName(ServicesConst.syslog.LIST) + '.item_%s/2'%(row,), message, occurrenceNum)
	
	def tableRowsNumber(self, row):
		if (self.objName(ServicesConst.syslog.LIST)).rowCount == row:
			return True
		else:
			return False
		
class Syslog(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = SyslogCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def on(self):
		Util().clickButton(self.objName(ServicesConst.syslog.ON))
	
	def off(self):
		Util().clickButton(self.objName(ServicesConst.syslog.OFF))
	
	@property
	def tableName(self):
		return self.objName(ServicesConst.syslog.LIST)

	@property
	def table(self):
		try:
			return findObject(self.tableName)
		except LookupError, e:
			return False
	
	def selectRow(self, row):
		Util().click(self.tableName + '.item_%s/0'%(row,))
		
	def selectEntry(self, entry):
		Util().click(self.tableName + '.item_%s'%(entry,))
	
	def clearLog(self):
		Util().clickButton(self.objName(ServicesConst.syslog.CLEAR_LOG_BUTTON))
