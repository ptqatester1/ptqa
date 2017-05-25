######################
##Author: AbbasH
######################
from API.Android.Device.AppsBase import (IPConfiguration, IPv6Configuration, Wireless)
from API.Android.Device.DeviceBase import DeviceBase

class Apps(DeviceBase):
    def __init__(self):
        self.ipConfig = IPConfiguration()
		self.ipv6Config = IPv6Configuration()
        self.wireless = Wireless()