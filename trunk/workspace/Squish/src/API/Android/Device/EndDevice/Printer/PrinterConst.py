##########################################################
#@author: Chris Allen
#@summary: holds object names used in Printer
##########################################################
from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class AppsConst(AppsBaseConst.AppButtonsConst):
	def __init__(self):
		pass
	
	class IPConfig(AppsBaseConst.IPconfigConst):
		pass
	
	class IPv6Config(AppsBaseConst.IPv6ConfigConst):
		pass
	
	class PCWireless(AppsBaseConst.PcWirelessConst):
		pass

class Physical(DeviceBaseConst.Physical):
    POWER = ''
    CURRENT_MODULE = ''
    MODULE_SLOT = ''
    LINKSYS_WMP300N = ''
    PT_HOST_NM_1CE = ''
    PT_HOST_NM_1CFE = ''
    PT_HOST_NM_1CGE = ''
    PT_HOST_NM_1FFE = ''
    PT_HOST_NM_1FGE = ''
    PT_HOST_NM_1W = ''
    PT_HOST_NM_1W_A = ''
    
class PrinterConst:
	Apps = AppsConst
	ContextMenu = DeviceBaseConst.EndDeviceMenus
	None