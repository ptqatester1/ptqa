from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 300, 200, "Router0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    completeTopology()
    checkpoint2()

def createTopology():
    pc0.create()

def checkpoint1():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.terminal()
    pc0.desktop.terminal.check.bitsPerSecond(None, property='count', value=8)
    pc0.desktop.terminal.check.bitsPerSecond("9600")
    pc0.desktop.terminal.check.dataBits(None, property='count', value=4)
    pc0.desktop.terminal.check.dataBits("8")
    pc0.desktop.terminal.check.parity(None, property='count', value=5)
    pc0.desktop.terminal.check.parity("None")
    pc0.desktop.terminal.check.stopBits(None, property='count', value=3)
    pc0.desktop.terminal.check.stopBits("1")
    pc0.desktop.terminal.check.flowControl(None, property='count', value=3)
    pc0.desktop.terminal.check.flowControl("None")
    pc0.desktop.terminal.configure(None, None, None, None, None)
    pc0.desktop.terminal.emptyTerminalCheck("")
    pc0.close()

def completeTopology():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    util.connect(pc0.x, pc0.y, r0.x, r0.y, ComponentBoxConst.Connection.CONN_CONSOLE, "RS 232", "Console")
    util.fastForwardTime()
    
def checkpoint2():
    pc0.select()
    pc0.clickTab('Desktop')
    pc0.desktop.applications.terminal()
    pc0.desktop.terminal.configure(None, None, None, None, None)
    snooze(5)
    pc0.desktop.terminal.textCheckPoint("Would you like to enter the initial configuration dialog?")
    pc0.desktop.terminal.closeTerminal()
    
    pc0.desktop.applications.terminal()
    pc0.desktop.terminal.configure("1200", None, None, None, None)
    pc0.desktop.terminal.emptyTerminalCheck("")