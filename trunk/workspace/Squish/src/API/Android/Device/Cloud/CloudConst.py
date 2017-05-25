#############################################################
#@author: Lesley Tse                                        # 
#@summary: CloudConst holds object names for Cloud devices	#
#############################################################

from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class CloudConst:
	def __init__(self):
		self.ContextMenu = DeviceBaseConst.EndDeviceMenus
		self.Apps = Apps

class Physical:
	pass

class Apps(AppsBaseConst.WirelessAppButtonsConst):
	class FrameRelayMapping(AppsBaseConst.FrameRelayConst):
		pass
		
	class DLCI_Config(AppsBaseConst.DLCI_Const):
		pass
	
	class WAN_Provider(AppsBaseConst.WAN_ProviderConst):
		pass