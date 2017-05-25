#**************************************************************************************************
#@author:Lesley Tse
#@summary: SaveNetwork handles saving a network
#**************************************************************************************************

from API.Android.SquishSyntax import SquishSyntax
from API.Android.ActionBar.File.FileConst import FileMenuConst
from API.Android.ActionBar.File.File import File
from API.Android.ActionBar.ActionBarConst import ActionBarConst
from API.Android.ActionBar.File.SaveNetwork.SaveNetworkConst import SaveNetworkConst

fileMenu = File()

class SaveNetwork(SquishSyntax):
	def selectSaveNetwork(self):
		fileMenu.selectFileItem(FileMenuConst.SAVE)
	
	def editFileName(self, p_fileName):
		self.setText(SaveNetworkConst.FILE_NAME, p_fileName)
	
	def saveFile(self, p_fileName):
		self.selectSaveNetwork()
		self.editFileName(p_fileName)
		self.tap(SaveNetworkConst.SAVE_BUTTON)
		snooze(2)
		#self.tap(SaveNetworkConst.SAVE_TO_FILE_OK)
	
	def cancelSave(self):
		self.tap(SaveNetworkConst.CANCEL_BUTTON)
	

