from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Utility.Util import Util
from API.Utility.Util import UtilConst

#Function initialization
util = Util()

def main():
    util.init()
    openFile()
    checkpoint()
    
def openFile():
    util.open("UI2_Zoom.pkt", UtilConst.UI_TEST)
    
def checkpoint():
    '''
    normal zoom
    zoom in (4 times)
    reset
    zoom out (4 times)
    reset
    '''
    checkVbar(3550, 3600, 'Normal view')
    zoomin()
    checkVbar(3950, 4000, 'Zoom in 1')
    zoomin()
    checkVbar(4350, 4400, 'Zoom in 2')
    zoomin()
    checkVbar(4750, 4800, 'Zoom in 3')
    zoomin()
    checkVbar(5150, 5200, 'Zoom in 4')
    reset()
    checkVbar(3550, 3600, 'Reset')
    zoomout()
    checkVbar(3150, 3200, 'Zoom out 1')
    zoomout()
    checkVbar(2750, 2800, 'Zoom out 2')
    zoomout()
    checkVbar(2350, 2400, 'Zoom out 3')
    zoomout()
    checkVbar(1950, 2000, 'Zoom out 4')
    reset()
    checkVbar(3550, 3600, 'Reset')
    None
    
def checkVbar(lowRange, highRange, failMessage):
    currentMax = findObject(UtilConst.WORKSPACE_SCROLL_VBAR).maximum
    if (lowRange <= currentMax <= highRange):
        test.passes("Pass")
    else:
        test.fail(failMessage)

def zoomin():
    util.clickButton(MainToolbarConst.ZOOM_IN)

def zoomout():
    util.clickButton(MainToolbarConst.ZOOM_OUT)

def reset():
    util.clickButton(MainToolbarConst.ZOOM_RESET)
    