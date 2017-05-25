##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Security.Asa import Asa

from API.ComponentBox import ComponentBoxConst

util = Util()
a0 = Asa(ComponentBoxConst.DeviceModel.ASA_5505, 100, 100, 'Asa0')

def main():
    util.init()
    create()
    checkDefaults()
    checkChanges()
    checkOtherInt()
    
def create():
    a0.create()
    util.fastForwardTime()
    
def checkDefaults():
    a0.select()
    a0.clickConfigTab()
    a0.config.selectInterface('Ethernet0/0')
    a0.config.interface.switch.check.portStatus(True)
    a0.config.interface.switch.check.bandwidth('Auto', True)
    a0.config.interface.switch.check.bandwidth('10', True)
    a0.config.interface.switch.check.duplex('Auto', True)
    a0.config.interface.switch.check.duplex('Half', True)
    a0.config.interface.switch.check.duplex('Full', False)
    a0.config.interface.switch.check.portType('Access')
    a0.config.interface.switch.check.vlanNumber('2')
    
def checkChanges():
    a0.config.interface.switch.portStatus(None)
    a0.config.interface.switch.duplex('Full')
    a0.config.interface.switch.bandwidth(None)
    
    a0.config.interface.switch.check.portStatus(False)
    a0.config.interface.switch.check.bandwidth('Auto', False)
    a0.config.interface.switch.check.bandwidth('10', True)
    a0.config.interface.switch.check.duplex('Auto', False)
    a0.config.interface.switch.check.duplex('Half', False)
    a0.config.interface.switch.check.duplex('Full', True)
    
def checkOtherInt():
    a0.config.selectInterface('Ethernet0/1')
    a0.config.interface.switch.check.portStatus(True)
    a0.config.interface.switch.check.bandwidth('Auto', True)
    a0.config.interface.switch.check.bandwidth('10', True)
    a0.config.interface.switch.check.duplex('Auto', True)
    a0.config.interface.switch.check.duplex('Half', True)
    a0.config.interface.switch.check.duplex('Full', False)
    a0.config.interface.switch.check.portType('Access')
    a0.config.interface.switch.check.vlanNumber('1')