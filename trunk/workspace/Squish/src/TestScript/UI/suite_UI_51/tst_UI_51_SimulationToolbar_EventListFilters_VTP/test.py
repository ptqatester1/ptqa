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
    configSwitch0()
    configSwitch1()
    util.speedUpConvergence()
    checkPoint()
    
def createTopology():
    switch0.create()
    switch1.create()
    util.connect(switch0.x, switch0.y, switch1.x, switch1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def configSwitch0():
    switch0.select()
    switch0.clickCliTab()
    switch0.cli.startConsole()
    switch0.cli.setCliText("enable")
    switch0.cli.setCliText("configure terminal")
    switch0.cli.setCliText("interface fastethernet0/1")
    switch0.cli.setCliText("switchport mode trunk")
    switch0.cli.setCliText("exit")
    switch0.cli.setCliText("vlan 10")
    switch0.cli.setCliText("name test")
    switch0.cli.setCliText("exit")
    switch0.cli.setCliText("vtp mode server")
    switch0.cli.setCliText("vtp domain cisco")
    switch0.cli.setCliText("vtp password cisco")
    switch0.cli.setCliText("end")

def configSwitch1():
    switch1.select()
    switch1.clickCliTab()
    switch1.cli.startConsole()
    switch1.cli.setCliText("enable")
    switch1.cli.setCliText("configure terminal")
    switch1.cli.setCliText("interface fastethernet0/1")
    switch1.cli.setCliText("switchport mode trunk")
    switch1.cli.setCliText("exit")
    switch1.cli.setCliText("vtp mode client")
    switch1.cli.setCliText("vtp domain cisco")
    switch1.cli.setCliText("vtp password cisco")
    switch1.cli.setCliText("end")

def checkPoint():
    util.clickOnSimulation()
    waitForObject(":CAppWindowBase")
    sendEvent("QMoveEvent", ":CAppWindowBase", 22, -13, 444, 0)
    eventListFilters.checkFilters('VTP', clearFilters=True)

    switch1.select()
    switch1.cli.setCliText("configure terminal")
    switch1.cli.setCliText("vtp mode transparent")
    switch1.cli.setCliText("vtp mode client")
    switch1.cli.setCliText("end")

    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(3)
    util.clickOnWorkspace(switch0.x + 35, switch0.y + 10)
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The VTP process sends out a Summary Advertisement.")