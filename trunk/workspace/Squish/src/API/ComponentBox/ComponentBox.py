#**************************************************************************
#@author: Thi Nguyen
#@summary: ComponentBox handles the clicking on device type box and device
#specific box
#**************************************************************************
from API.ComponentBox import ComponentBoxConst
from API.SquishSyntax import SquishSyntax
from squish import *
import object
class ComponentBox(SquishSyntax):
    def __init__(self):
        super(ComponentBox, self).__init__()
        
    def searchDevices(self, p_searchText):
        searchLine = ComponentBoxConst.SEARCH_LINE_EDIT
        self.setText(searchLine, p_searchText)
    
    def getSearchBoxText(self):
        searchLine = ComponentBoxConst.SEARCH_LINE_EDIT
        return findObject(searchLine).text
    
    def networkGroup(self):
        self.clickButton(ComponentBoxConst.DeviceGroup.NETWORK_DEVICES)
    
    def endDeviceGroup(self):
        self.clickButton(ComponentBoxConst.DeviceGroup.END_DEVICES)
    
    def componentsGroup(self):
        self.clickButton(ComponentBoxConst.DeviceGroup.COMPONENTS)
    
    def connectionsGroup(self):
        self.clickButton(ComponentBoxConst.DeviceGroup.CONNECTIONS)
    
    def miscGroup(self):
        self.clickButton(ComponentBoxConst.DeviceGroup.MISCELLANEOUS)
    
    def multiuserGroup(self):
        self.clickButton(ComponentBoxConst.DeviceGroup.MULTIUSER)