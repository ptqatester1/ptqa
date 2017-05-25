from API.Utility import UtilConst
from API.SquishSyntax import SquishSyntax
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from squish import *
import object

class Physical:
	def __init__(self):
		self.sq = SquishSyntax()
	
	@property
	def workspace(self):
		'''return the physical workspace object'''
		return findObject(UtilConst.PHYSICAL_WORKSPACE)
	
	@property
	def currentLocation(self):
		'''locationObjects = [GoldenPhysicalToolbarConst.GO_TO_INTERCITY,
						   GoldenPhysicalToolbarConst.GO_TO_CITY,
						   GoldenPhysicalToolbarConst.GO_TO_BUILDING,
						   GoldenPhysicalToolbarConst.GO_TO_CLOSET]
		locationList = []
		for location in locationObjects:
			obj = findObject(location)
			if obj.visible:
				if not 'Back' in str(obj.text):
					locationList.append(str(obj.text))
		name = locationList[0]
		if name.startswith(' '):
			name = name[1:]
		return name'''
		return str(findObject(GoldenPhysicalToolbarConst.CURRENT_LOCATION).text)
	
	@property
	def currentLocationButton(self):
		return findObject(GoldenPhysicalToolbarConst.CURRENT_LOCATION)
	@property
	def backButton(self):
		locationObjects = [GoldenPhysicalToolbarConst.GO_TO_INTERCITY,
						   GoldenPhysicalToolbarConst.GO_TO_CITY,
						   GoldenPhysicalToolbarConst.GO_TO_BUILDING,
						   GoldenPhysicalToolbarConst.GO_TO_CLOSET]
		locationList = []
		for location in locationObjects:
			obj = findObject(location)
			if obj.visible:
				if 'Back' in str(obj.text):
					locationList.append(obj)
		if not locationList:
			raise AssertionError('The back button is not present in Intercity')
		return locationList[0]
	
	def getObject(self, p_name, **kwargs):
		'''Return an object related to a device or container name or False if not found'''
		returnList = False
		if 'returnList' in kwargs:
			returnList = kwargs['returnList']
		foundItems = []
		workspaceItems = object.children(self.workspace)
		for item in workspaceItems:
			itemChildren = object.children(item)
			if itemChildren:
				for child in itemChildren:
					properties = object.properties(child)
					if 'text' in properties:
						if child.text == p_name:
							foundItems.append(object.parent(child))
		if returnList:
			return foundItems or False
		if foundItems:
			return foundItems[0]
		else:
			return False
	
	def scrollHorizontal(self, val):
		scrollbar = findObject(UtilConst.PHYSICAL_WORKSPACE_HORIZONTAL_SCROLLBAR)
		scrollbar.setValue(val)
	
	def scrollVertical(self, val):
		scrollbar = findObject(UtilConst.PHYSICAL_WORKSPACE_VERTICAL_SCROLLBAR)
		scrollbar.setValue(val)
	
	def copyObject(self, p_name):
		self.getObject(p_name).setSelected(True)
		MainToolbar().copyButton()
	
	def pasteObject(self):
		MainToolbar().pasteButton()
	
	def moveObject(self, obj, *destinationPathList):
		'''obj is the squish object that relates to the object to be moved
		destinationPathList is the path to the destination.
		Example:
			moveObject(routerObj, 'Home City', 'Corporate Office', 'Move to Corporate Office')
		'''
		self.sq.clickButton(GoldenPhysicalToolbarConst.MOVE_OBJECT)
		self.sq.click(obj)
		dropdown = GoldenPhysicalToolbarConst.MOVE_DROPDOWN
		for location in destinationPathList:
			snooze(1)
			self.sq.activateItem(dropdown, location)    
			dropdown = dropdown + "." + location
		if not 'Move to ' in destinationPathList[-1]:
			self.sq.activateItem(dropdown, "Move to " + destinationPathList[-1]) 

	def move(self, containerName, *destinationPathList, **kwargs):
		index = 0
		if 'index' in kwargs:
			index = kwargs['index']
		containerObject = self.getObject(containerName, returnList=True)[index]
		self.moveObject(containerObject, *destinationPathList)
	
	def goTo(self, *p_locations):
		'''Select a location to go to by name
		Example:
			goTo('Home City', 'Corporate Office', 'Main Wiring Closet')'''
		for location in p_locations:
			self.sq.click(self.getObject(location, returnList=True)[0])
	
	def goBack(self, destinationLoaction):
		if (not destinationLoaction in str(self.currentLocation) and
			not 'Intercity' in str(self.currentLocation)):
			self.sq.click(self.backButton)
			self.goBack(destinationLoaction)

