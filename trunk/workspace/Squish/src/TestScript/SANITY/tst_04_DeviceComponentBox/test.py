#######################
#@author: Pamela Vinco
#######################
from API.ComponentBox import ComponentBoxConst
from API.Device.AccessPoint.AccessPoint import AccessPoint
from API.Device.Bridge.Bridge import Bridge
from API.Device.Cloud.Cloud import Cloud
from API.Device.EndDevice.IPPhone.IPPhone import IPPhone
from API.Device.EndDevice.AnalogPhone.AnalogPhone import AnalogPhone
from API.Device.EndDevice.TV.TV import TV
from API.Device.EndDevice.VoIP.VoIP import VoIP
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Printer.Printer import Printer
from API.Device.EndDevice.Server.Server import Server
from API.Device.Hub.Hub import Hub
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Device.Modem.Modem import Modem
from API.Device.Repeater.Repeater import Repeater
from API.Device.Router.Router import Router
from API.Device.Switch.Switch import Switch
from API.Device.Extension.Extension import Extension
from API.Device.Extension.ExtensionConst import ExtensionConst
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization

#ROUTERS
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 50, "Router0")
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1941, 150, 50, "Router1")
r2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2620XM, 200, 50, "Router2")
r3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 250, 50, "Router3")
r4 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 300, 50, "Router4")
r5 = Router(ComponentBoxConst.DeviceModel.ROUTER_2901, 350, 50, "Router5")
r6 = Router(ComponentBoxConst.DeviceModel.ROUTER_2911, 400, 50, "Router6")
r7 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 450, 50, "Router7")
r8 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT_EMPTY, 500, 50, "Router8")

#SWITCHES
s0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 100, "Switch0")
s1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 150, 100, "Switch1")
s2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 200, 100, "Switch2")
s3 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 250, 100, "Switch3")
s4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 300, 100, "Switch4")
s5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 350, 100, "Switch5")
bridge0 = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 400, 100, "Bridge0")

#HUBS
hub0 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 100, 150, "Hub0")
repeater0 = Repeater(ComponentBoxConst.DeviceModel.REPEATER_PT, 150, 150, "Repeater0")
coaxialSplitter0 = Hub(ComponentBoxConst.DeviceModel.COAXIAL_SPLITTER_PT, 200, 150, "Coaxial Splitter0") 

#WIRELESS DEVICES
access0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 250, 150, "Access Point0")
access1 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT_A, 300, 150, "Access Point1")
access2 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT_N, 350, 150, "Access Point2")
linksys0 = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 400, 150, "Wireless Router0")

#END DEVICES
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
laptop0 = PC(ComponentBoxConst.DeviceModel.LAPTOP, 150, 200, "Laptop0")
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 200, "Server0")
printer0 = Printer(ComponentBoxConst.DeviceModel.PRINTER, 250, 200, "Printer0")
ipphone0 = IPPhone(ComponentBoxConst.DeviceModel.IPPHONE, 300, 200, "IP Phone0")
voip0 = VoIP(ComponentBoxConst.DeviceModel.VOIP, 350, 200, "Home VoIP0")
phone0 = AnalogPhone(ComponentBoxConst.DeviceModel.ANALOG_PHONE, 400, 200, "Analog Phone0")
tv0 = TV(ComponentBoxConst.DeviceModel.TV, 450, 200, "TV0")
wirelessTablet0 = PC(ComponentBoxConst.DeviceModel.TABLET_PC, 500, 200, "Tablet PC0")
smartDevice0 = PC(ComponentBoxConst.DeviceModel.PDA, 550, 200, "Pda0")
genericWireless0 = PC(ComponentBoxConst.DeviceModel.WIRELESS_END_DEVICE, 600, 200, "Wireless End Device0")
genericWired0 = PC(ComponentBoxConst.DeviceModel.WIRED_END_DEVICE, 650, 200, "Wired End Device0")

#WAN Emulation
cloud0 = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 100, 250, "Cloud0")
cloud1 = Cloud(ComponentBoxConst.DeviceModel.CLOUD_EMPTY, 150, 250, "Cloud1")
dsl0 = Modem(ComponentBoxConst.DeviceModel.DSL_MODEM, 200, 250, "DSL Modem0")
cable0 = Modem(ComponentBoxConst.DeviceModel.CABLE_MODEM, 250, 250, "Cable Modem0")

