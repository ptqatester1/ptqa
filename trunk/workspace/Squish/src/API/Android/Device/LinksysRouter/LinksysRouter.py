#**************************************************************************
#@author: Lesley Tse
#@summary: LinksysRouter has the functions for the wireless router
#**************************************************************************


from API.Android.Device.DeviceBase import DeviceBase, EndDeviceMenuBase,\
    CliDeviceMenuBase
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu
from API.Android.Utility.Util import Util
from API.Android.Device.LinksysRouter.Apps.Apps import Apps
from API.Android.Workspace.WorkspaceConst import NavigationBarConst
from squish import *

class LinksysRouter(DeviceBase):
    #@summary: set the x, y coordination, device model and device display name
    #to the object
    def __init__(self, p_model, p_x, p_y, p_displayName):
        #self.apps = Apps()
        #Can uncomment once apps.py is created
        self.util = Util()
        self.x = p_x
        self.y = p_y
        self.ip_add = ""
        self.ipv6_add = ""
        self.mac_add = ""
        self.model = p_model
        self.deviceType = MainContextMenu.WIRELESS
        self.displayName = p_displayName
        self.squishName = self.displayName
        self.apps = Apps()
        self.menu = EndDeviceMenuBase()
    
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
    
    def goToBasicSettings(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.basicSettingsButton()
        
    def goToPortForwarding(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.portForwardingButton()
        
    def returnToApps(self):
        self.util.tap(NavigationBarConst.APPS_BUTTON)