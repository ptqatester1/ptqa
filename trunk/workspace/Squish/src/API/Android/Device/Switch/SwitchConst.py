###############################################################
##Author: AbbasH
#@summary: SwitchConst holds object names for Switches Devices
###############################################################
from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class SwitchConst(DeviceBaseConst):
    None

class Physical(DeviceBaseConst.Physical):
    POWER_SPT = ''
    POWER_SPT_EMPTY = ''

    PT_SWITCH_NM_1CE   = ''
    PT_SWITCH_NM_1CFE  = ''
    PT_SWITCH_NM_1CGE  = ''
    PT_SWITCH_NM_1FFE  = ''
    PT_SWITCH_NM_1FGE  = ''

    CURRENT_MODULE_SLOT5 = ''
    CURRENT_MODULE_SLOT6 = ''
    CURRENT_MODULE_SLOT7 = ''
    CURRENT_MODULE_SLOT8 = ''
    CURRENT_MODULE_SLOT9 = ''
    CURRENT_MODULE_SLOT10 = ''

    PT_SWITCH_SLOT_1 = ''
    PT_SWITCH_SLOT_2 = ''
    PT_SWITCH_SLOT_3 = ''
    PT_SWITCH_SLOT_4 = ''
    PT_SWITCH_SLOT_5 = ''
    PT_SWITCH_SLOT_6 = ''
    PT_SWITCH_SLOT_7 = ''
    PT_SWITCH_SLOT_8 = ''
    PT_SWITCH_SLOT_9 = ''
    PT_SWITCH_SLOT_10 = ''
  
class Menu(AppsBaseConst.Menu):
    pass
	
class Cli(AppsBaseConst.Cli):
    pass