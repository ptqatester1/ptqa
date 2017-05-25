from API.Toolbar.GoldenSimulationToolbar.GoldenSimulationToolbarConst import GoldenSimulationToolbarConst
from API.Utility.Util import Util
from API.SimulationPanel.EventList.EventListConst import EventListConst
#Function initialization
util = Util()

#Device initialization

def main():
    util.init()
    checkPoint()

def checkPoint():
    util.clickOnSimulation()
    test.compare(findObject(EventListConst.SIMULATION_PANEL).visible, True)
    
    util.clickButton(GoldenSimulationToolbarConst.EVENT_LIST)
    test.compare(findObject(EventListConst.SIMULATION_PANEL).visible, False)
    
    util.clickButton(GoldenSimulationToolbarConst.EVENT_LIST)
    test.compare(findObject(EventListConst.SIMULATION_PANEL).visible, True)