#CUSTOM MADE DEVICES
r9 = Router(ComponentBoxConst.DeviceModel.CUSTOM_1841, 300, 250, "Router9")
r10 = Router(ComponentBoxConst.DeviceModel.CUSTOM_2621XM, 350, 250, "Router10")
r11 = Router(ComponentBoxConst.DeviceModel.CUSTOM_2811, 400, 250, "Router11")
pc1 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 450, 250, "PC1")

#MULTIUSER
multiuser0 = Extension(ComponentBoxConst.DeviceModel.MULTIUSER, 500, 250, "Peer0")

def main():
    util.init()
    createDevices()
    checkpoint()

def createDevices():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r1.model, r1.x, r1.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r2.model, r2.x, r2.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r3.model, r3.x, r3.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r4.model, r4.x, r4.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r5.model, r5.x, r5.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r6.model, r6.x, r6.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r7.model, r7.x, r7.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r8.model, r8.x, r8.y)
    
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s0.model, s0.x, s0.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s1.model, s1.x, s1.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s2.model, s2.x, s2.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s3.model, s3.x, s3.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s4.model, s4.x, s4.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, s5.model, s5.x, s5.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, bridge0.model, bridge0.x, bridge0.y)
    
    util.createDevice(ComponentBoxConst.DeviceType.HUB, hub0.model, hub0.x, hub0.y)
    util.createDevice(ComponentBoxConst.DeviceType.HUB, repeater0.model, repeater0.x, repeater0.y)
    util.createDevice(ComponentBoxConst.DeviceType.HUB, coaxialSplitter0.model, coaxialSplitter0.x, coaxialSplitter0.y)

    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, access0.model, access0.x, access0.y)
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, access1.model, access1.x, access1.y)
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, access2.model, access2.x, access2.y)
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, linksys0.model, linksys0.x, linksys0.y)
    
    pc0.create()
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, laptop0.model, laptop0.x, laptop0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, server0.model, server0.x, server0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, printer0.model, printer0.x, printer0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, ipphone0.model, ipphone0.x, ipphone0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, voip0.model, voip0.x, voip0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, phone0.model, phone0.x, phone0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, tv0.model, tv0.x, tv0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, wirelessTablet0.model, wirelessTablet0.x, wirelessTablet0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, smartDevice0.model, smartDevice0.x, smartDevice0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, genericWireless0.model, genericWireless0.x, genericWireless0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, genericWired0.model, genericWired0.x, genericWired0.y)  

    cloud0.create()
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cloud1.model, cloud1.x, cloud1.y)
    util.createDevice(ComponentBoxConst.DeviceType.WAN, dsl0.model, dsl0.x, dsl0.y)
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cable0.model, cable0.x, cable0.y)
    
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, r9.model, r9.x, r9.y)
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, r10.model, r10.x, r10.y)
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, r11.model, r11.x, r11.y)
    pc1.create()
    
    util.createDevice(ComponentBoxConst.DeviceType.MULTIUSER, multiuser0.model, multiuser0.x, multiuser0.y)

def checkpoint():
    #Check that the devices created earlier exist
    r0.exists()
    r1.exists()
    r2.exists()
    r3.exists()
    r4.exists()
    r5.exists()
    r6.exists()
    r7.exists()
    r8.exists()
    
    s0.exists()
    s1.exists()
    s2.exists()
    s3.exists()
    s4.exists()
    s5.exists()
    bridge0.exists()
    
    hub0.exists()
    repeater0.exists()
    coaxialSplitter0.exists()  
    
    access0.exists()
    access1.exists()
    access2.exists()
    linksys0.exists()
    
    pc0.exists()
    laptop0.exists()
    server0.exists()
    printer0.exists()
    ipphone0.exists()
    voip0.exists()
    phone0.exists()
    tv0.exists()
    wirelessTablet0.exists()
    smartDevice0.exists()
    genericWireless0.exists()
    genericWired0.exists()
    
    cloud0.exists()
    cloud1.exists()
    dsl0.exists()
    cable0.exists()

    r9.exists()
    r10.exists()
    r11.exists()
    pc1.exists()
    
    util.clickOnWorkspace(multiuser0.x, multiuser0.y)
    if object.exists(ExtensionConst.MULTIUSER_CONNECT_DIALOG):
        test.passes("Multiuser cloud exists on the workspace")
    else:
        test.fail("Multiuser cloud does not exist on the workspace")