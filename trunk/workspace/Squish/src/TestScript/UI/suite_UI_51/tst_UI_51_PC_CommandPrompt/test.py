from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")

def main():
    util.init()
    createTopology()
    checkpoint()


def createTopology():
    pc0.create()

def checkpoint():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("?")
    pc0.desktop.commandPrompt.setText('   ')
    pc0.desktop.commandPrompt.textCheckPoint("arp")
    pc0.desktop.commandPrompt.textCheckPoint("help")
    pc0.desktop.commandPrompt.textCheckPoint("ipconfig")
    pc0.desktop.commandPrompt.textCheckPoint("netstat")
    pc0.desktop.commandPrompt.textCheckPoint("ping")
    pc0.desktop.commandPrompt.textCheckPoint("ipv6config")
    pc0.desktop.commandPrompt.textCheckPoint("ssh")
    pc0.desktop.commandPrompt.textCheckPoint("telnet")
    pc0.desktop.commandPrompt.textCheckPoint("tracert")