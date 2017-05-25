######################
##Author: AbbasH
######################
from API.Android.Device.AppsBase import (IPConfiguration, IPv6Configuration, Wireless,
										 WebBrowser, Terminal, CommandPrompt, IpFirewall,
										 Ipv6Firewall, VPN, EmailClient, PPPoE_Dialer)
from API.Android.Device.DeviceBase import DeviceBase

class Apps(DeviceBase):
    def __init__(self):
		self.squishName = ""

