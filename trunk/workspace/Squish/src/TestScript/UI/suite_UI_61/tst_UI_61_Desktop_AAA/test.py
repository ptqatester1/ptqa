##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Router.Router import Router
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch
from API.Device.EndDevice.PC.PC import PC
from API.ComponentBox import ComponentBoxConst

util = Util()

r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 150, 325, 'Rourter0')
s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 500, 300, 'Server0')
s1 = Server(ComponentBoxConst.DeviceModel.SERVER, 410, 350, 'Server1')
pc = PC(ComponentBoxConst.DeviceModel.PC, 275, 200, 'PC0')
sw = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 275, 315, 'Switch0')

def main():
    util.init()
    create()
    checkLogging()
    
def create():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r1.model, r1.x, r1.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, sw.model, sw.x, sw.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, s0.model, s0.x, s0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, s1.model, s1.x, s1.y)
    pc.create()
    def autoConnect(dev, dev2):
        util.connect(dev.x, dev.y, dev2.x, dev2.y, ComponentBoxConst.Connection.CONN_AUTO, '', '')
    autoConnect(r1, sw)
    autoConnect(sw, s0)
    autoConnect(sw, s1)
    autoConnect(sw, pc)
    util.fastForwardTime()
    
    util.clickOnWorkspace(pc.x, pc.y)
    pc.updateName()
    pc.clickDesktopTab()
    pc.desktop.applications.ipConfiguration()
    pc.desktop.ipConfiguration.setIPConfiguration('192.168.10.3', '255.255.255.0', '192.168.10.1', '')
    pc.close()
    
    util.clickOnWorkspace(s0.x, s0.y)
    s0.updateName()
    s0.clickDesktopTab()
    s0.desktop.applications.ipConfiguration()
    s0.desktop.ipConfiguration.setIPConfiguration('192.168.10.6', '255.255.255.0', '192.168.10.1')
    s0.clickServicesTab()
    s0.services.selectInterface('AAA')
    s0.services.aaa.on()
    s0.services.aaa.networkConfiguration.addClient('R1', '192.168.10.1', 'ciscosecret', 'Radius')
    s0.services.aaa.userSetup.addUser('user', 'cisco')
    s0.close()
    
    s1.select()
    s1.clickDesktopTab()
    s1.desktop.applications.ipConfiguration()
    s1.desktop.ipConfiguration.setIPConfiguration('192.168.10.2', '255.255.255.0', '192.168.10.1')
    s1.clickServicesTab()
    s1.services.selectInterface('AAA')
    s0.services.aaa.on()
    s1.services.aaa.networkConfiguration.addClient('R1', '192.168.10.1', 'ciscosecret', 'Radius')
    s1.services.aaa.userSetup.addUser('user', 'cisco')
    s1.close()
    
    r1.select()
    r1.clickCliTab()
    r1.cli.startConsole()
    r1.cli.setCliText('''enable
configure terminal
hostname R1
enable secret cisco
aaa new-model
aaa authentication login default group radius none 
aaa authentication login telnet_lines group radius 
aaa accounting exec console_line start-stop group radius
ip cef
no ipv6 cef
ip ssh version 1
spanning-tree mode pvst
interface FastEthernet0/0
 ip address 192.168.10.1 255.255.255.0
 duplex auto
 speed auto
 no shut
interface FastEthernet0/1
 no ip address
 duplex auto
 speed auto
 no shut
interface Vlan1
 no ip address
 shutdown
ip classless
ip flow-export version 9
radius-server host 192.168.10.2 auth-port 1645 key ciscosecret
radius-server host 192.168.10.6 auth-port 1645 key ciscosecret
line con 0
 accounting exec console_line
line aux 0
line vty 0 4
 login authentication telnet_lines
 accounting exec console_line
ntp update-calendar
end
exit''')
    r1.close()
    util.fastForwardTime()
    
def checkLogging():
    util.clickOnWorkspace(pc.x, pc.y)
    pc.updateName()
    pc.desktop.applications.commandPrompt()
    pc.desktop.commandPrompt.setText("telnet 192.168.10.1")
    pc.desktop.commandPrompt.setText("user")
    pc.desktop.commandPrompt.setText("cisco")
    pc.close()
    #util.speedUpConvergence()
    
    s1.select()
    s1.clickDesktopTab()
    s1.desktop.applications.aaaAccounting()
    s1.desktop.aaaAccounting.tabs.radius()
    #snooze(15)
    #s1.desktop.aaaAccounting.textCheckPoint("DATE= \d*:\d*:\d* UTC \D* \d{2} \d{4}  ,Username= user  ,Caller Id= 192.168.10.3  ,Flag= Start  ,NAS IP= 192.168.10.2  ,NAS Port= vty0 ", 0)

    pc.select()
    pc.desktop.applications.commandPrompt()
    snooze(10)
    pc.desktop.commandPrompt.setText("exit")
    
    s1.select()
    snooze(3)
    s1.desktop.aaaAccounting.radius.checkText("DATE= \d*:\d*:\d* UTC \D* \d{2} \d{4}  ,Username= user  ,Caller Id= 192.168.10.3  ,Flag= Stop  ,NAS IP= 192.168.10.2  ,NAS Port= vty0 ", '1')

    pc.select()
    pc.desktop.commandPrompt.setText("telnet 192.168.10.1")
    pc.desktop.commandPrompt.setText("user")
    pc.desktop.commandPrompt.setText("cisco")
    util.speedUpConvergence()
    
    sw.select()
    sw.clickConfigTab()
    sw.config.selectInterface("FastEthernet0/2")
    sw.config.interface.ethernet.portStatus()
    util.speedUpConvergence()
    
    util.clickOnWorkspace(pc.x, pc.y)
    pc.updateName()
    pc.desktop.commandPrompt.setText("exit")
    pc.desktop.commandPrompt.setText("telnet 192.168.10.1")
    pc.desktop.commandPrompt.setText("user")
    pc.desktop.commandPrompt.setText("cisco")
    util.speedUpConvergence()
