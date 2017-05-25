from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbar import GoldenLogicalToolbar
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.ComponentBox import ComponentBoxConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Device.Router.Router import Router
from API.Toolbar.MainToolBar.PaletteWindow import PaletteWindow
from API.Toolbar.MainToolBar.PaletteWindowConst import PaletteWindowConst
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.MenuBar.File.Open.OpenConst import OpenConst
import os

util = Util()
commonToolsBar = CommonToolsBar()
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 100, "Router1")
copyrouter1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 50, "CopyRouter2")
goldenLogicalToolbar = GoldenLogicalToolbar()
paletteWindow = PaletteWindow()

def main():
    util.init()
    createRootCluster()
    createLayer1Cluster()
    createLayer2Cluster()
    moveRouterFromLayer2ToRoot()
    createClusterOfNoteShapeRouter()
    
def createRootCluster():
    router0.create()    
    snooze(1)
    util.selectObjectsOnWorkspace(router0.x, router0.y)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    util.clickOnWorkspace(router0.x, router0.y+30)
    snooze(2)
    util.setText(GoldenLogicalToolbarConst.CLUSTER_NAME_EDIT, "RootCluster")
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)     
    util.clickOnWorkspace(router0.x, router0.y)
    snooze(2)
    #if (os.name=='posix'):
    #    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[RootClusterCluster0]")
    #else:
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[RootCluster]")    

def createLayer1Cluster():
    util.selectObjectsOnWorkspace(router0.x, router0.y)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    util.clickOnWorkspace(router0.x, router0.y+30)
    util.setText(GoldenLogicalToolbarConst.CLUSTER_NAME_EDIT, "ClusterLayer1")
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL) 
    util.clickOnWorkspace(router0.x, router0.y)
    snooze(2)
    #if (os.name=='posix'):
    #    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[ClusterLayer1Cluster0]")
    #else:
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[ClusterLayer1]")   
    
def createLayer2Cluster():
    util.selectObjectsOnWorkspace(router0.x, router0.y)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    util.clickOnWorkspace(router0.x, router0.y+30)
    util.setText(GoldenLogicalToolbarConst.CLUSTER_NAME_EDIT, "ClusterLayer2")
    util.clickButton(MainToolbarConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL) 
    util.selectObjectsOnWorkspace(router0.x, router0.y)
    snooze(2)
    #if (os.name=='posix'):
    #    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "ClusterLayer2Cluster0")
    #else:
        # Verification Point 'VP1'
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[ClusterLayer1]")

def moveRouterFromLayer2ToRoot():
    util.clickButton(GoldenLogicalToolbarConst.MOVE_OBJECT)

    util.clickOnWorkspace(router0.x, router0.y)
    snooze(1)
    util.activateItem(GoldenLogicalToolbarConst.MOVE_DROPDOWN, "Move to Root")
    util.clickOnWorkspace(router0.x, router0.y)
    router0.doesNotExist()
    util.clickButton(GoldenLogicalToolbarConst.CLUSTER_BACK)
    util.clickOnWorkspace(router0.x, router0.y+30)
    snooze(2)
    #if (os.name=='posix'):
    #    test.compare(findObject(UtilConst.DEVICE_LABEL).text, "ClusterLayer2Cluster0")
    #else:
    test.compare(findObject(UtilConst.DEVICE_LABEL).plainText, "ClusterLayer1")
    util.clickOnWorkspace(router0.x, router0.y)
    util.clickButton(GoldenLogicalToolbarConst.CLUSTER_BACK)
    util.clickButton(GoldenLogicalToolbarConst.CLUSTER_BACK)
    snooze(2)
    test.compare(findObject(GoldenLogicalToolbarConst.CLUSTER_CURRENT_CLUSTER).text, "[Root]")
    util.mouseDrag(UtilConst.WORKSPACE, router0.x, router0.y, router0.x + 300, router0.y)
    util.clickOnWorkspace(504, 201)
    util.clickOnWorkspace(router0.x, router0.y)
    router0.exists()

def createClusterOfNoteShapeRouter():
    commonToolsBar.addPlaceNote("cluster", router0.x + 50, router0.y + 50)
    paletteWindow.drawShapeWithDefaultColor('rectangle', True, router0.x, router0.y, router0.x + 1, router0.y)
    util.mouseDrag(UtilConst.WORKSPACE, 0, 0, router0.x + 700, router0.y + 400)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    util.mouseDrag(UtilConst.WORKSPACE, 0, 0, router0.x + 700, router0.y + 400)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    util.mouseDrag(UtilConst.WORKSPACE, 0, 0, router0.x + 700, router0.y + 400)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
