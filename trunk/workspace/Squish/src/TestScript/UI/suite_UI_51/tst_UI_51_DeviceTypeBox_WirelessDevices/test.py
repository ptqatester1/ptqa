from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization

def main():
    util.init()
    checkPoint()

def checkPoint():
    util.clickButton(ComponentBoxConst.DeviceType.WIRELESS_DEVICE)
    snooze(2)
    test.compare(findObject(ComponentBoxConst.DeviceModel.LINKSYS).windowIconText, "Linksys-WRT300N")
    test.compare(findObject(ComponentBoxConst.DeviceModel.ACCESSPOINT_N).windowIconText, "AccessPoint-PT-N")
