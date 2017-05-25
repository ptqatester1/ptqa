##Chris Allen

from API.Toolbar.GoldenRealtimeToolbar.GoldenRealtimeToolbarConst import GoldenRealtimeToolbarConst
from API.Utility.Util import Util

class PtTime:
    def __init__(self, formatted, hours, minutes, seconds):
        self.formatted = formatted
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def resetNetworkDialog(self):
        try:
            return findObject(GoldenRealtimeToolbarConst.POWER_CYCLE_DEVICES_DIALOG)
        except LookupError, e:
            return False
    
    def resetNetworkYesButton(self):
        self.util.clickButton(GoldenRealtimeToolbarConst.POWER_CYCLE_DEVICES_DIALOG_YES)
    
    def resetNetworkNoButton(self):
        self.util.clickButton(GoldenRealtimeToolbarConst.POWER_CYCLE_DEVICES_DIALOG_NO)

class GoldenRealtimeToolbar:   
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()

    def powerCycleDevicesButton(self):
        self.util.clickButton(GoldenRealtimeToolbarConst.POWER_CYCLE_DEVICE)
    
    def fastForwardTimeButton(self):
        self.util.clickButton(GoldenRealtimeToolbarConst.FAST_FORWARD_TIME)
    
    def speedUpConvergence(self):
        for i in range(5):
            self.fastForwardTimeButton()
    
    def currentTime(self):
        '''Returns the current time value'''
        currentTime = str(findObject(GoldenRealtimeToolbarConst.TIME_LABEL).text).split()[-1]
        hours, minutes, seconds = currentTime.split(':')
        return PtTime(currentTime, hours, minutes, seconds)
    
    def powerCycleDevice(self, reset = True):
        self.powerCycleDevicesButton()
        if reset:
            self.popups.resetNetworkYesButton()
        else:
            self.popups.resetNetworkNoButton()