##Chris Allen
from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import PhysicalConst
from squish import *
import object
from API import functions

def err():
	raise NotImplementedError

class CustomView(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.util = Util()
	
	def updateName(self, squishName):
		self.squishName = squishName

	def browseButton(self):
		Util().clickButton(PhysicalConst.customizeImageWindow.BROWSE_BUTTON)

	def okButton(self):
		if object.exists(PhysicalConst.customizeImageWindow.OK_BUTTON_LOGICAL):
			Util().clickButton(PhysicalConst.customizeImageWindow.OK_BUTTON_LOGICAL)
		elif object.exists(PhysicalConst.customizeImageWindow.OK_BUTTON):
			Util().clickButton(PhysicalConst.customizeImageWindow.OK_BUTTON)
			
	def cancelButton(self):
		Util().clickButton(PhysicalConst.customizeImageWindow.CANCEL_BUTTON)

	def resetButton(self):
		Util().clickButton(PhysicalConst.customizeImageWindow.RESET_BUTTON)

	def filename(self, filename):
		Util().setText(PhysicalConst.FILE_NAME, filename)

	def openButton(self):
		Util().clickButton(PhysicalConst.customizeImageWindow.OPEN_BUTTON)

	def selectFile(self, filename):
		self.browseButton()
		self.filename(filename)
		self.openButton()

	def customizeView(self, filename, **kwargs):
		if 'physical' in kwargs:
			Util().clickButton(PhysicalConst.CUSTOMIZE_ICON_PHYSICAL_VIEW)
			
		elif 'logical' in kwargs:
			Util().clickButton(PhysicalConst.CUSTOMIZE_ICON_LOGICAL_VIEW)
		else:
			raise ValueError
		self.selectFile(filename)

class Physical(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.util = Util()
		self.customView = CustomView(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.customView.updateName(squishName)

	@property
	def moduleList(self):
		return findObject(self.objName(PhysicalConst.modules.MODULE_LIST))
	
	def getModuleObject(self, moduleName):
		for module in object.children(self.moduleList):
			if 'text' in object.properties(module):
				if moduleName == str(module.text):
					return module
		raise ValueError('Could not find module named: %s'%(moduleName,))
	
	@property
	def imageAreaObject(self):
		return findObject(self.objName(PhysicalConst.IMAGE_AREA))
	
	@property
	def imageObject(self):
		return findObject(self.objName(PhysicalConst.IMAGE))
	
	def selectModule(self, module):
		Util().click(self.getModuleObject(module))

	def zoomIn(self):
		Util().clickButton(self.objName(PhysicalConst.ZOOM_IN))

	def zoomOriginal(self):
		Util().clickButton(self.objName(PhysicalConst.ZOOM_ORIGINAL_SIZE))

	def zoomOut(self):
		Util().clickButton(self.objName(PhysicalConst.ZOOM_OUT))
	
	def customizeIconInLogicalViewButton(self):
		Util().clickButton(self.objName(PhysicalConst.CUSTOMIZE_ICON_LOGICAL_VIEW))
		
	def customizeIconInPhysicalViewButton(self):
		Util().clickButton(self.objName(PhysicalConst.CUSTOMIZE_ICON_PHYSICAL_VIEW))
		
	def customizePhysicalView(self, filename):
		CustomView().customizeView(filename, 'physical')

	def customizeLogicalView(self, filename):
		CustomView().customizeView(filename, 'logical')

	def checkModuleText(self, expectedText, occurrenceNum = -1, **kwargs):
		Util().textCheckPoint(self.objName(PhysicalConst.CURRENT_MODULE_TEXT), expectedText, occurrenceNum, **kwargs)

	def power(self, powerButtonName):
		powerButton = findObject(self.objName(powerButtonName))
		Util().click(powerButton)
	
	def clickModule(self, moduleName):
		moduleName = '.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab.m_moduleListScrollView.qt_scrollarea_viewport.QWidget1.QFrame1.' + moduleName
		module = findObject(self.objName(moduleName))
		Util().click(module)
	
	'''
	def powerAdapter(self, adapter, powerSlot):
		deviceWindow = findObject(self.objName(''))
		if not deviceWindow.isMaximized():
			Util().maximizeWindow(deviceWindow)
		if functions.getType(adapter) == functions.getType('str'):
			adapter = self.getModuleObject(adapter)
		if functions.getType(powerSlot) == functions.getType('str'):
			powerSlot = findObject(self.objName(powerSlot))
		Util().dragAndDrop(adapter, adapter.width/2, adapter.height/2, powerSlot, powerSlot.width/2, powerSlot.height/2)
	'''
		
	def removeModule(self, module):
		deviceWindow = findObject(self.objName(''))
		if not deviceWindow.isMaximized():
			Util().maximizeWindow(deviceWindow)
		modulesButton = self.getModuleObject('MODULES')
		if functions.getType(module) == functions.getType(''):
			module = findObject(self.objName(module))
		Util().dragAndDrop(module, module.width/2, module.height/2, modulesButton, modulesButton.width/2, modulesButton.height/2)
	
	def addModule(self, moduleName, targetModule):
		'''Takes the name of module to add and the squishname or module object of the target module
		moduleName: String (Name of the module to add
		targetModule: String || Object (SquishName of the module target or the module target object
		'''
		deviceWindow = findObject(self.objName(''))
		if not deviceWindow.isMaximized():
			Util().maximizeWindow(deviceWindow)
		module = self.getModuleObject(moduleName)
		if functions.getType(targetModule) == functions.getType('str'):
			targetModule = findObject(self.objName(targetModule))
		Util().dragAndDrop(module, module.width/2, module.height/2, targetModule, targetModule.width/2, targetModule.height/2)