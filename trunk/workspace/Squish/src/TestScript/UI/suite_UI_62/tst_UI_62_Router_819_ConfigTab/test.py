########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase import DeviceBaseConst
from API.SquishSyntax import SquishSyntax as sq

util = Util()
router = Router(ComponentBoxConst.DeviceModel.ROUTER_819, 175, 80, 'Router0')

def main():
    util.init()
    create()   
    checkGlobal()
    checkRouting()
    checkSwitching()
    checkInterfaceGigbitSerial()
    checkInterfaceFast()
    checkInterfaceWlan()
    ap0test()
    checkInterfaceCell()
    
def create():    
    router.create()
    router.select()
    util.speedUpConvergence()
    router.clickConfigTab()  

def checkGlobal():
    router.config.settings.check.displayName("Router0")
    router.config.settings.check.hostname("Router")
    router.config.settings.hostname('R0')
    snooze(2)
    router.cli.textCheckPoint('''Router\(config\)#hostname R0
R0\(config\)#''')
    router.config.settings.eraseButton()
    router.config.settings.popups.eraseStartupConfigNoButton()
    router.config.settings.saveButton()
    router.config.settings.loadButton()
    router.config.settings.fileDialog.cancelButton()
    router.config.settings.mergeButton()
    router.config.settings.fileDialog.cancelButton()
    router.config.settings.exportRunningConfigButton()
    router.config.settings.fileDialog.cancelButton()

    router.config.selectInterface('Algorithm Settings')
    router.config.algorithmSettings.check.globalSettings(True)
    router.config.algorithmSettings.check.halfOpenSessionMultiplier(None, property='enabled', value=False)
    router.config.algorithmSettings.check.halfOpenSessionMultiplier('1')
    router.config.algorithmSettings.check.maxConnections(None, property='enabled', value=False)
    router.config.algorithmSettings.check.maxConnections('100')
    router.config.algorithmSettings.check.maxOpen(None, property='enabled', value=False)
    router.config.algorithmSettings.check.maxOpen('1000')
    router.config.algorithmSettings.check.maxRetransmission(None, property='enabled', value=False)
    router.config.algorithmSettings.check.maxRetransmission('1000')
    
    router.config.algorithmSettings.globalSettings(None)
    router.config.algorithmSettings.halfOpenSessionMultiplier('2')
    router.config.algorithmSettings.maxConnections('50')
    router.config.algorithmSettings.maxOpen('1500')
    router.config.algorithmSettings.maxRetransmission('1500')
    
    router.config.algorithmSettings.check.globalSettings(False)
    router.config.algorithmSettings.check.halfOpenSessionMultiplier(None, property='enabled', value=True)
    router.config.algorithmSettings.check.halfOpenSessionMultiplier('2')
    router.config.algorithmSettings.check.maxConnections(None, property='enabled', value=True)
    router.config.algorithmSettings.check.maxConnections('50')
    router.config.algorithmSettings.check.maxOpen(None, property='enabled', value=True)
    router.config.algorithmSettings.check.maxOpen('1500')
    router.config.algorithmSettings.check.maxRetransmission(None, property='enabled', value=True)
    router.config.algorithmSettings.check.maxRetransmission('1500')
    
def checkRouting():    
    router.config.selectInterface('Static')
    test.compare(router.config.routing.static.routingTable.rowCount, 0)
    router.config.routing.static.addRoute('172.31.0.0', '255.255.255.0', '172.31.1.193')
    router.cli.textCheckPoint('ip route 172.31.0.0 255.255.255.0 172.31.1.193')
    router.config.routing.static.addRoute('172.31.1.196', '255.255.255.252', '172.31.1.193')
    router.cli.textCheckPoint('ip route 172.31.1.196 255.255.255.252 172.31.1.193')
    test.compare(router.config.routing.static.routingTable.rowCount, 2)
    router.config.routing.static.removeRow(0)
    test.compare(router.config.routing.static.routingTable.rowCount, 1)
    
    router.config.selectInterface('RIP')
    test.compare(router.config.routing.rip.routingTable.rowCount, 0)
    router.config.routing.rip.addRoute('192.168.1.1')
    router.cli.textCheckPoint('''R0\(config\)#router rip
R0\(config-router\)#network 192.168.1.0''')
    test.compare(router.config.routing.rip.routingTable.rowCount, 1)
    router.config.routing.rip.removeRow(0)
    test.compare(router.config.routing.rip.routingTable.rowCount, 0)
    router.cli.textCheckPoint('no network 192.168.1.0')
        
