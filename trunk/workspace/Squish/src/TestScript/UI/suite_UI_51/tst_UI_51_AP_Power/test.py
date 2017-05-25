from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.AccessPoint.AccessPoint import AccessPoint
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import Modules
#Device initialization
accessPoint0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 150, 100, "Access Point0")

#Function initialization
util = Util()

def main():
    util.init()
    createTopology()
    PowerToggle()
    
def createTopology():
    accessPoint0.create()

def PowerToggle():
    accessPoint0.select()
    accessPoint0.clickConfigTab()
    snooze(2)
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("AccessPoint is power on")
        accessPoint0.clickPhysicalTab()
    else:
        test.fail("AccessPoint is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        
    accessPoint0.physical.power(Modules.wireless.ap_pt.power)
    accessPoint0.clickConfigTab()
    snooze(2)
    if (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("AccessPoint is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    else:
        test.fail("AccessPoint is power on")
        accessPoint0.clickPhysicalTab()

    accessPoint0.physical.power(Modules.wireless.ap_pt.power)
    accessPoint0.clickConfigTab()
    snooze(2)
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("AccessPoint is power on")
    else:
        test.fail("AccessPoint is power off")
    accessPoint0.clickPhysicalTab()