#################################################
##Author: AbbasH
#@summary: holds instances of menu objects
#################################################

from API.Android.Device.DeviceBase import DeviceBase
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu
from API.Android.Utility.Util import Util

class Repeator(DeviceBase):
    #@summary: set the x, y coordination, device model and device display name
    #to the object
    def __init__(self, p_model, p_x, p_y, p_displayName):
        pass
    
    #@summary: Added in so the user can just call deviceName.create() in order to create the device
    def create(self):
        self.util.createDevice(self.deviceType, self.model, self.x, self.y)
        
    def select(self):
        self.util.tapOnWorkspace(self.x, self.y)