#**************************************************************************************************
#@author:Lesley Tse
#@summary: Exit handles closing PacketTracer
#**************************************************************************************************

from API.Android.SquishSyntax import SquishSyntax
from API.Android.ActionBar.File.FileConst import FileMenuConst
from API.Android.ActionBar.File.File import File
from API.Android.ActionBar.ActionBarConst import ActionBarConst
from API.Android.ActionBar.File.Exit.ExitConst import ExitConst

fileMenu = File()

class Exit(SquishSyntax):
	def selectExit(self):
		fileMenu.selectFileItem(FileMenuConst.EXIT)
	def exitYes(self):
		self.selectExit()
		self.tap(ExitConst.EXIT_YES)
	def exitNo(self):
		self.selectExit()
		self.tap(ExitConst.EXIT_NO)
		