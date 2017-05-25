from API.ComponentBox import ComponentBoxConst
from API.Device.AccessPoint.AccessPoint import AccessPoint

from API.Device.EndDevice.PC.PC import PC
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbar import GoldenPhysicalToolbar
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from API.Utility.Util import Util

#Function initialization
goldenPhysicalToolbar = GoldenPhysicalToolbar()
mainToolbar = MainToolbar()
util = Util()

#Device initialization
accessPoint0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 150, 100, "Access Point0")

def main():
    util.init()
    createTopology()
    checkPoint1()
    mainToolbar.newNoSave()
    createTopology()
    checkPoint2()
    mainToolbar.newNoSave()
    createTopology()
    checkPoint3()
    mainToolbar.newNoSave()
    createTopology()
    checkPoint4()

def createTopology():
    accessPoint0.create()    

def checkPoint1():
    util.clickOnPhysical()
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.Home City.Corporate Office.Main Wiring Closet.Rack_1.Access Point0")
    goldenPhysicalToolbar.moveRackDevice(1, 1, "Intercity", 0, 0)
    util.clickButton(GoldenPhysicalToolbarConst.GO_TO_BUILDING)
    util.clickButton(GoldenPhysicalToolbarConst.GO_TO_CITY)
    util.clickButton(GoldenPhysicalToolbarConst.GO_TO_INTERCITY)    
    
    util.clickOnPhysicalWorkspace(60, 48)
    accessPoint0.updateName()
    try:
        accessPoint0.clickPhysicalTab()
        test.passes("Access Point was moved")
    except LookupError, e:
        test.fail("Access Point wasn't moved")

def checkPoint2():
    util.clickOnPhysical()

    util.clickButton(GoldenPhysicalToolbarConst.NEW_CITY)
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.Home City.Corporate Office.Main Wiring Closet.Rack_1.Access Point0")
    goldenPhysicalToolbar.moveRackDevice(1, 1, "City/City", 0, 0)
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.City_1")
    
    util.clickOnPhysicalWorkspace(60, 48)
    accessPoint0.updateName()
    try:
        accessPoint0.clickPhysicalTab()
        test.passes("Access Point was moved")
    except LookupError, e:
        test.fail("Access Point wasn't moved")

def checkPoint3():
    util.clickOnPhysical()
    util.clickButton(GoldenPhysicalToolbarConst.NEW_BUILDING)
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.Home City.Corporate Office.Main Wiring Closet.Rack_1.Access Point0")
    goldenPhysicalToolbar.moveRackDevice(1, 1, "Office Building/Office Building", 0, 0)
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.Office Building")
    
    util.clickOnPhysicalWorkspace(60, 48)
    accessPoint0.updateName()
    try:
        accessPoint0.clickPhysicalTab()
        test.passes("Access Point was moved")
    except LookupError, e:
        test.fail("Access Point wasn't moved")

def checkPoint4():
    util.clickOnPhysical()
    util.clickButton(GoldenPhysicalToolbarConst.NEW_CLOSET)
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.Home City.Corporate Office.Main Wiring Closet.Rack_1.Access Point0")
    goldenPhysicalToolbar.moveRackDevice(1, 1, "Wiring Closet", 0, 0)
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.Wiring Closet")
    util.click_x_y(":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CRackView1.qt_scrollarea_viewport.CRackViewWidget1.CRack1.CModuleContainer1", 222, 255)
    accessPoint0.updateName()
    try:
        accessPoint0.clickPhysicalTab()
        test.passes("Access Point was moved")
    except LookupError, e:
        test.fail("Access Point wasn't moved")
