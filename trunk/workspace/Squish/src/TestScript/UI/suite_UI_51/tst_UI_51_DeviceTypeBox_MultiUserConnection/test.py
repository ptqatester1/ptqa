from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization

def main():
    util.init()
    checkPoint()

def checkPoint():

    util.clickButton(ComponentBoxConst.DeviceType.MULTIUSER)
    snooze(2)
    # Verification Point 'VP1'
    test.compare(findObject(ComponentBoxConst.SEARCH_LINE_EDIT).text, "[Multiuser Connection]")
