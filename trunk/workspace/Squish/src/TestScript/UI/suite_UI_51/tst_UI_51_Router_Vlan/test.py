##################################################################
#@author: Thi Nguyen
##############################################################
from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Utility.Util import Util
from API.Utility import UtilConst
from TestScript.UI.suite_UI_51.tst_UI_51_Router_Config.test import createTopology
import os
#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 200, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 200, 200, "Router1")

def main():
    util.init()
    createTopology()
    addVlan()
    removeVlan()

def createTopology():
    router0.create()
    router1.create()
    util.clickOnSimulation()
    util.clickOnRealtime()

    
def addVlan():
    for rtr in [router0, router1]:
        rtr.select()
        rtr.clickConfigTab()
        rtr.config.selectInterface('VLAN Database')
        rtr.config.vlan.addVlan('SwitchCopy', '100')
        rtr.cli.textCheckPoint("name SwitchCopy")
        rtr.cli.textCheckPoint("vlan 100")
    
def removeVlan():
    for rtr in [router0, router1]:
        rtr.select()
        rtr.config.selectInterface('VLAN Database')
        rtr.config.vlan.removeVlanNumber('100')
        rtr.cli.textCheckPoint("no vlan 100")
        rtr.close()