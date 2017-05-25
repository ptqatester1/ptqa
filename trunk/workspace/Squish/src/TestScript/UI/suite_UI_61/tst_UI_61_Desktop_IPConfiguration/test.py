##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.PC.PC import PC

from API.Device.EndDevice.Server.Server import Server

from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, 'Server0')
pc = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, 'PC1')
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 200, 200, 'Router0')

def main():
    util.init()
    create()
    checkStatic()
    checkDhcpNoServer()
    setDhcpServer()
    checkDhcpWithServer()
    checkStatelessAutoConfig()
    
def create():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, s0.model, s0.x, s0.y)
    pc.create()
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, p1.model, p1.x, p1.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    util.connect(s0.x, s0.y, pc.x, pc.y, ComponentBoxConst.Connection.CONN_AUTO, '', '')
    util.connect(r0.x, r0.y, p1.x, p1.y, ComponentBoxConst.Connection.CONN_AUTO, '', '')
    util.fastForwardTime()
    
def checkStatic():
    util.clickOnWorkspace(pc.x, pc.y)
    pc.updateName()
    pc.clickDesktopTab()
    pc.desktop.applications.ipConfiguration()
    pc.desktop.ipConfiguration.setIPConfiguration('1.1.1.1', '255.255.255.0', '1.1.1.254', '1.1.1.254')
    pc.desktop.ipConfiguration.setIpv6Configuration('1::1', '64', '1::2', '1::2')
    pc.desktop.ipConfiguration.linkLocal('FE80::2')
    pc.desktop.ipConfiguration.check.ip('1.1.1.1')
    pc.desktop.ipConfiguration.check.subnet('255.255.255.0')
    pc.desktop.ipConfiguration.check.gateway('1.1.1.254')
    pc.desktop.ipConfiguration.check.dns('1.1.1.254')
    pc.desktop.ipConfiguration.check.ipv6('1::1')
    pc.desktop.ipConfiguration.check.subnetv6('64')
    pc.desktop.ipConfiguration.check.linkLocal('FE80::2')
    pc.desktop.ipConfiguration.check.gatewayv6('1::2')
    pc.desktop.ipConfiguration.check.dnsv6('1::2')
    pc.desktop.ipConfiguration.check.static(True)
    pc.desktop.ipConfiguration.check.staticv6(True)
    pc.desktop.ipConfiguration.check.dhcp(False)
    pc.desktop.ipConfiguration.check.dhcpv6(False)
    pc.desktop.ipConfiguration.check.autoconfig(False)
    
def checkDhcpNoServer():
    pc.desktop.ipConfiguration.dhcp()
    pc.desktop.ipConfiguration.dhcpv6()
    util.fastForwardTime()
    util.fastForwardTime()
    pc.desktop.ipConfiguration.check.ip('169.254.\d{1,3}.\d{1,3}')
    pc.desktop.ipConfiguration.check.subnet('255.255.0.0')
    pc.desktop.ipConfiguration.check.gateway('0.0.0.0')
    pc.desktop.ipConfiguration.check.linkLocal('FE80::2')
    pc.desktop.ipConfiguration.check.dns('0.0.0.0')
    pc.desktop.ipConfiguration.check.ipv6('')
    pc.desktop.ipConfiguration.check.subnetv6('')
    pc.desktop.ipConfiguration.check.gatewayv6('')
    pc.desktop.ipConfiguration.check.dnsv6('')
    pc.close()
    
def setDhcpServer():
    s0.select()
    s0.clickDesktopTab()
    s0.desktop.applications.ipConfiguration()
    s0.desktop.ipConfiguration.setIPConfiguration('2.1.1.1', '255.0.0.0', '2.1.1.254')
    s0.clickServicesTab()
    s0.services.selectInterface('DHCP')
    s0.services.dhcp.on()
    s0.services.dhcp.edit('serverPool', None, '2.1.1.254', '2.1.1.254', '2.1.1.100', '255.0.0.0', '512', '')
    
    s0.services.selectInterface('DHCPv6')
    s0.services.dhcpv6.on()
    s0.services.dhcpv6.dhcpv6Pool.addNewDhcpv6Pool('newV6Pool', '1::254', 'dhcp.com', '1::2', '64', '11-22-33-44-55-66-77-88-99-00', '', '', '', '', '')
    s0.services.dhcpv6.ipv6LocalPool.addNewLocalPool('newLocal', '1::', '64', '80')
    
def checkDhcpWithServer():
    pc.select()
    pc.clickDesktopTab()
    pc.desktop.applications.ipConfiguration()
    pc.desktop.ipConfiguration.static()
    pc.desktop.ipConfiguration.dhcp()
    pc.desktop.ipConfiguration.staticv6()
    pc.desktop.ipConfiguration.dhcpv6()
    util.fastForwardTime()
    util.fastForwardTime()
    
    pc.desktop.ipConfiguration.check.ip('2.1.1.1[0-9][0-9]') #IP should start at 1.1.1.100 with the config of the DHCP server
    pc.desktop.ipConfiguration.check.subnet('255.0.0.0')
    pc.desktop.ipConfiguration.check.gateway('2.1.1.254')
    pc.desktop.ipConfiguration.check.ipv6('1::2')
    pc.desktop.ipConfiguration.check.subnetv6('80')
    pc.desktop.ipConfiguration.check.linkLocal('FE80::2')
    pc.desktop.ipConfiguration.check.gatewayv6('FE80::')
    pc.desktop.ipConfiguration.check.dnsv6('1::254')
    
def checkStatelessAutoConfig():
    r0.select()
    r0.clickCliTab()
    r0.cli.startConsole()
    r0.cli.setCliText('enable')
    r0.cli.setCliText('configure terminal')
    r0.cli.setCliText('''ipv6 unicast-routing
ipv6 dhcp pool Stateless_Pool
 dns-server 1::1:1
 domain-name dhcpPools.com
interface FastEthernet0/0
 ipv6 address 1::1/64
 ipv6 nd other-config-flag
 ipv6 enable
 ipv6 dhcp server Stateless_Pool
 no shut
end''')
    r0.close()
    util.fastForwardTime()
    
    p1.select()
    p1.clickDesktopTab()
    p1.desktop.applications.ipConfiguration()
    p1.desktop.ipConfiguration.autoconfig()
    util.fastForwardTime()
    
    p1.desktop.ipConfiguration.check.ipv6('1::')
    p1.desktop.ipConfiguration.check.subnetv6('64')
    p1.desktop.ipConfiguration.check.linkLocal('FE80::')
    p1.desktop.ipConfiguration.check.gatewayv6('FE80::')
    p1.desktop.ipConfiguration.check.dnsv6('1::1:1')
    None
    
def isChecked(testObj):
    test.compare(findObject(testObj).checked, True)
    
def isNotChecked(testObj):
    test.compare(findObject(testObj).checked, False)
    