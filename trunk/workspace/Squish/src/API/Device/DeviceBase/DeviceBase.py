##Chris Allen
from __builtin__ import object as Object
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase.DeviceBaseConst import DeviceBaseConst
from API.Device.DeviceBase.ConfigBase import ConfigBaseConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Device.Ioe import IoeBaseConst
from squish import *
import test
from API import functions

class DeviceBase(Object):
	def __init__(self, p_model, p_x, p_y, p_displayName, p_deviceType):
		self.util = Util()  
		self.model = p_model
		self.x = p_x
		self.y = p_y
		self.displayName = p_displayName
		self.squishName = ':' + self.displayName
		self.deviceType = p_deviceType

	def objName(self, obj):
		if obj.startswith(':'):
			return obj
		else:
			return self.squishName + obj
			
	def getCurrentDeviceName(self):
		snooze(.2)
		print "p_displayName- :" + self.displayName
		if not self.util.checkObjectExist(":" + self.displayName):
			print "getCurrentDeviceName- :CBaseDeviceWidget"
			return ":CBaseDeviceWidgetClass"
		else:
			print "getCurrentDeviceName- :" + self.displayName
			return ":" + self.displayName

	def updateName(self):
		self.squishName = self.getCurrentDeviceName()
	
	#@summary: call clickTab defined in SquishSyntax
	#@param p_obj: obj name   
	#@param p_tabName: name of the tab, CLI, Config...
	def clickTab(self, *args, **kwargs):  
		'''Takes up to two arugments.
		Either just the tab name for a device or the tabbar object name and the tab name'''     
		if 'snooze' in kwargs:
			snooze(kwargs['snooze'])
		if len(args) == 1:
			p_tabName = args[0]
			self.util.clickTab(self.squishName + DeviceBaseConst.DeviceTab.DEVICE_TAB, p_tabName)
		elif len(args) == 2:
			p_obj = args[0]
			p_tabName = args[1]
			if p_obj.startswith(":"):
				self.util.clickTab(p_obj, p_tabName)            
			else:
				self.util.clickTab(self.squishName + p_obj, p_tabName)
		else:
			raise Exception('To many or to few arguments enter tab name or object and tab name')
			

	def clickConfigTab(self):
		self.clickTab("Config")
		
	def clickCliTab(self):
		self.clickTab("CLI")
		
	def clickDesktopTab(self):
		self.clickTab("Desktop")
		
	def clickGuiTab(self):
		self.clickTab("GUI")
		
	def clickPhysicalTab(self):
		self.clickTab("Physical")
	
	def clickServicesTab(self):
		self.clickTab("Services")

	def clickProgrammingTab(self):
		if not findObject(IoeBaseConst.Specifications.ADVANCED_BUTTON).checked:
			Util().clickButton(self.objName(IoeBaseConst.Specifications.ADVANCED_BUTTON))
		self.clickTab("Programming")

	def exists(self):
		self.select()
		if (self.util.checkObjectExist(self.squishName +  DeviceBaseConst.DeviceTab.DEVICE_TAB)):
			test.passes("Device exists")
			self.close()
		else:
			test.fail("Device does not exist")

	def doesNotExist(self):
		self.select()
		if (self.util.checkObjectNotExist(self.squishName +  DeviceBaseConst.DeviceTab.DEVICE_TAB)):
			test.passes("Device does not exist")
		else:
			test.fail("Device exists")
			
	def existsOnPhysical(self, p_deviceName = "", p_x = -1, p_y = -1, p_obj = ""):
		if p_x == -1:
			self.util.clickOnPhysicalWorkspace(self.x, self.y)
		else:
			self.util.clickOnPhysicalWorkspace(p_x, p_y, p_obj)
		self.updateName()

		if (self.util.checkObjectExist(self.squishName +  DeviceBaseConst.DeviceTab.DEVICE_TAB + ".TabItem2")):
			self.clickTab(DeviceBaseConst.DeviceTab.DEVICE_TAB, "Config")
			if (self.util.checkObjectExist(self.squishName + ConfigBaseConst.GlobalSettings.DISPLAY_NAME_EDIT)) and (p_deviceName == (findObject(self.squishName + DeviceBaseConst.Config.DISPLAY_NAME).displayText)):
				test.passes("device exists")
				self.close()  
			elif (self.util.checkObjectExist(self.squishName + DeviceBaseConst.Config.WORKSTATION_DISPLAY_NAME)) and (p_deviceName == (findObject(self.squishName + DeviceBaseConst.Config.WORKSTATION_DISPLAY_NAME).displayText)):
				test.passes("device exists")
				self.close()
			else:
				test.fail("device does not exist", Util().getLineNum())
			
		else:
			if (self.util.checkObjectExist(self.squishName + DeviceBaseConst.DeviceTab.TV_ON)):
				test.passes("device exists")
				self.close()                
			else:
				test.fail("device does not exist", Util().getLineNum())
				
	
	def minimizeDeviceWindow(self):
		self.util.minimizeWindow(self.squishName)
		
	def restoreDeviceWindow(self):
		self.util.restoreWindow(self.squishName)
		
	def maximizeDeviceWindow(self):
		self.util.maximizeWindow(self.squishName)
	
	def connect(self, otherDevice, cableType = ComponentBoxConst.Connection.CONN_AUTO, port1 = '', port2 = '', **kwargs):
		from API.functions import getType
		if 'workspace' in kwargs:
			if kwargs['workspace'] == 'physical':
				if 'location1' in kwargs and 'locations2' in kwargs:
					location1 = kwargs['location1']
					location2 = kwargs['location2']
				else:
					location1 = ''
					location2 = ''
				self.util.connectOnPhysical(self.x, self.y, otherDevice.x, otherDevice.y, cableType, port1, port2, location1, location2)    
			elif kwargs['workspace'] == 'closet':
				if not ('deviceObject0' in kwargs and 'deviceObject1' in kwargs):
					raise ValueError('Need to specify the deviceObject')
				if getType('') == getType(kwargs['deviceObject0']):
					deviceObject0 = findObject(kwargs['deviceObject0'])
					deviceObject1 = findObject(kwargs['deviceObject1'])
				else:
					deviceObject0 = kwargs['deviceObject0']
					deviceObject1 = kwargs['deviceObject1']
				self.util.connectOnCloset(deviceObject0, deviceObject1,
										  cableType, port1, port2)
		else:
			self.util.connect(self.x, self.y, otherDevice.x, otherDevice.y, cableType, port1, port2)

	def create(self, *args):
		#Though the PC/Router/Other misc devices share the same API they are in different device selection windows
		if '.'.join(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC.split('.')[:-1]) in self.model:
			self.deviceType = ComponentBoxConst.DeviceType.MISCELLANEOUS
		if len(args) > 0:
			if args[0] == 'physical':
				if len(args) > 1:
					raise ValueError('This function takes a maximum of one argument')
					#self.util.createDeviceOnPhysical(self.deviceType, self.model, self.x, self.y, args[1])
				else:
					#self.util.createDeviceOnPhysical(self.deviceType, self.model, self.x, self.y)
					self.util.createDevice(self.deviceType, self.model, self.x, self.y)
			elif args[0] == 'closet':
				self.util.createDeviceOnClosetWorkspace(self.deviceType, self.model, self.x, self.y)
		else:
			self.util.createDevice(self.deviceType, self.model, self.x, self.y)

	def delete(self):
		CommonToolsBar().deleteItem(self.x, self.y)
	
	def select(self, *args):
		if len(args) > 0:
			if args[0] == 'physical':
				self.util.clickOnPhysicalWorkspace(self.x, self.y)
		else:
			self.util.clickOnWorkspace(self.x, self.y)
		self.updateName()
	
	def close(self):
		Util().close(self.squishName)

class SquishObjectName(Object):
	def __init__(self):
		None
	
	def objName(self, obj):
		if obj.startswith(':'):
			return obj
		else:
			return self.squishName + obj