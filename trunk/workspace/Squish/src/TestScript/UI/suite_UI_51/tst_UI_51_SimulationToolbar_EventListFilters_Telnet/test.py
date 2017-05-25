from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.EventListFilters.EventListFiltersConst import EventListFiltersConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.Utility.Util import Util

#Function initialization
eventListFilters = EventListFilters()
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 100, "Router1")

def main():
    util.init()
    createTopology()
    util.clickOnSimulation()
    util.clickOnRealtime()
    configRouter0()
    configRouter1()
    checkPoint()

def createTopology():
    router0.create()
    router1.create()
    util.connect(router0.x, router0.y, router1.x, router1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def configRouter0():
    router0.select()
    router0.clickCliTab()
    router0.cli.startConsole()
    router0.cli.setCliText("enable")
    router0.cli.setCliText("configure terminal")
    router0.cli.setCliText("interface fastethernet0/0")
    router0.cli.setCliText("ip address 1.1.1.1 255.0.0.0")
    router0.cli.setCliText("no shutdown")
    router0.cli.setCliText("exit")
    router0.cli.setCliText("line vty 0 4")
    router0.cli.setCliText("password cisco")
    router0.cli.setCliText("login")
    router0.cli.setCliText("end")

def configRouter1():
    router1.select()
    router1.clickCliTab()
    router1.cli.startConsole()
    router1.cli.setCliText("enable")
    router1.cli.setCliText("configure terminal")
    router1.cli.setCliText("interface fastethernet0/0")
    router1.cli.setCliText("ip address 1.1.1.2 255.0.0.0")
    router1.cli.setCliText("no shutdown")
    router1.cli.setCliText("end")

def checkPoint():
    util.clickOnSimulation()
    waitForObject(":CAppWindowBase")
    sendEvent("QMoveEvent", ":CAppWindowBase", 22, -13, 444, 0)
    eventListFilters.checkFilters('Telnet', clearFilters=True)

    router1.select()
    router1.cli.setCliText("telnet 1.1.1.1")

    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    util.clickOnWorkspace(router1.x + 10, router1.y + 10)
    util.clickButton(PDUConst.NEXT_LAYER)
    util.clickButton(PDUConst.NEXT_LAYER)
    util.clickButton(PDUConst.NEXT_LAYER)
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The TELNET client receives server data. It prints out the data.")