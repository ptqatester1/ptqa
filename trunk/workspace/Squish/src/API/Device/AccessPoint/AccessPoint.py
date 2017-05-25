##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.DeviceBase.ConfigBase.ConfigItems.Interfaces import WiredInterface, ApWirelessInterface
from API.Device.DeviceBase.ConfigBase.ConfigBase import GlobalSettings
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config as ConfigBase
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.ComponentBox import ComponentBoxConst

class Interface:
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.port0 = WiredInterface(self)
        self.port1 = ApWirelessInterface(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
        self.port0.updateName(squishName)
        self.port1.updateName(squishName)

class Config(ConfigBase):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.settings = GlobalSettings(self)
        self.interface = Interface(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
        self.settings.updateName(squishName)
        self.interface.updateName(squishName)
        
class AccessPoint(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.WIRELESS_DEVICE
        super(AccessPoint, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)
        
    def updateName(self):
        super(AccessPoint, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
