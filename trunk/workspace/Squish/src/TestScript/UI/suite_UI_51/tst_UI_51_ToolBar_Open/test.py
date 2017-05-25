from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.File.Save.SaveConst import SaveConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import UtilConst
from API.Device.Router.Router import Router
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst

util = Util()
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 200, 100, "Router1")

def main():
    util.init()
    open_noItemOnWorkspace()
    open_noItemOnWorkspaceCancel()
    open_itemOnWorkspaceCancel()
    open_saveItemOnWorkspace()  
    open_notSaveItemOnWorkspace()
    open_saveFileOpenedOnWorkspace()
    open_notSaveFileOpenedOnWorkspace()
    
     
def open_noItemOnWorkspace():
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    if(object.exists(OpenConst.OPEN_FILE_WINDOW)):
        test.passes("Open File Window found")
    else:
        test.fail("Open File Window not found")
    util.setText(OpenConst.OPEN_FILE_NAME, util.getFilePath("UI1_File_Menu_New.pkt", UtilConst.UI_TEST))
    util.clickButton(OpenConst.CONFIRM_OPEN_FILE)
    router0.exists()
    util.newWorkspace()
 
def open_noItemOnWorkspaceCancel():
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.CANCEL_OPEN_FILE)
    router0.doesNotExist()
    
def open_itemOnWorkspaceCancel():
    router1.create()   
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)     
    router1.exists()
    
def open_saveItemOnWorkspace(): 
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    if (object.exists(OpenConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
    else:
        test.fail("Save Network Prompt not found")
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_YES)
    snooze(2)
    if (object.exists(SaveConst.SAVE_FILE_NAME)):
        test.passes("Save Dialog found")
    else:
        test.fail("Save Dialog not found")  
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI1_File_Menu_Open.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    snooze(2)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    snooze(2)
    if(object.exists(OpenConst.OPEN_FILE_WINDOW)):
        test.passes("Open File Window found")
    else:
        test.fail("Open File Window not found")
    util.setText(OpenConst.OPEN_FILE_NAME, util.getFilePath("UI1_File_Menu_New.pkt", UtilConst.UI_TEST))
    util.clickButton(OpenConst.CONFIRM_OPEN_FILE)
    router0.exists()
    util.newWorkspace()
    
def open_notSaveItemOnWorkspace():
    router1.create()   
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    if (object.exists(OpenConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
    else:
        test.fail("Save Network Prompt not found")
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_NO)
    snooze(2)
    if(object.exists(OpenConst.OPEN_FILE_WINDOW)):
        test.passes("Open File Window found")
    else:
        test.fail("Open File Window not found")
    util.setText(OpenConst.OPEN_FILE_NAME, util.getFilePath("UI1_File_Menu_New.pkt", UtilConst.UI_TEST))
    util.clickButton(OpenConst.CONFIRM_OPEN_FILE)
    router0.exists()

    
def open_saveFileOpenedOnWorkspace():
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    if (object.exists(OpenConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
    else:
        test.fail("Save Network Prompt not found")
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_YES)
    snooze(2)
    if(object.exists(OpenConst.OPEN_FILE_WINDOW)):
        test.passes("Open File Window found")
    else:
        test.fail("Open File Window not found")
    util.setText(OpenConst.OPEN_FILE_NAME, util.getFilePath("UI1_File_Menu_Open.pkt", UtilConst.UI_TEST))
    util.clickButton(OpenConst.CONFIRM_OPEN_FILE)
    router1.exists()
    
def open_notSaveFileOpenedOnWorkspace():
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    if (object.exists(OpenConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
    else:
        test.fail("Save Network Prompt not found")
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_NO)
    snooze(2)
    if(object.exists(OpenConst.OPEN_FILE_WINDOW)):
        test.passes("Open File Window found")
    else:
        test.fail("Open File Window not found")
    util.setText(OpenConst.OPEN_FILE_NAME, util.getFilePath("UI1_File_Menu_Open.pkt", UtilConst.UI_TEST))
    util.clickButton(OpenConst.CONFIRM_OPEN_FILE)
    router1.exists()
    snooze(1)