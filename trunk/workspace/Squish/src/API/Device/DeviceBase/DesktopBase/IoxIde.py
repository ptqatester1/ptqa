##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst

class Project(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def open(self):
		Util().activateItem(self.objName(DesktopConst.ioxide.PROJECT), 'Open')
	
	def delete(self):
		Util().activateItem(self.objName(DesktopConst.ioxide.PROJECT), 'Delete')

class Open(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def openProject(self, projectName):
		Util().clickItem(self.objName(DesktopConst.ioxide.PROJECT_OPEN_FILE_TREE), projectName)
		Util().clickButton(self.objName(DesktopConst.ioxide.PROJECT_OPEN_OPEN_BUTT))

class Delete(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

class IoxIde(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.projectOption = Project(self)
		self.openOption = Open(self)
		self.deleteOption = Delete(self)

	def updateName(self, squishName):
		self.squishName = squishName
	
	def Project(self):
		Util().activateItem(self.objName(DesktopConst.ioxide.MENU_BAR), 'Project')
	
	def selectFile(self, file):
		Util().clickItem(self.objName(DesktopConst.ioxide.PROJECT_FILE_TREE), file)
	
	def close(self):
		Util().clickButton(self.objName(DesktopConst.ioxide.CLOSE_BUTT))

	
