##########################################################
#@author: Chris Allen
#@summary: holds object names used in PC
##########################################################
from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class Physical(DeviceBaseConst.Physical):
    POWER = ''
    CURRENT_MODULE = ''
    MODULE_SLOT = ''
    LINKSYS_WMP300N = ''
    PT_CAMERA = ''
    PT_HEADPHONE = ''
    PT_HOST_NM_1AM = ''
    PT_LAPTOP_NM_1AM = ''
    PT_HOST_NM_1CE = ''
    PT_HOST_NM_1CFE = ''
    PT_HOST_NM_1CGE = ''
    PT_HOST_NM_1FFE = ''
    PT_HOST_NM_1FGE = ''
    PT_LAPTOP_NM_1FGE = ''
    PT_LAPTOP_NM_3G4G = ''
    PT_HOST_NM_1W = ''
    PT_HOST_NM_1W_A = ''
    PT_MICROPHONE = ''
    PT_USB_HARD_DRIVE = ''
  
class AppsConst(AppsBaseConst.AppButtonsConst):
    def __init__(self):
        pass
    
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
  
class Menu(AppsBaseConst.Menu):
    pass

class PCConst:
    Apps = AppsConst
    ContextMenu = DeviceBaseConst.EndDeviceMenus
    None
