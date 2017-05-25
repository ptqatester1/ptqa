from API.ComponentBox import ComponentBoxConst

from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.Open.OpenConst import OpenConst

#Function initialization
util = Util()
fileMenu = File()

#Device initialization
Linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 150, 100, "Wireless Router0")

def main():
    util.init()
    createTopology()
    setDisplayName()
    checkpoint()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, Linksys.model, Linksys.x, Linksys.y)

def setDisplayName():
    util.clickOnWorkspace(Linksys.x, Linksys.y)
    Linksys.updateName()
    Linksys.clickConfigTab()
    Linksys.config.settings.displayName("TEST")
    Linksys.close()
    
def checkpoint():
    util.clickOnWorkspace(Linksys.x, Linksys.y + 40)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "TEST")