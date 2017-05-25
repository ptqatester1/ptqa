##Chris Allen

from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import MibBrowser
from API.Utility.Util import Util

def err(msg = ''):
	raise NotImplementedError(msg)

class Advanced(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName

	def address(self, address):
		Util().setText(self.objName(MibBrowser.advanced.ADDRESS_EDIT), address)

	def port(self, port):
		Util().setText(self.objName(MibBrowser.advanced.PORT_EDIT), port)

	def readCommunity(self, readCommunity):
		Util().setText(self.objName(MibBrowser.advanced.READ_COMMUNITY_EDIT), readCommunity)

	def writeCommunity(self, writeCommunity):
		Util().setText(self.objName(MibBrowser.advanced.WRITE_COMMUNITY_EDIT), writeCommunity)

	def snmpVersion(self, version):
		err()

	def okButton(self):
		Util().clickButton(self.objName(MibBrowser.advanced.OK_BUTTON))

	def cancelButton(self):
		Util().clickButton(self.objName(MibBrowser.advanced.CANCEL_BUTTON))

class SnmpMibs:
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName

	def select(self, treeItem):
		err('operation to select an item in the tree')

	def expand(self, treeItem):
		err('operation to expand item in the tree')

class ResultTable:
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName

	def select(self):
		err('operation to select item in the ResultTable')

	def checkName(self, name):
		err()

	def checkOid(self, oid):
		err()

	def checkSyntax(self, syntax):
		err()

	def checkAccess(self, access):
		err()

	def checkDescription(self):
		err()
		

class MIBBrowser(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.resultTable = ResultTable(self)
		self.advanced = Advanced(self)
		self.snmpMibs = SnmpMibs(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.advanced.updateName(squishName)
		
	def address(self, address):
		Util().setText(self.objName(MibBrowser.ADDRESS_EDIT), address)

	def oid(self, oid):
		Util().setConsoleText(self.objName(MibBrowser.OID_EDIT), oid)

	def advancedButton(self):
		Util().clickButton(self.objName(MibBrowser.ADVANCED_BUTT))

	def operations(self, operation):
		err()

	def go(self):
		Util().clickButton(self.objName(MibBrowser.GO_BUTT))
		
	def close(self):
		Util().clickButton(self.objName(DesktopConst.mibBrowser.CLOSE_BUTT))
