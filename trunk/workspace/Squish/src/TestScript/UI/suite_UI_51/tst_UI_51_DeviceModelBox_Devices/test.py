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
from API.Utility.Util import Util

util = Util()

r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 105, "Router0")
r2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2620XM, 200, 105, "Router1")
r3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 300, 105, "Router2")
r4 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 400, 105, "Router3")
r5 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 500, 105, "Router4")
r6 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT_EMPTY, 600, 105, "Router5")

s1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 180, "Switch0")
s2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 200, 180, "Switch1")
s3 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 300, 180, "Switch2")
s4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 400, 180, "Switch3")
s5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 500, 180, "Switch4")
s6 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 600, 180, "Switch5")
bridge = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 700, 180, "Bridge0")

hub1 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 100, 255, "Hub0")
repeater1 = Repeater(ComponentBoxConst.DeviceModel.REPEATER_PT, 200, 255, "Repeater0")
access = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 300, 255, "Access Point0")
linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 400, 255, "Wireless Router0")
dsl = Modem(ComponentBoxConst.DeviceModel.DSL_MODEM, 500, 255, "DSL Modem0")
cable = Modem(ComponentBoxConst.DeviceModel.CABLE_MODEM, 600, 255, "Cable Modem0")

pc1 = PC(ComponentBoxConst.DeviceModel.PC, 100, 30, "PC0")
server = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 30, "Server0")
printer = Printer(ComponentBoxConst.DeviceModel.PRINTER, 300, 30, "Printer0")
phone =IPPhone(ComponentBoxConst.DeviceModel.IPPHONE, 400, 30, "IP Phone0")
cloud1 = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 500, 30, "Cloud0")
cloud2 = Cloud(ComponentBoxConst.DeviceModel.CLOUD_EMPTY, 600, 30, "Cloud1")

r7 = Router(ComponentBoxConst.DeviceModel.CUSTOM_1841, 100, 330, "Router6")
r8 = Router(ComponentBoxConst.DeviceModel.CUSTOM_2621XM, 200, 330, "Router7")
r9 = Router(ComponentBoxConst.DeviceModel.CUSTOM_2811, 300, 330, "Router8")
pc2 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 400, 330, "PC1")


def main():
    util.init()
    checkpoint1()
    createDevices()
    checkpoint2()
    
def checkpoint1():
    util.clickButton(ComponentBoxConst.DeviceType.ROUTER)
    snooze(2)


def createDevices():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r1.model, r1.x, r1.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r2.model, r2.x, r2.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r3.model, r3.x, r3.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r4.model, r4.x, r4.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r5.model, r5.x, r5.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r6.model, r6.x, r6.y)
    
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s1.model, s1.x, s1.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s2.model, s2.x, s2.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s3.model, s3.x, s3.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s4.model, s4.x, s4.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s5.model, s5.x, s5.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s6.model, s6.x, s6.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, bridge.model, bridge.x, bridge.y)
    
    util.createDevice(ComponentBoxConst.DeviceType.HUB, hub1.model, hub1.x, hub1.y)
    util.createDevice(ComponentBoxConst.DeviceType.HUB, repeater1.model, repeater1.x, repeater1.y)
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, access.model, access.x, access.y)
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, linksys.model, linksys.x, linksys.y)
    util.createDevice(ComponentBoxConst.DeviceType.WAN, dsl.model, dsl.x, dsl.y)
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cable.model, cable.x, cable.y)
    
    pc1.create()
    server.create()
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, printer.model, printer.x, printer.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, phone.model, phone.x, phone.y)
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cloud1.model, cloud1.x, cloud1.y)
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cloud2.model, cloud2.x, cloud2.y)
    
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, r7.model, r7.x, r7.y)
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, r8.model, r8.x, r8.y)
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, r9.model, r9.x, r9.y)
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, pc2.model, pc2.x, pc2.y)  

def checkpoint2():
    r1.exists()
    r1.exists()
    r2.exists()
    r3.exists()
    r4.exists()
    r5.exists()
    r6.exists()
    s1.exists()
    s2.exists()
    s3.exists()
    s4.exists()
    s5.exists()
    s6.exists()
    bridge.exists()
    hub1.exists()
    repeater1.exists()
    access.exists()
    linksys.exists()
    dsl.exists()
    cable.exists()
    pc1.exists()
    server.exists()
    printer.exists()
    cloud1.exists()
    cloud2.exists()
    r7.exists()
    r8.exists()
    r9.exists()
    pc2.exists()