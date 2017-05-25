from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util
from API.Utility import UtilConst
util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")

def main():
    util.init()
    createTopology()
    setDisplayName()
    checkpoint()

def createTopology():
    pc0.create()

def setDisplayName():
    pc0.select()
    pc0.clickConfigTab()
    pc0.config.settings.displayName("Test")
    pc0.close()
    
def checkpoint():
    util.clickOnWorkspace(pc0.x, pc0.y+40)
    test.compare(findObject(UtilConst.DEVICE_LABEL).plainText, "Test")