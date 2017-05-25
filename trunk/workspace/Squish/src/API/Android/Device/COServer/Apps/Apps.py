####################################################
#@author: Chris Allen, Lesley Tse
####################################################
from API.Android.Device.AppsBase import BackboneSetup, COServerDHCP, COServerAppButtons
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.Utility.Util import Util

class Apps(DeviceBase):
    def __init__(self):
        self.Backbone = BackboneSetup()
        self.Dhcp = COServerDHCP()
        self.appButtons = COServerAppButtons()
        self.util = Util()