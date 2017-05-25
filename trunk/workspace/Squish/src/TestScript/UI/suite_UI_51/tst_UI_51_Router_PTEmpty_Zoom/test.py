from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Utility.Util import Util
from API.Utility import UtilConst
#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT_EMPTY, 100, 200, "Router0")

def main():
    util.init()
    createTopology()
    checkPoint()

def createTopology():
    router0.create()

def checkPoint():
    router0.select()
    router0.select()
    router0.physical.zoomIn()
    checkRange(router0.physical.imageObject.maximumSize.width, 941)

    router0.physical.zoomOriginal()
    checkRange(router0.physical.imageObject.maximumSize.width, 470)

    for i in range(2):
        router0.physical.zoomOut()
    checkRange(router0.physical.imageObject.maximumSize.width, 235)

def checkRange(size, x):
    if size in range(x-15, x+15):
        test.passes("")
    else:
        test.fail("")