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
switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 300, 200, "Switch1")
switch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 200, 300, "Switch2")

def main():
    util.init()
    createTopology()
    switchToSimulation()
    configSwitch0()
    configSwitch1()
    configSwitch2()
    checkPoint()
    
def createTopology():
    switch0.create()
    switch1.create()
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, switch2.model, switch2.x, switch2.y)
    util.connect(switch0.x, switch0.y, switch1.x, switch1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.connect(switch1.x, switch1.y, switch2.x, switch2.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.connect(switch2.x, switch2.y, switch0.x, switch0.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def switchToSimulation():
    util.clickOnSimulation()
    waitForObject(":CAppWindowBase")
    sendEvent("QMoveEvent", ":CAppWindowBase", 22, -13, 444, 0)
    eventListFilters.checkFilters('DTP', clearFilters=True)

def configSwitch0():
    switch0.select()
    switch0.clickCliTab()
    switch0.cli.startConsole()
    switch0.cli.setCliText("enable")
    switch0.cli.setCliText("configure terminal")
    switch0.cli.setCliText("interface fastethernet0/1")
    switch0.cli.setCliText("switchport mode trunk")
    switch0.cli.setCliText("exit")
    switch0.cli.setCliText("interface fastethernet0/2")
    switch0.cli.setCliText("switchport mode trunk")
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
    switch1.cli.setCliText("interface fastethernet0/2")
    switch1.cli.setCliText("switchport mode trunk")
    switch1.cli.setCliText("end")

def configSwitch2():
    util.clickOnWorkspace(switch2.x, switch2.y)
    switch2.updateName()
    switch2.clickCliTab()
    switch2.cli.startConsole()
    switch2.cli.setCliText("enable")
    switch2.cli.setCliText("configure terminal")
    switch2.cli.setCliText("interface fastethernet0/1")
    switch2.cli.setCliText("switchport mode trunk")
    switch2.cli.setCliText("exit")
    switch2.cli.setCliText("interface fastethernet0/2")
    switch2.cli.setCliText("switchport mode trunk")
    switch2.cli.setCliText("end")

def checkPoint():
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(3)
    util.clickOnWorkspace(switch2.x + 5, switch2.y + 10)
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "4. The device receives a DTP frame")