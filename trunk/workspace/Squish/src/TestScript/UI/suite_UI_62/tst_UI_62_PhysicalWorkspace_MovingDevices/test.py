########################
##Author: AbbasH
########################

from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Utility import UtilConst
from API.Utility.Util import Util
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst
from API.ComponentBox.ComponentBox import ComponentBox
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Device.EndDevice.TV.TV import TV
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Workspace.Physical import Physical, Closet

#Function initialization
util = Util()
componentBox = ComponentBox()

global TVOnTable2, Table3, TVOnTable3, RouterOnRack1, Rack2, RouterOnRack2

TVOnTable2 = GoldenPhysicalToolbarConst.TABLE_BASE_2 + "4.QWidget2.QWidget1.CModuleContainer1"
Table3 = GoldenPhysicalToolbarConst.TABLE_BASE_2 + "5.QWidget2.QWidget1"
TVOnTable3 = GoldenPhysicalToolbarConst.TABLE_BASE_2 + "5.QWidget2.QWidget2.CModuleContainer1"
RouterOnRack1 = GoldenPhysicalToolbarConst.RACK_BASE + "1.CModuleContainer1"
Rack2 = GoldenPhysicalToolbarConst.RACK_BASE + "2.QWidget1"
RouterOnRack2 = GoldenPhysicalToolbarConst.RACK_BASE + "2.CModuleContainer2"

tv0OnTable2X = 103
tv0OnTable2Y = 269
tv0OnTable3X = 100
tv0OnTable3Y = 292

r4OnRack1X = 296
r4OnRack1Y = 152
r4OnRack2X = 90
r4OnRack2Y = 567

r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, 'Router1')
r4 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 300, 300, "Router4")
tv0 = TV(ComponentBoxConst.DeviceModel.TV, 0, 0, "TV0")


def main():
    util.init()
    util.maximizePT()
    maketop()
    moveDevices()

def maketop():
    util.open("PhysicalWorkspace_MovingDevices.pkt", UtilConst.UI_TEST)    
    util.clickOnPhysical()
    snooze(2)
    util.clickOnPhysicalWorkspace(215, 194)
    snooze(2)
    util.clickOnPhysicalWorkspace(125, 99)
    snooze(2)
    util.clickOnPhysicalWorkspace(316, 176)

def moveDevices():
    Physical().goTo('Home City', 'Corporate Office', 'Main Wiring Closet')
    
    devices = Closet().rackDeviceDict
    racks = Closet().rackDict
    router4 = devices['rack1']['dev1']
    checkDeviceExists(r4, router4)
    
    util.dragAndDrop(router4, 100, 20, racks['rack2'], 100, 400)
    
    devices = Closet().rackDeviceDict
    racks = Closet().rackDict
    
    router1 = devices['rack2']['dev1']
    router4 = devices['rack2']['dev2']
    checkDeviceExists(r1, router1)
    checkDeviceExists(r4, router4)
    
    
    util.maximizePT()
    util.clickButton(MainToolbarConst.ZOOM_OUT)
    
def checkDeviceExists(dev, devobject):
    util.click(devobject)
    dev.updateName()
    dev.clickTab('Physical')
    dev.close()
    test.passes('Device ' + dev.displayName + ' exists')