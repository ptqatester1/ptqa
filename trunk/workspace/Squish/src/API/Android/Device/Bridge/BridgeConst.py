#############################################################
#@author: Lesley Tse                                    	# 
#@summary: BridgeConst holds object names for Bridge Devices#
#############################################################

from API.Android.Device.DeviceBase import DeviceBaseConst

class BridgeConst(DeviceBaseConst):
    def __init__(self):
        self.ContextMenu = DeviceBaseConst.ContextMenu
	
class Physical(DeviceBaseConst.Physical):
    POWER = ''
    CURRENT_MODULE_SLOT0 = ''
    CURRENT_MODULE_SLOT1 = ''
    MODULE_SLOT0 = ''
    MODULE_SLOT1 = ''
    PT_SWITCH_NM_1CE   = ''     
    PT_SWITCH_NM_1CFE  = ''
    PT_SWITCH_NM_1CGE  = ''
    PT_SWITCH_NM_1FFE  = ''
    PT_SWITCH_NM_1FGE  = ''