from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import Util
from API.Utility import UtilConst

#Function initialization
util = Util()

#Device initialization

def main():
    util.init()
    checkPoint()

def checkPoint():
    util.clickButton(ComponentBoxConst.DeviceGroup.CONNECTIONS)
    util.clickButton(ComponentBoxConst.DeviceType.CONNECTION)
    snooze(2)    
    test.compare(findObject(ComponentBoxConst.SEARCH_LINE_EDIT).text, "[Connections]")