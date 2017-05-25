########################
##Author: AbbasH
########################

from API.Device.EndDevice.PC.PC import PC

from API.Device.Switch.Switch import Switch

from API.Utility import UtilConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst

util = Util()

s1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 150, 100, "Switch0")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 50, 250, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 250, 250, "PC1")

def main():
    util.init()
    createDevices()
    configTopology()
    checkPoint()
    
def createDevices():
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s1.model, s1.x, s1.y)
    pc0.create()
    pc1.create()
    util.connect(s1.x, s1.y, pc0.x, pc0.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.connect(s1.x, s1.y, pc1.x, pc1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def configTopology():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.ip("192.168.0.2")
    pc0.desktop.ipConfiguration.ip("<Tab>")
    pc0.close()
    
    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.ipConfiguration()
    pc1.desktop.ipConfiguration.ip("192.168.0.3")
    pc1.desktop.ipConfiguration.ip("<Tab>")
    pc1.close()
    
def checkPoint():

    util.speedUpConvergence()
    pc1.select()
    pc1.desktop.applications.commandPrompt()
    pc1.desktop.commandPrompt.setText("ping 192.168.0.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc1.desktop.commandPrompt.textCheckPoint("Reply from 192.168.0.2")

    util.speedUpConvergence()
    pc0.select()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping 192.168.0.3")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc0.desktop.commandPrompt.textCheckPoint("Reply from 192.168.0.3")    