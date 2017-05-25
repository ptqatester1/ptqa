from API.MenuBar.Edit.EditConst import EditConst
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Device.Router.Router import Router

from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.MenuBar.File.Exit.ExitConst import ExitConst
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
editMenu = Edit()
fileMenu = File()
util = Util()
commonToolsBar = CommonToolsBar()
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 100, "Router1")
copyrouter1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 50, "CopyRouter2")
def main():
    util.init()
    undoCreateDevice()
    undoConnectDevice()
    undoCopyDevice()
    undoCreateNote()
    undoCreateCluster()
    undoDeleteCluster()

def undoCreateDevice():
    router0.create()    
    editMenu.selectEditItem(EditConst.UNDO)
    util.clickOnWorkspace(router0.x, router0.y)
    snooze(2)
    router0.doesNotExist()
    
def undoConnectDevice():
    router0.create()    
    router1.create()    
    util.connect(router0.x, router0.y, router1.x, router1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    snooze(2)
    editMenu.selectEditItem(EditConst.UNDO)
    util.connect(router0.x, router0.y, router1.x, router1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.connect(router0.x, router0.y, router1.x, router1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    snooze(2)
    if (not object.exists(UtilConst.CONNECTION_ERROR_POPUP)):
        test.passes("cable was removed")
    else:
        test.fails("cable wasn't removed")
        util.clickButton(UtilConst.CONNECTION_ERROR_OK)
    

def undoCopyDevice():
    util.selectObjectsOnWorkspace(router1.x, router1.y)
    snooze(2)
    editMenu.selectEditItem(EditConst.COPY)
    editMenu.selectEditItem(EditConst.PASTE)
    util.clickOnWorkspace(copyrouter1.x, copyrouter1.y)
    copyrouter1.exists() 
    editMenu.selectEditItem(EditConst.UNDO)
    copyrouter1.doesNotExist() 
        
def undoCreateNote():
    commonToolsBar.addPlaceNote("Edit_Menu_Undo", 300, 100)
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)  
    # Verification Point 'VP3'
    util.clickOnWorkspace(345, 106)
    snooze(2)

    test.compare(findObject(CommonToolsBarConst.PLACENOTE_TEXT_EDIT).plainText, "Edit_Menu_Undo")
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)  
    snooze(2)
    editMenu.selectEditItem(EditConst.UNDO)
    snooze(2)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_NAME_EDIT).visible, False)
    util.typeText(UtilConst.WORKSPACE, "<Alt+F4>")
    snooze(2)
    if (object.exists(ExitConst.SAVE_NETWORK_PROMPT)):
        test.passes("Save Network Prompt found")
        util.clickButton(ExitConst.SAVE_NETWORK_PROMPT_NO)

    
def undoCreateCluster():
    startApplication(UtilConst.PACKETTRACER)
    router1.create()  
    util.selectObjectsOnWorkspace(router1.x, router1.y)
    snooze(1)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    snooze(1)
    editMenu.selectEditItem(EditConst.UNDO)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Root]")
    router1.select()
    router1.clickTab('CLI')
    router1.close()

    
def undoDeleteCluster():
    util.selectObjectsOnWorkspace(router1.x, router1.y)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    util.clickOnWorkspace(router1.x, router1.y)
    snooze(2)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Cluster0]")
    util.clickButton(GoldenLogicalToolbarConst.CLUSTER_BACK)
    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    util.clickOnWorkspace(router1.x, router1.y)
    util.clickButton(CommonToolsBarConst.DELETE_CLUSTER_DIALOG_DELETE_CLUSTER)
    snooze(2)
    util.clickButton(CommonToolsBarConst.SELECT_TOOL)
    editMenu.selectEditItem(EditConst.UNDO)
    util.clickOnWorkspace(router1.x, router1.y)
    snooze(2)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Cluster0]")