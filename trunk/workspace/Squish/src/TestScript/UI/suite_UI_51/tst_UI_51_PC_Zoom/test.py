from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility import UtilConst
from API.Utility.Util import Util

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")

def main():
    util.init()
    createTopology()
    checkpoint()

def createTopology():
    pc0.create()

def checkpoint():
    pc0.select()
    pc0.physical.zoomIn()
    checkRange(pc0.physical.imageObject.width, 1005)
    pc0.physical.zoomOriginal()
    checkRange(pc0.physical.imageObject.width, 502)
    pc0.physical.zoomOut()
    checkRange(pc0.physical.imageObject.width, 335)
    
def checkRange(size, x):
    if size in range(x-15, x+15):
        test.passes("")
    else:
        test.fail("")