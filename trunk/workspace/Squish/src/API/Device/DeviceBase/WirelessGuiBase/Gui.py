##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase 
from API.Device.DeviceBase.WirelessGuiBase.AccessRestrictions import AccessRestrictions
from API.Device.DeviceBase.WirelessGuiBase.Administration import Administration
from API.Device.DeviceBase.WirelessGuiBase.ApplicationsAndGaming import ApplicationsAndGaming
from API.Device.DeviceBase.WirelessGuiBase.Security import Security
from API.Device.DeviceBase.WirelessGuiBase.Setup import Setup
from API.Device.DeviceBase.WirelessGuiBase.Status import Status
from API.Device.DeviceBase.WirelessGuiBase.Tabs import Tabs
from API.Device.DeviceBase.WirelessGuiBase.Wireless import Wireless
    
class GuiBase(DeviceBase):
    def __init__(self, parent, isRouter=True):
        self.squishName = parent.squishName
        self.isRouter = isRouter
        self.accessRestrictions = AccessRestrictions(self)
        self.administration = Administration(self)
        self.applicationsAndGaming = ApplicationsAndGaming(self)
        self.security = Security(self)
        self.setup = Setup(self)
        self.status = Status(self)
        self.tabs = Tabs(self)
        self.wireless = Wireless(self)
        
    
    #@summary: update the actual name of object that squish uses to reference
    #@param p_squishName: display name of the device        
    def updateName(self, squishName):
        self.squishName = squishName
        self.accessRestrictions.updateName(squishName)
        self.administration.updateName(squishName)
        self.applicationsAndGaming.updateName(squishName)
        self.security.updateName(squishName)
        self.setup.updateName(squishName)
        self.status.updateName(squishName)
        self.tabs.updateName(squishName)
        self.wireless.updateName(squishName)
        
            
