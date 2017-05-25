#####################
#@author: Pam Vinco
#####################
from API.ComponentBox import ComponentBoxConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Router.Router import Router
from API.SimulationPanel.PDU.PDU import PDU

#Function initialization
util = Util()
pdu = PDU()

#Device initialization
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 185, 360, "R1")
r2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 375, 35, "R2")
r3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 545, 355, "R3")

def main():
    util.init()
    openFile()
    checkpoint_r1()
    checkpoint_r2()
    checkpoint_r3()
    checkpoint_simulation()
    
def openFile():
    util.open("SIM_60_Ipv6_EIGRP_Routing.pkt", UtilConst.PROTOCOLS_TEST)
    util.speedUpConvergence()
    
def checkpoint_r1():
    #FF02::A should not be included in the Joined group addresses
    r1.select()
    r1.clickCliTab()
    r1.cli.setCliText("")
    r1.cli.setCliText("en")
    r1.cli.setCliText("sh ipv6 int s0/0/0")
    r1.cli.textCheckPoint("Serial0/0/0 is up, line protocol is up\n  IPv6 is enabled, link-local address is FE80::1\n  No Virtual link-local address\(es\):\n  Global unicast address\(es\):\n    FEC0::12:1, subnet is FEC0::12:0/112\n  Joined group address\(es\):\n    FF02::1\n    FF02::2\n    FF02::A\n    FF02::1:FF00:1\n    FF02::1:FF12:1\n  MTU is 1500 bytes\n  ICMP error messages limited to one every 100 milliseconds\n  ICMP redirects are enabled\n  ICMP unreachables are sent\n  ND DAD is enabled, number of DAD attempts: 1\n  ND reachable time is 30000 milliseconds")
    r1.close()
    
def checkpoint_r2():
    #Link local address should be present and outputs aligned to 0 and 1
    r2.select()
    r2.clickCliTab()
    r2.cli.setCliText("")
    r2.cli.setCliText("en")
    r2.cli.setCliText("sh ipv6 int fa0/0")
    r2.cli.textCheckPoint("FastEthernet0/0 is up, line protocol is up\n  IPv6 is enabled, link-local address is FE80::203:E4FF:FED2:1101\n  No Virtual link-local address\(es\):\n  Global unicast address\(es\):\n    FEC0:23::203:E4FF:FED2:1101, subnet is FEC0:23::/64 \[EUI\]\n  Joined group address\(es\):\n    FF02::1\n    FF02::2\n    FF02::A\n    FF02::1:FFD2:1101\n  MTU is 1500 bytes\n  ICMP error messages limited to one every 100 milliseconds\n  ICMP redirects are enabled\n  ICMP unreachables are sent\n  ND DAD is enabled, number of DAD attempts: 1\n  ND reachable time is 30000 milliseconds")
    r2.cli.setCliText("sh ipv6 eigrp neighbors")
    r2.cli.textCheckPoint("0   Link-local address:       Se0/0/0      [\d][\d]   00:[\d][\d]:[\d][\d]  40     1000  0   [\d]\n    FE80::1")
    r2.cli.textCheckPoint("1   Link-local address:       Fa0/0        [\d][\d]   00:[\d][\d]:[\d][\d]  40     1000  0   [\d][\d]\n    FE80::290:21FF:FE9C:7201")
    r2.close()
    
def checkpoint_r3():
    r3.select()
    r3.clickCliTab()
    r3.cli.setCliText("")
    r3.cli.setCliText("en")
    r3.cli.setCliText("sh ipv6 eigrp top")
    r3.cli.textCheckPoint("P FEC0::3:0/112, 1 successors, FD is 128256\n         via Connected, Loopback0")
    r3.cli.textCheckPoint("P FEC0:23::/64, 1 successors, FD is 28160\n         via Connected, FastEthernet0/0")
    r3.cli.textCheckPoint("P FEC0::13:0/112, 1 successors, FD is 40512000\n         via Connected, Serial0/0/0")
    r3.cli.textCheckPoint("P FEC0::1:0/112, 1 successors, FD is 40640000\n         via FE80::201:C7FF:FEDE:1402 \(40640000/128256\), Serial0/0/0")
    r3.cli.textCheckPoint("P FEC0::12:0/112, 1 successors, FD is 40514560\n         via FE80::203:E4FF:FED2:1101 \(40514560/40512000\), FastEthernet0/0\n         via FE80::201:C7FF:FEDE:1402 \(41024000/40512000\), Serial0/0/0")
    r3.cli.textCheckPoint("P FEC0::2:0/112, 1 successors, FD is 156160\n         via FE80::203:E4FF:FED2:1101 \(156160/128256\), FastEthernet0/0")
    r3.close()
    
def checkpoint_simulation():
    util.clickOnSimulation()
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    util.clickOnWorkspace(r2.x+10, r2.y+15)
    
    #Check that the IPv6 DST IP is FF02::A
    for i in range (0, 8):
        if (object.exists(PDUConst.PDU_SECOND_TAB)):
            if((findObject(PDUConst.PDU_SECOND_TAB).text) == "Inbound PDU Details"):
                pdu.tabs.inbound()
                pdu.checkInboundPdu('IPv6', 'DST IP', 'FF02::A')
                break;
        else:
            util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
            snooze(5)
            util.clickOnWorkspace(r2.x+10, r2.y+15)