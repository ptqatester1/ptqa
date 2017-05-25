from API.ComponentBox import ComponentBoxConst
from API.Device.AccessPoint.AccessPoint import AccessPoint
from API.Utility.Util import Util
from API.Utility import UtilConst

#Function initialization
util = Util()

#Device initialization
accessPoint0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 150, 100, "Access Point0")

def main():
    util.init()
    createTopology()
    setDisplayName()
    checkpoint()

def createTopology():
    accessPoint0.create()

def setDisplayName():
    accessPoint0.select()
    accessPoint0.clickConfigTab()
    accessPoint0.config.settings.displayName("TEST")
    accessPoint0.close()

def checkpoint():
    util.clickOnWorkspace(accessPoint0.x, accessPoint0.y+30)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "TEST")