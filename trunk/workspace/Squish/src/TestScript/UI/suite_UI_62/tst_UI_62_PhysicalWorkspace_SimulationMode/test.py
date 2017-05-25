########################
##Author: AbbasH
########################

from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Utility import UtilConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.ComponentBox.ComponentBox import ComponentBox
from API.Device.Switch.Switch import Switch
from API.Device.EndDevice.PC.PC import PC
 
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.EventListFilters.EventListFiltersConst import EventListFiltersConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.Workspace.Physical import Physical


#Function initialization
util = Util()
componentBox = ComponentBox()
eventListFilters = EventListFilters()

s0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 128, 61, "Switch0")
s1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 219, 105, "Switch1")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 48, 52, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 296, 285, "PC1")

def main():
    util.init()
    config()
    test()

def config():
    util.clickOnPhysical()
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s0.model, s0.x, s0.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s1.model, s1.x, s1.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pc0.model, pc0.x+5, pc0.y+5)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pc1.model, 300, 300)
    
    util.connectOnPhysical(pc0.x, pc0.y, s0.x, s0.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    homecity = Physical().getObject('Home City')
    util.connectOnPhysical(homecity.x + 15, homecity.y + 15, s1.x, s1.y, ComponentBoxConst.Connection.CONN_STRAIGHT, "FastEthernet0", "FastEthernet0/1", "PC1", "")
    
    util.connectOnPhysical(s0.x, s0.y, s1.x, s1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    
    util.clickOnPhysicalWorkspace(pc0.x, pc0.y)
    pc0.updateName()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.setIPConfiguration("10.1.1.1", "255.0.0.0", "", "")
    snooze(2)
    pc0.close()
    
    util.clickOnPhysicalWorkspace(300, 300)
    snooze(2)
    util.clickOnPhysicalWorkspace(pc1.x, pc1.y)
    pc1.updateName()
    pc1.clickDesktopTab()
    pc1.desktop.applications.ipConfiguration()
    pc1.desktop.ipConfiguration.setIPConfiguration("10.1.1.2", "255.0.0.0", "", "")
    snooze(2)    
    pc1.close()
    
    util.speedUpConvergence()

def test():
    util.clickButton(GoldenPhysicalToolbarConst.GO_TO_INTERCITY)
    util.clickOnPhysicalWorkspace(pc0.x, pc0.y)
    pc0.updateName()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping 10.1.1.2")
    util.speedUpConvergence()
    pc0.desktop.commandPrompt.textCheckPoint("Received = 0")

    util.clickOnSimulation()    
    eventListFilters.checkFilters('ICMP', clearFilters=True)
    
    util.clickOnPhysicalWorkspace(pc0.x, pc0.y)
    pc0.updateName()
    pc0.desktop.commandPrompt.setText("ping 10.1.1.2")
    pc0.close()

    util.clickButton(PlayControlsConst.CAPTURE_FORWARD) 
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD) 
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD) 
    snooze(10)
    util.clickOnPhysicalWorkspace(pc0.x+30, pc0.y+30)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer3")
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 10.1.1.1, Dest. IP: 10.1.1.2\nICMP Message\nType: 8")
    util.close(PDUConst.PDU_WINDOW)
       
    
        
    None
