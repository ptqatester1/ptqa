##################################################################
#@author: Thi Nguyen
##############################################################
from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 200, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2620XM, 200, 200, "Router1")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 300, 200, "Router2")
router3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 400, 200, "Router3")
router4 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 500, 200, "Router4")
router5 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT_EMPTY, 600, 200, "Router5")

def main():
    util.init()
    createTopology()
    addRIP(router0)
    addRIP(router1)
    addRIP(router2)
    addRIP(router3)
    addRIP(router4)
    addRIP(router5)
    removeRIP(router0)
    removeRIP(router1)
    removeRIP(router2)
    removeRIP(router3)
    removeRIP(router4)
    removeRIP(router5)

def createTopology():
    router0.create()
    router1.create()
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router2.model, router2.x, router2.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router3.model, router3.x, router3.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router4.model, router4.x, router4.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router5.model, router5.x, router5.y)
    util.clickOnSimulation()
    util.clickOnRealtime()
    
def addRIP(device):
    device.select()
    device.clickConfigTab()
    device.config.selectInterface('RIP')
    device.config.routing.rip.addRoute("10.0.0.0")
    device.cli.textCheckPoint("network 10.0.0.0", 1)

def removeRIP(device):
    device.select()
    device.config.selectInterface('RIP')
    device.config.routing.rip.removeRow(0)
    device.cli.textCheckPoint("no network 10.0.0.0", 1)

