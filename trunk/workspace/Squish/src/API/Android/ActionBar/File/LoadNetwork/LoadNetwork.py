#**************************************************************************************************
#@author:Lesley Tse
#@summary: LoadNetwork handles loading a network
#**************************************************************************************************
from API.Android.SquishSyntax import SquishSyntax
from API.Android.ActionBar.File.FileConst import FileMenuConst
from API.Android.ActionBar.File.File import File
from API.Android.ActionBar.ActionBarConst import ActionBarConst
from API.Android.ActionBar.File.LoadNetwork.LoadNetworkConst import LoadNetworkConst
from API.Android.Utility.functions import functions
from squish import *
import object

class LoadNetwork(SquishSyntax):
	def __init__(self):
		self.filemenu = File()
		
	def selectLoadNetwork(self):
		self.filemenu.selectFileItem(FileMenuConst.LOAD)

	def selectSaveNetwork(self):
		self.filemenu.selectFileItem(FileMenuConst.SAVE)		
	
	def selectSaveAs(self):
		self.filemenu.selectFileItem(FileMenuConst.SAVE_AS)
	
	def selectExit(self):
		self.filemenu.selectFileItem(FileMenuConst.EXIT)
	
	#@summary: Used to change the Files dropdown from local to saves
	#@param p_location: File location
	def fileLocation(self):
		self.tap(LoadNetworkConst.FILE_LOCATION)
		
		
	def selectFileLocation(self, p_location):
		self.fileLocation()
		if p_location.lower() == 'saves':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_SAVE))
			#self.tap(waitForObject(LoadNetworkConst.DONE_BUTTON))
		elif p_location.lower() == 'local':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_LOCAL))
			#self.tap(waitForObject(LoadNetworkConst.DONE_BUTTON))
		elif p_location.lower() == 'netspace':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_NETSPACE))
			#self.tap(waitForObject(LoadNetworkConst.DONE_BUTTON))
		elif p_location.lower() == 'box':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_BOX))
			#self.tap(waitForObject(LoadNetworkConst.DONE_BUTTON))
		elif p_location.lower() == 'dropbox':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_DROPBOX))
			#self.tap(waitForObject(LoadNetworkConst.DONE_BUTTON))
		else:
			self.tap(waitForObject(p_location))
			#self.tap(waitForObject(LoadNetworkConst.DONE_BUTTON))
   		
	def saveFileLocation(self):
		self.tap(LoadNetworkConst.SAVE_FILE_LOCATION)

	def selectSaveFileLocation(self, p_location):
		self.saveFileLocation()
		if p_location.lower() == 'saves':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_SAVE))
		elif p_location.lower() == 'local':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_LOCAL))
		elif p_location.lower() == 'netspace':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_NETSPACE))
		elif p_location.lower() == 'dropbox':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_DROPBOX))
		elif p_location.lower() == 'box':
			self.tap(waitForObject(LoadNetworkConst.FILE_LOCATION_BOX))
		else:
			self.tap(waitForObject(p_location))
	
	#@summary: Selects a file from the file list
	def selectFileFromList(self, p_fileName):
		self.openFileNameEdit(p_fileName)
		snooze(10)
		self.tap_x_y(functions().findTag(':lstFiles_HTML_Object', 'DIV', p_fileName), 128, 8)
		#try:
		#	self.tap_x_y(waitForObject(':' + p_fileName + '_HTML_Object'), 123, 8)
		#except:
		#	try:
		#		self.tap_x_y(waitForObject(':' + p_fileName + '_HTML_Object_2'), 123, 8)
		#	except:
		#		raise Exception('Unable to find file object')
			
	#@summary: To enter a value in the search field
	def openFileNameEdit(self, p_fileName):
		from API.Android.Utility.Util import Util
		util = Util()
		util.setSearchText(LoadNetworkConst.SEARCH_FILE, p_fileName)

	#@summary: To enter a value in the file name field
	def saveFileNameEdit(self, p_fileName):
		from API.Android.Utility.Util import Util
		util = Util()
		util.setText(LoadNetworkConst.SAVE_FILE_NAME, p_fileName)
	
	#@summary: Opens the file
	def openFile(self, p_fileName, p_location = ''):
		self.selectLoadNetwork()
		if p_location:
			self.selectFileLocation(p_location)
		#Box and Dropox adds a / in front of the filename, which is causing trouble opening from box/dropbox
		#if p_location == 'box':
		#	self.selectFileFromList('/' + p_fileName)
		#elif p_location == 'dropbox':
		#	self.tap(waitForObject(LoadNetworkConst.SEARCH_FILE))
		#	self.typeText(LoadNetworkConst.SEARCH_FILE, p_fileName)
		#	self.tap(waitForObject(":/" + p_fileName + "_HTML_Object"))
		#else:
		#	self.selectFileFromList(p_fileName)
		self.selectFileFromList(p_fileName)
		snooze(5)
		self.tap(LoadNetworkConst.OPEN_BUTTON)

	#@summary: Cancels/exits Load Network window
	def cancelOpenFile(self):
		self.tap(LoadNetworkConst.CANCEL_BUTTON)

	#@summary: Save New file
	def saveNewFile(self, p_fileName, p_location = ''):
		self.selectSaveNetwork()
		if p_location:
			self.selectFileLocation(p_location)
		self.saveFileNameEdit('')
		self.saveFileNameEdit(p_fileName)
		self.tap(LoadNetworkConst.SAVE_BUTTON)
		
	#@summary: Saves the file as another file 
	def saveAsFile(self,p_fileName, p_location = ''):
		self.selectSaveAs()
		if p_location:
			self.selectSaveFileLocation(p_location)
		if p_fileName:
			self.saveFileNameEdit('')
			self.saveFileNameEdit(p_fileName)
		self.tap(LoadNetworkConst.SAVE_BUTTON)
	
	def exitPT(self):
		self.selectExit()
		#no object name for yes/no buttons and their parents. to be edited later
		