from API.ComponentBox import ComponentBoxConst
from API.ComponentBox import ComponentBox
from API.Utility.Util import Util
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter

Linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 150, 100, "Wireless Router0")
util = Util()

def main():
    util.init()
    createTopology()
    zoom()

def createTopology():
    Linksys.create()

def zoom():
    Linksys.select()
    Linksys.physical.zoomIn()
    checkRange(Linksys.physical.imageObject.maximumSize.width, 500)
    Linksys.physical.zoomOriginal()
    checkRange(Linksys.physical.imageObject.maximumSize.width, 250)
    Linksys.physical.zoomOut()
    checkRange(Linksys.physical.imageObject.maximumSize.width, 166)

def checkRange(size, x):
    if size in range(x-15, x+15):
        test.passes("")
    else:
        test.fail("")