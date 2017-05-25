##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.DeviceBase.ConfigBase.CiscoDeviceConfig import Config
from API.Device.DeviceBase.CliBase.CliBase import Cli
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.ComponentBox import ComponentBoxConst

class Router(DeviceBase):
    #@summary: set the x, y coordination, device model and device display name
    #to the object
    def __init__(self, model, x, y, displayName):
        self.deviceType = ComponentBoxConst.DeviceType.ROUTER
        super(Router, self).__init__(model, x, y, displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)
        self.cli = Cli(self)
        
    #@summary: this is called to update the actual name of device that 
    #squish uses to reference.
    def updateName(self):
        super(Router, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        self.cli.updateName(self.squishName)