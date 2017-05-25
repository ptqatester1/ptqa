####################################################
#@author: Chris Allen
####################################################
from API.Android.Device.AppsBase import (AaaAccounting, CommandPrompt, Dhcp, Dhcpv6, Dns, EmailServer, Ftp, Http,
                                         IPConfiguration, IpFirewall, IPv6Configuration, Ipv6Firewall,
                                         Netflow, Ntp, PCWireless, PPPoE_Dialer, Terminal, Tftp, VPN, WebBrowser, EmailServer,
    EmailClient, Syslog)
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.Device.AppsBase import AppButtons
from API.Android.Utility.Util import Util

util = Util()

class Apps(DeviceBase):
    def __init__(self):
        self.appButtons = AppButtons()  
        self.aaaAcounting = AaaAccounting()
        self.commandPrompt = CommandPrompt()
        self.dhcp = Dhcp()
        self.dhcpv6 = Dhcpv6()
        self.dns = Dns()
        self.email = EmailClient()
        self.ftp = Ftp()
        self.http = Http()
        self.ipConfig = IPConfiguration()
        self.ipFirewall = IpFirewall()
        self.ipv6Config = IPv6Configuration()
        self.ipv6Firewall = Ipv6Firewall()
        self.netflow = Netflow()
        self.ntp = Ntp()
        self.ppoe = PPPoE_Dialer()
        self.syslog = Syslog()
        self.terminal = Terminal()
        self.tftp = Tftp()
        self.vpn = VPN()
        self.webbrowser = WebBrowser()
        self.pcWireless= PCWireless()
        self.emailServer = EmailServer()
        self.util = util