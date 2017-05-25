#######################################################
#@author: Chris Allen                                 #
#@summary: This holds common functions for the server #
#######################################################
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.Device.EndDevice.Server.Apps.Apps import Apps
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu
from API.Android.Utility.Util import Util
from API.Android.Device.DeviceBase import DeviceBase, EndDeviceMenuBase
from API.Android.Workspace.WorkspaceConst import NavigationBarConst
from squish import *

class Server(DeviceBase):

    
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
            self.util.hideCLIKeyboard()()
        except:
            pass
        self.util.tap(NavigationBarConst.APPS_BUTTON)
        
    def doubleTapSelect(self):
        self.util.doubleTapOnWorkspace(self.x, self.y)
        
    #All goTo functions are intended to be called from the desktop
    def goToAppsView(self):
        self.doubleTapSelect()
        snooze(1)
        
    def goToCMD(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.commandPromptButton()
        
    def goToIpConfig(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.ipConfigurationButton()
        
    def goToIpv6Config(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.ipv6ConfigurationButton()

    def goToHttp(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.httpButton()
        
    def goToFtp(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.ftpButton()
        
    def goToEmailService(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.emailServiceButton()