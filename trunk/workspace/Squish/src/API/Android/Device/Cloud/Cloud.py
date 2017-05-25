#**************************************************************************
#@author: Lesley Tse
#@summary: Cloud has the functions for the Cloud devices
#**************************************************************************

#from API.Android.Device.Cloud.Apps.Apps import Apps
#Need to create the Apps file
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu
from API.Android.Utility.Util import Util
from API.Android.Device.DeviceBase import DeviceMenuBase

class Cloud(DeviceBase):
    #@summary: set the x, y coordination, device model and device display name
    #to the object
    def __init__(self, p_model, p_x, p_y, p_displayName):
        #self.apps = Apps()
        #Can be uncommented once apps file is created
        self.util = Util()
        self.x = p_x
        self.y = p_y
        self.ip_add = ""
        self.ipv6_add = ""
        self.mac_add = ""
        self.model = p_model
        self.deviceType = MainContextMenu.CLOUD
        self.displayName = p_displayName
        self.squishName = self.displayName
        self.menu = DeviceMenuBase()

    
    #@summary: Added in so the user can just call deviceName.create() in order to create the device
    def create(self):
        self.util.createDevice(self.deviceType, self.model, self.x, self.y)
        
    def select(self):
        self.util.tapOnWorkspace(self.x, self.y)