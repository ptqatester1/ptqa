######################
#@author: Pamela Vinco
######################
from API.functions import pathFromOS
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.Router.Router import Router
from API.MenuBar.File.Open.Open import Open

#Function initialization
util = Util()
openFile = Open()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 265, 170, "PC0")
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_819_IOX, 105, 300, "Router0")

def main():
    util.init()
    openSampleFile()
    login()
    checkRouterConfig()

def openSampleFile():
    openFile.openSamples(pathFromOS("Router/basic_configuration_outside_nat.pkt"))
    util.speedUpConvergence()
    
def login():
    util.clickOnWorkspace(pc0.x, pc0.y)
    pc0.updateName()
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
    util.clickOnWorkspace(router0.x, router0.y)
    router0.updateName()
    router0.clickCliTab()
    router0.cli.setCliText("\r")
    router0.cli.setCliText("en")
    router0.cli.setCliText("show run")
    for i in range(0,5):
        router0.cli.setCliText(" ")
    router0.cli.textCheckPoint("username cisco privilege 15 password 0 cisco")
    router0.cli.textCheckPoint('''interface GigabitEthernet0
 ip address 172.1.1.1 255.255.255.0
 ip nat outside''')
    router0.cli.textCheckPoint('''interface Ethernet1
 ip address 192.168.3.1 255.255.255.0
 ip nat inside''')
    router0.cli.textCheckPoint('''interface VirtualPortGroup0
 ip unnumbered GigabitEthernet0
 ip helper-address 172.1.1.2''')
    router0.cli.textCheckPoint('''iox
 host ip address 192.168.3.2 255.255.255.0
 host ip default-gateway 192.168.3.1''')
    router0.cli.textCheckPoint('''ip nat inside source list NAT_ACL interface GigabitEthernet0 overload
ip nat inside source static tcp 192.168.3.2 8443 172.1.1.1 8443 
ip default-gateway 172.1.1.2
ip classless
ip route 0.0.0.0 0.0.0.0 172.1.1.2 ''')  
    router0.cli.textCheckPoint('''ip access-list standard NAT_ACL
 permit 192.168.0.0 0.0.255.255''')
    router0.close()