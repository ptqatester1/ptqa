from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbar import GoldenPhysicalToolbar
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Utility.Util import Util

#Function initialization
goldenPhysicalToolbar = GoldenPhysicalToolbar()
util = Util()

def main():
    util.init()
    util.clickOnPhysical()
    checkPoint()

def checkPoint():
    util.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)
    util.textCheckPoint(GoldenPhysicalToolbarConst.CURRENT_LOCATION_LABEL, "Current Location: Intercity")
    util.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)

    util.clickButton(GoldenPhysicalToolbarConst.NEW_CITY)
    util.clickButton(GoldenPhysicalToolbarConst.NEW_BUILDING)
    util.clickButton(GoldenPhysicalToolbarConst.NEW_CLOSET)
    
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.City_1")
    util.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)
    util.textCheckPoint(GoldenPhysicalToolbarConst.CURRENT_LOCATION_LABEL, "Current Location: City")
    util.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)
    
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.Office Building")
    util.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)
    util.textCheckPoint(GoldenPhysicalToolbarConst.CURRENT_LOCATION_LABEL, "Current Location: Office Building")
    util.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)
    
    goldenPhysicalToolbar.jumpToSelectedLocation("Intercity_1.Wiring Closet_1")
    util.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)
    util.textCheckPoint(GoldenPhysicalToolbarConst.CURRENT_LOCATION_LABEL, "Current Location: Wiring Closet")
    util.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)