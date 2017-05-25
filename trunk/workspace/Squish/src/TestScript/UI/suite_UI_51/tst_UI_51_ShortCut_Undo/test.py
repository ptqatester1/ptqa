from API.MenuBar.Edit.EditConst import EditConst
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Device.Router.Router import Router

from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from API.MenuBar.File.Exit.ExitConst import ExitConst
from API.Workspace.Physical import Physical

editMenu = Edit()
fileMenu = File()
mainToolbar = MainToolbar()
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
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    nativeType("<Ctrl+z>")
    snooze(2)
    util.clickOnWorkspace(router0.x, router0.y)
    try:
        router0.clickPhysicalTab()
        test.fail("router still exists")
    except LookupError, e:
        test.passes("router is gone")

def undoConnectDevice():
    router0.create()    
    router1.create()    
    util.connect(router0.x, router0.y, router1.x, router1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    nativeType("<Ctrl+z>")
    snooze(2)
    util.connect(router0.x, router0.y, router1.x, router1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.connect(router0.x, router0.y, router1.x, router1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    snooze(2)
    if (not object.exists(UtilConst.CONNECTION_ERROR_OK)):
        test.passes("cable was removed")
    else:
        test.fail("cable wasn't removed")
        util.clickButton(UtilConst.CONNECTION_ERROR_OK)
    snooze(2)
    nativeType("<Escape>")

def undoCopyDevice():
    util.selectObjectsOnWorkspace(router1.x, router1.y)
    snooze(2)
    editMenu.selectEditItem(EditConst.COPY)
    editMenu.selectEditItem(EditConst.PASTE)
    util.clickOnWorkspace(copyrouter1.x, copyrouter1.y)
    copyrouter1.exists() 
    nativeType("<Ctrl+z>")
    snooze(2)
    copyrouter1.doesNotExist() 
        
def undoCreateNote():
    commonToolsBar.addPlaceNote("Edit_Menu_Undo", 300, 100)
    snooze(2)
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)  
    snooze(2)
    util.textCheckPoint(UtilConst.PLACE_NOTE_LABEL, "Edit_Menu_Undo")
    snooze(2)
    nativeType("<Ctrl+z>")
    snooze(2)
    test.compare(findObject(UtilConst.PLACE_NOTE_LABEL).visible, False)
    
    mainToolbar.newNoSave()
    
def undoCreateCluster():
    router1.create()  
    util.selectObjectsOnWorkspace(router1.x, router1.y)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    snooze(1)
    nativeType("<Ctrl+z>")
    snooze(2)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Root]")
    router1.select()
    router1.clickTab('CLI')
    router1.close()
    
def undoDeleteCluster():
    util.selectObjectsOnWorkspace(router1.x, router1.y)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    util.clickOnWorkspace(router1.x, router1.y)
    snooze(1)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Cluster0]")
    util.clickButton(GoldenLogicalToolbarConst.CLUSTER_BACK)
    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    util.clickOnWorkspace(router1.x, router1.y)
    util.clickButton(CommonToolsBarConst.DELETE_CLUSTER_DIALOG_DELETE_CLUSTER)
    snooze(2)
    util.clickButton(CommonToolsBarConst.SELECT_TOOL)
    nativeType("<Ctrl+z>")
    snooze(2)
    util.clickOnWorkspace(router1.x, router1.y)
    snooze(1)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Cluster0]")