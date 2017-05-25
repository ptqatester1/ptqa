from API.ComponentBox import ComponentBoxConst

from API.Device.Switch.Switch import Switch
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.EventListFilters.EventListFiltersConst import EventListFiltersConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.Utility.Util import Util

#Function initialization
eventListFilters = EventListFilters()
util = Util()

#Device initialization
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 100, 200, "Switch0")
switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 200, 200, "Switch1")

def main():
    util.init()
    createTopology()
    switchToSimulation()
    configSwitch0()
    checkPoint()

    
def createTopology():
    switch0.create()
    switch1.create()
    util.connect(switch0.x, switch0.y, switch1.x, switch1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.connect(switch0.x, switch0.y, switch1.x, switch1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def switchToSimulation():
    util.clickOnSimulation()
    waitForObject(":CAppWindowBase")
    sendEvent("QMoveEvent", ":CAppWindowBase", 22, -13, 444, 0)
    eventListFilters.checkFilters('PAgP', clearFilters=True)

def configSwitch0():
    switch0.select()
    switch0.clickCliTab()
    switch0.cli.startConsole()
    switch0.cli.setCliText("enable")
    switch0.cli.setCliText("configure terminal")
    switch0.cli.setCliText("interface fastethernet0/1")
    switch0.cli.setCliText("channel-protocol pagp")
    switch0.cli.setCliText("channel-group 1 mode desirable")
    switch0.cli.setCliText("exit")
    switch0.cli.setCliText("interface fastethernet0/2")
    switch0.cli.setCliText("channel-protocol pagp")
    switch0.cli.setCliText("channel-group 1 mode desirable")
    switch0.cli.setCliText("end")

def checkPoint():
    util.clickOnWorkspace(switch0.x + 10, switch0.y + 10)
    util.textCheckPoint(PDUConst.OSI_HEADER_INFO, "PAgP Multicast Address")