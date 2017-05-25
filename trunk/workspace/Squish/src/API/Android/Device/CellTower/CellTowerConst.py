###############################################
##Author: AbbasH
#@summary: CellTowerConst holds object names
###############################################

from API.Android.Device.DeviceBase import DeviceBaseConst
from API.Android.Device import AppsBaseConst


class CellTowerConst:
	def __init__(self):
		self.ContextMenu = DeviceBaseConst.ContextMenu
		self.Apps = Apps

class Physical(DeviceBaseConst.Physical):
    POWER = ''
    CURRENT_MODULE = ''
    MODULE_SLOT = ''
    PT_CELL_NM_1CX  = ''
    PT_CELL_NM_3G_4G = ''

class Apps(AppsBaseConst.AppButtonsConst):
	pass