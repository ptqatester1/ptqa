#######################################################
#@author: Chris Allen                                 #
#@summary: This holds common functions for the server #
#######################################################
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.Device.EndDevice.Server.Apps.Apps import Apps
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu
from API.Android.Utility.Util import Util

class VoIP(DeviceBase):

    
    #@summary: Set the x,y coordinates, model, and display name
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.x = p_x
        self.y = p_y
        self.ip_add = ''
        self.ipv6_add = ''
        self.mac_add = ''
        self.model = p_model
        self.displayName = p_displayName
        self.deviceType = MainContextMenu.END_DEVICES
        self.apps = Apps()
        self.util = Util()
        self.squishName = self.displayName
        
    def create(self):
        self.util.createDevice(self.deviceType, self.model, self.x, self.y)
    
    def select(self):
        self.util.tapOnWorkspace(self.x, self.y)
        