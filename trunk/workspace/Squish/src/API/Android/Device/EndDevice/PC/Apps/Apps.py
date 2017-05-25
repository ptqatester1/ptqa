######################
##Author: AbbasH
######################
from API.Android.Device.AppsBase import (IPConfiguration, IPv6Configuration, PCWireless,
                                         WebBrowser, Terminal, CommandPrompt, IpFirewall,
                                         Ipv6Firewall, VPN, EmailClient, PPPoE_Dialer)
from API.Android.Device.DeviceBase import DeviceBase

class Apps(DeviceBase):
    def __init__(self):
        self.ipConfig = IPConfiguration()
        self.ipv6Config = IPv6Configuration()
        self.wireless = PCWireless()
        self.webbrowser = WebBrowser()
        self.terminal = Terminal()
        self.commandPrompt = CommandPrompt()
        self.ipFirewall = IpFirewall()
        self.ipv6Firewall = Ipv6Firewall()
        self.vpn = VPN()
        self.emailClient = EmailClient()
        self.ppoe = PPPoE_Dialer()

