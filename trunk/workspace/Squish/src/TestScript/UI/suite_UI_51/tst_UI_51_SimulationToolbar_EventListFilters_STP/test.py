from API.ComponentBox import ComponentBoxConst
from API.Device.Switch.Switch import Switch
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.EventListFilters.EventListFiltersConst import EventListFiltersConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.Utility.Util import Util

#Function initialization
eventListFilters = EventListFilters()
util = Util()

#Device initialization
switch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 34, 240, "Switch2")

def main():
    util.init()
    createTopology()
    checkPoint()
    
def createTopology():
    util.open("B7_1.pkt")

def checkPoint():
    util.clickOnSimulation()
    waitForObject(":CAppWindowBase")
    sendEvent("QMoveEvent", ":CAppWindowBase", 22, -13, 444, 0)
    eventListFilters.checkFilters('STP', clearFilters=True)
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.BACK)
    snooze(3)
    util.clickOnWorkspace(switch2.x + 15, switch2.y + 10)
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The STP process sends out a configuration BPDU.")