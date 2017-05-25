from API.MenuBar.File.Exit.ExitConst import ExitConst
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.Save.SaveConst import SaveConst
util = Util()
fileMenu = File()

def main():
    util.init()
    exit_noItemOnWorkspace()
    exit_noSaveItemOnWorkspace()
    exit_saveItemOnWorkspace()
    exit_noSaveFileOpenedOnWorkspace()
    exit_saveFileOpenedOnWorkspace()
  


def exit_noItemOnWorkspace():
    fileMenu.selectFileItem(FileConst.EXIT)
    snooze(10)
    if (not object.exists(UtilConst.WORKSPACE)):
        test.passes("PT exited")
    else:
        test.fail("PT did not exit")

def exit_noSaveItemOnWorkspace():
    startApplication(UtilConst.PACKETTRACER)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100)    
    fileMenu.selectFileItem(FileConst.EXIT)
    snooze(10)
    if (object.exists(ExitConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
        util.clickButton(ExitConst.SAVE_NETWORK_PROMPT_NO)
    else:
        test.fail("Save Network Prompt not found")
    snooze(10)
    if (not object.exists(UtilConst.WORKSPACE)):
        test.passes("PT exited")
    else:
        test.fail("PT did not exit")
        
def exit_saveItemOnWorkspace():
    startApplication(UtilConst.PACKETTRACER)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100)    
    fileMenu.selectFileItem(FileConst.EXIT)
    snooze(10)
    if (object.exists(ExitConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
        util.clickButton(ExitConst.SAVE_NETWORK_PROMPT_YES)
    else:
        test.fail("Save Network Prompt not found")
    snooze(10)
    if (object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save Dialog found")
    else:
        test.fail("Save Dialog not found")
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Exit.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(10)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    snooze(10)
    if (not object.exists(UtilConst.WORKSPACE)):
        test.passes("PT exited")
    else:
        test.fail("PT did not exit")

def exit_noSaveFileOpenedOnWorkspace():
    startApplication(UtilConst.PACKETTRACER)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100)    
    fileMenu.selectFileItem(FileConst.EXIT)
    snooze(10)
    if (object.exists(ExitConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
        util.clickButton(ExitConst.SAVE_NETWORK_PROMPT_NO)
    else:
        test.fail("Save Network Prompt not found")
    snooze(10)
    if (not object.exists(UtilConst.WORKSPACE)):
        test.passes("PT exit")
    else:
        test.fail("PT did not exit")
        
def exit_saveFileOpenedOnWorkspace():
    startApplication(UtilConst.PACKETTRACER)
    util.open("UI1_File_Menu_Exit.pkt", UtilConst.UI_TEST)
    fileMenu.selectFileItem(FileConst.EXIT)
    snooze(10)
    if (object.exists(ExitConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
        util.clickButton(ExitConst.SAVE_NETWORK_PROMPT_YES)
    else:
        test.fail("Save Network Prompt not found")
    snooze(10)
    if (not object.exists(UtilConst.WORKSPACE)):
        test.passes("PT exited")
    else:
        test.fail("PT did not exit")
