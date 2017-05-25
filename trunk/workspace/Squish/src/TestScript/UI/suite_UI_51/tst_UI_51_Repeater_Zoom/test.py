from API.ComponentBox import ComponentBoxConst

from API.Device.Repeater.Repeater import Repeater
from API.Utility.Util import Util
from API.Utility import UtilConst
#Function initialization
util = Util()

#Device initialization
repeater0 = Repeater(ComponentBoxConst.DeviceModel.REPEATER_PT, 100, 200, "Repeater0")

def main():
    util.init()
    createTopology()
    checkPoint()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.HUB, repeater0.model, repeater0.x, repeater0.y)

def checkPoint():
    util.clickOnWorkspace(repeater0.x, repeater0.y)
    repeater0.updateName()
    repeater0.physical.zoomIn()
    checkRange(repeater0.physical.imageObject.maximumSize.width, 300)

    repeater0.physical.zoomOriginal()
    checkRange(repeater0.physical.imageObject.maximumSize.width, 150)

    for i in range(2):
        repeater0.physical.zoomOut()
    checkRange(repeater0.physical.imageObject.maximumSize.width, 75)

def checkRange(size, x):
    if size in range(x-15, x+15):
        test.passes("")
    else:
        test.fail("")