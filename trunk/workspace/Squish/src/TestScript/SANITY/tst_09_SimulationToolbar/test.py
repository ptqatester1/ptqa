#######################
#@author: Pamela Vinco
#######################
from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Utility import UtilConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.SimulationPanel.PDU.PDUConst import PDUConst

#Function initialization
util = Util()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 200, 200, "PC1")

def main():
    util.init()
    openFile()
    util.clickOnSimulation()
    playControls1()
    resetSimulation()
    playControls2()
    filters()
    toggleEventList()
        
def openFile():
    util.open("simulationToolbar.pkt", UtilConst.SANITY_TEST)
    
def playControls1():
    #Click on Auto Capture Play inside the Event List and check that the PDU moves from PC0 to PC1
    util.clickButton(PlayControlsConst.AUTO_CAPTURE_PLAY)
    snooze(5)
    
    #Stop the Auto Capture play and check that there is no PDU on PC0
    util.clickButton(PlayControlsConst.AUTO_CAPTURE_PLAY)
    
    util.clickOnWorkspace(pc0.x+5, pc0.y+5)
    if object.exists(PDUConst.PDU_WINDOW):
        test.fail("PDU is still on PC0")
    else:
        test.passes("PDU is not on PC0 anymore")
        
    #Click on Back inside the Event List and check that the PDU moves from PC0 to PC1
