from API.ComponentBox import ComponentBoxConst

from API.Device.EndDevice.Server.Server import Server

from API.Device.Router.Router import Router
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.EventListFilters.EventListFiltersConst import EventListFiltersConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.Utility.Util import Util

#Function initialization
eventListFilters = EventListFilters()
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, "Server0")

def main():
    util.init()
    createTopology()
    configServer0()
    configRouter0()
    checkPoint()

def createTopology():
    router0.create()
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, server0.model, server0.x, server0.y)
    util.connect(router0.x, router0.y, server0.x, server0.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.fastForwardTime()

def configServer0():
    util.clickOnWorkspace(server0.x, server0.y)
    server0.updateName()
    server0.clickConfigTab()
    server0.config.settings.gateway("1.1.1.1")
    server0.config.selectInterface("FastEthernet0")
    server0.config.interface.wired.ip("1.1.1.2")
    server0.config.interface.wired.subnet("255.0.0.0")

def configRouter0():
    router0.select()
    router0.clickCliTab()
    router0.cli.startConsole()
    router0.cli.setCliText("enable")
    router0.cli.setCliText("configure terminal")
    router0.cli.setCliText("interface fastethernet0/0")
    router0.cli.setCliText("ip address 1.1.1.1 255.0.0.0")
    router0.cli.setCliText("end")

def checkPoint():
    util.clickOnSimulation()
    eventListFilters.checkFilters('TFTP', clearFilters=True)

    router0.select()
    router0.cli.setCliText("copy tftp flash:")
    router0.cli.setCliText("1.1.1.2")
    router0.cli.setCliText("c1841-advipservicesk9-mz.124-15.T1.bin")
    router0.cli.setCliText("\r")
    router0.cli.setCliText("\r")
    router0.cli.setCliText("\r")
    router0.cli.setCliText("\r")

    util.clickOnWorkspace(router0.x + 10, router0.y + 10)
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The TFTP client starts a read session with the TFTP server.")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "2. The TFTP client sends a TFTP request to the TFTP server.")