from API.MenuBar.File.New.NewConst import NewConst
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.MenuBar.File.Save.SaveConst import SaveConst
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router

fileMenu = File()
util = Util()
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")

def main():
    util.init()
    new_noItemOnWorkspace()
    new_saveItemOnWorkspace()
    new_notSaveItemOnWorkspace()
    new_itemOnWorkspaceCancel()
    new_saveFileOpenedOnWorkspace()
    new_notSaveFileOpenedOnWorkspace()
    
def new_noItemOnWorkspace():
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.CANCEL_OPEN_FILE)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+N>")

def new_saveItemOnWorkspace():
    router0.create()    
    util.clickOnWorkspace(router0.x, router0.y)
    router0.exists()
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    snooze(2)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+N>")
    snooze(2)
    if (object.exists(NewConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
    else:
        test.fail("Save Network Prompt not found")
    snooze(2)
    util.clickButton(NewConst.SAVE_NETWORK_PROMPT_YES)
    snooze(2)
    if (object.exists(SaveConst.SAVE_FILE_NAME)):
        test.passes("Save Dialog found")
    else:
        test.fail("Save Dialog not found")  
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_New.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(2)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    router0.doesNotExist()

def new_notSaveItemOnWorkspace():
    router0.create()  
    router0.exists()
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    snooze(2)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+N>")
    snooze(2)
    util.clickButton(NewConst.SAVE_NETWORK_PROMPT_NO)
    router0.doesNotExist()

def new_itemOnWorkspaceCancel():
    router0.create()   
    util.clickOnWorkspace(router0.x, router0.y)
    router0.exists()
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    snooze(2)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+N>")
    snooze(2)
    util.clickButton(NewConst.SAVE_NETWORK_PROMPT_CANCEL)
    router0.exists()
    util.newWorkspace()

def new_saveFileOpenedOnWorkspace():
    util.open("UI1_File_Menu_New.pkt", UtilConst.UI_TEST)
    snooze(5)
    router0.exists()
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    snooze(2)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+N>")
    snooze(2)
    if (object.exists(NewConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
    else:
        test.fail("Save Network Prompt not found")
    util.clickButton(NewConst.SAVE_NETWORK_PROMPT_YES)
    snooze(2)
    router0.doesNotExist()
    util.newWorkspace()
def new_notSaveFileOpenedOnWorkspace():
    util.open("UI1_File_Menu_New.pkt", UtilConst.UI_TEST)
    snooze(5)
    router0.exists()
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    snooze(2)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+N>")
    snooze(2)
    if (object.exists(NewConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
    else:
        test.fail("Save Network Prompt not found")
    util.clickButton(NewConst.SAVE_NETWORK_PROMPT_NO)
    router0.doesNotExist()