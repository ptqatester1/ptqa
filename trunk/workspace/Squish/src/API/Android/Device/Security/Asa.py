#######################################################
##Author: AbbasH
#@summary: Asa holds instances of cli and menu objects
#######################################################
#from API.Android.Device.Asa.Cli import Cli
#Need to make Cli.py
#from API.Android.Device.Asa.Menu import Menu
#Need to make Menu.py
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.ContextMenus.ContextMenusConst import MainContextMenu
from API.Android.Device.DeviceBase import CliDeviceMenuBase
from API.Android.Utility.Util import Util

class Asa(DeviceBase):
    #cli = Cli()
    #Can uncomment after making Cli.py
    #menu = CliDeviceMenuBase()
    #Can uncomment after making Menu.py
    #@summary: set the x, y coordination, device model and device display name
    #to the object
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.util = Util()
        self.x = p_x
        self.y = p_y
        self.ip_add = ""
        self.ipv6_add = ""
        self.mac_add = ""
        self.model = p_model
        self.deviceType = MainContextMenu.SECURITY
        self.displayName = p_displayName
        self.squishName = ":" + p_displayName

    #@summary: set the display name of the device
    #@param p_displayName: display name
    def setDisplayName(self, p_displayName):
        self.displayName = p_displayName
        
    #@summary: this is called to update the actual name of device that 
    #squish uses to reference.
    def updateName(self):
        self.squishName = self.util.getCurrentDeviceName(self.displayName)
        super(Asa, self).updateName(self.squishName)
        self.cli.updateName(self.squishName)
    
    #@summary: Added in so the user can just call deviceName.create() in order to create the device
    def create(self):
        self.util.createDevice(self.deviceType, self.model, self.x, self.y)
        
    def select(self):
        self.util.tapOnWorkspace(self.x, self.y)
    
    def goToConsole(self):
        self.select()
        self.menu.selectCli()