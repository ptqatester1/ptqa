#############################################################
#@author: Lesley Tse                                    	# 
#@summary: ModemConst holds object names for Modem Devices  #
#############################################################

from API.Android.Device.DeviceBase import DeviceBaseConst

class ModemConst(DeviceBaseConst):
    def __init__(self):
        self.ContextMenu = DeviceBaseConst.EndDeviceMenus  
	#modems are currently has context menu with Desktop section. Not sure if that's working as intended.
	
class Physical:
	pass