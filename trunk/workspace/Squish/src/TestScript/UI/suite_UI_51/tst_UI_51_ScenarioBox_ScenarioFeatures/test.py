from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.UserCreatedPacketWindow.ScenarioBox import ScenarioBox
from API.UserCreatedPacketWindow.ScenarioBox import ScenarioBoxConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.UserCreatedPacketWindow.UserCreatedPDUListConst import UserCreatedPDUListConst
from API.Utility.Util import Util

#Function initialization
util = Util()
commonToolsBar = CommonToolsBar()
scenarioBox = ScenarioBox()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 200, "PC1")

def main():
    util.init()
    scenario1()
    createTopology()
    configure_PCs()
    scenario2()
    deleteScenario()

def scenario1():
    ScenarioBox().expandScenarioToggle()
    util.clickButton(ScenarioBoxConst.SCENARIO_DESCRIPTION)
    test.compare(findObject(ScenarioBoxConst.SCENARIO_DESCRIPTION_WINDOW).enabled, True)
    scenarioBox.addScenarioDescription("Scenario 0", "This is the first scenario")
    
    util.clickButton(ScenarioBoxConst.SCENARIO_DESCRIPTION)    
    util.click(ScenarioBoxConst.SCENARIO_DESCRIPTION_WINDOW)
    util.nativeType("<Ctrl+a>")
    test.compare(findObject(ScenarioBoxConst.SCENARIO_DESCRIPTION_TEXT).selectedText, "This is the first scenario")

def createTopology():
    pc0.create()
    pc1.create()
    pc0.connect(pc1, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    
def configure_PCs():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.setIPConfiguration("192.168.1.1", "", "", "")
    pc0.desktop.ipConfiguration.close()
    
    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.ipConfiguration()
    pc1.desktop.ipConfiguration.setIPConfiguration("192.168.1.2", "", "", "")
    pc1.desktop.ipConfiguration.close()
    commonToolsBar.addSimplePDU(pc0.x, pc0.y, pc1.x, pc1.y)
  
def scenario2():
    util.clickButton(ScenarioBoxConst.NEW_SCENARIO)
    snooze(2)
    test.compare(findObject(UserCreatedPDUListConst.PDU_LIST).topLevelItemCount, 0)
    util.clickButton(ScenarioBoxConst.SCENARIO_DESCRIPTION)
    util.click(ScenarioBoxConst.SCENARIO_DESCRIPTION_WINDOW)
    util.setText(ScenarioBoxConst.SCENARIO_DESCRIPTION_TEXT, "<Ctrl+a>")
    test.compare(findObject(ScenarioBoxConst.SCENARIO_DESCRIPTION_TEXT).innerText, "")
    
def deleteScenario():
    util.clickButton(UserCreatedPDUListConst.EXPAND_LIST_BUTTON)
    scenarioBox.selectScenario("Scenario 0")
    util.clickButton(ScenarioBoxConst.SCENARIO_DESCRIPTION)
    util.click(ScenarioBoxConst.SCENARIO_DESCRIPTION_WINDOW)
    util.setText(ScenarioBoxConst.SCENARIO_DESCRIPTION_TEXT, "<Ctrl+a>")
    test.compare(findObject(ScenarioBoxConst.SCENARIO_DESCRIPTION_TEXT).selectedText, "This is the first scenario")
    util.clickButton(ScenarioBoxConst.DELETE_SCENARIO)
    snooze(2)
    util.textCheckPoint(ScenarioBoxConst.SCENARIO_NAME_TEXT, "Scenario 1")
