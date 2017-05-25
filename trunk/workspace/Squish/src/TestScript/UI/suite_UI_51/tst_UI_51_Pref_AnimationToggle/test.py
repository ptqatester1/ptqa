from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst

util = Util()
common = CommonToolsBar()
options = Options()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 200, "PC1")

def main():
    util.init()
    #Can't check animation")
    createTopology()
    configureDevices()
    goToSimulation()
    editOptionsSetting()
    playSimulation()
    editOptionsSetting()
    playSimulation()

def createTopology():
    pc0.create()
    pc1.create()
    pc0.connect(pc1, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    
def configureDevices():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.setIPConfiguration("1.1.1.1", "", "", "")
    pc0.close()
    
    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.ipConfiguration()
    pc1.desktop.ipConfiguration.setIPConfiguration("1.1.1.2", "", "", "")
    pc1.close()
    
def goToSimulation():
    util.clickOnSimulation()
    common.addSimplePDU(pc0.x, pc0.y, pc1.x, pc1.y)

def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickButton(InterfaceConst.SHOW_ANIMATION)
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def playSimulation():
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)