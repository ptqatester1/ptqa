#**************************************************************************
#@author: Lesley Tse
#@summary: Access point holds instances of menu objects 
#**************************************************************************
from API.Android.Device.COServer.Apps.Apps import Apps
from API.Android.Device.DeviceBase import DeviceBase, DeviceMenuBase
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu
from API.Android.Utility.Util import Util
from squish import *

class COServer(DeviceBase):
    #@summary: set the x, y coordination, device model and device display name
    #to the object
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.util = Util()
        self.x = p_x
        self.y = p_y
        self.ip_add = ""
        self.ipv6_add = ""
        self.mac_add = ""
        self.apps = Apps()
        self.model = p_model
        self.deviceType = MainContextMenu.WIRELESS
        self.menu = DeviceMenuBase()
        self.displayName = p_displayName
        self.squishName = self.displayName
    
    #@summary: Added in so the user can just call deviceName.create() in order to create the device
    def create(self):
        self.util.createDevice(self.deviceType, self.model, self.x, self.y)
        
    def select(self):
        self.util.tapOnWorkspace(self.x, self.y)

    def doubleTapSelect(self):
        self.util.doubleTapOnWorkspace(self.x, self.y)
    
    def goToAppsView(self):
        self.doubleTapSelect()
        snooze(1)