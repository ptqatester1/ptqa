#**************************************************************************
#@author: Thi Nguyen
#@summary: PC hold instances of config, physical, and desktop object 
#**************************************************************************
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config
from API.Device.DeviceBase.DesktopBase.DesktopBase import Desktop
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.Device.DeviceBase.WirelessGuiBase.PcGui import Gui
from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.ComponentBox import ComponentBoxConst

class PC(DeviceBase):
    #@summary: set the x, y coordination, device model and device display name
    #to the object
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.END_DEVICE
        super(PC, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)    
        self.desktop = Desktop(self)
        self.gui = Gui(self)
    
    #@summary: this is called to update the actual name of device that 
    #squish uses to reference.    
    def updateName(self):
        super(PC, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        self.desktop.updateName(self.squishName)
        self.gui.updateName(self.squishName)
