##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.PC.PC import PC

from API.Device.EndDevice.Server.Server import Server

from API.Device.Router.Router import Router

from API.Device.Switch.Switch import Switch

from API.ComponentBox import ComponentBoxConst

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 150, 350, 'Server0')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 50, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 200, 50, 'PC1')
p2 = PC(ComponentBoxConst.DeviceModel.PC, 300, 50, 'PC2')
p3 = PC(ComponentBoxConst.DeviceModel.PC, 400, 50, 'PC3')
p4 = PC(ComponentBoxConst.DeviceModel.PC, 350, 350, 'PC4')
sw0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 250, 150, 'Switch0')
sw1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 250, 350, 'Switch1')
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 250, 250, 'Router0')

def main():
    util.init()
    create()
    addressDevices()
    configureFirewall()
    checkFirewallWorks()
    
def create():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, s0.model, s0.x, s0.y)
    for pc in [p0, p1, p2, p3, p4]:
        pc.create()
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, sw0.model, sw0.x, sw0.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, sw1.model, sw1.x, sw1.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    
    def connect(dev1, dev2):
        util.connect(dev1.x, dev1.y, dev2.x, dev2.y, ComponentBoxConst.Connection.CONN_AUTO, '', '')
    for pc in [p0, p1, p2, p3]:
        connect(pc, sw0)
    connect(sw0, r0)
    connect(r0, sw1)
    connect(sw1, s0)
    connect(sw1, p4)
    util.fastForwardTime()

def addressDevices():
    for i,pc in enumerate([p0, p1, p2, p3, p4]):
        util.clickOnWorkspace(pc.x, pc.y)
        pc.updateName()
        pc.clickDesktopTab()
        pc.desktop.applications.ipConfiguration()
        pc.desktop.ipConfiguration.setIpv6Configuration(str(i+1) + '::2', '64', str(i+1) + '::1', '')
        pc.close()
    
    util.clickOnWorkspace(s0.x, s0.y)
    s0.updateName()
    s0.clickDesktopTab()
    s0.desktop.applications.ipConfiguration()
    s0.desktop.ipConfiguration.setIpv6Configuration('5::3', '64', '5::1')
    s0.close()
    
    util.clickOnWorkspace(sw0.x, sw0.y)
    sw0.updateName()
    sw0.clickCliTab()
    sw0.cli.startConsole()
    sw0.cli.setCliText('enable')
    sw0.cli.setCliText('configure terminal')
    for i in range(1, 5):
        sw0.cli.setCliText('vlan ' + str(i) + '0')
        sw0.cli.setCliText('int fa0/' + str(i))
        sw0.cli.setCliText('switch mode access')
        sw0.cli.setCliText('switch access vlan ' + str(i) + '0')
    sw0.cli.setCliText('int fa0/5')
    sw0.cli.setCliText('switch mode trunk')
    sw0.close()

    r0.select()
    r0.clickCliTab()
    r0.cli.startConsole()
    r0.cli.setCliText('enable')
    r0.cli.setCliText('configure terminal')
    r0.cli.setCliText('ipv6 unicast-routing')
    r0.cli.setCliText('int fa0/0')
    r0.cli.setCliText('no shut')
    for i in range(1, 5):
        vlan = str(i) + '0'
        r0.cli.setCliText('int fa0/0.' + vlan)
        r0.cli.setCliText('enc dot1Q ' + vlan)
        r0.cli.setCliText('ipv6 address ' + str(i) + '::1/64')
    r0.cli.setCliText('int fa0/1')
    r0.cli.setCliText('ipv6 address 5::1/64')
    r0.cli.setCliText('no shut')
    r0.close()
    util.speedUpConvergence()
    
def configureFirewall():
    p0.select()
    p0.clickDesktopTab()
    p0.desktop.applications.firewallv6()
    p0.desktop.firewallv6.on()
    p0.desktop.firewallv6.addRule('Allow', 'IPv6', '2::2', '128', '', '')
    p0.desktop.firewallv6.addRule('Deny', 'IPv6', '3::2', '128', '', '')
    p0.desktop.firewallv6.addRule('Deny', 'ICMPv6', '5::0', '112', '', '')
    p0.desktop.firewallv6.addRule('Allow', 'TCP', '5::0', '112', '80', 'any')
    p0.desktop.firewallv6.addRule('Deny', 'TCP', '5::1', '128', '23', 'any')
    p0.desktop.firewallv6.addRule('Allow', 'UDP', '5::0', '112', '69', 'any')
    p0.close()
    
def checkFirewallWorks():
    p0.select()
    p0.clickDesktopTab()
    p0.desktop.applications.commandPrompt()
    for i in range(1, 5):
        p0.desktop.commandPrompt.setText('ping ' + str(i) + '::2')
        util.fastForwardTime()
    for i in range(1, 4):
        p0.desktop.commandPrompt.setText('ping 5::' + str(i))
        util.fastForwardTime()
    p0.desktop.commandPrompt.textCheckPoint('Received = 0', 5)
    p0.desktop.commandPrompt.textCheckPoint('Received = [1234]', 2)
    p0.desktop.commandPrompt.setText('telnet 5::1')
    util.fastForwardTime()
    p0.desktop.commandPrompt.textCheckPoint('% Connection timed out; remote host not responding')
    p0.desktop.commandPrompt.close()
    
    p0.desktop.applications.webBrowser()
    snooze(2)
    p0.desktop.webBrowser.browse('5::3')
    util.fastForwardTime()
    p0.desktop.webBrowser.textCheckPoint('Welcome to Cisco Packet Tracer. Opening doors to new opportunities. Mind Wide Open')
    None