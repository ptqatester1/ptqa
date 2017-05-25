from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Utility.Util import Util
from API.Utility import UtilConst
#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_2620XM, 100, 200, "Router0")

def main():
    util.init()
    createTopology()
    util.clickOnSimulation()
    util.clickOnRealtime()
    checkPoint()

def createTopology():
    router0.create()

def checkPoint():
    router0.select()
    router0.clickConfigTab()
    router0.config.settings.displayName("TEST")
    util.clickOnWorkspace(router0.x, router0.y+40)
    test.compare(findObject(UtilConst.DEVICE_LABEL).plainText, "TEST")