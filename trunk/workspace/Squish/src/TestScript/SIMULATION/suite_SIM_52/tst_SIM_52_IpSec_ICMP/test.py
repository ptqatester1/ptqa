#Thi
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters

#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 151, 136, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 263, 34, "Router1")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 368, 148, "Router2")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 57, 236, "PC0")
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 452, 248, "Server0")
server1 = Server(ComponentBoxConst.DeviceModel.SERVER, 515, 48, "Server1")

eventListFilters = EventListFilters()
def main():
    util.init()
    createTopology()
    ping()
    at_Router1_outBound_ToRouter2()
    checkpoint()
    
def createTopology():
    util.open("ipsec_sim.pkt", UtilConst.PROTOCOLS_TEST)

def ping():    
    util.clickOnSimulation()
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()  
    
    pc0.desktop.commandPrompt.setText("ping 2.1.1.2") 
        
def at_Router1_outBound_ToRouter2():
    for i in range (0, 30):
        util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
        if (object.exists(PlayControlsConst.BUFFER_FULL_WINDOW)):
            util.clickButton(PlayControlsConst.BUFFER_FULL_DIALOG_VIEW_PREVIOUS_EVENTS)

def checkpoint():
    pc0.select()
    pc0.desktop.commandPrompt.textCheckPoint("Received = 0", 0)#Bug 15326 