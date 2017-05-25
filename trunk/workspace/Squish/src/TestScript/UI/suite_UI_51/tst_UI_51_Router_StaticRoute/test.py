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
    addStaticRoute(router0)
    addStaticRoute(router1)
    addStaticRoute(router2)
    addStaticRoute(router3)
    addStaticRoute(router4)
    addStaticRoute(router5)
    removeStaticRoute(router0)
    removeStaticRoute(router1)
    removeStaticRoute(router2)
    removeStaticRoute(router3)
    removeStaticRoute(router4)
    removeStaticRoute(router5)

def createTopology():
    router0.create()
    router1.create()
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router2.model, router2.x, router2.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router3.model, router3.x, router3.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router4.model, router4.x, router4.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router5.model, router5.x, router5.y)
    util.clickOnSimulation()
    util.clickOnRealtime()
    
def addStaticRoute(device):
    device.select()
    device.clickConfigTab()
    device.config.selectInterface('Static')
    device.config.routing.static.addRoute("10.0.0.0", "255.0.0.0", "10.0.0.1")
    device.cli.textCheckPoint("ip route 10.0.0.0 255.0.0.0 10.0.0.1", 1)

def removeStaticRoute(device):
    util.clickOnWorkspace(device.x, device.y)
    device.updateName()
    device.config.selectInterface('Static')
    device.config.routing.static.removeRow(0)
    device.cli.textCheckPoint("no ip route 10.0.0.0 255.0.0.0 10.0.0.1", 1)

