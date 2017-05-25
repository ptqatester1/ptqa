from API.Utility.Util import Util
from API.Utility import UtilConst
from API.SimulationPanel.EventList.EventListConst import EventListConst

#Function initialization
util = Util()


def main():
    util.init()
    checkPoint()

def checkPoint():
    test.compare(findObject(UtilConst.SIMULATION_SWITCH).toolTip, "Simulation Mode (Shift+S)")
    test.compare(findObject(UtilConst.REALTIME_SWITCH).toolTip, "Realtime Mode (Shift+R)")
    
    util.clickOnSimulation()
    test.compare(findObject(EventListConst.SIMULATION_PANEL).visible, True)
    
    util.clickOnRealtime()
    test.compare(findObject(EventListConst.SIMULATION_PANEL).visible, False)