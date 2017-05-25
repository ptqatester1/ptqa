##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase, SquishObjectName
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config as ConfigBase
from API.Device.DeviceBase.ConfigBase.ConfigItems.Interfaces import Lan, Internet, WirelessRouterInterface
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.Device.DeviceBase.HomeGatewayGuiBase.Gui import Gui
from API.ComponentBox import ComponentBoxConst

class Interface:
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.internet = Internet(self)
        self.lan = Lan(self)
        self.wireless = WirelessRouterInterface(self)
    
    def updateName(self, squishName):
        self.squishName = squishName
        self.internet.updateName(squishName)
        self.lan.updateName(squishName)
        self.wireless.updateName(squishName)
        
class Config(ConfigBase):
    def __init__(self, parent):
        self.squishName = parent.squishName
        super(Config, self).__init__(self)
        self.interface = Interface(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
        super(Config, self).updateName(squishName)
        self.interface.updateName(squishName)
        
class HomeGateway(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.WIRELESS_DEVICE
        super(HomeGateway, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)
        self.gui = Gui(self)
            
    def updateName(self):
        super(HomeGateway, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        self.gui.updateName(self.squishName)

