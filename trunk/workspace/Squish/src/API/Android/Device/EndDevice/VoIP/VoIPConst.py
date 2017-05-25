#################################################
##Author: AbbasH
#@summary: holds object names used in VoIP
#################################################
from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class VoIPConst:
	def __init__(self):
		self.ContextMenu = DeviceBaseConst.EndDeivceMenus
		self.Apps = Apps

class Physical(DeviceBaseConst.Physical):
	pass


class Apps(AppsBaseConst.AppButtonsConst):
	pass