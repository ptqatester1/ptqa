##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Security.Asa import Asa

from API.ComponentBox import ComponentBoxConst

util = Util()

a0 = Asa(ComponentBoxConst.DeviceModel.ASA_5505, 100, 100, 'Asa0')

def main():
    util.init()
    check()
    
def check():
    util.createDevice(ComponentBoxConst.DeviceType.SECURITY, a0.model, a0.x, a0.y)
    a0.exists()
    None
    