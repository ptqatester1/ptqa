##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.ComponentBox import ComponentBoxConst

class Printer(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.END_DEVICE
        super(Printer, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)
        
    def updateName(self):
        super(Printer, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
