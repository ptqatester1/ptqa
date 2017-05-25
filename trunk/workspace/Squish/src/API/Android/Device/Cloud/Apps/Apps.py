####################################################
#@author: Lesley Tse
####################################################
from API.Android.Device.AppsBase import (FrameRelayMapping, DLCI_Config, WAN_Provider)
from API.Android.Device.DeviceBase import DeviceBase

class Apps(DeviceBase):
    def __init__(self):
        self.frameRelay = FrameRelayMapping()
        self.dlciConfig = DLCI_Config()
        self.wanProvider = WAN_Provider()