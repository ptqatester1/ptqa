##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server

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
    checkInt1Defaults()
    checkInt1()
    checkConnectivity()

def openfile():
    util.open('Services_DHCP.pkt', UtilConst.UI_TEST)
    util.fastForwardTime()

def checkInt0Defaults():
    util.clickOnWorkspace(s0.x, s0.y)
    s0.updateName()
    s0.clickServicesTab()
    s0.services.selectInterface('DHCP')
    s0.services.dhcp.check.interface('FastEthernet0')
    s0.services.dhcp.check.on(False)
    s0.services.dhcp.check.off(True)
    s0.services.dhcp.check.poolName('serverPool')
    s0.services.dhcp.check.gateway('0.0.0.0')
    s0.services.dhcp.check.dns('0.0.0.0')
    s0.services.dhcp.check.start_ip_1('1')
    s0.services.dhcp.check.start_ip_2('0')
    s0.services.dhcp.check.start_ip_3('0')
    s0.services.dhcp.check.start_ip_4('0')
    s0.services.dhcp.check.start_subnet_1('255')
    s0.services.dhcp.check.start_subnet_2('0')
    s0.services.dhcp.check.start_subnet_3('0')
    s0.services.dhcp.check.start_subnet_4('0')
    s0.services.dhcp.check.maxUsers('512')
    s0.services.dhcp.check.tftpServer('0.0.0.0')
    s0.services.dhcp.check.addButton(property='enabled', value=True)
    s0.services.dhcp.check.saveButton(property='enabled', value=True)
    s0.services.dhcp.check.removeButton(property='enabled', value=False)
    
    s0.services.dhcp.check.tablePoolName('serverPool', 0)
    s0.services.dhcp.check.tableGateway('0.0.0.0', 0)
    s0.services.dhcp.check.tableDns('0.0.0.0', 0)
    s0.services.dhcp.check.tableIp('1.0.0.0', 0)
    s0.services.dhcp.check.tableSubnet('255.0.0.0', 0)
    s0.services.dhcp.check.tableMax('512', 0)
    s0.services.dhcp.check.tableTftp('0.0.0.0', 0)
    None
    
def checkInt0():
    s0.services.dhcp.on()
    s0.services.dhcp.add('newPool', '1.1.1.254', '1.1.1.254', '1.1.1.100', '255.0.0.0', '512', None, None)
    s0.services.dhcp.check.tablePoolName('newPool', 0)
    s0.services.dhcp.check.tableGateway('1.1.1.254', 0)
    s0.services.dhcp.check.tableDns('1.1.1.254', 0)
    s0.services.dhcp.check.tableIp('1.1.1.100', 0)
    s0.services.dhcp.check.tableSubnet('255.0.0.0', 0)
    s0.services.dhcp.check.tableMax('512', 0)
    s0.services.dhcp.check.tableTftp('0.0.0.0', 0)

    s0.services.dhcp.remove('newPool')
    s0.services.dhcp.edit('serverPool', None, '1.1.1.254', '1.1.1.254', '1.1.1.100', '255.0.0.0', '512', '')
    
def checkInt1Defaults():
    util.clickOnWorkspace(s0.x, s0.y)
    s0.updateName()
    s0.clickServicesTab()
    s0.services.selectInterface('DHCP')
    s0.services.dhcp.interface('FastEthernet1')
    s0.services.dhcp.check.interface('FastEthernet1')
    s0.services.dhcp.check.on(False)
    s0.services.dhcp.check.off(True)
    s0.services.dhcp.check.poolName('serverPool')
    s0.services.dhcp.check.gateway('0.0.0.0')
    s0.services.dhcp.check.dns('0.0.0.0')
    s0.services.dhcp.check.start_ip_1('2')
    s0.services.dhcp.check.start_ip_2('0')
    s0.services.dhcp.check.start_ip_3('0')
    s0.services.dhcp.check.start_ip_4('0')
    s0.services.dhcp.check.start_subnet_1('255')
    s0.services.dhcp.check.start_subnet_2('0')
    s0.services.dhcp.check.start_subnet_3('0')
    s0.services.dhcp.check.start_subnet_4('0')
    s0.services.dhcp.check.maxUsers('512')
    s0.services.dhcp.check.tftpServer('0.0.0.0')
    s0.services.dhcp.check.addButton(property='enabled', value=True)
    s0.services.dhcp.check.saveButton(property='enabled', value=True)
    s0.services.dhcp.check.removeButton(property='enabled', value=False)
    
    s0.services.dhcp.check.tablePoolName('serverPool', 0)
    s0.services.dhcp.check.tableGateway('0.0.0.0', 0)
    s0.services.dhcp.check.tableDns('0.0.0.0', 0)
    s0.services.dhcp.check.tableIp('2.0.0.0', 0)
    s0.services.dhcp.check.tableSubnet('255.0.0.0', 0)
    s0.services.dhcp.check.tableMax('512', 0)
    s0.services.dhcp.check.tableTftp('0.0.0.0', 0)
    
def checkInt1():
    s0.services.dhcp.on()
    s0.services.dhcp.add('newPool', '2.1.1.254', '2.1.1.254', '2.1.1.100', '255.0.0.0', '512', None, None)
    
    s0.services.dhcp.check.tablePoolName('newPool', 0)
    s0.services.dhcp.check.tableGateway('2.1.1.254', 0)
    s0.services.dhcp.check.tableDns('2.1.1.254', 0)
    s0.services.dhcp.check.tableIp('2.1.1.100', 0)
    s0.services.dhcp.check.tableSubnet('255.0.0.0', 0)
    s0.services.dhcp.check.tableMax('512', 0)
    s0.services.dhcp.check.tableTftp('0.0.0.0', 0)
    
    s0.services.dhcp.remove('newPool')
    s0.services.dhcp.edit('serverPool', None, '2.1.1.254', '2.1.1.254', '2.1.1.100', '255.0.0.0', '512', '')
    
def checkConnectivity():
    p0.select()
    p0.clickDesktopTab()
    p0.desktop.applications.ipConfiguration()
    p0.desktop.ipConfiguration.dhcp()
    util.fastForwardTime()
    p0.desktop.ipConfiguration.check.ip('1.1.1.1[0-9][0-9]')
    p0.desktop.ipConfiguration.check.subnet('255.0.0.0')
    p0.desktop.ipConfiguration.check.gateway('1.1.1.254')
    p0.desktop.ipConfiguration.check.dns('1.1.1.254')
    p0.close()
    
    p1.select()
    p1.clickDesktopTab()
    p1.desktop.applications.ipConfiguration()
    p1.desktop.ipConfiguration.dhcp()
    util.fastForwardTime()
    p1.desktop.ipConfiguration.check.ip('2.1.1.1[0-9][0-9]')
    p1.desktop.ipConfiguration.check.subnet('255.0.0.0')
    p1.desktop.ipConfiguration.check.gateway('2.1.1.254')
    p1.desktop.ipConfiguration.check.dns('2.1.1.254')
    p1.close()