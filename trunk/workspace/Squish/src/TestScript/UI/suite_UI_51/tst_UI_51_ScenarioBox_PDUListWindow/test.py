from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.UserCreatedPacketWindow.ScenarioBox import ScenarioBox
from API.UserCreatedPacketWindow.ScenarioBox import ScenarioBoxConst
from API.UserCreatedPacketWindow.UserCreatedPDUListConst import UserCreatedPDUListConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Utility.Util import Util
from API.Utility import UtilConst
import os
#Function initialization
util = Util()
commonToolsBar = CommonToolsBar()
scenarioBox = ScenarioBox()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 200, "PC1")

def main():
    util.init()
    checkpoint()
    
def checkpoint():
    util.clickButton(UserCreatedPDUListConst.EXPAND_LIST_BUTTON)
    test.compare(findObject(UserCreatedPDUListConst.PDU_LIST).visible, True)
    test.compare(findObject(UserCreatedPDUListConst.PDU_LIST_TOGGLED_VIEW).visible, False)
    
    util.clickButton(ScenarioBoxConst.TOGGLE_PDU_LIST_WINDOW)
    
    test.compare(findObject(UserCreatedPDUListConst.PDU_LIST).visible, False)
    test.compare(findObject(UserCreatedPDUListConst.PDU_LIST_TOGGLED_VIEW).visible, True)