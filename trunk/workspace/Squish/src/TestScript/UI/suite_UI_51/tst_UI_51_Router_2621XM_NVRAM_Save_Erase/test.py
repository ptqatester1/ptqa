from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 100, 200, "Router0")

def main():
    util.init()
    createTopology()
    util.clickOnSimulation()
    util.clickOnRealtime()
    checkPoint1()
    checkPoint2()

def createTopology():
    router0.create()

def checkPoint1():
    router0.select()
    router0.clickConfigTab()
    router0.config.settings.saveButton()
    router0.clickCliTab()
    router0.cli.textCheckPoint("Router#copy running-config startup-config")
    router0.cli.textCheckPoint("Destination filename \[startup-config\]?")
    router0.cli.textCheckPoint("Building configuration...")
    router0.cli.textCheckPoint("\[OK\]")

def checkPoint2():
    router0.clickConfigTab()
    router0.config.settings.eraseButton()
    router0.config.settings.popups.eraseStartupConfigNoButton()
    
    router0.clickCliTab()
    router0.cli.textCheckPoint("Erase of nvram: complete", 0)
    router0.clickConfigTab()
    router0.config.settings.eraseButton()
    router0.config.settings.popups.eraseStartupConfigYesButton()
    
    router0.clickCliTab()
    router0.cli.textCheckPoint("Erase of nvram: complete")