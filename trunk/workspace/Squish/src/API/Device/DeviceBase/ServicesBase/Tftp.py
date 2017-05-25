##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *
import object
from API import functions

class TftpCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def on(self, checked = True):
		Util().isChecked(self.objName(ServicesConst.tftp.ON), checked)
	
	def off(self, checked = True):
		Util().isChecked(self.objName(ServicesConst.tftp.OFF), checked)

	def removeFileButtonText(self, text):
		Util().textCheckPoint(self.objName(ServicesConst.tftp.REMOVE_FILE_BUTT), text)
	
	@property
	def fileList(self):
		return findObject(self.objName(ServicesConst.tftp.FILE_PATH_LIST))
	
	def fileInList(self, filename):	
		for child in object.children(self.fileList):
			if 'text' in object.properties(child):
				if str(child.text) == filename:
					return child
		return False
	
	def fileExists(self, filename):
		functions.check(self.fileInList(filename))
		
	def fileNotExists(self, filename):
		functions.check(not self.fileInList(filename))

class Tftp(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = TftpCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def on(self):
		Util().clickButton(self.objName(ServicesConst.tftp.ON))
	
	def off(self):
		Util().clickButton(self.objName(ServicesConst.tftp.OFF))
	
	def removeFileButton(self):
		Util().clickButton(self.objName(ServicesConst.tftp.REMOVE_FILE_BUTT))
	
	@property
	def fileListName(self):
		return self.objName(ServicesConst.tftp.FILE_PATH_LIST)
	
	@property
	def fileList(self):
		return findObject(self.fileListName)
	
	def selectFile(self, filename):
		for child in object.children(self.fileList):
			if 'text' in object.properties(child):
				if str(child.text) == filename:
					Util().click(child)
					return child
		raise ValueError('Unable to find file with the name ' + filename)
	
	def remove(self, filename):
		self.selectFile(filename)
		self.removeFileButton()