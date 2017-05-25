from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst
from API.MenuBar.Options.Preferences.Administrative.AdministrativeConst import AdministrativeConst
from API.MenuBar.Options.Preferences.Administrative.Administrative import Administrative
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.File.Print.PrintConst import PrintConst
from API.MenuBar.File.Print.Print import Print
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
from API.ComponentBox import ComponentBoxConst
from API.UserCreatedPacketWindow.ScenarioBoxConst import ScenarioBoxConst
from API.UserCreatedPacketWindow.ScenarioBox import ScenarioBox

util = Util()
filePrint = Print()
fileMenu = File()
administrative =Administrative()
optionsMenu = Options()
def main():
    util.init()
    snooze(7)
    print_noItemOnWorkspace()
    print_itemOnWorkspace()
    print_simulationMode()
    print_togglePDUList()
    print_viewPort()


def print_noItemOnWorkspace():
    fileMenu.selectFileItem(FileConst.PRINT)
    snooze(2)

    
    util.close(PrintConst.PRINT_DIALOG_WINDOW)



    
def print_itemOnWorkspace():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100)    
    util.clickOnWorkspace(100,100)
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)   
    fileMenu.selectFileItem(FileConst.PRINT)

    snooze(2)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPhyPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_instructionsRB").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntActDlg").enabled, False)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogImage").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntCmdLnOpHist").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogsList").count, 0)
    
    util.close(PrintConst.PRINT_DIALOG_WINDOW)

def print_simulationMode():
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)  
    util.clickOnSimulation()
    snooze(5)
    fileMenu.selectFileItem(FileConst.PRINT)
    snooze(5)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPhyPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_instructionsRB").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntActDlg").enabled, False)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogImage").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntCmdLnOpHist").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogsList").count, False)
    util.close(PrintConst.PRINT_DIALOG_WINDOW)
    util.clickOnRealtime()




def print_togglePDUList():
    ScenarioBox().expandScenarioToggle()
    util.clickButton(ScenarioBoxConst.TOGGLE_PDU_LIST_WINDOW)
    fileMenu.selectFileItem(FileConst.PRINT)
    snooze(2)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPhyPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_instructionsRB").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntActDlg").enabled, False)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogImage").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntCmdLnOpHist").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogsList").count, 0)
    
    util.close(PrintConst.PRINT_DIALOG_WINDOW)


    util.clickButton(ScenarioBoxConst.TOGGLE_PDU_LIST_WINDOW)
def print_viewPort():
    util.clickButton(GoldenLogicalToolbarConst.VIEWPORT)
    fileMenu.selectFileItem(FileConst.PRINT)
    snooze(2)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPhyPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_instructionsRB").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntActDlg").enabled, False)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogImage").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntCmdLnOpHist").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogsList").count, False)
    util.close(PrintConst.PRINT_DIALOG_WINDOW)

def print_to_file():
    #Cant' think of a way to save in the right folder")
    filePrint.printToFile(util.getFilePath("File_Menu_Print", UtilConst.UI_TEST))
    snooze(2)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+R>")
    util.clickTab(InterfaceConst.TAB_BAR, AdministrativeConst.ADMINISTRATIVE)
    administrative.addImages(util.getFilePath("File_Menu_Print", UtilConst.UI_TEST))
