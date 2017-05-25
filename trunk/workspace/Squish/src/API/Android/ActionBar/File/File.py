#*****************************************
#@author: Lesley Tse
#@summary: File handles the PT Icon button
#*****************************************

from API.Android.SquishSyntax import SquishSyntax
from API.Android.ActionBar.ActionBarConst import ActionBarConst
from API.Android.ActionBar.File.FileConst import FileMenuConst
import object
from squish import *

class File(SquishSyntax):
    #@summary: Selects the ptIcon to show the file dropDown menu
    def selectPT_Icon(self):
        self.tap(ActionBarConst.PT_ICON)
    
    #@summary: This would be used to select an Item from the file menu
    #@param p_item: This would be an item in the file menu such as FileMenuConst.NEW
    def selectFileItem(self, p_item):
        item = None
        try:
            item = findObject(p_item)
        except LookupError, e:
            None
        except Exception, e:
            raise Exception(e)
        if not item:
            self.selectPT_Icon()
        self.tap(waitForObject(p_item))