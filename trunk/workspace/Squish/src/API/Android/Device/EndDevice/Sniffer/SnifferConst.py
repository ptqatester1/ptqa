##########################################################
##Author: AbbasH
#@summary: serverConst holds object names used in Server
##########################################################
from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class ServerConst:
	def __init__(self):
		self.ContextMenu = DeviceBaseConst.EndDeviceMenus
		self.Apps = Apps
		
class PhysicalConst(DeviceBaseConst.Physical):
    POWER = ''
    CURRENT_MODULE_TOP = ''
    MODULE_SLOT_TOP = ''
    MODULE_SLOT_BOTTOM = ''
    LINKSYS_WMP300N = ''
    PT_HOST_NM_1AM = ''
    PT_HOST_NM_1CE = ''
    PT_HOST_NM_1CFE = ''
    PT_HOST_NM_1CGE = ''
    PT_HOST_NM_1FFE = ''
    PT_HOST_NM_1FGE = ''
    PT_HOST_NM_1W = ''
    PT_HOST_NM_1W_A = ''

class Apps(AppsBaseConst.AppButtonsConst):
	class IPConfig(AppsBaseConst.IPconfigConst):
		pass
	
	class IPv6Config(AppsBaseConst.IPv6ConfigConst):
		pass
	
	class PCWireless(AppsBaseConst.PcWirelessConst):
		pass
	
	class WebBrowser(AppsBaseConst.WebBrowserConst):
		pass
	
	class Terminal(AppsBaseConst.TerminalConst):
		pass
	
	class CommandPrompt(AppsBaseConst.CommandPromptConst):
		pass
	
	class IPFirewall(AppsBaseConst.IPFirewallConst):
		pass
	
	class IPv6Firewall(AppsBaseConst.IPv6FirewallConst):
		pass
	
	class VPN(AppsBaseConst.VPNConst):
		pass
	
	class Email(AppsBaseConst.EmailConst):
		pass
	
	class PPPoE(AppsBaseConst.PPPoEConst):
		pass
	
	class Tftp(AppsBaseConst.TftpConst):
		pass
	
	class Ftp(AppsBaseConst.FtpConst):
		pass
	
	class Http(AppsBaseConst.HttpConst):
		pass
	
	class Dhcp(AppsBaseConst.DhcpConst):
		pass
	
	class Dns(AppsBaseConst.DnsConst):
		pass
	
	class Email(AppsBaseConst.EmailServerConst):
		pass
	
	class AaaAcounting(AppsBaseConst.AAA_AccountingConst):
		pass
	
	