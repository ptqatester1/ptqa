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
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 200, "Switch0")
switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 200, 200, "Switch1")

def main():
    util.init()
    createTopology()
    util.speedUpConvergence()
    checkPoint()
    
def createTopology():
    switch0.create()
    switch1.create()
    util.connect(switch0.x, switch0.y, switch1.x, switch1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def checkPoint():
    util.clickOnSimulation()
    eventListFilters.checkFilters('CDP', clearFilters=True)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    util.clickOnRealtime()
    util.clickOnSimulation()
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(10)
    util.clickOnWorkspace(switch0.x + 10, switch0.y + 10)
    if (not object.exists(PDUConst.PDUINFO_TAB_BAR)):
        util.clickOnWorkspace(switch1.x + 10, switch1.y + 10)
    snooze(1)
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "CDP")