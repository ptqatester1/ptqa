##Chris Allen

from API.Utility.Util import Util
from API.Toolbar.GoldenSimulationToolbar.GoldenSimulationToolbarConst import GoldenSimulationToolbarConst

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
            return findObject(GoldenSimulationToolbarConst.POWER_CYCLE_DEVICES_DIALOG)
        except LookupError, e:
            return False
    
    def resetNetworkYesButton(self):
        self.util.clickButton(GoldenSimulationToolbarConst.POWER_CYCLE_DEVICES_DIALOG_YES)
    
    def resetNetworkNoButton(self):
        self.util.clickButton(GoldenSimulationToolbarConst.POWER_CYCLE_DEVICES_DIALOG_NO)

class GoldenSimulationToolbar:   
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()

    def powerCycleDevicesButton(self):
        self.util.clickButton(GoldenSimulationToolbarConst.POWER_CYCLE_DEVICES)
    
    def currentTime(self):
        '''Returns the current time value'''
        currentTime = str(findObject(GoldenSimulationToolbarConst.TIME_LABEL).text).split()[-1]
        hours, minutes, seconds = currentTime.split(':')
        return PtTime(currentTime, hours, minutes, seconds)
    
    def powerCycleDevice(self, reset = True):
        self.powerCycleDevicesButton()
        if reset:
            self.popups.resetNetworkYesButton()
        else:
            self.popups.resetNetworkNoButton()
    
    def backButton(self):
        self.util.clickButton(GoldenSimulationToolbarConst.BACK)
    
    def autoCapturePlayButton(self):
        self.util.clickButton(GoldenSimulationToolbarConst.AUTO_CAPTURE_PLAY)
    
    def captureForwardButton(self):
        self.util.clickButton(GoldenSimulationToolbarConst.CAPTURE_FORWARD)
    
    def eventListButton(self):
        self.util.clickButton(GoldenSimulationToolbarConst.EVENT_LIST)