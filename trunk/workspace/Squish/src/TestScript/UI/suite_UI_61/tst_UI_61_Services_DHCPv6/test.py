##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from API.Device.EndDevice.PC.PC import PC

from API.ComponentBox import ComponentBoxConst

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, 'Server0')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 100, 'PC1')

def main():
    util.init()
    openfile()
    checkInt0Defaults()
    checkInt0()
    util.init()
    openfile()
    checkInt1Defaults()
    checkInt1()

def openfile():
    util.open('Services_DHCP.pkt', UtilConst.UI_TEST)
    util.fastForwardTime()

def checkInt0Defaults():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('DHCPv6')
    s0.services.dhcpv6.check.interface('FastEthernet0')
    s0.services.dhcpv6.check.on(False)
    s0.services.dhcpv6.check.off(True)
    s0.services.dhcpv6.check.dhcpv6Pool('')
    s0.services.dhcpv6.dhcpv6Pool.check.poolList('')
    s0.services.dhcpv6.dhcpv6Pool.check.domainName('')
    
    test.compare(findObject(s0.squishName + ServicesConst.dhcpv6.PREFIX_CREATE_BUTTON).enabled, False)
    test.compare(findObject(s0.squishName + ServicesConst.dhcpv6.PREFIX_EDIT_BUTTON).enabled, False)
    test.compare(findObject(s0.squishName + ServicesConst.dhcpv6.PREFIX_REMOVE_BUTTON).enabled, False)
    
def checkInt0():
    s0.services.dhcpv6.on()
    s0.services.dhcpv6.dhcpv6Pool.addNewDhcpv6Pool('pool1', '1::1:1', 'pool1.com', '1::1', '64', '11-22-33-44-55-66-77-88-99-00', '', '', '', '', '')
    s0.services.dhcpv6.ipv6LocalPool.addNewLocalPool('localPool1', '1::', '64', '80')
    None
    
def checkInt1Defaults():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('DHCPv6')
    s0.services.dhcpv6.check.interface('FastEthernet0')
    s0.services.dhcpv6.check.on(False)
    s0.services.dhcpv6.check.off(True)
    s0.services.dhcpv6.check.dhcpv6Pool('')
    s0.services.dhcpv6.dhcpv6Pool.check.poolList('')
    s0.services.dhcpv6.dhcpv6Pool.check.domainName('')
    
    test.compare(findObject(s0.squishName + ServicesConst.dhcpv6.PREFIX_CREATE_BUTTON).enabled, False)
    test.compare(findObject(s0.squishName + ServicesConst.dhcpv6.PREFIX_EDIT_BUTTON).enabled, False)
    test.compare(findObject(s0.squishName + ServicesConst.dhcpv6.PREFIX_REMOVE_BUTTON).enabled, False)
    
def checkInt1():
    s0.services.dhcpv6.on()
    s0.services.dhcpv6.dhcpv6Pool.addNewDhcpv6Pool('pool1', '1::1:1', 'pool1.com', '1::1', '64', '11-22-33-44-55-66-77-88-99-00', '', '', '', '', '')
    s0.services.dhcpv6.ipv6LocalPool.addNewLocalPool('localPool1', '1::', '64', '80')
