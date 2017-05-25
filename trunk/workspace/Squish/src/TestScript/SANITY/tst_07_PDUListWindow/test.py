#######################
#@author: Pamela Vinco
#######################
from API.Utility.Util import Util
from API.UserCreatedPacketWindow.UserCreatedPDUListConst import UserCreatedPDUListConst
from API.UserCreatedPacketWindow.ScenarioBoxConst import ScenarioBoxConst

#Function initialization
util = Util()

def main():
    util.init()
    scenarioDescription()
    scenarioNew()
    scenarioDelete()
    togglePDU()
    
def scenarioDescription():
    #Click on Scenario Description and check that the Scenario Description Window appears
    util.clickButton(ScenarioBoxConst.SCENARIO_DESCRIPTION)
    if object.exists(ScenarioBoxConst.SCENARIO_DESCRIPTION_WINDOW):
        test.passes("Scenario Description Window found")
        util.close(ScenarioBoxConst.SCENARIO_DESCRIPTION_WINDOW)
    else:
        test.fail("Scenario Description Window not found")
        
def scenarioNew():
    #Click on New and check that Scenario 1 is created
    util.clickButton(ScenarioBoxConst.NEW_SCENARIO)
    util.textCheckPoint(ScenarioBoxConst.SCENARIO_NAME_TEXT, "Scenario 1")
    
def scenarioDelete():
    #Click on Delete and check that Scenario 1 is deleted
    util.clickButton(ScenarioBoxConst.DELETE_SCENARIO)
    util.textCheckPoint(ScenarioBoxConst.SCENARIO_NAME_TEXT, "Scenario 0")

def togglePDU():
    #Click on Toggle PDU List Window and check that the window goes into a different view
    test.compare(findObject(UserCreatedPDUListConst.PDU_LIST_TOGGLED_VIEW).visible, False)
    
    util.clickButton(ScenarioBoxConst.TOGGLE_PDU_LIST_WINDOW)
    
    #Click again on Toggle PDU List Window and check that the window goes into a different view
    test.compare(findObject(UserCreatedPDUListConst.PDU_LIST_TOGGLED_VIEW).visible, True)