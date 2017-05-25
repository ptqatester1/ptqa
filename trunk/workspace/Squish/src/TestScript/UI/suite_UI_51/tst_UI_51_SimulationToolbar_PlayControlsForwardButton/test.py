from API.ComponentBox import ComponentBoxConst

from API.Device.EndDevice.PC.PC import PC
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.GoldenSimulationToolbar.GoldenSimulationToolbarConst import GoldenSimulationToolbarConst
from API.Utility.Util import Util

#Function initialization
commonToolsBar = CommonToolsBar()
util = Util()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 200, 200, "PC1")

def main():
    util.init()
    createTopology()
    configPC0()
    configPC1()
    util.clickOnSimulation()
    checkPoint()

def createTopology():
    pc0.create()
    pc1.create()
    util.connect(pc0.x, pc0.y, pc1.x, pc1.y, ComponentBoxConst.Connection.CONN_CROSS, "FastEthernet0", "FastEthernet0")

def configPC0():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.setIPConfiguration("1.1.1.1", "255.0.0.0", "", "")
    pc0.desktop.ipConfiguration.close()

def configPC1():
    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.ipConfiguration()
    pc1.desktop.ipConfiguration.setIPConfiguration("1.1.1.2", "255.0.0.0", "", "")
    pc1.desktop.ipConfiguration.close()

def checkPoint():
    commonToolsBar.addSimplePDU(pc0.x, pc0.y, pc1.x, pc1.y)
    util.clickButton(GoldenSimulationToolbarConst.CAPTURE_FORWARD)
    snooze(5)
    util.clickOnWorkspace(214, 208)
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "FastEthernet0 receives the frame.")