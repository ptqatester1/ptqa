from API.ComponentBox import ComponentBoxConst

from API.Device.Hub.Hub import Hub
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.Open.OpenConst import OpenConst
#Function initialization
util = Util()

#Device initialization
hub0 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 100, 200, "Hub0")
fileMenu = File()
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
    hub0.config.settings.displayName("TEST")
    util.clickOnWorkspace(hub0.x, hub0.y + 40)
    test.compare(findObject(UtilConst.DEVICE_LABEL).plainText, "TEST")
    fileMenu.selectFileItem(FileConst.OPEN)

    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)  