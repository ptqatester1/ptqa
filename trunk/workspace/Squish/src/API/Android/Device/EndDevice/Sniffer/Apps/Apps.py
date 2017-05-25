####################################################
#@author: Chris Allen
####################################################
from API.Android.Device.AppsBase import SnifferList, SnifferAppButtons
from API.Android.Simulation.EventList.EventList import EventListFilter
from API.Android.Device.DeviceBase import DeviceBase
from API.Android.Device.AppsBase import AppButtons
from API.Android.Utility.Util import Util

util = Util()

class Apps(DeviceBase):
    def __init__(self):
        self.appButtons = SnifferAppButtons()
        self.filter = EventListFilter()
        sniffer = SnifferList()
        self.editFilter = SnifferList().editFilter
        self.util = util

    