from API.ComponentBox import ComponentBoxConst

from API.Device.EndDevice.PC.PC import PC

from API.Device.EndDevice.Server.Server import Server
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.EventListFilters.EventListFiltersConst import EventListFiltersConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.Utility.Util import Util

#Function initialization
eventListFilters = EventListFilters()
util = Util()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, "PC0")
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, "Server0")

def main():
    util.init()
    createTopology()
    configServer0()
    checkPoint()

def createTopology():
    pc0.create()
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, server0.model, server0.x, server0.y)
    util.connect(pc0.x, pc0.y, server0.x, server0.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def configServer0():
    util.clickOnWorkspace(server0.x, server0.y)
    server0.updateName()
    server0.clickConfigTab()
    server0.config.selectInterface("FastEthernet0")
    server0.config.interface.wired.ip("1.1.1.1")
    server0.config.interface.wired.subnet("255.0.0.0")
    
    server0.clickServicesTab()
    server0.services.selectInterface("DHCP")
    server0.services.dhcp.on()
    server0.services.dhcp.gateway("1.1.1.1")
    server0.services.dhcp.ip('1.1.1.2')
    server0.services.dhcp.maxUsers('2')
    
def checkPoint():
    util.clickOnSimulation()
    waitForObject(":CAppWindowBase")
    sendEvent("QMoveEvent", ":CAppWindowBase", 22, -13, 444, 0)
    eventListFilters.checkFilters('DHCP', clearFilters=True)

    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.dhcp()

    util.clickOnWorkspace(pc0.x + 10, pc0.y + 10)
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The DHCP client constructs a Discover packet and sends it out.")