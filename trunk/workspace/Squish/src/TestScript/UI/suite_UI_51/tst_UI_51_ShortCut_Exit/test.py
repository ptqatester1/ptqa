from API.MenuBar.File.Exit.ExitConst import ExitConst
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.Save.SaveConst import SaveConst
from API.MenuBar.File.Open.OpenConst import OpenConst
util = Util()
fileMenu = File()

def main():
    util.init()
    snooze(7)
    exit_noItemOnWorkspace()
    exit_noSaveItemOnWorkspace()
    exit_saveItemOnWorkspace()
    exit_noSaveFileOpenedOnWorkspace()
    exit_saveFileOpenedOnWorkspace()
  


def exit_noItemOnWorkspace():
    test.compare(findObject(UtilConst.WORKSPACE).visible, True)
    nativeType("<Alt+F4>")
    snooze(2)
    test.compare(findObject(UtilConst.WORKSPACE).visible, False)

def exit_noSaveItemOnWorkspace():
    startApplication("PacketTracer7")
    test.compare(findObject(UtilConst.WORKSPACE).visible, True)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100)    
    nativeType("<Alt+F4>")
    snooze(2)
    if (object.exists(ExitConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
        util.clickButton(ExitConst.SAVE_NETWORK_PROMPT_NO)
    else:
        test.fail("Save Network Prompt not found")
    snooze(2)
    test.compare(findObject(UtilConst.WORKSPACE).visible, False)
        
def exit_saveItemOnWorkspace():
    startApplication(UtilConst.PACKETTRACER)
    test.compare(findObject(UtilConst.WORKSPACE).visible, True)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100)    
    nativeType("<Alt+F4>")
    snooze(2)
    if (object.exists(ExitConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
        util.clickButton(ExitConst.SAVE_NETWORK_PROMPT_YES)
    else:
        test.fail("Save Network Prompt not found")
    snooze(2)
    if (object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save Dialog found")
    else:
        test.fail("Save Dialog not found")
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Exit.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(2)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    snooze(2)
    test.compare(findObject(UtilConst.WORKSPACE).visible, False)
    None
def exit_noSaveFileOpenedOnWorkspace():
    startApplication(UtilConst.PACKETTRACER)
    test.compare(findObject(UtilConst.WORKSPACE).visible, True)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100)    
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    nativeType("<Alt+F4>")
    snooze(2)
    if (object.exists(ExitConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
        util.clickButton(ExitConst.SAVE_NETWORK_PROMPT_NO)
    else:
        test.fail("Save Network Prompt not found")
    snooze(2)
    test.compare(findObject(UtilConst.WORKSPACE).visible, False)
        
def exit_saveFileOpenedOnWorkspace():
    startApplication(UtilConst.PACKETTRACER)
    test.compare(findObject(UtilConst.WORKSPACE).visible, True)
    util.open("UI1_File_Menu_Exit.pkt", UtilConst.UI_TEST)
    snooze(3)
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    nativeType("<Alt+F4>")
    snooze(2)
    if (object.exists(ExitConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
        util.clickButton(ExitConst.SAVE_NETWORK_PROMPT_YES)
    else:
        test.fail("Save Network Prompt not found")
    snooze(2)
    test.compare(findObject(UtilConst.WORKSPACE).visible, False)