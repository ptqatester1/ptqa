##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.EndDevice.TV.TVConst import TVConst
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName

class PhysicalCheck(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def on(self, checked=True):
        Util().isChecked(self.objName(TVConst.physical.ON), checked)
    
    def off(self, checked=True):
        Util().isChecked(self.objName(TVConst.physical.OFF), checked)
    

class Physical(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.check = PhysicalCheck(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
        self.check.updateName(squishName)
        
    def on(self):
        Util().clickButton(self.objName(TVConst.physical.ON))
    
    def off(self):
        Util().clickButton(self.objName(TVConst.physical.OFF))
        
class TV(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.END_DEVICE
        super(TV, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.physical = Physical(self)
        
    def updateName(self):
        super(TV, self).updateName()
        self.physical.updateName(self.squishName)