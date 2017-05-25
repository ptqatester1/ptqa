from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util
from API.Utility import UtilConst

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 200, "PC1")

def main():
    util.init()
    util.open("UI16_PC_Modem.pkt", UtilConst.UI_TEST)
    checkpoint1()
    checkpoint2()
    
def checkpoint1():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.dialUp()
    snooze(1)
    util.textCheckPoint(UtilConst.NO_MODEM_POPUP, "A modem interface is required to dial out")
    util.clickButton(UtilConst.NO_MODEM_OK)

def checkpoint2():
    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.dialUp()
    # Verification Point 'VP1'
    snooze(2)
    pc1.desktop.dialUp.check.status("")#Message should be blank
    pc1.desktop.dialUp.dial("test", "testing", "444")
    snooze(10)
    pc1.desktop.dialUp.check.status("No dial tone")