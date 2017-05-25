##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.Device.DeviceBase.PhoneGuiBase.Gui import Gui
from API.ComponentBox import ComponentBoxConst

class AnalogPhone(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.END_DEVICE
        super(AnalogPhone, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.physical = Physical(self)
        self.config = Config(self)
        self.gui = Gui(self)
        
    def updateName(self):
        self.squishName = self.util.getCurrentDeviceName(self.displayName)
        super(AnalogPhone, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        self.gui.updateName(self.squishName)