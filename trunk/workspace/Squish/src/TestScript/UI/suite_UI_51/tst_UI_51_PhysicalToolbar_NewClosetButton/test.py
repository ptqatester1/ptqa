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
    util.clickButton(GoldenPhysicalToolbarConst.NEW_CLOSET)
    snooze(2)
    test.compare(findObject(":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.QGraphicsItem_2").toolTip, "Wiring Closet")
    # Verification Point 'VP3'
    test.compare(findObject(":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CGeoView1.QGraphicsItem_2").visible, True)
