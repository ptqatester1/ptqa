##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server

from API.Device.EndDevice.PC.PC import PC

from API.ComponentBox import ComponentBoxConst
import time

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, 'Server0')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 100, 'PC1')

month = ('January',
         'February',
         'March',
         'April',
         'May',
         'June',
         'July',
         'August',
         'September',
         'October',
         'November',
         'December')


def main():
    util.init()
    create()
    checkDefaults()
    changeTime()
    
def create():
    s0.create()
    util.fastForwardTime()

def checkDefaults():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('NTP')
    s0.services.ntp.check.on(True)
    s0.services.ntp.check.off(False)
    s0.services.ntp.check.enable(False)
    s0.services.ntp.check.disable(True)
    s0.services.ntp.check.key(None, property='enabled', value=False)
    s0.services.ntp.check.key('')
    s0.services.ntp.check.password(None, property='enabled', value=False)
    s0.services.ntp.check.password('')
    s0.services.ntp.check.month(month[time.localtime().tm_mon-1])
    s0.services.ntp.check.year(str(time.localtime().tm_year))
    s0.services.ntp.check.day(time.localtime().tm_mday)

def changeTime():
    s0.services.ntp.enable()
    s0.services.ntp.key('1')
    s0.services.ntp.password('pass')
    if not time.localtime().tm_mon == 1:
        newMonth = month[1]
    else:
        newMonth = month[2]
    if not time.localtime().tm_mday == 1:
        newDay = '1'
    else:
        newDay = '2'

    s0.services.ntp.date(newMonth, newDay, '2000')
    s0.services.ntp.time('12', '12', '12', 'AM')
    
    s0.services.ntp.check.key('1')
    s0.services.ntp.check.password('pass')
    s0.services.ntp.check.month(newMonth)
    s0.services.ntp.check.year('2000')
    s0.services.ntp.check.day(newDay)
