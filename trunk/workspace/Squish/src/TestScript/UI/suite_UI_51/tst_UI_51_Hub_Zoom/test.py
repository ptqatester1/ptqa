from API.ComponentBox import ComponentBoxConst

from API.Device.Hub.Hub import Hub
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization
hub0 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 100, 200, "Hub0")

def main():
    util.init()
    createTopology()
    checkPoint()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.HUB, hub0.model, hub0.x, hub0.y)

def checkPoint():
    hub0.select()
    hub0.physical.zoomIn()
    checkRange(hub0.physical.imageObject.maximumSize.width, 434)
    hub0.physical.zoomOriginal()
    checkRange(hub0.physical.imageObject.maximumSize.width, 217)
    hub0.physical.zoomOut()
    checkRange(hub0.physical.imageObject.maximumSize.width, 144)

def checkRange(size, x):
    if size in range(x-15, x+15):
        test.passes("")
    else:
        test.fail("")