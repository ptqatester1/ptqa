#############################################################
#@author: Lesley Tse                                        # 
#@summary: LinkSysRouterConst holds object names for the Linksys Router#
#############################################################

from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class LinksysRouterConst:
	def __init__(self):
		self.ContextMenu = DeviceBaseConst.EndDeviceMenus
		self.Apps = Apps()

class Physical:
	pass
	
class Apps(AppsBaseConst.WirelessAppButtonsConst):
	class BasicSetup(AppsBaseConst.Basic_SetupConst):
		pass
		
	class WirelessSetting(AppsBaseConst.Wireless_SettingConst):
		pass
	
	class WirelessSecurity(AppsBaseConst.Wireless_SecurityConst):
		pass
	
	class WirelessStatus(AppsBaseConst.Wireless_StatusConst):
		pass
	
	class MacFilter(AppsBaseConst.MAC_Address_FilterConst):
		pass
		
	class WirelessMgmt(AppsBaseConst.Wireless_Admin_MgmtConst):
		pass
	
	