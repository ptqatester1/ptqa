##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.EndDevice.AnalogPhone.PhoneConst import PhoneConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from squish import snooze

def err(msg = ''):
    raise NotImplementedError(msg)

class Sounds(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def do(self):
        Util().clickButton(self.objName(PhoneConst.gui.DO_BUTT))
    
    def re(self):
        Util().clickButton(self.objName(PhoneConst.gui.RE_BUTT))
    
    def mi(self):
        Util().clickButton(self.objName(PhoneConst.gui.MI_BUTT))

class GuiCheck(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName        
        
    def updateName(self, squishName):
        self.squishName = squishName
        
    def status(self, status):
        Util().textCheckPoint(self.objName(PhoneConst.gui.STATUS_LABEL), status)
        
    def fromNumber(self, fromNumber):
        Util().textCheckPoint(self.objName(PhoneConst.gui.FROM_NUMBER), fromNumber)
        
    def number(self, number):
        Util().textCheckPoint(self.objName(PhoneConst.gui.NUMBER_LABEL), number)
        
    def date(self, date):
        Util().textCheckPoint(self.objName(PhoneConst.gui.DATE_TIME_LABEL), date)
    
    def soundStatus(self, text):
        Util().textCheckPoint(self.objName(PhoneConst.gui.DO_RE_ME_INDICATION), text)
        
class Gui(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName        
        self.sounds = Sounds(self)
        self.check = GuiCheck(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
        self.sounds.updateName(squishName)
        self.check.updateName(squishName)
    
    def pickup(self):
        Util().click(self.objName(PhoneConst.gui.PICKUP))
    
    def hangup(self):
        Util().click(self.objName(PhoneConst.gui.HANG_UP))
    
    def number(self, num):
        Util().clickButton(self.objName(PhoneConst.gui.NUMBER + str(num)))
    
    def dial(self, number):
        for num in str(number):
            self.number(num)
            snooze(0.5)
        self.pickup()