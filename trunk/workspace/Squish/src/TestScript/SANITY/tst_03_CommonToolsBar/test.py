#######################
#@author: Pamela Vinco
#######################
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Device.DeviceBase.DeviceBaseConst import DeviceBaseConst
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Toolbar.MainToolBar.PaletteWindowConst import PaletteWindowConst
from API.Toolbar.CommonToolsBar.ComplexPDUWindowConst import ComplexPDUWindowConst

#Function initialization
util = Util()
ctb = CommonToolsBar()

#Device initialization
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")

def main():
    util.init()
    createDevice()
    commonTools_select()
    commonTools_moveLayout()
    commonTools_placeNote()
    commonTools_delete()
    commonTools_inspect()
    commonTools_palette()
    commonTools_resize()
    commonTools_addSimplePDU()
    commonTools_addComplexPDU()
    
def createDevice():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    
def commonTools_select():
    #Use the Select tool to click on the router on the workspace and check that the device config dialog opens
    util.clickButton(CommonToolsBarConst.SELECT_TOOL)
    r0.select()
    if object.exists(r0.squishName +  DeviceBaseConst.DeviceTabs.DEVICE_TAB):
        test.passes("Select tool works")
        r0.close()
    else:
        test.fail("Select tool does not work")
    
def commonTools_moveLayout():
    test.log("Move Layout tool removed in PT6.1")
    
def commonTools_placeNote():
    #Use the Place Note tool and check that notes can be added on the workspace    
    ctb.addPlaceNote("TESTING", 200, 200)
    util.deselectObjectsOnWorkspace()
    util.clickOnWorkspace(200, 200)
    util.textCheckPoint(CommonToolsBarConst.PLACENOTE_TEXT_EDIT, "TESTING")
    
def commonTools_delete():
    #Use the Delete tool to remove the router on the workspace and check that the device does not exist anymore
    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    util.clickOnWorkspace(r0.x, r0.y)
    r0.doesNotExist()
    
    #Click on Undo to place the router on the workspace again 
    util.clickButton(MainToolbarConst.UNDO)
    
def commonTools_inspect():
    #Use the Inspect tool to open ARP table for the router and check that the table appears
    ctb.inspectDevice(r0.x, r0.y, CommonToolsBarConst.ARP_TABLE)
    snooze(1)
    if(object.exists(CommonToolsBarConst.ARP_TABLE_WINDOW + " for Router0")):
        test.passes("ARP Table Window found")
        util.close(CommonToolsBarConst.ARP_TABLE_WINDOW + " for Router0")
    else:
        test.fail("ARP Table Window not found")
    
def commonTools_palette():
    #Click on Drawing Palette and check that the Drawing Palette Window appears
    util.clickButton(CommonToolsBarConst.DRAW_TOOL)
    snooze(1)
    if(object.exists(PaletteWindowConst.PALETTE_WINDOW)):
        test.passes("Palette Window found")
        util.close(PaletteWindowConst.PALETTE_WINDOW)
    else:
        test.fail("Palette Window not found")
        
    test.log("Check that drawing lines and shapes work manually since it's hard to create reliable checkpoints for drawn objects")

def commonTools_resize():
    test.log("Check resizing of shapes manually since it's hard to create reliable checkpoints for resized objects")
    
def commonTools_addSimplePDU():
    #Use the Add Simple PDU tool to try and add a PDU to the router on the workspace and check that the No functional ports error message is found (meaning the tool is in Add Simple PDU mode)
    util.clickButton(CommonToolsBarConst.ADD_SIMPLE_PDU)
    util.clickOnWorkspace(r0.x, r0.y)
    util.clickOnWorkspace(r0.x-10, r0.y-10)
    if object.exists(UtilConst.NO_FUNCTIONAL_PORTS_ERROR):
        test.passes("No functional ports error message found")
        util.clickButton(UtilConst.NO_FUNCTIONAL_PORTS_ERROR_OK)
    else:
        test.fail("No functional ports error message not found")
    
def commonTools_addComplexPDU():
    #Use the Add Complex PDU tool to try and add a PDU to the router and check that the Complex PDU Window appears
    util.clickButton(CommonToolsBarConst.ADD_COMPLEX_PDU)
    util.clickOnWorkspace(r0.x, r0.y)
    if object.exists(ComplexPDUWindowConst.COMPLEX_PDU_WINDOW):
        test.passes("Complex PDU Window found")
    else:
        test.fail("Complex PDU Window not found")