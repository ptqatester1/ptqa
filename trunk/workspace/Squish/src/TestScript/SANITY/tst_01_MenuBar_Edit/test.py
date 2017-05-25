#######################
#@author: Pamela Vinco
#######################
from API.MenuBar.Edit.EditConst import EditConst
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

#Function initialization
util = Util()
editMenu = Edit()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, "PC0")
copypc0= PC(ComponentBoxConst.DeviceModel.PC, 100, 50, "PC0")

def main():
    util.init()
    edit_copy()
    edit_paste()
    edit_undo()
    edit_redo()
    
def edit_copy():
    #Select Copy from Edit Menu to copy an instance of the device
    pc0.create()    
    util.selectObjectsOnWorkspace(pc0.x, pc0.y)
    editMenu.selectEditItem(EditConst.COPY)
    
def edit_paste():
    #Select Paste from Edit Menu and check that the copied instance of the device exists
    editMenu.selectEditItem(EditConst.PASTE)
    copypc0.exists()
    
def edit_undo():
    #Select Undo from Edit Menu and check that the copied instance of the device is removed from the workspace
    editMenu.selectEditItem(EditConst.UNDO)
    copypc0.doesNotExist()
    
def edit_redo():
    #Select Redo from Edit Menu and check that the copied instance of the device is put back on the workspace
    editMenu.selectEditItem(EditConst.REDO)
    copypc0.exists()