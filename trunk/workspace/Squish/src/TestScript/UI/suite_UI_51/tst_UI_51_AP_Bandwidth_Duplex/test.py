from API.ComponentBox import ComponentBoxConst
from API.Device.AccessPoint.AccessPoint import AccessPoint
from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, "PC0")
accessPoint0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 250, 100, "Access Point0")
pc1 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 500, 100, "PC1")

#Function initialization
util = Util()

def main():
    util.init()
    createTopology()
    configPCs()
    checkPoint1()
    checkPoint2()
    checkPoint3()
    checkPoint4()
    checkPoint5()

def createTopology():
    pc0.create()
    accessPoint0.create()
    pc1.create()
    pc0.connect(accessPoint0, ComponentBoxConst.Connection.CONN_CROSS, "FastEthernet0", "Port 0")
    
def configPCs():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.setIPConfiguration("1.1.1.1", "255.0.0.0", "", "")
    pc0.desktop.ipConfiguration.close()

    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.ipConfiguration()
    pc1.desktop.ipConfiguration.setIPConfiguration("1.1.1.2", "255.0.0.0", "", "")
    pc1.desktop.ipConfiguration.close()

def checkPoint1():
    accessPoint0.select()
    accessPoint0.clickConfigTab()
    accessPoint0.config.selectInterface("Port 0")
    snooze(1)
    accessPoint0.config.interface.port0.check.bandwidth('Auto', False)

def checkPoint2():
    accessPoint0.config.interface.port0.bandwidth('10')
    accessPoint0.config.interface.port0.duplex('full')

    pc0.select()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping 1.1.1.2")
    util.speedUpConvergence()
    pc0.desktop.commandPrompt.textCheckPoint("Received = 0", 1)

def checkPoint3():
    accessPoint0.select()
    accessPoint0.config.interface.port0.bandwidth('auto')

    pc0.select()
    pc0.desktop.commandPrompt.setText("ping 1.1.1.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc0.desktop.commandPrompt.textCheckPoint("Received = 0", 1)
    pc0.desktop.commandPrompt.close()

def checkPoint4():
    pc0.clickConfigTab()
    pc0.config.selectInterface("FastEthernet0")
    pc0.config.interface.wired.bandwidth('10')
    pc0.config.interface.wired.duplex('full')

    accessPoint0.select()
    accessPoint0.config.interface.port0.bandwidth('100')
    accessPoint0.config.interface.port0.duplex('half')

    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping 1.1.1.2")
    util.speedUpConvergence()
    pc0.desktop.commandPrompt.textCheckPoint("Received = 0", 2)
    pc0.desktop.commandPrompt.close()

def checkPoint5():
    pc0.clickConfigTab()
    pc0.config.selectInterface("FastEthernet0")
    pc0.config.interface.wired.duplex('half')
    pc0.config.interface.wired.bandwidth('100')

    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping 1.1.1.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc0.desktop.commandPrompt.textCheckPoint("Received = 0", 2)