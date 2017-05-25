###############################################
##Author: AbbasH
#@summary: AccessPointConst holds object names
###############################################

from API.Android.Device.DeviceBase import DeviceBaseConst
from API.Android.Device import AppsBaseConst

class AccessPoint:
	def __init__(self):
		self.ContextMenu = DeviceBaseConst.ContextMenu
		self.Apps = Apps

class Physical(DeviceBaseConst.Physical):
    POWER = ''
    CURRENT_MODULE = ''
    MODULE_SLOT = ''
    PT_REPEATER_NM_1CE  = ''
    PT_REPEATER_NM_1CFE = ''
    PT_REPEATER_NM_1CGE = ''
    PT_REPEATER_NM_1FFE  = ''
    PT_REPEATER_NM_1FGE  = ''

class Apps(AppsBaseConst.AppButtonsConst):
	pass