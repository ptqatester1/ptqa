######################
#@author: Pamela Vinco
######################
from API.functions import pathFromOS
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.Router.Router import Router
from API.MenuBar.File.Open.Open import Open
from API import functions
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst

#Function initialization
util = Util()
openFile = Open()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 65, 100, "PC0")
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_819_IOX, 270, 100, "Router0")

def main():
    util.init()
    openSampleFile()
    login()
    checkRouterConfig()

def openSampleFile():
    openFile.openSamples(pathFromOS("Router/819HG_4G_IOX/basic_configuration.pkt"))
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
    router0.select()
    router0.clickCliTab()
    router0.cli.setCliText("\r")
    router0.cli.setCliText("en")
    router0.cli.setCliText("show run")
    for i in range(0,5):
        router0.cli.setCliText(" ")
    router0.cli.textCheckPoint("username cisco privilege 15 password 0 cisco")
    router0.cli.textCheckPoint("ip dhcp excluded-address 192.168.1.0 192.168.1.1")
    router0.cli.textCheckPoint('''ip dhcp pool iox-apps
 network 192.168.1.0 255.255.255.0
 default-router 192.168.1.1''')
    router0.cli.textCheckPoint('''interface GigabitEthernet0
 ip address 172.1.1.1 255.255.255.0
 ip nat outside''')
    router0.cli.textCheckPoint('''interface Ethernet1
 ip address 192.168.3.1 255.255.255.0
 ip nat inside''')
    router0.cli.textCheckPoint('''interface VirtualPortGroup0
 ip address 192.168.1.1 255.255.255.0
 ip nat inside''')
    router0.cli.textCheckPoint('''iox
 host ip address 192.168.3.2 255.255.255.0
 host ip default-gateway 192.168.3.1''')
    router0.cli.textCheckPoint('''ip nat inside source list NAT_ACL interface GigabitEthernet0 overload
ip nat inside source static tcp 192.168.3.2 8443 172.1.1.1 8443''')
    router0.cli.textCheckPoint('''ip access-list standard NAT_ACL
 permit 192.168.0.0 0.0.255.255''')
    router0.close()