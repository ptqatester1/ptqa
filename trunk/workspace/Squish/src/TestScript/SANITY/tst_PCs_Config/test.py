########################
##Author: AbbasH
########################

from API.ComponentBox import ComponentBoxConst

from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util
from API.Utility.Util import UtilConst

#Function initialization
util = Util()

#Device initialization
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, "PC0")
pc2 = PC(ComponentBoxConst.DeviceModel.PC, 200, 100, "PC1")

def main():
    util.init()
    createDevices()
    configTopology()
    checkPoint()
    
def createDevices():
    pc1.create()
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pc2.model, pc2.x, pc2.y)
    
    util.connect(pc2.x, pc2.y, pc1.x, pc1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")

def configTopology():
    
    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.ipConfiguration()
    pc1.desktop.ipConfiguration.ip("10.0.0.1")
    pc1.desktop.ipConfiguration.ip("<Tab>")
    pc1.close()
    
    pc2.select()
    pc2.clickDesktopTab()
    pc2.desktop.applications.ipConfiguration()
    pc2.desktop.ipConfiguration.ip("10.0.0.2")
    pc2.desktop.ipConfiguration.ip("<Tab>")
    pc2.close()

    util.speedUpConvergence()
    
def checkPoint():

    pc1.select()
    pc1.desktop.applications.commandPrompt()
    pc1.desktop.commandPrompt.setText("ping 10.0.0.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc1.desktop.commandPrompt.textCheckPoint("Reply from 10.0.0.2")

    util.speedUpConvergence()
    pc2.select()
    pc2.desktop.applications.commandPrompt()
    pc1.desktop.commandPrompt.setText("ping 10.0.0.1")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc2.desktop.commandPrompt.textCheckPoint("Reply from 10.0.0.1")