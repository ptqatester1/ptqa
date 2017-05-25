from API.MenuBar.File.Save.SaveConst import SaveConst
from API.MenuBar.File.File import File
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.FileConst import FileConst
from API.Utility.Util import UtilConst
from API.Device.Router.Router import Router

util = Util()
fileMenu = File()
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")

def main():
    util.init()
    saveAs_noItemOnWorkspace()
    saveAs_noItemOnWorkspaceCancel()
    saveAs_itemOnWorkspaceCancel()
    saveAs_saveAsItemOnWorkspace()  
    saveAs_saveAsFileOpenedOnWorkspace()
    saveAs_notSaveFileOpenedOnWorkspace()
    
     
def saveAs_noItemOnWorkspace():
    fileMenu.selectFileItem(FileConst.SAVE_AS)
    snooze(1)
    if(object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save File Window found")
    else:
        test.fail("Save File Window not found")
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Save_As.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(1)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        snooze(1)
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    router0.doesNotExist()
    util.newWorkspace()
 
def saveAs_noItemOnWorkspaceCancel():
    fileMenu.selectFileItem(FileConst.SAVE_AS)
    snooze(2)
    util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    router0.doesNotExist()
def saveAs_itemOnWorkspaceCancel():
    router0.create()   
    fileMenu.selectFileItem(FileConst.SAVE_AS)
    snooze(2)
    util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    router0.exists()
def saveAs_saveAsItemOnWorkspace(): 
    fileMenu.selectFileItem(FileConst.SAVE_AS)
    snooze(1)
    if (object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save Dialog found")
    else:
        test.fail("Save Dialog not found")  
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Save_As.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(1)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        snooze(1)
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    router0.exists()
def saveAs_saveAsFileOpenedOnWorkspace():
    fileMenu.selectFileItem(FileConst.SAVE_AS)
    snooze(1)
    if (object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save Dialog found")
    else:
        test.fail("Save Dialog not found")  
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Save_As.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(1)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        snooze(1)
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    router0.exists()


def saveAs_notSaveFileOpenedOnWorkspace():
    fileMenu.selectFileItem(FileConst.SAVE_AS)
    snooze(1)
    if (object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save Dialog found")
    else:
        test.fail("Save Dialog not found")  
    util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    router0.exists()

