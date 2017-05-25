##Chris Allen
from API.Utility.Util import Util
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from squish import *
import object

class AaaList(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.util = Util()
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	def getListItem(self, row):
		for item in object.children(self.listObject):
			try:
				if item.row == row:
					return item
			except AttributeError, e:
				print(e)
		raise ValueError('No item at row: %s'%(row,))
	
	def selectListItem(self, row):
		self.util.click(self.getListItem(row))
	
	def checkText(self, expectedText, row):
		self.util.textCheckPoint(self.getListItem(row), expectedText)

class Tacacs(AaaList):
	@property
	def listObject(self):
		try:
			return findObject(self.objName(DesktopConst.aaaAccounting.TACACS_LIST))
		except LookupError, e:
			return False
		
class Radius(AaaList):
	@property
	def listObject(self):
		try:
			return findObject(self.objName(DesktopConst.aaaAccounting.RADIUS_LIST))
		except LookupError, e:
			return False
	
class Tabs(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.util = Util()
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def _clickTab(self, tab):
		self.util.clickTab(DesktopConst.aaaAccounting.TABBAR, tab)

	def tacacs(self):
		self._clickTab('TACACS+ Accounting')
	
	def radius(self):
		self._clickTab('RADIUS Accounting')

class AaaAccounting:
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.tabs = Tabs(self)
		self.tacacs = Tacacs(self)
		self.radius = Radius(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.tabs.updateName(squishName)
		self.tacacs.updateName(squishName)
		self.radius.updateName(squishName)
	
	def textCheckPoint(self, searchText, row):
		if self.tacacs.listObject:
			self.tacacs.checkText(searchText, row)
		elif self.radius.listObject:
			self.radius.checkText(searchText, row)
		else:
			raise LookupError('Could not find the list object')
	