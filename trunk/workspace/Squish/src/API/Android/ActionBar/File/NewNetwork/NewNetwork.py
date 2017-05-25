#****************************************
#@author: Lesley Tse
#@summary: NewNetwork handles creating new networks
#****************************************

from API.Android.SquishSyntax import SquishSyntax
from API.Android.ActionBar.File.FileConst import FileMenuConst
from API.Android.ActionBar.File.File import File
from API.Android.ActionBar.ActionBarConst import ActionBarConst

fileMenu = File()

class NewNetwork:
	def selectNewNetwork(self):
		fileMenu.selectFileItem(FileMenuConst.NEW)
		
		