from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst
from API.ComponentBox import ComponentBoxConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Device.Router.Router import Router

from API.MenuBar.File.Open.OpenConst import OpenConst
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from API.MenuBar.File.Exit.ExitConst import ExitConst
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
util = Util()
commonToolsBar = CommonToolsBar()
fileMenu = File()
mainToolbar = MainToolbar()
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
    util.clickButton(MainToolbarConst.UNDO)
    util.clickOnWorkspace(router0.x, router0.y)
    snooze(2)
    try:
        router0.clickPhysicalTab()
        test.fail("router still exists")
    except LookupError, e:
        test.passes("router is gone")
        

def undoConnectDevice():
    router0.create()    
    router1.create()    
    util.connect(router0.x, router0.y, router1.x, router1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    snooze(2)
    util.clickButton(MainToolbarConst.UNDO)
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
    util.clickButton(MainToolbarConst.COPY)
    util.clickButton(MainToolbarConst.PASTE)
    util.clickOnWorkspace(copyrouter1.x, copyrouter1.y)
    copyrouter1.exists() 
    util.clickButton(MainToolbarConst.UNDO)
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
    util.clickButton(MainToolbarConst.UNDO)
    snooze(2)
    test.compare(findObject(UtilConst.PLACE_NOTE_LABEL).visible, False)
    
    mainToolbar.newNoSave()

def undoCreateCluster():
    router1.create()  
    util.selectObjectsOnWorkspace(router1.x, router1.y)
    snooze(1)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    snooze(1)
    util.clickOnWorkspace(router1.x, router1.y)
    snooze(2)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Cluster0]")
    util.clickButton(MainToolbarConst.UNDO)
    util.clickOnWorkspace(router1.x, router1.y)
    snooze(2)
    #Undo from within the cluster was removed in 7.0
    #test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Root]")

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
    snooze(2)
    util.clickButton(MainToolbarConst.UNDO)
    util.clickOnWorkspace(router1.x, router1.y)
    snooze(2)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Cluster0]")