#**************************************************************************
#@author: Thi Nguyen
#@summary: Server hold instances of config and physical object 
#**************************************************************************
from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.DeviceBase.ServicesBase.ServicesBase import Services
from API.Device.DeviceBase.DesktopBase.DesktopBase import Desktop
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config
from API.ComponentBox import ComponentBoxConst

class Server(DeviceBase):
    #@summary: set the x, y coordination, device model and device display name
    #to the object
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.END_DEVICE
        super(Server, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)    
        self.desktop = Desktop(self)
        self.services = Services(self)

    #@summary: this is called to update the actual name of device that 
    #squish uses to reference.    
    def updateName(self):
        super(Server, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        self.desktop.updateName(self.squishName)
        self.services.updateName(self.squishName)