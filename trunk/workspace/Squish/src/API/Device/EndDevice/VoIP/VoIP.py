##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst
from API.Utility.Util import Util

def err(msg = ''):
    raise NotImplementedError(msg)

class Settings(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updatename(self, squishName):
        self.squishName = squishName
    
    def displayName(self, name):
        Util().setText(self.objName(ConfigConst.settings.DISPLAY_NAME_EDIT), name)
        
    def serverAddress(self, serverAddress):
        Util().setText(self.objName(ConfigConst.settings.SERVER_ADDRESS), serverAddress)


class VoIP(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.END_DEVICE
        super(VoIP, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)
        
    def updateName(self):
        self.squishName = self.util.getCurrentDeviceName(self.displayName)
        super(VoIP, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        
