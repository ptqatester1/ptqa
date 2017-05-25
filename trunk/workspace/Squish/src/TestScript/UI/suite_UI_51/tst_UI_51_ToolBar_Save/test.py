from API.MenuBar.File.Save.SaveConst import SaveConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import UtilConst
from API.Device.Router.Router import Router
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
util = Util()
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")

def main():
    util.init()
    save_noItemOnWorkspace()
    save_noItemOnWorkspaceCancel()
    save_itemOnWorkspaceCancel()
    save_saveItemOnWorkspace()  
    save_saveFileOpenedOnWorkspace()
    save_notSaveFileOpenedOnWorkspace()
    
def save_noItemOnWorkspace():
    util.clickButton(MainToolbarConst.SAVE)
    snooze(2)
    if(object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save File Window found")
    else:
        test.fail("Save File Window not found")
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Save.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(2)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        snooze(1)
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    router0.doesNotExist()
    util.newWorkspace()
 
def save_noItemOnWorkspaceCancel():
    util.clickButton(MainToolbarConst.SAVE)
    snooze(2)
    util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    router0.doesNotExist()

def save_itemOnWorkspaceCancel():
    router0.create()   
    util.clickButton(MainToolbarConst.SAVE)
    snooze(2)
    util.clickButton(SaveConst.CANCEL_SAVE_FILE)      
    router0.exists()
      
def save_saveItemOnWorkspace(): 
    util.clickButton(MainToolbarConst.SAVE)
    snooze(2)
    if (object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save Dialog found")
    else:
        test.fail("Save Dialog not found")  
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Save.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(2)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        snooze(1)
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    router0.exists()
    
def save_saveFileOpenedOnWorkspace():
    util.clickButton(MainToolbarConst.SAVE)

    router0.exists()
def save_notSaveFileOpenedOnWorkspace():
    util.clickButton(MainToolbarConst.SAVE)

    router0.exists()