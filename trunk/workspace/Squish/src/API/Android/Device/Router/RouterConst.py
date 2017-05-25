#############################################################
#@author: Chris Allen                                       # 
#@summary: RouterConst holds object names for Router Devices#
#############################################################
from API.Android.Device import AppsBaseConst
from API.Android.Device.DeviceBase import DeviceBaseConst

class RouterConst(DeviceBaseConst):
    None

class Physical(DeviceBaseConst.Physical):
    R1841_LEFT_SLOT = ''
    R1841_RIGHT_SLOT = ''
    
    R1941_LEFT_SLOT = ''
    R1941_RIGHT_SLOT = ''
    
    R2620XM_RIGHT_SLOT = ''
    R2620XM_LEFT_SLOT = ''
    R2620XM_NM_SLOT = ''

    R2621XM_RIGHT_SLOT = ''
    R2621XM_LEFT_SLOT = ''
    R2621XM_NM_SLOT = ''

    R2811_TOP_LEFT_SLOT = ''
    R2811_TOP_RIGHT_SLOT = ''
    R2811_BOTTOM_LEFT_SLOT = ''
    R2811_BOTTOM_RIGHT_SLOT = ''
    R2811_NM_SLOT = ''

    R2901_SLOT_0 = ''
    R2901_SLOT_1 = ''
    R2901_SLOT_2 = ''
    R2901_SLOT_3 = ''
    
    R2911_SLOT_0 = ''
    R2911_SLOT_1 = ''
    R2911_SLOT_2 = ''
    R2911_SLOT_3 = ''

    R_PT_FIRST_LEFT_SLOT = ''

    
    POWER_R1841 = ''
    POWER_R1941 = ''
    POWER_R2620XM = ''
    POWER_R2621XM = ''
    POWER_R2811 = ''
    POWER_R2901 = ''
    POWER_R2911 = ''
    POWER_R_PT = ''
    POWER_R_PT_EMPTY = ''

    HWIC_2T = ''
    HWIC_4ESW = ''
    HWIC_8A = ''
    HWIC_AP_AG_B = ''
    WIC_1AM = ''
    WIC_1ENET = ''
    WIC_1T = ''
    WIC_2AM = ''
    WIC_2T = ''
    WIC_COVER = ''

    NM_2W = ''
    NM_4AS = ''
    NM_8AS = ''
    NM_1E = ''
    NM_4E = ''
    NM_1E2W = ''
    NM_2E2W = ''
    NM_1FE_FX = ''
    NM_1FE_TX = ''
    NM_1FE2W = ''
    NM_2FE2W = ''
    NM_8AM = ''
    NM_ESW_161 = ''
    NM_COVER = ''

    PT_ROUTER_NM_1AM = ''
    PT_ROUTER_NM_1CE = ''
    PT_ROUTER_NM_1CFE = ''
    PT_ROUTER_NM_1CGE = ''
    PT_ROUTER_NM_1FFE = ''
    PT_ROUTER_NM_1FGE = ''
    PT_ROUTER_NM_1S = ''
    PT_ROUTER_NM_1SS = ''
	
class Menu(AppsBaseConst.Menu):
    pass
	
class Cli(AppsBaseConst.Cli):
    pass