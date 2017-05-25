#####################
#@author: Pam Vinco
#####################
from API.ComponentBox import ComponentBoxConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.Device.Modem.Modem import Modem
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Router.Router import Router

from API.Device.Cloud.Cloud import Cloud

#Function initialization
util = Util()

#Device initialization
r2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2911, 66, 73, "Router2")
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 117, 255, "Router1")
cloud = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 132, 138, "Cloud0")
cableModem = Modem(ComponentBoxConst.DeviceModel.CABLE_MODEM, 51, 197, "Cable Modem0")

def main():
    util.init()
    openFile()
    
    #Ping in Realtime
    ping_realtime_r2()
    
    #Ping in Simulation
    ping_simulation_r2()
    
def openFile():
    util.open("SIM_60_IPv4_CableTest.pkt", UtilConst.PROTOCOLS_TEST)
    util.speedUpConvergence()
    
def ping_realtime_r2():
    #Check that the ping from Router2 is successful ("Success rate is 0 percent" should not be found)
    r2.select()
    r2.clickCliTab()
    r2.cli.setCliText("\r")
    r2.cli.setCliText("en")
    r2.cli.setCliText("ping 10.10.10.1")
    util.fastForwardTime()
    r2.cli.textCheckPoint("Success rate is 0 percent", 0)
    
