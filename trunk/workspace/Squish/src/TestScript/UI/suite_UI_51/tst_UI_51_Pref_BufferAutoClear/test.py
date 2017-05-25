from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Miscellaneous.MiscellaneousConst import MiscellaneousConst
from API.SimulationPanel.EventList.EventListConst import EventListConst
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.MenuBar.Options.Preferences.PreferencesConst import PreferencesConst

util = Util()
options = Options()
eventListFilters = EventListFilters()

def main():
    util.init()
    util.open("UI13.pkt", UtilConst.UI_TEST )
    util.speedUpConvergence()
    editOptionsSetting()
    checkpoint1()
    resetOptionsSetting()
    
def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(PreferencesConst.TAB_BAR, PreferencesConst.MISCELLANEOUS)
    util.clickButton(MiscellaneousConst.AUTO_CLEAR_EVENT_LIST)
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def checkpoint1():
    util.clickOnSimulation()
    util.clickButton(EventListConst.RESET_SIMULATION)
    for i in range(0, 8):
        util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(10)
    if (object.exists(PlayControlsConst.BUFFER_FULL_DIALOG_LABEL)):
        test.fail("Buffer window found")
    else:
        test.passes("Buffer window not found")
    
    
def resetOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(PreferencesConst.TAB_BAR, PreferencesConst.MISCELLANEOUS)
    util.clickButton(MiscellaneousConst.PROMPT)
    util.close(OptionsConst.OPTIONS_DIALOG)