#*****************************************
#@author: Lesley Tse
#@summary: File handles the PT Icon button
#*****************************************

from API.Android.SquishSyntax import SquishSyntax
from API.Android.ActionBar.ActionBarConst import ActionBarConst
from API.Android.ActionBar.File.FileConst import FileMenuConst
import object
from squish import *

class OverFlow(SquishSyntax):
    #@summary: Selects the ptIcon to show the file dropDown menu
    def selectOverFlow(self):
        self.tap(ActionBarConst.OVERFLOW_BUTTON)
    
    #@summary: This would be used to select an Item from the file menu
    #@param p_item: This would be an item in the file menu such as FileMenuConst.NEW
    def selectOverFlowItem(self, p_item):
        self.selectOverFlow()
        snooze(1)
        self.tap(waitForObject(p_item))