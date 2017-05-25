from API.Utility.Util import Util
from API.Utility import UtilConst
#Function initialization
util = Util()

#Device initialization

def main():
    util.init()
    checkPoint()

def checkPoint():
    test.compare(findObject(UtilConst.PHYSICAL_SWITCH).toolTip, "Physical Workspace (Shift+P)")
    test.compare(findObject(UtilConst.LOGICAL_SWITCH).toolTip, "Logical Workspace (Shift+L)")
    
    util.clickOnPhysical()
    test.compare(findObject(UtilConst.PHYSICAL_WORKSPACE).visible, True)
    test.compare(findObject(UtilConst.WORKSPACE).visible, False)
    
    util.clickOnLogical()
    test.compare(findObject(UtilConst.PHYSICAL_WORKSPACE).visible, False)
    test.compare(findObject(UtilConst.WORKSPACE).visible, True)