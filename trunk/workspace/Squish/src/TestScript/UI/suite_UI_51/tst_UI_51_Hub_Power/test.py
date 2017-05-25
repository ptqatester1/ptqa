from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import Modules
from API.Device.Hub.Hub import Hub
from API.Utility.Util import Util
from API.Utility import UtilConst
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
    util.clickOnWorkspace(hub0.x, hub0.y)
    hub0.updateName()
    hub0.clickConfigTab()
    snooze(2)
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Hub is power on")
        hub0.clickPhysicalTab()
    else:
        test.fail("Hub is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        
    hub0.physical.power(Modules.hub.hub.power)
    hub0.clickConfigTab()
    snooze(2)
    if (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Hub is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    else:
        test.fail("Hub is power on")
        hub0.clickPhysicalTab()
    hub0.physical.power(Modules.hub.hub.power)
    hub0.clickConfigTab()
    snooze(2)
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Hub is power on")
    else:
        test.fail("Hub is power off")
    hub0.clickPhysicalTab()