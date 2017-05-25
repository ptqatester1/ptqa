#############################################################
#@author: Lesley Tse                                    	# 
#@summary: HubConst holds object names for Hub Devices		#
#############################################################

from API.Android.Device.DeviceBase import DeviceBaseConst

class HubConst(DeviceBaseConst):
    def __init__(self):
        self.ContextMenu = DeviceBaseConst.ContextMenu
	
class Physical(DeviceBaseConst.Physical):
    POWER = ''
    MODULE_SLOT_TOP_LEFT = ''
    MODULE_SLOT_TOP_RIGHT = ''
    MODULE_SLOT_BOTTOM_LEFT = ''
    MODULE_SLOT_BOTTOM_RIGHT = ''
    PT_REPEATER_NM_1CE  =  '' 
    PT_REPEATER_NM_1CFE =  ''
    PT_REPEATER_NM_1CGE =  ''
    PT_REPEATER_NM_1FFE =  ''
    PT_REPEATER_NM_1FGE =  ''