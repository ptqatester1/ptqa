from API.Utility.Util import Util
from API.Device.EndDevice.PC.PC import PC
from API.ComponentBox import ComponentBoxConst
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Utility.Util import UtilConst
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.MenuBar.File.Save.Save import Save
from API.ActivityWizard.ActivityWizard import ActivityWizard
#Function initialization
fileMenu =File()
util = Util()
commonToolsBar = CommonToolsBar()
aw = ActivityWizard()

#Device initialization
Host1 = PC(ComponentBoxConst.DeviceModel.PC, 124, 93, "PC0")
Host2 = PC(ComponentBoxConst.DeviceModel.PC, 568, 104, "PC1")

def main():
    util.init()
    openFile()
    goToActivityWizard()
    DeletePC1()
    ExportInitialNetwork()

def openFile():
    util.open("UI14WelcomeTest.pkt", "UI")

def goToActivityWizard():
    aw.goToAW(useNetwork=True)
    
    aw.selectInitialNetwork()
    aw.initialNetwork.showInitialNetworkButton()
    aw.initialNetwork.copyFromAnswerNetwork()
    aw.initialNetwork.showInitialNetworkButton()
    Host1.exists()
    util.clickOnWorkspace(10, 10)

def DeletePC1():
    commonToolsBar.deleteItem(569, 103)
    
def ExportInitialNetwork():
    aw.initialNetwork.exportInitialNetwork(util.getFilePath("UI41AnsweNetwork3.pkt", UtilConst.UI_TEST), overwrite=True)
    aw.initialNetwork.importInitialNetwork(util.getFilePath("UI41AnsweNetwork3.pkt", UtilConst.UI_TEST))
    aw.initialNetwork.showInitialNetworkButton()
    
    Host1.select()
    Host2.select()
    
    aw.save.saveAs(util.getFilePath("UI41InitialNetwork.pka", UtilConst.UI_TEST), overwrite=True)