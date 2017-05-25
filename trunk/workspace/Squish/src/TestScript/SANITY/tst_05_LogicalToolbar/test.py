#######################
#@author: Pamela Vinco
#######################
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst

#Function initialization
util = Util()

#Device initialization
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 200, "Router1")

def main():
    util.init()
    createDevice()
    logicalPhysicalSwitch()
    cluster()
    moveObject()
    setBackground()
    openViewport()
    
def createDevice():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    
def logicalPhysicalSwitch():
    #Click on Physical tab and check that the physical workspace is visible
    util.clickOnPhysical()
    test.compare(findObject(UtilConst.PHYSICAL_WORKSPACE).visible, True)
    #Click on Logical tab and check that the logical workspace is visible
    util.clickOnLogical()
    test.compare(findObject(UtilConst.WORKSPACE).visible, True)

def cluster():
    util.selectObjectsOnWorkspace(r0.x, r0.y)
    
    #Create a new cluster and check that the router gets moved inside the cluster
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
    
    #First checkpoint should not open the device dialog since it is going inside the cluster (device does not exist on this level)
    r0.doesNotExist()
    
    #Second checkpoint will open the device dialog since the earlier step brings us inside the cluster (device exists on this level)
    r0.exists()
    
    #Click on Back button and check that it bring us to the top level cluster (device does not exist on this level)
    util.clickButton(GoldenLogicalToolbarConst.CLUSTER_BACK)
    r0.doesNotExist()
    
def moveObject():
    #Create a new device inside the cluster
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r1.model, r1.x, r1.y)

    #Move the router out of the cluster
    util.clickButton(GoldenLogicalToolbarConst.MOVE_OBJECT)
    util.clickOnWorkspace(r1.x, r1.y)
    util.activateItem(GoldenLogicalToolbarConst.MOVE_DROPDOWN, "Move to Root")
    
    #Go back to the top level cluster and check that the device was moved (device exists on this level)
    util.clickButton(GoldenLogicalToolbarConst.CLUSTER_BACK)
    r1.exists()

def setBackground():
    #Click on Set Background and check that the Set Background Dialog appears
    util.clickButton(GoldenLogicalToolbarConst.SET_TILED_BACKGROUND)
    if object.exists(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_DIALOG):
        test.passes("Select Background Dialog found")
        util.close(GoldenLogicalToolbarConst.SELECT_BACKGROUND_IMAGE_DIALOG)
    else:
        test.fail("Select Background Dialog not found")
        
    test.log("Check setting of background image manually since screenshot checkpoints are very unreliable.")

def openViewport():
    #Click on Viewport and check that the Viewport appears
    util.clickButton(GoldenLogicalToolbarConst.VIEWPORT)
    if object.exists(GoldenLogicalToolbarConst.VIEWPORT_WINDOW):
        test.passes("Viewport found")
    else:
        test.fail("Viewport not found")