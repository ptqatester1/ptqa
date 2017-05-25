#######################################################
#@author: Chris Allen                                 #
#@summary: This holds common functions for the server #
#######################################################
from API.Android.Device.DeviceBase import DeviceBase, EndDeviceMenuBase
from API.Android.Device.EndDevice.Server.Apps.Apps import Apps
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu,\
    EndSubMenuConst
from API.Android.Utility.Util import Util
from API.Android.Workspace.WorkspaceConst import NavigationBarConst
from squish import *
from API.Android.Utility import UtilConst
from API.Android.AddPdu.AddPdu import ComplexPdu, SimplePdu

complexPdu = ComplexPdu()
simplePdu = SimplePdu()

class PC(DeviceBase):
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
    
    def doubleTapSelect(self):
        self.util.doubleTapOnWorkspace(self.x, self.y)
        
    def returnToApps(self):
        try:
            findObject(UtilConst.KeyboardConst.PT_KEYBOARD)
            self.util.hideCLIKeyboard()
        except:
            pass
        for i in range(5):
            try:
                waitForObject(NavigationBarConst.APPS_BUTTON)
            except:
                snooze(1)
        self.util.tap(NavigationBarConst.APPS_BUTTON)
        
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
        
    def goToTextEditor(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.textEditorButton()
        
    def goToTerminal(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.terminalButton()
        
    def goToWebBrowser(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.webBrowserButton()
        
    def goToEmail(self):
        self.goToAppsView()
        snooze(1)
        self.apps.appButtons.emailButton()
    
    #Add a simple pdu
    #p_device2 is the device the PDU will be sent to
    #the pdu will be sent from the calling device
    def addPdu(self, p_device2):
        simplePdu.addSimplePdu(self, p_device2)
    
    def addComplexPdu(self, p_application = None, p_destinationIp = None, p_sourceIp = None, p_tos = None, p_ttl = None, p_sequenceNumber = None,
                    p_size = None, p_oneShot = True, p_seconds = None, p_sourcePort = None, p_destinationPort = None, p_portName = 'Auto'):
        complexPdu.addComplexPdu(self, p_application, p_destinationIp, p_sourceIp, p_tos, p_ttl, p_sequenceNumber, p_size, p_oneShot, p_seconds, p_sourcePort, p_destinationPort, p_portName)