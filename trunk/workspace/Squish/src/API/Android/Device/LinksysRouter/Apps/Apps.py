####################################################
#@author: Chris Allen, Lesley Tse
####################################################
from API.Android.Device.AppsBase import (BasicSetup, MacFilter, WirelessManagement, WirelessSecurity, WirelessSetting, WirelessStatus, LinksysAppButtons, PortForwarding)
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.Utility.Util import Util

class Apps(DeviceBase):
    def __init__(self):
        self.basicSetup = BasicSetup()
        self.macFilter = MacFilter()
        self.wirelessMgmt = WirelessManagement()
        self.wirelessSecurity = WirelessSecurity()
        self.wirelessSetting = WirelessSetting()
        self.wirelessStatus = WirelessStatus()
        self.appButtons = LinksysAppButtons()
        self.portForwarding = PortForwarding()
        self.util = Util()