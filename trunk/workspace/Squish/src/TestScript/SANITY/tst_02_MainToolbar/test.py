##Chris Allen
##Pamela Vinco (modified and added a few more checks)
##Sanity test to check if all of the buttons on the main tool bar work

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.MenuBar.File.Print.PrintConst import PrintConst
from API.Device.Router.Router import Router
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.Save.SaveConst import SaveConst
from API.Toolbar.MainToolBar.CustomDeviceWindowConst import CustomDeviceWindowConst
from API.Toolbar.MainToolBar.PaletteWindowConst import PaletteWindowConst

util = Util()
mtb = MainToolbar()

r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
cpR0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 80, 45, "CopyRouter0")

def main():
    createDevices()
    newFile()
    
    createDevices()
    saveFile()
    
    util.init()
    openFile()
    
    printFile()
    
    util.init()
    goToAW()
    util.init()
    util.closePT()
    
    startApplication(UtilConst.PACKETTRACER)
    util.init()
    createDevices()
    copyAndPaste()
    
    undoRedo()
    zoomInOutReset()
    
    drawingPalette()
    customDevices()
    
def createDevices():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    
def newFile():
    #Click on New and check that the device created earlier is removed
    mtb.newNoSave()
    r0.doesNotExist()
    
def saveFile():
    #Click on Save and check that the overwrite prompt appears (saving works)
    mtb.saveFile(util.getFilePath("checkMTB_Buttons.pkt", UtilConst.SANITY_TEST))
    if(object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        test.passes("Overwrite prompt appears")
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    
def openFile():
    #Click on Open, select previously saved file and check that the device exists (file was opened)
    mtb.openFile(util.getFilePath("checkMTB_Buttons.pkt", UtilConst.SANITY_TEST))
    r0.exists()
    
def printFile():
    #Click on Print and check that the Print Dialog appears
    util.clickButton(MainToolbarConst.PRINT)
    snooze(1)
    if(object.exists(PrintConst.PRINT_DIALOG_WINDOW)):
        test.passes("Print Window found")
        util.close(PrintConst.PRINT_DIALOG_WINDOW)
    else:
        test.fail("Print Window not found")
        
def goToAW():
    #Click on Activity Wizard and check that PT goes to Activity Wizard mode
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    snooze(1)
    if(object.exists(ActivityWizardConst.ACTIVITY_WIZARD_WINDOW)):
        test.passes("Activity Wizard Window found")
    else:
        test.fail("Activity Wizard Window not found")
    
def copyAndPaste():
    #Select router, click on Copy, click on Paste and check that the device copy exists
    util.selectObjectsOnWorkspace(r0.x, r0.y)
    util.clickButton(MainToolbarConst.COPY)
    util.clickButton(MainToolbarConst.PASTE)
    cpR0.exists()
    
def undoRedo():
    #Click on Undo and check that the copy of the device is removed from the workspace
    mtb.clickButton(MainToolbarConst.UNDO)
    cpR0.doesNotExist()
        
    #Click on Redo and check that the copy of the device is back on the workspace
    mtb.clickButton(MainToolbarConst.REDO)
    cpR0.exists()

def zoomInOutReset():
    #Click Zoom In and check that the vertical scrollbar on the workspace changes value
    mtb.click(MainToolbarConst.ZOOM_IN)
    zoomedIn = findObject(UtilConst.WORKSPACE_SCROLL_VBAR)
    if(zoomedIn.maximum >= 1750):
        test.passes("Zoom in works")
    else:
        test.fail("Zoom is not working properly")
        
    #Click Zoom Reset and check that the vertical scrollbar on the workspace changes value
    mtb.click(MainToolbarConst.ZOOM_RESET)
    zoomReset = findObject(UtilConst.WORKSPACE_SCROLL_VBAR)
    if(zoomReset.maximum >= 1550 and zoomReset.maximum <= 1650):
        test.passes("Zoom reset works")
    else:
        test.fail("Zoom is not working properly")
        
    #Click Zoom Out and check that the vertical scrollbar on the workspace changes value
    mtb.click(MainToolbarConst.ZOOM_OUT)
    zoomedOut = findObject(UtilConst.WORKSPACE_SCROLL_VBAR)
    if(zoomedOut.maximum <= 1400):
        test.passes("Zoom out works")
    else:
        test.fail("Zoom is not working properly")
    
def drawingPalette():    
    #Click on Drawing Palette and check that the Drawing Palette Window appears
    util.clickButton(MainToolbarConst.PALETTE)
    snooze(1)
    if(object.exists(PaletteWindowConst.PALETTE_WINDOW)):
        test.passes("Palette Window found")
        util.close(PaletteWindowConst.PALETTE_WINDOW)
    else:
        test.fail("Palette Window not found")
        
def customDevices():
    #Click Custom Devices Dialog and check that the Custom Devices Dialog appears
    util.clickButton(MainToolbarConst.CUSTOM_DEVICES)
    snooze(1)
    if(object.exists(CustomDeviceWindowConst.CUSTOM_DEVICE_WINDOW)):
        test.passes("Custom Device Window found")
        util.close(CustomDeviceWindowConst.CUSTOM_DEVICE_WINDOW)
    else:
        test.fail("Custom Device Window not found")