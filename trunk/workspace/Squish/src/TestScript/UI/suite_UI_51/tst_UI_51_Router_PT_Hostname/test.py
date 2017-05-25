from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 100, 200, "Router0")

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
    router0.config.settings.hostname("TEST")
    router0.clickCliTab()
    router0.cli.textCheckPoint("TEST\(config\)#")