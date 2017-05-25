####################################################
#@author: Chris Allen, Lesley Tse
####################################################
from API.Android.Device.AppsBase import APPortSetup
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.Utility.Util import Util

class Apps(DeviceBase):
    def __init__(self):
        self.portSetup = APPortSetup()
        self.util = Util()