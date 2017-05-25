from API.ComponentBox import ComponentBoxConst
from API.Device.AccessPoint.AccessPoint import AccessPoint
from API.Device.Bridge.Bridge import Bridge
from API.Device.Cloud.Cloud import Cloud
from API.Device.EndDevice.IPPhone.IPPhone import IPPhone
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Printer.Printer import Printer
from API.Device.EndDevice.Server.Server import Server
from API.Device.Hub.Hub import Hub

from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Device.Modem.Modem import Modem
from API.Device.Repeater.Repeater import Repeater
from API.Device.Router.Router import Router
from API.Device.Switch.Switch import Switch

from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbar import GoldenPhysicalToolbar
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Utility.Util import Util

#Function initialization
goldenPhysicalToolbar = GoldenPhysicalToolbar()
util = Util()

#Device initialization
accessPoint0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 100, 100, "Access Point0")
bridge0 = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 200, 100, "Bridge0")
cloud0 = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 300, 100, "Cloud0")
cloud1 = Cloud(ComponentBoxConst.DeviceModel.CLOUD_EMPTY, 400, 100, "Cloud1")
ipPhone0 = IPPhone(ComponentBoxConst.DeviceModel.IPPHONE, 500, 100, "IP Phone0")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 600, 100, "PC0")
printer0 = Printer(ComponentBoxConst.DeviceModel.PRINTER, 700, 100, "Printer0")
server0 = Server(ComponentBoxConst.DeviceModel.PC, 100, 200, "Server0")
hub0 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 200, 200, "Hub0")
wirelessRouter0 = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 300, 200, "Wireless Router0")
dslModem0 = Modem(ComponentBoxConst.DeviceModel.DSL_MODEM, 400, 200, "DSL Modem0")
cableModem0 = Modem(ComponentBoxConst.DeviceModel.CABLE_MODEM, 500, 200, "Cable Modem0")
repeater0 = Repeater(ComponentBoxConst.DeviceModel.REPEATER_PT, 600, 200, "Repeater0")
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 300, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2620XM, 200, 300, "Router1")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 300, 300, "Router2")
router3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 400, 300, "Router3")
router4 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 500, 300, "Router4")
router5 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT_EMPTY, 600, 300, "Router5")
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 400, "Switch0")
switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 200, 400, "Switch1")
switch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 400, 400, "Switch2")
switch3 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 400, 400, "Switch3")
switch4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 500, 400, "Switch4")
switch5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 600, 400, "Switch5")

def main():
    util.init()
    createTopology1()
    checkPoint1()
    createTopology2()
    checkPoint2()

def createTopology1():
    accessPoint0.create()
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, bridge0.model, bridge0.x, bridge0.y)
    cloud0.create()
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cloud1.model, cloud1.x, cloud1.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, ipPhone0.model, ipPhone0.x, ipPhone0.y)
    pc0.create()
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, printer0.model, printer0.x, printer0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, server0.model, server0.x, server0.y)
    util.createDevice(ComponentBoxConst.DeviceType.HUB, hub0.model, hub0.x, hub0.y)
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, wirelessRouter0.model, wirelessRouter0.x, wirelessRouter0.y)

def checkPoint1():
    util.clickOnPhysical()
    util.clickButton(GoldenPhysicalToolbarConst.WORKING_CLOSET)
    util.click_x_y(":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CRackView1.qt_scrollarea_viewport.CRackViewWidget1.CRack1.CModuleContainer5.CModuleTarget13", 170, 70)
    hub0.updateName()
    try:
        hub0.clickPhysicalTab()
        test.passes("Current working closet contains Hub0")
    except LookupError, e:
        test.fail("Current working closet does not contain Hub0")
    util.clickOnLogical()

def createTopology2():
    util.createDevice(ComponentBoxConst.DeviceType.WAN, dslModem0.model, dslModem0.x, dslModem0.y)
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cableModem0.model, cableModem0.x, cableModem0.y)
    util.createDevice(ComponentBoxConst.DeviceType.HUB, repeater0.model, repeater0.x, repeater0.y)
    router0.create()
    router1.create()
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router2.model, router2.x, router2.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router3.model, router3.x, router3.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router4.model, router4.x, router4.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router5.model, router5.x, router5.y)
    switch0.create()
    switch1.create()
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, switch2.model, switch2.x, switch2.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, switch3.model, switch3.x, switch3.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, switch4.model, switch4.x, switch4.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, switch5.model, switch5.x, switch5.y)

def checkPoint2():
    util.clickOnPhysical()
    util.clickButton(GoldenPhysicalToolbarConst.WORKING_CLOSET)
    snooze(2)
    util.click_x_y(":CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.QStackedWidget1.CWorkspace1.CRackView1.qt_scrollarea_viewport.CRackViewWidget1.CRack2.CModuleContainer6.CModuleTarget10", 170, 70)
    
    switch5.updateName()
    try:
        switch5.clickPhysicalTab()
        test.passes("Current working closet contains Switch5")
    except LookupError, e:
        test.fail("Current working closet does not contain Switch5")
