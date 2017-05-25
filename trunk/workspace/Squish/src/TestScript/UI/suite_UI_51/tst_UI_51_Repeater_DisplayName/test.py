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
    repeater0.clickConfigTab()
    repeater0.config.settings.displayName("TEST")
    repeater0.close()
    util.clickOnWorkspace(repeater0.x, repeater0.y+30)
    test.compare(findObject(UtilConst.DEVICE_LABEL).plainText, "TEST")