######################
#Author: Alex Leung ##
######################
from API.functions import pathFromOS
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.Router.Router import Router
from API.Device.EndDevice.PC.PC import PC
from API.MenuBar.File.Open.Open import Open

#Function initialization
util = Util()
openFile = Open()

#Device initialization
s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 145, 300, "11.0.0.1")
s1 = Server(ComponentBoxConst.DeviceModel.SERVER, 180, 30, "Server1")
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_819_IOX, 285, 100, "r0")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 65, 100, "PC0")

def main():
    openSampleFile()
    login()
    checkRouterConfig()
    startServers()
    checkpoint()
    
def openSampleFile():
    util.init()
    openFile.openSamples(pathFromOS("Router\819HG_4G_IOX\tcp_client_app_on_819.pkt"))
    util.speedUpConvergence()

def login():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("https://172.1.1.1:8443")
    snooze(5)
    pc0.desktop.webBrowser.ciscoApplicationManagement.login("cisco", "cisco")
    snooze(5)
    try:
        (findObject(pc0.squishName + DesktopConst.webbrowser.CiscoApplicationManagementPage.Applications.APPLICATIONS_TABLE).visible, True)
        test.passes("Cisco Application Management Login Successful")
    except LookupError, e:
        test.fail("Cisco Application Management Login Failed")
    except Exception, e:
        raise Exception(e)
    pc0.close()
    
def checkRouterConfig():
    r0.select()
    r0.clickCliTab()
    r0.cli.setCliText("\r")
    r0.cli.setCliText("en")
    r0.cli.setCliText("show run")
    for i in range(0,5):
        r0.cli.setCliText(" ")
    r0.cli.textCheckPoint("username cisco privilege 15 password 0 cisco")
    r0.cli.textCheckPoint("ip dhcp excluded-address 192.168.1.0 192.168.1.1")
    r0.cli.textCheckPoint('''ip dhcp pool iox-apps
 network 192.168.1.0 255.255.255.0
 default-router 192.168.1.1''')
    r0.cli.textCheckPoint('''interface GigabitEthernet0
 ip address 172.1.1.1 255.255.255.0
 ip nat outside''')
    r0.cli.textCheckPoint('''interface Ethernet1
 ip address 192.168.3.1 255.255.255.0
 ip nat inside''')
    r0.cli.textCheckPoint('''interface VirtualPortGroup0
 ip address 192.168.1.1 255.255.255.0
 ip nat inside''')
    r0.cli.textCheckPoint('''iox
 host ip address 192.168.3.2 255.255.255.0
 host ip default-gateway 192.168.3.1''')
    r0.cli.textCheckPoint('''ip nat inside source list NAT_ACL interface GigabitEthernet0 overload
ip nat inside source static tcp 192.168.3.2 8443 172.1.1.1 8443 
ip default-gateway 172.1.1.3
ip classless
ip route 0.0.0.0 0.0.0.0 172.1.1.3 ''')
    r0.cli.textCheckPoint('''ip access-list standard NAT_ACL
 permit 192.168.0.0 0.0.255.255''')
    r0.close()
    
def startServers():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('VM Management')
    s0.services.vmManagement.start()
    s0.close()
    
    s1.select()
    s1.clickServicesTab()
    s1.services.selectInterface('VM Management')
    s1.services.vmManagement.start()
    s1.close()
    
    r0.select()
    r0.clickCliTab()
    r0.cli.setCliText('conf t')
    r0.cli.setCliText('virtual-service tcp_client')
    r0.cli.setCliText('activate')
    
def checkpoint():
    s0.select()
    s0.desktop.applications.commandPrompt()
    s0.desktop.commandPrompt.textCheckPoint("new client: 172.1.1.4:1025")
    s0.desktop.commandPrompt.textCheckPoint("new client: 172.1.1.1:1025")
    s0.close()
       
    r0.select()
    r0.clickCliTab()
    r0.cli.setCliText('''
    en
    show virtual-service list
    ''')
    r0.cli.textCheckPoint('tcp_client              Installed          tcp_client.ova')
    r0.cli.setCliText('''conf t
    virtual-service tcp_client
    activate
    end
    
    show virtual-service list
    ''')
    r0.cli.textCheckPoint('tcp_client              Activated          tcp_client.ova')