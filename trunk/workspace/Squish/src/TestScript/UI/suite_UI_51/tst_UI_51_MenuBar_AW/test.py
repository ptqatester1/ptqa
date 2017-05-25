from API.MenuBar.Extensions.Extensions import Extensions
from API.MenuBar.Extensions.ExtensionsConst import ExtensionsConst
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.ActivityWizard.Exit.ExitConst import ExitConst
from API.ActivityWizard.Exit.Exit import Exit as AwExit
from API.Utility import UtilConst
from API.MenuBar.File.File import File
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
extensionsMenu = Extensions()
util = Util()
fileMenu = File()

def main():
    util.init()
    AW_noItemOnWorkspace()
    AW_ItemOnWorkspace_NoAnswerNetwork()
    AW_ItemOnWorkspace_AnswerNetwork()

def AW_noItemOnWorkspace():
    extensionsMenu.selectExtensionsItem(ExtensionsConst.ACTIVITY_WIZARD)
    snooze(2)
    if (object.exists(ActivityWizardConst.WELCOME)):
        test.passes("Activity Wizard window found")
    else:
        test.fail("Activity Wizard window not found")
    AwExit().exit()

def AW_ItemOnWorkspace_AnswerNetwork():
    startApplication(UtilConst.PACKETTRACER)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 100)
    extensionsMenu.selectExtensionsItem(ExtensionsConst.ACTIVITY_WIZARD)
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
    extensionsMenu.selectExtensionsItem(ExtensionsConst.ACTIVITY_WIZARD)
    snooze(2)
    util.clickButton(ActivityWizardConst.USE_AS_ANSWER_NETWORK_NO)
    snooze(1)
    if (object.exists(ActivityWizardConst.WELCOME)):
        test.passes("Activity Wizard window found")
    else:
        test.fail("Activity Wizard window not found")
    AwExit().exit()
