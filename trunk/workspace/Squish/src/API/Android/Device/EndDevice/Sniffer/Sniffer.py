#######################################################
#@author: Chris Allen                                 #
#@summary: This holds common functions for the Sniffer #
#######################################################
from API.Android.Simulation.EventList.EventListConst import EventListConst, EventListFilterConst
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.Device.EndDevice.Sniffer.Apps.Apps import Apps
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu
from API.Android.Utility.Util import Util
from API.Android.Device.DeviceBase import DeviceBase, EndDeviceMenuBase
from API.Android.Workspace.WorkspaceConst import NavigationBarConst
from squish import *

class Sniffer(DeviceBase):
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
        self.menu = EndDeviceMenuBase()
        self.squishName = self.displayName
        
    def create(self):
        self.util.createDevice(self.deviceType, self.model, self.x, self.y)
    
    def select(self):
        self.util.tapOnWorkspace(self.x, self.y)
        
    def returnToApps(self):
        try:
            self.util.hideKeyboard()
        except:
            pass
        self.util.tap(NavigationBarConst.APPS_BUTTON)
        
    def doubleTapSelect(self):
        self.util.doubleTapOnWorkspace(self.x, self.y)

    def goToAppsView(self):
        self.doubleTapSelect()
        snooze(1)