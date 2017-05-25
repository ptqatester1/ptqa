from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst
from API.MenuBar.Options.Preferences.Administrative.AdministrativeConst import AdministrativeConst
from API.MenuBar.Options.Preferences.Administrative.Administrative import Administrative
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.File.Print.PrintConst import PrintConst
from API.MenuBar.File.Print.Print import Print
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
from API.ComponentBox import ComponentBoxConst
from API.UserCreatedPacketWindow.ScenarioBoxConst import ScenarioBoxConst
from API.UserCreatedPacketWindow.ScenarioBox import ScenarioBox

#Function initialization
util = Util()
filePrint = Print()
fileMenu = File()
administrative =Administrative()
optionsMenu = Options()

def main():
    util.init()
    fileMenu.selectFileItem(FileConst.OPEN)
    util.clickButton(OpenConst.CANCEL_OPEN_FILE)
    print_noItemOnWorkspace()
    print_itemOnWorkspace()
    print_simulationMode()
    print_togglePDUList()
    print_viewPort()

def print_noItemOnWorkspace():
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+P>")
    
    test.compare(findObject(PrintConst.PRINT_DIALOG_WINDOW).visible, True)
    
    test.compare(findObject(PrintConst.ACTIVITY_INSTRUCTION_RADIO).enabled, True)
    test.compare(findObject(PrintConst.VIEWABLE_LOGICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.ACTIVE_DOCKABLE_DIALOG_RADIO).enabled, False)
    test.compare(findObject(PrintConst.VIEWABLE_PHYSICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.IMAGE_OF_DIALOG_RADIO).enabled, True)
    test.compare(findObject(PrintConst.COMMAND_LINE_HISTORY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.DIALOG_LIST).count, 0)

    util.close(PrintConst.PRINT_DIALOG_WINDOW)
 
def print_itemOnWorkspace():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100)    
    util.clickOnWorkspace(100,100)

    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    
    snooze(2)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+P>")
    
    snooze(2)
    
    test.compare(findObject(PrintConst.PRINT_DIALOG_WINDOW).visible, True)
    
    test.compare(findObject(PrintConst.ACTIVITY_INSTRUCTION_RADIO).enabled, True)
    test.compare(findObject(PrintConst.VIEWABLE_LOGICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.ACTIVE_DOCKABLE_DIALOG_RADIO).enabled, False)
    test.compare(findObject(PrintConst.VIEWABLE_PHYSICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.IMAGE_OF_DIALOG_RADIO).enabled, True)
    test.compare(findObject(PrintConst.COMMAND_LINE_HISTORY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.DIALOG_LIST).count, 0)
    
    util.close(PrintConst.PRINT_DIALOG_WINDOW)
    
def print_simulationMode():
    util.clickOnSimulation()
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+P>")
    snooze(2)
    test.compare(findObject(PrintConst.PRINT_DIALOG_WINDOW).visible, True)
    
    test.compare(findObject(PrintConst.ACTIVITY_INSTRUCTION_RADIO).enabled, True)
    test.compare(findObject(PrintConst.VIEWABLE_LOGICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.ACTIVE_DOCKABLE_DIALOG_RADIO).enabled, False)
    test.compare(findObject(PrintConst.VIEWABLE_PHYSICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.IMAGE_OF_DIALOG_RADIO).enabled, True)
    test.compare(findObject(PrintConst.COMMAND_LINE_HISTORY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.DIALOG_LIST).count, 0)
    util.close(PrintConst.PRINT_DIALOG_WINDOW)
    util.clickOnRealtime()

def print_togglePDUList():
    ScenarioBox().expandScenarioToggle()
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+P>")
    snooze(2)
    test.compare(findObject(PrintConst.ACTIVITY_INSTRUCTION_RADIO).enabled, True)
    test.compare(findObject(PrintConst.VIEWABLE_LOGICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.ACTIVE_DOCKABLE_DIALOG_RADIO).enabled, False)
    test.compare(findObject(PrintConst.VIEWABLE_PHYSICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.IMAGE_OF_DIALOG_RADIO).enabled, True)
    test.compare(findObject(PrintConst.COMMAND_LINE_HISTORY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.DIALOG_LIST).count, 0)
    util.close(PrintConst.PRINT_DIALOG_WINDOW)


    util.clickButton(ScenarioBoxConst.TOGGLE_PDU_LIST_WINDOW)
def print_viewPort():
    util.clickButton(GoldenLogicalToolbarConst.VIEWPORT)
    snooze(2)
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    snooze(5)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+P>")
    snooze(2)
    test.compare(findObject(PrintConst.ACTIVITY_INSTRUCTION_RADIO).enabled, True)
    test.compare(findObject(PrintConst.VIEWABLE_LOGICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.ACTIVE_DOCKABLE_DIALOG_RADIO).enabled, False)
    test.compare(findObject(PrintConst.VIEWABLE_PHYSICAL_TOPOLOGY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.IMAGE_OF_DIALOG_RADIO).enabled, True)
    test.compare(findObject(PrintConst.COMMAND_LINE_HISTORY_RADIO).enabled, True)
    test.compare(findObject(PrintConst.DIALOG_LIST).count, 0)
    util.close(PrintConst.PRINT_DIALOG_WINDOW)