def checkSwitching():
    router.config.selectInterface('VLAN Database')
    test.compare(router.config.vlan.vlanTable.rowCount, 5)
    router.config.vlan.check.vlanTableRow('default', '1', 0)
    router.config.vlan.removeRow(0)
    router.config.vlan.check.vlanTableRow('fddi-default', '1002', 1)
    router.config.vlan.removeRow(1)
    router.config.vlan.check.vlanTableRow('token-ring-default', '1003', 2)
    router.config.vlan.removeRow(2)
    router.config.vlan.check.vlanTableRow('fddinet-default', '1004', 3)
    router.config.vlan.removeRow(3)
    router.config.vlan.check.vlanTableRow('trnet-default', '1005', 4)
    router.config.vlan.removeRow(4)
    test.compare(router.config.vlan.vlanTable.rowCount, 5)#Default vlans should not be removed
    
    router.config.vlan.addVlan('VLAN100', '100')
    router.cli.textCheckPoint('''vlan 100 name VLAN100
VLAN 100 modified:
    Name: VLAN100
R0\(vlan\)#''')
    router.config.vlan.addVlan('VLAN200', '200')
    test.compare(router.config.vlan.vlanTable.rowCount, 7)
    router.config.vlan.removeRow(2)
    test.compare(router.config.vlan.vlanTable.rowCount, 6)
    
def checkInterfaceGigbitSerial():
    router.config.selectInterface("GigabitEthernet0")
    router.config.interface.ethernet.txRingLimit('20')
    router.config.interface.ethernet.ip('1.1.1.1')
    router.config.interface.ethernet.subnet('255.0.0.0')
    router.config.interface.ethernet.mac('0030.A330.0002')
    router.config.interface.ethernet.duplex('Full')
    router.config.interface.ethernet.duplex('Half')
    router.config.interface.ethernet.bandwidth('10')
    router.config.interface.ethernet.bandwidth('100')
    router.config.interface.ethernet.bandwidth('1000')
    router.config.interface.ethernet.portStatus(None)
    
    router.cli.textCheckPoint("R0\(config\)#interface GigabitEthernet0\nR0\(config-if\)#tx-ring-limit 20\nR0\(config-if\)#ip address 1.1.1.1 255.0.0.0\nR0\(config-if\)#mac-address 0030.A330.0002\nR0\(config-if\)#duplex half\nR0\(config-if\)#duplex full\nR0\(config-if\)#duplex half\nR0\(config-if\)#speed 1000\nR0\(config-if\)#speed 10\nR0\(config-if\)#speed 100\nR0\(config-if\)#speed 1000\nR0\(config-if\)#no shutdown\n\nR0\(config-if\)#\n%LINK-5-CHANGED: Interface GigabitEthernet0, changed state to up")

    router.config.selectInterface("Serial0")
    router.config.interface.serial.check.duplex('Full', True)
    router.config.interface.serial.txRingLimit('20')
    router.config.interface.serial.ip('2.2.2.2')
    router.config.interface.serial.subnet('255.0.0.0')
    router.config.interface.serial.clockrate('128000')
    router.config.interface.serial.portStatus(None)
    
    router.cli.textCheckPoint( "R0\(config\)#interface Serial0\nR0\(config-if\)#tx-ring-limit 20\nR0\(config-if\)#ip address 2.2.2.2 255.0.0.0\nR0\(config-if\)#clock rate 128000\nR0\(config-if\)#no shutdown\n\n%LINK-5-CHANGED: Interface Serial0, changed state to down")
    
