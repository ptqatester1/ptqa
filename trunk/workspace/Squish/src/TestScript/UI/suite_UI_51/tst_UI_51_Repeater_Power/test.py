from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import Modules
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
    repeater0.create()

def checkPoint():
    repeater0.select()
    repeater0.clickConfigTab()
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Repeater is power on")
        repeater0.clickPhysicalTab()
    else:
        test.fail("Repeater is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        
    repeater0.physical.power(Modules.hub.repeater.power)
    repeater0.clickConfigTab()
    if (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Repeater is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    else:
        test.fail("Repeater is power on")
        repeater0.clickPhysicalTab()

    repeater0.physical.power(Modules.hub.repeater.power)
    repeater0.clickConfigTab()
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Repeater is power on")
    else:
        test.fail("Repeater is power off")
    repeater0.clickPhysicalTab()