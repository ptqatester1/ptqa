from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.ActivityWizard.Exit.ExitConst import ExitConst
from API.ActivityWizard.Exit.Exit import Exit as AwExit
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.ComponentBox import ComponentBoxConst
util = Util()
fileMenu = File()

def main():
    util.init()
    snooze(7)
    AW_noItemOnWorkspace()
    AW_ItemOnWorkspace_NoAnswerNetwork()
    AW_ItemOnWorkspace_AnswerNetwork()
    

def AW_noItemOnWorkspace():
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.CANCEL_OPEN_FILE)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+W>")
    snooze(2)
    if (object.exists(ActivityWizardConst.WELCOME)):
        test.passes("Activity Wizard window found")
    else:
        test.fail("Activity Wizard window not found")
    AwExit().exit()
    
def AW_ItemOnWorkspace_AnswerNetwork():
    startApplication(UtilConst.PACKETTRACER)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 100)
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+W>")
    snooze(2)
    util.clickButton(ActivityWizardConst.USE_AS_ANSWER_NETWORK_YES)
    snooze(2)
    if (object.exists(ActivityWizardConst.WELCOME)):
        test.passes("Activity Wizard window found")
    else:
        test.fail("Activity Wizard window not found")
    AwExit().exit()
    
    
def AW_ItemOnWorkspace_NoAnswerNetwork():  
    startApplication(UtilConst.PACKETTRACER)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 100)
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+W>")
    snooze(2)
    util.clickButton(ActivityWizardConst.USE_AS_ANSWER_NETWORK_NO)
    snooze(2)
    if (object.exists(ActivityWizardConst.WELCOME)):
        test.passes("Activity Wizard window found")
    else:
        test.fail("Activity Wizard window not found")
    AwExit().exit()
    