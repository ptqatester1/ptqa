###############################################
##Author: AbbasH
#@summary: COServerConst holds object names
###############################################

from API.Android.Device.DeviceBase import DeviceBaseConst
from API.Android.Device import AppsBaseConst

class COServerConst:
	def __init__(self):
		self.ContextMenu = DeviceBaseConst.ContextMenu
		self.Apps = Apps

class Physical(DeviceBaseConst.Physical):
    POWER = ''

class Apps(AppsBaseConst.AppButtonsConst):
	pass