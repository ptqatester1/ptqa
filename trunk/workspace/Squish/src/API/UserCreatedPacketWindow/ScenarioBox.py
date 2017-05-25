#********************************************************
#@author: Pam Vinco
#@summary: ScenarioBox handles all Scenario Box functions
#********************************************************
from API.SquishSyntax import SquishSyntax
from API.UserCreatedPacketWindow.ScenarioBoxConst import ScenarioBoxConst
from API.Utility import UtilConst
from API.Utility.Util import Util
util = Util()

class ScenarioBox:
    def __init__(self):
        self.util = Util()
        self.check = ScenarioBoxCheck()
        
    #@summary: Selects a scenario from the scenario dropdown list
    #@param p_item: Name of scenario to select
    #@note: p_item is not a constant, p_item is the EXACT name of the scenario in quotation marks (Scenario 1 = "Scenario 1")
    def selectScenario(self, p_scenario):
        Util().clickItem(ScenarioBoxConst.SCENARIO_DROPDOWN, p_scenario)
        
    def deleteButton(self):
        Util().clickButton(ScenarioBoxConst.DELETE_SCENARIO)
        
    def newButton(self):
        Util().clickButton(ScenarioBoxConst.NEW_SCENARIO)
    
    def deleteScenario(self, scenario):
        self.selectScenario(scenario)
        self.deleteButton()
        
    def addScenarioDescription(self, p_scenario, p_description):
        self.selectScenario(p_scenario)
        self.commonAddScenarioDescription(p_scenario, p_description)
    
    def changeScenarioName(self, p_scenario, p_name):
        self.selectScenario(p_scenario)
        self.commonChangeScenarioName(p_name)
    
    def createNewScenario(self, p_description, p_name):
        Util().clickButton(ScenarioBoxConst.NEW_SCENARIO)
        self.commonChangeScenarioName(p_name)
        self.commonAddScenarioDescription(p_name, p_description)

    def commonAddScenarioDescription(self, p_scenario, p_description):
        Util().clickButton(ScenarioBoxConst.SCENARIO_DESCRIPTION)
        for i in range(1,3):
            Util().click(ScenarioBoxConst.SCENARIO_DESCRIPTION_TEXT_FIRST_PART + p_scenario + ScenarioBoxConst.SCENARIO_DESCRIPTION_TEXT_LAST_PART)
            Util().snooze(1)
        Util().setText(ScenarioBoxConst.SCENARIO_DESCRIPTION_TEXT, p_description)
        Util().close(ScenarioBoxConst.SCENARIO_DESCRIPTION_WINDOW)
        
    def commonChangeScenarioName(self, p_name):
        Util().setText(ScenarioBoxConst.SCENARIO_NAME_TEXT, p_name)
        Util().typeText(ScenarioBoxConst.SCENARIO_NAME_TEXT, "\r")
    
    def expandScenarioToggle(self):
        Util().clickButton(ScenarioBoxConst.SCENARIO_BOX_EXPANDER)
        
class ScenarioBoxCheck:
    def __init__(self):
        self.util = Util()
        
    def scenarioName(self, scenarioName):
        Util().textCheckPoint(ScenarioBoxConst.SCENARIO_NAME_TEXT, scenarioName)