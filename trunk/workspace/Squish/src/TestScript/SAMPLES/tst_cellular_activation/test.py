########################
#Author: Pamela Vinco
########################

from API.Utility.Util import Util
from API.Device.Router.Router import Router
from API.functions import pathFromOS
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.Open.Open import Open
from API.Device.COServer.COServer import COServer

#Function initialization
util = Util()
openFile = Open()

#Device initialization
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_819, 110, 275, 'Router1')
c0 = COServer(ComponentBoxConst.DeviceModel.CO_SERVER, 505, 275, 'Central Office Server0')

def main():
    util.init()
    topology()
    serverCheckpoint()
    cellActivation()
    getIPaddress()
    connectivityCheck()
    removeActivation()
    
def topology():
    openFile.openSamples(pathFromOS("Router/819HGW/cellular_activation.pkt"))
    
def serverCheckpoint():
    c0.select()
    c0.clickServicesTab()
    c0.services.selectInterface('PAP/CHAP')
    c0.services.papChap.interface('Coaxial0/0')
    c0.services.papChap.selectUser('cisco')
    c0.services.papChap.check.username('cisco')
    c0.services.papChap.check.password('cisco')
    c0.close()
    
def cellActivation():
    r1.select()
    r1.clickCliTab()
    r1.cli.startConsole()
    r1.cli.setCliText("enable")
    r1.cli.setCliText("cellular 0 gsm profile create 1 pt.cisco.com pap cisco cisco")
    util.speedUpConvergence()
    r1.cli.textCheckPoint("MODEM_ACTIVATION_IN_PROGRESS: Cellular0 modem is under activating.")
    r1.cli.textCheckPoint("%LINK-5-CHANGED: Interface Cellular0, changed state to up")
    r1.cli.textCheckPoint("%LINEPROTO-5-UPDOWN: Line protocol on Interface Cellular0, changed state to up")
    r1.cli.textCheckPoint("MODEM_ACTIVATION_COMPLETED: Cellular0 modem is activated.")
    
def getIPaddress():
    r1.cli.setCliText('configure terminal')
    r1.cli.setCliText('interface cellular 0')
    r1.cli.setCliText('ip address negotiated')
    r1.cli.setCliText('end')
    util.speedUpConvergence()
    r1.cli.setCliText('show ip route')
    r1.cli.textCheckPoint('''C       10.10.10.0/29 is directly connected, Vlan1
L       10.10.10.1/32 is directly connected, Vlan1
     172.16.0.0/16 is variably subnetted, 2 subnets, 2 masks
C       172.16.1.0/24 is directly connected, Cellular0
L       172.16.1.100/32 is directly connected, Cellular0
S\*   0.0.0.0/0 \[254/0] via 172.16.1.1''')
    
def connectivityCheck():
    r1.cli.setCliText('ping 172.16.1.1')
    util.fastForwardTime()
    r1.cli.textCheckPoint('Success rate is (20|40|60|80|100)')
    
def removeActivation():
    r1.cli.setCliText("cellular 0 gsm profile delete 1")
    util.fastForwardTime()
    r1.cli.textCheckPoint("%LINK-5-CHANGED: Interface Cellular0, changed state to administratively down")
    r1.cli.textCheckPoint("%LINEPROTO-5-UPDOWN: Line protocol on Interface Cellular0, changed state to down")
    r1.close()