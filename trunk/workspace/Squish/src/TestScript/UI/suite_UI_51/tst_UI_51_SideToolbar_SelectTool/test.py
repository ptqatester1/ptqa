from API.ComponentBox import ComponentBoxConst
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Device.EndDevice.PC.PC import PC
from API.Utility import UtilConst
from API.Utility.Util import Util

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 200, 200, "PC1")
pc2 = PC(ComponentBoxConst.DeviceModel.PC, 300, 200, "PC2")
util = Util()

def main():  
    util.init()
    createTopology()
    Step1()
    Step2()
    Step3()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,pc0.model,pc0.x,pc0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,pc1.model,pc1.x,pc1.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,pc2.model,pc2.x,pc2.y)

def Step1():
    util.clickButton(CommonToolsBarConst.SELECT_TOOL)
    pc0.updateName()
    pc0.exists()
    
def Step2():
    util.mouseDrag(UtilConst.WORKSPACE, 201, 199, -3, 97)
    util.clickOnWorkspace(197, 292)
    pc1.updateName()
    pc1.exists()
    
def Step3():
    util.mouseDrag(UtilConst.WORKSPACE, 50, 150, 450, 250)
    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    snooze(1)
    test.compare(findObject(CommonToolsBarConst.DELETE_CONFIRM_DIALOG).visible, True)