class Closet:
	def __init__(self):
		self.sq = SquishSyntax()
	
	@property
	def rackList(self):
		racks = []
		count = 1
		while object.exists(GoldenPhysicalToolbarConst.RACK_BASE + str(count)):
			rack = findObject(GoldenPhysicalToolbarConst.RACK_BASE + str(count))
			count += 1
			widgets = []
# 			for item in object.children(rack):
# 				if item.className() == 'QWidget':
# 					widgets.append(item)
# 			if len(widgets) <= 2:
			if len(object.children(rack)) <= 2:
				continue#This is a table device so don't append
			racks.append(rack)
		return racks

	@property
	def rackDict(self):
		racks = self.rackList
		d = {}
		for i, rack in enumerate(racks):
			d['rack%s'%(i+1)] = rack
		return d
	
	@property
	def tableList(self):
		tables = []
		count = 1
		while object.exists(GoldenPhysicalToolbarConst.RACK_BASE + str(count)):
			table = findObject(GoldenPhysicalToolbarConst.RACK_BASE + str(count))
			count += 1
			widgets = []
# 			for item in object.children(table):
# 				if item.className() == 'QWidget':
# 					widgets.append(item)
# 			if len(widgets) > 2:
			if len(object.children(table)) > 2:
				continue#This is a rack device so don't append
			tables.append(table)
		return tables

	@property
	def tableDict(self):
		tables = self.tableList
		d = {}
		for i, table in enumerate(tables):
			d['table%s'%(i+1)] = table
		return d
	
	@property
	def rackDeviceList(self):
		'''Return a list of lists
		The index of the list will be [rack - 1][device - 1]
		example: (get the first rack and first device)
			self.rackDeviceList[0][0]'''
		racks = self.rackList
		deviceList = []
		for rack in racks:
			devs = []
			for item in object.children(rack):
					if len(object.children(item)) > 1:
						devs.append(item)
			deviceList.append(devs)
		return deviceList
	
	@property
	def rackDeviceDict(self):
		'''Return a dict of dicts related to rack/device
		A more readable version of rackDeviceList
		example: (get the first rack and first device)
			self.rackDeviceDict['rack1']['dev1']'''
		devList = self.rackDeviceList
		d = {}
		for i, rack in enumerate(devList):
			devDict = {}
			for j, dev in enumerate(rack):
				devDict['dev%s'%(j+1)] = dev
			d.update({'rack%s'%(i+1):devDict})
		return d


	@property
	def tableDeviceList(self):
		'''Return a list of lists
		The index of the list will be [table - 1][device - 1]
		example: (get the first table and first device)
			self.tableDeviceList[0][0]'''
		#Structure is as follows
		#"Rack area"
		#---Table
		#---Device areas (1 for each device)
		#-------Device object
		tables = self.tableList
		deviceList = []
		for table in tables:
			deviceArea = object.children(table)[1]
			devs = []
			for widget in object.children(deviceArea):
				for item in object.children(widget):
					try:
						if item.className() == 'CModuleContainer':
							devs.append(item)
					except AttributeError, e:
						pass
			deviceList.append(devs)
		return deviceList
	
	@property
	def tableDeviceDict(self):
		'''Return a dict of dicts related to table/device
		A more readable version of tableDeviceList
		example: (get the first table and first device)
			self.tableDeviceDict['table1']['dev1']'''
		devList = self.tableDeviceList
		d = {}
		for i, table in enumerate(devList):
			devDict = {}
			for j, dev in enumerate(table):
				devDict['dev%s'%(j+1)] = dev
			d.update({'table%s'%(i+1):devDict})
		return d