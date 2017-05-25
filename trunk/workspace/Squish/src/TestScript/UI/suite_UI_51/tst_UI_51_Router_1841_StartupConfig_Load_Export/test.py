from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Utility.Util import Util
from API.Utility import UtilConst
#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 200, "Router0")

def main():
    util.init()
    createTopology()
    util.clickOnSimulation()
    util.clickOnRealtime()
    configRouter()
    checkPoint1()
    checkPoint2()

def createTopology():
    router0.create()

def configRouter():
    router0.select()
    router0.clickConfigTab()
    router0.config.settings.hostname("TEST")
    router0.clickCliTab()
    router0.clickConfigTab()
    router0.config.settings.saveButton()

def checkPoint1():
    router0.config.settings.exportStartupConfigButton()
    router0.config.settings.fileDialog.cancelButton()
    router0.config.settings.exportStartupConfig(util.getFilePath("Router0_startup-config.txt", UtilConst.UI_TEST))
    router0.clickCliTab()
    router0.cli.setCliText("show startup-config")
    router0.cli.textCheckPoint("hostname TEST", 2)

def checkPoint2():
    router0.clickConfigTab()
    router0.config.settings.loadButton()
    router0.config.settings.fileDialog.cancelButton()
    router0.config.settings.loadStartupConfig(util.getFilePath("startup-config.txt", UtilConst.UI_TEST))
    router0.clickCliTab()
    router0.cli.setCliText("\x03")
    router0.cli.setCliText("show startup-config")    
    router0.cli.textCheckPoint("hostname testStartupConfig")