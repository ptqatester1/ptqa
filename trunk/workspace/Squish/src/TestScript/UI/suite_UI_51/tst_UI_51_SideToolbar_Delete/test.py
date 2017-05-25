#Balaji   
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Device.Router.Router import Router

from API.Device.Switch.Switch import Switch

from API.Utility.Util import Util
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbarConst import GoldenLogicalToolbarConst
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.MenuBar.File.Save.SaveConst import SaveConst

util = Util()
commonToolsBar = CommonToolsBar()
fileMenu = File()
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 398, 251, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 536, 247, "PC1")
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 253, 178, "Router0")
s0=  Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 390, 149, "Switch0")
s1=  Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 537, 151, "Switch1")

def main():
    util.init()
    createTopology()
    connectDevices()
    cluster1()
    cluster2()
    addplacenote()    
    deleterouter()    
    deletecluster1()
    deletecluster2()
    deleteplacenote()
    deletePCs()
def createTopology():
    
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,pc0.model,pc0.x,pc0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,pc1.model,pc1.x,pc1.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER,r0.model,r0.x,r0.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH,s0.model,s0.x,s0.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH,s1.model,s1.x,s1.y)
def connectDevices():
    
    util.connect(pc0.x, pc0.y, pc1.x, pc1.y, ComponentBoxConst.Connection.CONN_STRAIGHT, "FastEthernet0", "FastEthernet0")
def cluster1():
    util.selectObjectsOnWorkspace(pc0.x, pc0.y)
    util.selectObjectsOnWorkspace(pc1.x, pc1.y)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
def cluster2():
    util.selectObjectsOnWorkspace(s0.x, s0.y)
    util.selectObjectsOnWorkspace(s1.x, s1.y)
    util.clickButton(GoldenLogicalToolbarConst.NEW_CLUSTER)
def addplacenote():
    util.clickButton(CommonToolsBarConst.PLACENOTE_TOOL)
    util.clickOnWorkspace(100, 100)
    util.typeText(CommonToolsBarConst.PLACENOTE_TEXT_EDIT, "placenote")
    fileMenu.selectFileItem(FileConst.SAVE)
    snooze(2)
    util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    util.clickOnWorkspace(200, 100)
    
def deleteplacenote():
    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    
    util.clickOnWorkspace(100, 100)


def deleterouter():

    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    util.clickOnWorkspace(253, 178)
def deletecluster1():

    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    util.clickOnWorkspace(465, 263)
    util.textCheckPoint(CommonToolsBarConst.DELETE_CONFIRM_DIALOG, "Do you want to uncluster the components of Cluster0", 1)
    snooze(1)
    util.clickButton(CommonToolsBarConst.DELETE_CLUSTER_DIALOG_UNCLUSTER)
    
def deletecluster2():

    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    util.clickOnWorkspace(459, 150)
    util.textCheckPoint(CommonToolsBarConst.DELETE_CONFIRM_DIALOG, "Do you want to uncluster the components of Cluster1", 1)
    snooze(1)
    util.clickButton(CommonToolsBarConst.DELETE_CLUSTER_DIALOG_UNCLUSTER)

    

def deletePCs():
    util.clickButton(CommonToolsBarConst.SELECT_TOOL)
    util.selectObjectsOnWorkspace(pc0.x, pc0.y)
    util.selectObjectsOnWorkspace(pc1.x, pc1.y)
    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    snooze(5)
    util.textCheckPoint(CommonToolsBarConst.DELETE_CONFIRM_DIALOG, "Do you want to delete the 2 selected items", 1)
    snooze(1)
    util.clickButton(CommonToolsBarConst.DELETE_CONFIRM_DIALOG_NO)
    
    util.clickButton(CommonToolsBarConst.SELECT_TOOL)
    util.selectObjectsOnWorkspace(pc0.x, pc0.y)
    util.selectObjectsOnWorkspace(pc1.x, pc1.y)
    
    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    
    util.textCheckPoint(CommonToolsBarConst.DELETE_CONFIRM_DIALOG, "Do you want to delete the 2 selected items", 1)
    snooze(1)
    util.clickButton(CommonToolsBarConst.DELETE_CONFIRM_DIALOG_CANCEL)
    
    util.clickButton(CommonToolsBarConst.SELECT_TOOL)
    util.selectObjectsOnWorkspace(pc0.x, pc0.y)
    util.selectObjectsOnWorkspace(pc1.x, pc1.y)
    util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    
    util.textCheckPoint(CommonToolsBarConst.DELETE_CONFIRM_DIALOG, "Do you want to delete the 2 selected items", 1)
    snooze(1)
    util.clickButton(CommonToolsBarConst.DELETE_CONFIRM_DIALOG_YES)
    