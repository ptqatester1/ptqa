##########################################################
#@author: Chris Allen
#@summary: holds object names used in TV
##########################################################
from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class TVConst:
	def __init__(self):
		self.ContextMenu = DeviceBaseConst.EndDeivceMenus

class Physical(DeviceBaseConst.Physical):
    POWER_ON = ''
    POWER_OFF = ''