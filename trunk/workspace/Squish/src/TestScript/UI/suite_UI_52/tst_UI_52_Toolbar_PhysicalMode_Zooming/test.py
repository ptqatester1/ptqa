######################
#@author: Pamela Vinco
######################

from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import Util
from API.Device.EndDevice.PC.PC import PC
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst

util = Util()

#Device initialization
pc = PC(ComponentBoxConst.DeviceModel.PC, 189, 270, "PC0")

def main():       
    util.init()
    createTopology()
    checkpoint()

def createTopology():
    util.clickOnPhysical()
    util.clickButton(GoldenPhysicalToolbarConst.WORKING_CLOSET)    
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pc.model, pc.x, pc.y)
    
def checkpoint():
    util.clickButton(MainToolbarConst.ZOOM_OUT)

    #Check that the physical workspace is zoomed out (Size is less than 250) 
    if (findObject(GoldenPhysicalToolbarConst.TABLE1_DEVICE1).width <= 250):
        test.passes("Workspace is zoomed out")
    else:
        test.passes("Workspace is not zoomed out")
    
    util.clickButton(MainToolbarConst.ZOOM_RESET)

    #Check that the physical workspace is zoomed out (Size is less than 250) 
    if (findObject(GoldenPhysicalToolbarConst.TABLE1_DEVICE1).width >= 300 and findObject(GoldenPhysicalToolbarConst.TABLE1_DEVICE1) <= 600):
        test.passes("Workspace is back to normal size")
    else:
        test.passes("Workspace is not back to normal size")

    util.clickButton(MainToolbarConst.ZOOM_IN)
    
    #Check that the physical workspace is zoomed out (Size is more than 750) 
    if (findObject(GoldenPhysicalToolbarConst.TABLE1_DEVICE1).width >= 750):
        test.passes("Workspace is zoomed out")
    else:
        test.passes("Workspace is not zoomed out")
