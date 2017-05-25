from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization

def main():
    util.init()
    util.clickOnPhysical()
    checkPoint()

def checkPoint():
    util.clickButton(GoldenPhysicalToolbarConst.NEW_CITY)
    snooze(2)
    # Verification Point 'VP1'
    test.compare(findObject(":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.QGraphicsItem_2").toolTip, "City")
    # Verification Point 'VP3'
    test.compare(findObject(":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.QGraphicsItem_2").visible, True)
    
