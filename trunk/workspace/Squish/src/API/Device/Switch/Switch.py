##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.DeviceBase.ConfigBase.CiscoDeviceConfig import Config
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.Device.DeviceBase.CliBase.CliBase import Cli
from API.ComponentBox import ComponentBoxConst

class Switch(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.SWITCH
        super(Switch, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)
        self.cli = Cli(self)
        
    def updateName(self):
        super(Switch, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        self.cli.updateName(self.squishName)