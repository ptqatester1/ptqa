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
    checkChangedImage()
    
def create():
    util.createDevice(ComponentBoxConst.DeviceType.SECURITY, a0.model, a0.x, a0.y)
    
def checkChangedImage():
    util.clickOnWorkspace(a0.x, a0.y)
    a0.updateName()
    a0.physical.customizeIconInPhysicalViewButton()
    a0.physical.customizePhysicalView(util.getFilePath('host1.png', UtilConst.P2_TEST))#This can be the path to any image file
    a0.physical.customizeIconInLogicalViewButton()
    a0.physical.customizeLogicalView(util.getFilePath('host1.png', UtilConst.P2_TEST))#This can be the path to any image file
    None
    
    