def ping_simulation_r2():
    util.clickOnSimulation()
    
    #Trace the PDU as it goes through the devices for the ping from Router2
    r2.select()
    r2.cli.setCliText("ping 10.10.10.1")
    
    #PDU Information - OSI Model at Router2
    util.clickOnWorkspace(r2.x+10, r2.y+10)

    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 10.10.10.2, Dest. IP: 10.10.10.1\nICMP Message\nType: 8")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The Ping process starts the next ping request.\n2. The Ping process creates an ICMP Echo Request message and sends it to the lower process.\n3. The device encapsulates the data into an IP packet.\n4. The device looks up the destination IP address in the routing table.\n5. The routing table finds a routing entry to the destination IP address.\n6. The destination network is directly connected. The device sets destination as the next-hop.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n00E0.A3A0.A501 >> 000A.416C.CC01")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is a unicast. The ARP process looks it up in the ARP table.\n2. The next-hop IP address is in the ARP table. The ARP process sets the frame's destination MAC address to the one found in the table.\n3. The device encapsulates the PDU into an Ethernet frame.")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): GigabitEthernet0/0 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. GigabitEthernet0/0 sends out the frame.")

    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router2 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Outbound PDU at Router2 - IP
    util.textCheckPoint(PDUConst.OUTBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_ID, "ID: 0x6")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_SRC_IP, "SRC IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DST_IP, "DST IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router2 - ICMP
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_TYPE, "TYPE: 0x8")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Cloud0
    util.clickOnWorkspace(cloud.x+10, cloud.y+10)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Ethernet6")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Ethernet6 receives the frame.")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Coaxial7 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Coaxial7 sends out the frame.")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Cloud0 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Inbound PDU at Cloud0 - IP
    util.textCheckPoint(PDUConst.INBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.INBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.INBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.INBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.INBOUND_IP_ID, "ID: 0x6")
    util.textCheckPoint(PDUConst.INBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.INBOUND_IP_SRC_IP, "SRC IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.INBOUND_IP_DST_IP, "DST IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.INBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Cloud0 - ICMP
    util.textCheckPoint(PDUConst.INBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_TYPE, "TYPE: 0x8")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Cloud0 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Outbound PDU at Cloud0 - IP
    util.textCheckPoint(PDUConst.OUTBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_ID, "ID: 0x6")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_SRC_IP, "SRC IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DST_IP, "DST IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Cloud0 - ICMP
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_TYPE, "TYPE: 0x8")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Cable Modem0
    util.clickOnWorkspace(cableModem.x+10, cableModem.y+10)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Port 0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Port 0 receives the frame.")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Port 1 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Port 1 sends out the frame.")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Cable Modem0 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Inbound PDU at Cable Modem0 - IP
    util.textCheckPoint(PDUConst.INBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.INBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.INBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.INBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.INBOUND_IP_ID, "ID: 0x6")
    util.textCheckPoint(PDUConst.INBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.INBOUND_IP_SRC_IP, "SRC IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.INBOUND_IP_DST_IP, "DST IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.INBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Cable Modem0 - ICMP
    util.textCheckPoint(PDUConst.INBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_TYPE, "TYPE: 0x8")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Cable Modem0 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Outbound PDU at Cable Modem0 - IP
    util.textCheckPoint(PDUConst.OUTBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_ID, "ID: 0x6")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_SRC_IP, "SRC IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DST_IP, "DST IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Cable Modem0 - ICMP
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_TYPE, "TYPE: 0x8")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Router1
    util.clickOnWorkspace(r1.x+10, r1.y+10)

    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port GigabitEthernet0/0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. GigabitEthernet0/0 receives the frame.")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n00E0.A3A0.A501 >> 000A.416C.CC01")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 10.10.10.2, Dest. IP: 10.10.10.1\nICMP Message\nType: 8")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The destination IP address matches the IP address of one of the interfaces. The device dispatches the packet to the upper layer.\n2. The packet is an ICMP packet. The ICMP process processes it.\n3. The ICMP process received an Echo Request message.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 10.10.10.1, Dest. IP: 10.10.10.2\nICMP Message\nType: 0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The ICMP process replies to the Echo Request by setting ICMP type to Echo Reply.\n2. The ICMP process sends an Echo Reply.\n3. The device encapsulates the data into an IP packet.\n4. The device looks up the destination IP address in the routing table.\n5. The routing table finds a routing entry to the destination IP address.\n6. The destination network is directly connected. The device sets destination as the next-hop.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n000A.416C.CC01 >> 00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is a unicast. The ARP process looks it up in the ARP table.\n2. The next-hop IP address is in the ARP table. The ARP process sets the frame's destination MAC address to the one found in the table.\n3. The device encapsulates the PDU into an Ethernet frame.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): GigabitEthernet0/0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. GigabitEthernet0/0 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Router1 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Inbound PDU at Router1 - IP
    util.textCheckPoint(PDUConst.INBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.INBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.INBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.INBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.INBOUND_IP_ID, "ID: 0x6")
    util.textCheckPoint(PDUConst.INBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.INBOUND_IP_SRC_IP, "SRC IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.INBOUND_IP_DST_IP, "DST IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.INBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Router1 - ICMP
    util.textCheckPoint(PDUConst.INBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_TYPE, "TYPE: 0x8")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router1 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Outbound PDU at Router1 - IP
    util.textCheckPoint(PDUConst.OUTBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_ID, "ID: 0x5")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_SRC_IP, "SRC IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DST_IP, "DST IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router1 - ICMP
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_TYPE, "TYPE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Cable Modem0
    util.clickOnWorkspace(cableModem.x+10, cableModem.y+10)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Port 1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Port 1 receives the frame.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Port 0 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Port 0 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Cable Modem0 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Inbound PDU at Cable Modem0 - IP
    util.textCheckPoint(PDUConst.INBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.INBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.INBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.INBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.INBOUND_IP_ID, "ID: 0x5")
    util.textCheckPoint(PDUConst.INBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.INBOUND_IP_SRC_IP, "SRC IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.INBOUND_IP_DST_IP, "DST IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.INBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Cable Modem0 - ICMP
    util.textCheckPoint(PDUConst.INBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_TYPE, "TYPE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Cable Modem0 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Outbound PDU at Cable Modem0 - IP
    util.textCheckPoint(PDUConst.OUTBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_ID, "ID: 0x5")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_SRC_IP, "SRC IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DST_IP, "DST IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Cable Modem0 - ICMP
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_TYPE, "TYPE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Cloud0
    util.clickOnWorkspace(cloud.x+10, cloud.y+10)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Coaxial7")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Coaxial7 receives the frame.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Ethernet6 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Ethernet6 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Cloud0 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Inbound PDU at Cloud0 - IP
    util.textCheckPoint(PDUConst.INBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.INBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.INBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.INBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.INBOUND_IP_ID, "ID: 0x5")
    util.textCheckPoint(PDUConst.INBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.INBOUND_IP_SRC_IP, "SRC IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.INBOUND_IP_DST_IP, "DST IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.INBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Cloud0 - ICMP
    util.textCheckPoint(PDUConst.INBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_TYPE, "TYPE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Cloud0 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Outbound PDU at Cloud0 - IP
    util.textCheckPoint(PDUConst.OUTBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_ID, "ID: 0x5")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_SRC_IP, "SRC IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DST_IP, "DST IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Cloud0 - ICMP
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_TYPE, "TYPE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Router2
    util.clickOnWorkspace(r2.x+10, r2.y+10)

    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port GigabitEthernet0/0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. GigabitEthernet0/0 receives the frame.\n")
   
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n000A.416C.CC01 >> 00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 10.10.10.1, Dest. IP: 10.10.10.2\nICMP Message\nType: 0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The destination IP address matches the IP address of one of the interfaces. The device dispatches the packet to the upper layer.\n2. The packet is an ICMP packet. The ICMP process processes it.\n3. The ICMP process received an Echo Reply message.\n4. The Ping process received an Echo Reply message.\n")

    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router2 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>00E0.A3A0.A501")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>000A.416C.CC01")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
   
    #PDU Information - Outbound PDU at Router2 - IP
    util.textCheckPoint(PDUConst.INBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.INBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.INBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.INBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TL, "TL: 128")
    util.textCheckPoint(PDUConst.INBOUND_IP_ID, "ID: 0x5")
    util.textCheckPoint(PDUConst.INBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IP_PRO, "PRO: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.INBOUND_IP_SRC_IP, "SRC IP: 10.10.10.1")
    util.textCheckPoint(PDUConst.INBOUND_IP_DST_IP, "DST IP: 10.10.10.2")
    util.textCheckPoint(PDUConst.INBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router2 - ICMP
    util.textCheckPoint(PDUConst.INBOUND_ICMP_HEADER, "ICMP")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_TYPE, "TYPE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_ID, "ID: 0x3")
    util.textCheckPoint(PDUConst.INBOUND_ICMP_SEQ_NUM, "SEQ NUMBER: 6")