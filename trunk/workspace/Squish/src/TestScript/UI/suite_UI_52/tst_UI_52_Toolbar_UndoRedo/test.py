######################
#@author: Pamela Vinco
######################

from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst

util = Util()
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 200, 100, "PC1")
pc2 = PC(ComponentBoxConst.DeviceModel.PC, 300, 100, "PC2")
pc3 = PC(ComponentBoxConst.DeviceModel.PC, 400, 100, "PC3")
pc4 = PC(ComponentBoxConst.DeviceModel.PC, 500, 100, "PC4")

def main():
    util.init()
    test.log("Bug 3003")
    createDevices()
    undoCreateDevices()
    checkpoint_undo()
    redoCreateDevices()
    checkpoint_redo()
    
def createDevices():
    pc0.create()
    pc1.create()
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pc2.model, pc2.x, pc2.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pc3.model, pc3.x, pc3.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pc4.model, pc4.x, pc4.y)

def undoCreateDevices():
    util.clickButton(MainToolbarConst.UNDO)
    util.clickButton(MainToolbarConst.UNDO)
    util.clickButton(MainToolbarConst.UNDO)
    
def checkpoint_undo():
    util.clickOnWorkspace(pc4.x, pc4.y)
    pc4.doesNotExist()
        
def redoCreateDevices():
    util.clickButton(MainToolbarConst.REDO)
    util.clickButton(MainToolbarConst.REDO)
    util.clickButton(MainToolbarConst.REDO)
    
def checkpoint_redo():        
    util.clickOnWorkspace(pc4.x, pc4.y)
    pc4.exists()