#Thi
from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Device.EndDevice.PC.PC import PC

from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.EventListFilters.EventListFiltersConst import EventListFiltersConst
from API.SimulationPanel.PDU.PDUConst import PDUConst

#Function initialization
util = Util()
eventListFilters = EventListFilters()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 398, 132, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 257, 133, "Router1")
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 239, 253, "Switch0")
switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 415, 258, "Switch1")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 157, 340, "PC1")
pc2 = PC(ComponentBoxConst.DeviceModel.PC, 431, 352, "PC2")
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 571, 171, "Server0")

def main():    
    util.init()
    createTopology()
    ping()

def createTopology():
    util.speedUpConvergence()
    util.open("Lab1_PC_SW_R_OSPF_May_13_2009_SN.pkt", UtilConst.PROTOCOLS_TEST)
    
def ping():
    util.clickOnSimulation()
    
    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.commandPrompt()
    pc1.desktop.commandPrompt.setText("ping 172.16.20.20")
    
    util.clickOnRealtime()
    util.clickOnSimulation()
    util.clickOnRealtime()
    util.clickOnSimulation()
    util.clickOnRealtime()
    util.clickOnSimulation()
    
    #Ping is not successful because network hasn't converged yet.
    pc1.desktop.commandPrompt.textCheckPoint("Received = 0")