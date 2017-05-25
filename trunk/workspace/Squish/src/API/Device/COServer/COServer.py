##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.COServer.CentralOfficeServerConfig import Config
from API.Device.COServer.CentralOfficeServerServices import Services
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.ComponentBox import ComponentBoxConst

class COServer(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.WIRELESS_DEVICE
        super(COServer, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)
        self.services = Services(self)
        
    def updateName(self):
        self.squishName = self.util.getCurrentDeviceName(self.displayName)
        super(COServer, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        self.services.updateName(self.squishName)