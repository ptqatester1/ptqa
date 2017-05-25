##########################################################
#@author: Chris Allen
#@summary: holds object names used in IPPhone
##########################################################
from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class IPPhoneConst:
	def __init__(self):
		self.ContextMenu = DeviceBaseConst.EndDeivceMenus
		self.Apps = Apps

class Physical(DeviceBaseConst.Physical):
    POWER_ADAPTER = ''
    MODULE_SLOT = ''

class Apps(AppsBaseConst.AppButtonsConst):
	pass