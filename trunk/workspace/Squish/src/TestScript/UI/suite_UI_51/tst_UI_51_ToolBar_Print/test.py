from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst
from API.MenuBar.Options.Preferences.Administrative.AdministrativeConst import AdministrativeConst
from API.MenuBar.Options.Preferences.Administrative.Administrative import Administrative
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.File.Print.PrintConst import PrintConst
from API.MenuBar.File.Print.Print import Print
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
from API.ComponentBox import ComponentBoxConst
from API.UserCreatedPacketWindow.ScenarioBoxConst import ScenarioBoxConst
from API.UserCreatedPacketWindow.ScenarioBox import ScenarioBox

util = Util()
filePrint = Print()
optionsMenu = Options()
administrative =Administrative()
def main():
    util.init()
    snooze(7)
    print_noItemOnWorkspace()
    print_itemOnWorkspace()
    print_simulationMode()
    print_togglePDUList()
    print_viewPort()
    #print_to_file()

def print_noItemOnWorkspace():

    util.clickButton(MainToolbarConst.PRINT)
    snooze(2)
    
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPhyPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_instructionsRB").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntActDlg").enabled, False)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogImage").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntCmdLnOpHist").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogsList").count, 0)

    util.close(PrintConst.PRINT_DIALOG_WINDOW)

    
def print_itemOnWorkspace():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100)    
    util.clickOnWorkspace(100,100)
    util.clickButton(MainToolbarConst.PRINT)
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
    util.clickOnSimulation()
    snooze(5)
    util.clickButton(MainToolbarConst.PRINT)
    snooze(5)

    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPhyPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_instructionsRB").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntActDlg").enabled, False)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogImage").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntCmdLnOpHist").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogsList").count, 0)

    util.close(PrintConst.PRINT_DIALOG_WINDOW)
    util.clickOnRealtime()




def print_togglePDUList():
    ScenarioBox().expandScenarioToggle()
    util.clickButton(MainToolbarConst.PRINT)
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
    util.clickButton(MainToolbarConst.PRINT)
    snooze(2)
    
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPhyPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_instructionsRB").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntScrn").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntActDlg").enabled, False)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogImage").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_pPrntCmdLnOpHist").enabled, True)
    test.compare(findObject(":CAppWindowBase.PrintDlgBase.m_printOptionsGrp.m_dialogsList").count, 0)
    snooze(2)
    util.close(PrintConst.PRINT_DIALOG_WINDOW)

def print_to_file():
    filePrint.printToFile(util.getFilePath("File_Menu_Print", UtilConst.UI_TEST))
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+R>")
    util.clickTab(InterfaceConst.TAB_BAR, AdministrativeConst.ADMINISTRATIVE)
    administrative.addImages(util.getFilePath("File_Menu_Print", UtilConst.UI_TEST))