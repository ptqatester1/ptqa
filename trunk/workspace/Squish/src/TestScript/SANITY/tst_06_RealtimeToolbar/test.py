#######################
#@author: Pamela Vinco
#######################
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router
from API.Toolbar.GoldenRealtimeToolbar.GoldenRealtimeToolbarConst import GoldenRealtimeToolbarConst
from API.SimulationPanel.EventList.EventListConst import EventListConst

#Function initialization
util = Util()

#Device initialization
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 200, "Router1")

def main():
    util.init()
    createDevice()
    realtimeSimulationSwitch()
    powerCycle()
    timeClock()
    fastForward()
    
def createDevice():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    
def realtimeSimulationSwitch():
    #Click on Simulation tab and check that the Event List is visible
    util.clickOnSimulation()
    test.compare(findObject(EventListConst.EVENT_LISTVIEW).visible, True)
    #Click on Logical tab and check that the Event List is not visible
    util.clickOnRealtime()
    test.compare(findObject(EventListConst.EVENT_LISTVIEW).visible, False)
    
def powerCycle():
    #Click on Power Cycle Devices and check that the Confirm Power Cycle Dialog appears
    util.clickButton(GoldenRealtimeToolbarConst.POWER_CYCLE_DEVICE)
    if object.exists(GoldenRealtimeToolbarConst.POWER_CYCLE_DEVICES_DIALOG):
        test.passes("Confirm Power Cycle Dialog found")
        util.clickButton(GoldenRealtimeToolbarConst.POWER_CYCLE_DEVICES_DIALOG_YES)
    else:
        test.fail("Confirm Power Cycle Dialog not found")
        
def timeClock():
    #Check that the time is moving (not 00:00:00)
    util.textCheckPoint(GoldenRealtimeToolbarConst.TIME_LABEL, "00:00:00", 0)
    
def fastForward():
    #Click on fast forward time a few times and check that the current time is at least at the 2 minute mark
    util.clickButton(GoldenRealtimeToolbarConst.FAST_FORWARD_TIME)
    util.clickButton(GoldenRealtimeToolbarConst.FAST_FORWARD_TIME)
    util.clickButton(GoldenRealtimeToolbarConst.FAST_FORWARD_TIME)
    util.clickButton(GoldenRealtimeToolbarConst.FAST_FORWARD_TIME)
    util.clickButton(GoldenRealtimeToolbarConst.FAST_FORWARD_TIME)
    snooze(1)
    util.textCheckPoint(GoldenRealtimeToolbarConst.TIME_LABEL, "00:0[2-5]:[\d][\d]")