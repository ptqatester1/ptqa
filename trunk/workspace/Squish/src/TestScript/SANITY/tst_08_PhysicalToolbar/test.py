#######################
#@author: Pamela Vinco
#######################
from API.Utility.Util import Util
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst

#Function initialization
util = Util()

def main():
    util.init()
    util.clickOnPhysical()
    newCity()
    newBuilding()
    newCloset()
    grid()
    setBackground()
    moveAndNavigate()
    workingCloset()
    back()
    
def newCity():
    #Click on New City and check that a new city is created
    util.clickButton(GoldenPhysicalToolbarConst.NEW_CITY)
    NewCity = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.QGraphicsItem_2"
    test.compare(findObject(NewCity).visible, True)

def newBuilding():
    #Click on New Building and check that a new building is created
    util.clickButton(GoldenPhysicalToolbarConst.NEW_BUILDING)
    NewBuilding = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.QGraphicsItem_4"
    snooze(1)
    test.compare(findObject(NewBuilding).visible, True)
    
def newCloset():
    #Click on New Closet and check that a new closet is created
    util.clickButton(GoldenPhysicalToolbarConst.NEW_CLOSET)
    NewCloset = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.QGraphicsItem_6"
    snooze(1)
    test.compare(findObject(NewCloset).visible, True)
    
def grid():
    #Click on Grid and check that the Grid Dialog appears
    util.clickButton(GoldenPhysicalToolbarConst.GRID)
    if object.exists(GoldenPhysicalToolbarConst.GRID_DIALOG):
        test.passes("Grid Dialog found")
        util.close(GoldenPhysicalToolbarConst.GRID_DIALOG)
    else:
        test.fail("Grid Dialog not found")
        
    test.log("Check setting of grid manually since screenshot checkpoints are very unreliable.")
    
def setBackground():
    #Click on Set Background and check that the Set Background Dialog appears
    util.clickButton(GoldenPhysicalToolbarConst.SET_BACKGROUND)
    if object.exists(GoldenPhysicalToolbarConst.SET_BACKGROUND_DIALOG):
        test.passes("Select Background Dialog found")
        util.close(GoldenPhysicalToolbarConst.SET_BACKGROUND_DIALOG)
    else:
        test.fail("Select Background Dialog not found")
        
    test.log("Check setting of background image manually since screenshot checkpoints are very unreliable.")
    
def moveAndNavigate():
    #Move the New Building
    NewBuilding = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.QGraphicsItem_4"
    util.clickButton(GoldenPhysicalToolbarConst.MOVE_OBJECT)
    util.click(NewBuilding)
    util.activateItem(GoldenPhysicalToolbarConst.MOVE_DROPDOWN, "City")
    util.activateItem(GoldenPhysicalToolbarConst.MOVE_OBJECT_POPUP_MENU + ".City", "Move to City")
    
    #Click on Navigate and check that the Navication Dialog appears
    util.clickButton(GoldenPhysicalToolbarConst.NAVIGATION)
    if object.exists(GoldenPhysicalToolbarConst.NAVIGATION_DIALOG):
        test.passes("Navigation Dialog found")
        util.clickItem(GoldenPhysicalToolbarConst.NAVIGATION_LIST, "Intercity_1.City_1")
        util.clickButton(GoldenPhysicalToolbarConst.JUMP_TO_SELECTED_LOCATION)
        util.close(GoldenPhysicalToolbarConst.NAVIGATION_DIALOG)
    else:
        test.fail("Navigation Dialog not found")
    
    #Check that the object moved in the earlier steps is in the new location
    Building = ":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.QGraphicsItem_0"
    test.compare(findObject(Building).visible, True)
    
def workingCloset():
    #Click on Working Closet and check that the view changes to the working closet
    util.clickButton(GoldenPhysicalToolbarConst.WORKING_CLOSET)
    test.compare(findObject(GoldenPhysicalToolbarConst.RACK_VIEW).visible, True)
    
def back():
    #Click on Back and check that the view changes to Building View
    util.clickButton(GoldenPhysicalToolbarConst.GO_TO_BUILDING)
    util.textCheckPoint(GoldenPhysicalToolbarConst.GO_TO_BUILDING, "[ Corporate Office ]")
    
    #Click on Back and check that the view changes to City View
    util.clickButton(GoldenPhysicalToolbarConst.GO_TO_CITY)
    util.textCheckPoint(GoldenPhysicalToolbarConst.GO_TO_CITY, "[ Home City ]")

    #Click on Back and check that the view changes to Intercity View
    util.clickButton(GoldenPhysicalToolbarConst.GO_TO_INTERCITY)
    util.textCheckPoint(GoldenPhysicalToolbarConst.GO_TO_CITY, "[ Intercity ]")