def checkInterfaceFast():
    for i in range(4):
        router.config.selectInterface("FastEthernet%s"%(i,))
        router.config.interface.switch.txRingLimit('%s0'%(i+1,))
        router.config.interface.switch.vlanNumber('1002')
        router.config.interface.switch.portType('Trunk')
        router.config.interface.switch.vlanNumber('1')
        router.config.interface.switch.duplex('Full')
        router.config.interface.switch.duplex('Half')
        router.config.interface.switch.bandwidth('10')
        router.config.interface.switch.bandwidth('100')
        router.config.interface.switch.portStatus(None)
             
    router.cli.textCheckPoint( "R0\(config\)#interface FastEthernet0\nR0\(config-if\)#\nR0\(config-if\)#\nR0\(config-if\)#switchport access vlan 1002\nR0\(config-if\)#\nR0\(config-if\)#switchport mode trunk\nR0\(config-if\)#\nR0\(config-if\)#\nR0\(config-if\)#switchport trunk allowed vlan remove 1\nR0\(config-if\)#duplex half\nR0\(config-if\)#duplex full\nR0\(config-if\)#duplex half\nR0\(config-if\)#speed 100\nR0\(config-if\)#speed 10\nR0\(config-if\)#speed 100\nR0\(config-if\)#shutdown\n\nR0\(config-if\)#\n%LINK-5-CHANGED: Interface FastEthernet0, changed state to administratively down")

    router.cli.textCheckPoint( '''R0\(config\)#interface FastEthernet1
R0\(config-if\)#tx-ring-limit 20
R0\(config-if\)#
R0\(config-if\)#
R0\(config-if\)#switchport access vlan 1002
R0\(config-if\)#
R0\(config-if\)#switchport mode trunk
R0\(config-if\)#
R0\(config-if\)#
R0\(config-if\)#switchport trunk allowed vlan remove 1002
R0\(config-if\)#duplex half
R0\(config-if\)#duplex full
R0\(config-if\)#duplex half
R0\(config-if\)#speed 100
R0\(config-if\)#speed 10
R0\(config-if\)#speed 100
R0\(config-if\)#shutdown''')

    router.cli.textCheckPoint( '''R0\(config\)#interface FastEthernet2
R0\(config-if\)#tx-ring-limit 30
R0\(config-if\)#
R0\(config-if\)#
R0\(config-if\)#switchport mode trunk
R0\(config-if\)#
R0\(config-if\)#duplex half
R0\(config-if\)#duplex full
R0\(config-if\)#duplex half
R0\(config-if\)#speed 100
R0\(config-if\)#speed 10
R0\(config-if\)#speed 100
R0\(config-if\)#shutdown''')

    router.cli.textCheckPoint( '''R0\(config\)#interface FastEthernet3
R0\(config-if\)#tx-ring-limit 40
R0\(config-if\)#
R0\(config-if\)#
R0\(config-if\)#switchport mode trunk
R0\(config-if\)#
R0\(config-if\)#duplex half
R0\(config-if\)#duplex full
R0\(config-if\)#duplex half
R0\(config-if\)#speed 100
R0\(config-if\)#speed 10
R0\(config-if\)#speed 100
R0\(config-if\)#shutdown''')

def checkInterfaceWlan():
    router.config.selectInterface("Wlan-GigabitEthernet0")
    test.log('This needs fixed at a later time when the interface is corrected')
    router.config.interface.switch.txRingLimit('100')
    router.config.interface.switch.vlanNumber('1002')
    router.config.interface.switch.portType('Trunk')
    router.config.interface.switch.vlanNumber('1')
    router.config.interface.switch.bandwidth()
    router.config.interface.switch.bandwidth('10')
    router.config.interface.switch.bandwidth('100')
    router.config.interface.switch.portStatus()
    
    router.cli.textCheckPoint('''R0(config-if)#tx-ring-limit 100
R0(config-if)#switchport access vlan 1002
R0(config-if)#switchport mode trunk
R0(config-if)#switchport trunk allowed vlan remove 1
R0(config-if)#speed 100
R0(config-if)#speed 10
R0(config-if)#speed 100
R0(config-if)#shutdown
% Shutdown not allowed on Wlan-GigabitEthernet0 interface, as it is an internal interface connecting to the wlan-ap module.''')
    
def ap0test():
    router.config.selectInterface("wlan-ap0")
    router.config.interface.ethernet.txRingLimit('20')    
    snooze(1)
    router.config.interface.ethernet.ip('3.3.3.3')
    router.config.interface.ethernet.subnet('255.0.0.0')
    snooze(1)
    router.config.interface.ethernet.mac('0030.A330.00AA')
    snooze(1)
    router.config.interface.ethernet.bandwidth()
    router.config.interface.ethernet.bandwidth('10')
    router.config.interface.ethernet.bandwidth('100')
    router.config.interface.ethernet.bandwidth('1000')
    router.config.interface.ethernet.portStatus()
    snooze(2)
    router.cli.textCheckPoint('''R0\(config\)#interface wlan-ap0
The wlan-ap 0 interface is used for managing the embedded AP.
Please use the "service-module wlan-ap 0 session" command to console into the embedded AP
R0\(config-if\)#tx-ring-limit 20
R0\(config-if\)#ip address 3.3.3.3 255.255.255.248
R0\(config-if\)#ip address 3.3.3.3 255.0.0.0
R0\(config-if\)#mac-address 0030.A330.00AA
R0\(config-if\)#speed 10
R0\(config-if\)#speed 100
R0\(config-if\)#speed 1000
R0\(config-if\)#shutdown
%WLAN_AP_INTF-6-NOCHANGE: Interface wlan-ap0, always stays up, to session into service-module
R0\(config-if\)#''')
    #test.log("Awaiting fix for 17224")
    
def checkInterfaceCell():
    router.config.selectInterface("Cellular0")
    router.config.interface.cell.check.ip(None, property='enabled', value=False)
    router.config.interface.cell.check.subnet(None, property='enabled', value=False)
    router.config.interface.cell.check.ipv6(None, property='enabled', value=False)
    router.config.interface.cell.check.subnetv6(None, property='enabled', value=False)