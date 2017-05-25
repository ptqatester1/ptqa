from API.ComponentBox import ComponentBoxConst
from API.Device.AccessPoint.AccessPoint import AccessPoint
from API.Utility.Util import Util

#Device initialization
accessPoint0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 150, 100, "Access Point0")

#Function initialization
util = Util()

def main():
    util.init()
    createTopology()
    zoom()

def createTopology():
    accessPoint0.create()

def zoom():
    accessPoint0.select()
    
    #ZOOM IN
    accessPoint0.physical.zoomIn()
    if (accessPoint0.physical.imageObject.height>= 100):
        test.passes("Image is zoomed in")
    else:
        test.fail("Image is not zoomed in")
        
    #ZOOM RESET   
    accessPoint0.physical.zoomOriginal()
    if (accessPoint0.physical.imageObject.height > 20 and accessPoint0.physical.imageObject.height < 90):
        test.passes("Image is back to normal size")
    else:
        test.fail("Image is not back to normal size")
        
    #ZOOM OUT
    accessPoint0.physical.zoomOut()
    if (accessPoint0.physical.imageObject.height <= 55):
        test.passes("Image is zoomed out")
    else:
        test.fail("Image is not zoomed out")