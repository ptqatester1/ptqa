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
    setDisplayName()
    checkpoint()

def createTopology():
    router0.create()
    util.fastForwardTime()

def setDisplayName():
    router0.select()
    router0.clickConfigTab()
    router0.config.settings.displayName("TEST")
    router0.close()
    
def checkpoint():
    util.clickOnWorkspace(router0.x, router0.y+40)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "TEST")