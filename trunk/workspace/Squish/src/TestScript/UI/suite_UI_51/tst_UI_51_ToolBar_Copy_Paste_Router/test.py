from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router

from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst

util = Util()
editMenu = Edit()
commonToolsBar = CommonToolsBar()

CopyRouter0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 50, "CopyRouter0")
CopyRouter1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2620XM, 200,  50, "CopyRouter1")
CopyRouter2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 300, 50, "CopyRouter2")
CopyRouter3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 400, 50, "CopyRouter3")
CopyRouter4 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 500, 50, "CopyRouter4")
CopyRouter5 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT_EMPTY, 635,  35, "CopyRouter5")

Router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
Router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2620XM,  200, 100, "Router1")
Router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 300, 100, "Router2")
Router3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 400, 100,  "Router3")
Router4 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 500, 100, "Router4")
Router5 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT_EMPTY,  600, 100, "Router5")

def main():
    util.init()
    copyPaste_deviceOnWorkspace()



def copyPaste_deviceOnWorkspace():
    for rtr in [Router0, Router1, Router2, Router3, Router4, Router5]:
        rtr.create()
    util.clickOnSimulation()
    util.clickOnRealtime()
    for rtr in [Router0, Router1, Router2, Router3, Router4, Router5]:
        rtr.select()
        rtr.clickConfigTab()
        rtr.config.settings.hostname("RouterCopy")
        rtr.config.selectInterface('Static')
        rtr.config.routing.static.addRoute("10.0.0.0", "255.0.0.0", "10.1.1.1")
        rtr.config.selectInterface('RIP')
        rtr.config.routing.rip.addRoute("10.0.0.0")
        if not rtr is Router5:
            rtr.config.selectInterface("FastEthernet0/0")
            rtr.config.interface.ethernet.ip("10.1.1.2")
            rtr.config.interface.ethernet.subnet("255.0.0.0")
            rtr.config.interface.ethernet.bandwidth(None)
            rtr.config.interface.ethernet.duplex(None)
            rtr.config.interface.ethernet.portStatus(None)
        rtr.close()

    util.selectObjectsOnWorkspace(Router0.x, Router0.y)
    util.selectObjectsOnWorkspace(Router1.x, Router1.y)
    util.selectObjectsOnWorkspace(Router2.x, Router2.y)
    util.selectObjectsOnWorkspace(Router3.x, Router3.y)
    util.selectObjectsOnWorkspace(Router4.x, Router4.y)
    util.selectObjectsOnWorkspace(Router5.x, Router5.y)
    snooze(2)
    util.clickButton(MainToolbarConst.COPY)
    util.clickButton(MainToolbarConst.PASTE)

    for i, rtr in enumerate([CopyRouter0, CopyRouter1, CopyRouter2, CopyRouter3, CopyRouter4, CopyRouter5]):
        rtr.select()
        rtr.clickConfigTab()
        rtr.config.settings.check.hostname("RouterCopy")
        rtr.config.settings.check.displayName("CopyRouter%s"%(i,))
        rtr.config.selectInterface('Static')
        rtr.config.routing.static.removeRow(0)
        rtr.config.selectInterface('RIP')
        rtr.config.routing.rip.removeRow(0)
        rtr.cli.textCheckPoint("no ip route 10.0.0.0 255.0.0.0 10.1.1.1")       
        rtr.cli.textCheckPoint("no network 10.0.0.0")
        if not rtr is CopyRouter5:
            rtr.config.selectInterface("FastEthernet0/0")
            rtr.config.interface.ethernet.check.ip("10.1.1.2")
            rtr.config.interface.ethernet.check.subnet("255.0.0.0")
            rtr.config.interface.ethernet.check.bandwidth('Auto', False)
            rtr.config.interface.ethernet.check.duplex('Auto', False)
            rtr.config.interface.ethernet.check.portStatus(True)
        rtr.close()