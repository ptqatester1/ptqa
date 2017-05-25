from API.MenuBar.File.Save.SaveConst import SaveConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import UtilConst
from API.Device.Router.Router import Router
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.MenuBar.File.Open.OpenConst import OpenConst
util = Util()
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
fileMenu = File()
def main():
    util.init()
    save_noItemOnWorkspace()
    save_noItemOnWorkspaceCancel()
    save_itemOnWorkspaceCancel()
    save_saveItemOnWorkspace()  
    save_saveFileOpenedOnWorkspace()
    save_notSaveFileOpenedOnWorkspace()
    
def save_noItemOnWorkspace():
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.CANCEL_OPEN_FILE)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+S>")
    snooze(2)
    if(object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save File Window found")
    else:
        test.fail("Save File Window not found")
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Save.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(2)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    router0.doesNotExist()
    fileMenu.selectFileItem(FileConst.EXIT)
    startApplication(UtilConst.PACKETTRACER)
 
def save_noItemOnWorkspaceCancel():    
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+S>")
    snooze(2)
    util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    router0.doesNotExist()
    snooze(5)

def save_itemOnWorkspaceCancel():
    router0.create()   
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+S>")
    snooze(2)
    util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    router0.exists()
      
def save_saveItemOnWorkspace(): 
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+S>")
    snooze(2)
    if (object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save Dialog found")
    else:
        test.fail("Save Dialog not found")  
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Save.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(2)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    router0.exists()
    snooze(5)
    
def save_saveFileOpenedOnWorkspace():
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+S>")
    router0.exists()
def save_notSaveFileOpenedOnWorkspace():
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+S>")
    router0.exists()

