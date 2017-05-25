from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.ActivityWizard.Exit.ExitConst import ExitConst
from API.ActivityWizard.Exit.Exit import Exit as AwExit
from API.MenuBar.File.File import File
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Utility import UtilConst

#Function initialization
util = Util()
fileMenu = File()
def startPT():
    startApplication(UtilConst.PACKETTRACER)

def main():
    util.init()
    AW_noItemOnWorkspace()
    startPT()
    util.init()
    AW_ItemOnWorkspace_NoAnswerNetwork()
    startPT()
    util.init()
    AW_ItemOnWorkspace_AnswerNetwork()
    
def AW_noItemOnWorkspace():
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    snooze(1)
    if (object.exists(ActivityWizardConst.WELCOME)):
        test.passes("Activity Wizard window found")
    else:
        test.fail("Activity Wizard window not found")
        
    AwExit().exit()
    util.closePT()
    
def AW_ItemOnWorkspace_NoAnswerNetwork():
    startApplication(UtilConst.PACKETTRACER)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, ComponentBoxConst.DeviceModel.PC, 100, 100)
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    snooze(1)
    util.clickButton(ActivityWizardConst.USE_AS_ANSWER_NETWORK_NO)
    snooze(1)
    if (object.exists(ActivityWizardConst.WELCOME)):
        test.passes("Activity Wizard window found")
    else:
        test.fail("Activity Wizard window not found")
    AwExit().exit()
    
    util.closePT()
    
def AW_ItemOnWorkspace_AnswerNetwork():
    startApplication(UtilConst.PACKETTRACER)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, ComponentBoxConst.DeviceModel.PC, 100, 100)
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    snooze(1)
    util.clickButton(ActivityWizardConst.USE_AS_ANSWER_NETWORK_YES)
    snooze(1)
    if (object.exists(ActivityWizardConst.WELCOME)):
        test.passes("Activity Wizard window found")
    else:
        test.fail("Activity Wizard window not found")
    AwExit().exit()
    util.closePT()