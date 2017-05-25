#####################
#@author: Pam Vinco
#####################
from API.ComponentBox import ComponentBoxConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Router.Router import Router
from API.Device.EndDevice.PC.PC import PC


#Function initialization
util = Util()

#Device initialization
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 188, 268, "Router1")
r2 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 340, 108, "Router2")
r3 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 527, 266, "Router3")

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 121, 329, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 587, 317, "PC1")

def main():
    util.init()
    openFile()
    
    #Ping in simulation
    ping_simulation()

def openFile():
    util.open("SIM_60_IPv6_Tunneling.pkt", UtilConst.PROTOCOLS_TEST)
    util.speedUpConvergence()
    
def ping_simulation():
    util.clickOnSimulation()
    
    #Trace the PDU as it goes through the devices for the ping from PC0 to PC1
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping FEC0::5:2")
    pc0.minimizeDeviceWindow()
    
    util.clickOnWorkspace(pc0.x+10, pc0.y+15)
    snooze(1)
    
    #PDU Information - OSI Model at PC0
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The Ping process starts the next ping request.\n2. The Ping process creates an ICMP Echo Request message and sends it to the lower process.\n3. The source IP address is not specified. The device sets it to the port's IP address.\n4. The destination IP address is not in the same subnet and is not the broadcast address.\n5. The default gateway is set. The device sets the next-hop to default gateway.\n")
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2:")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is unicast address. The ND Process looks it up in the neighbor table.\n2. The next-hop IP address is not in the neighbor table. The NDP process sends a neighbor solicitation for that IP address and buffers this packet.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at PC0 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 128")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at PC0 - ICMP Echo
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickOnWorkspace(pc0.x+40, pc0.y+15)
    
    #PDU Information - OSI Model at PC0
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FF02::1:FF04:1\nICMPv6 Neighbor Message\nType: 135")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The NDP process constructs a Neighbor Solicitation for the target IPv6 address.\n2. The device sets TTL in the packet header.\n3. The destination IP address is in the same subnet. The device sets the next-hop to destination.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n0006.2A9E.C300 >> 3333.FF04.0001")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is multicast address. The ND Process sets the frame's destination MAC address to a multicast MAC address.\n2. The device encapsulates the PDU into an Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0 sends out the frame.")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at PC0 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>3333.FF04.0001")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0006.2A9E.C300")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Outbound PDU at PC0 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 43")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FF02::1:FF04:1")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at PC0 - ICMPv6 Neighbor Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_HEADER, "ICMPv6 Neighbor Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_TYPE, "TYPE: 0x87")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_R, "R")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_S, "S")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_O, "O")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_RESERVED, "Reserved")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_TARGET_ADDR, "TARGET ADDR:<br/>FEC0::4:1")

    #PDU Information - Outbound PDU at PC0 - Link Layer Option
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_HEADER, "Link Layer Option")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_TYPE, "TYPE: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_LENGTH, "LENGTH: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_LINK_LAYER_ADDR, "LINK LAYER ADDR:")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_ADD, "0006.2A9E.C300")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    util.clickOnWorkspace(r1.x+15, r1.y+15)
    
    #PDU Information - OSI Model at Router1
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/1 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n0006.2A9E.C300 >> 3333.FF04.0001")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FF02::1:FF04:1\nICMPv6 Neighbor Message\nType: 135")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is coming from an outside network. The device looks up its NAT table for necessary translations.\n2. The destination IP address is a broadcast or multicast address. The device dispatches the packet to the upper layer.\n3. The packet is an ICMP packet. The ICMP process processes it.\n4. The packet is an NDP packet. The device processes the packet.\n5. The ND packet is a Neighbor Solicitation.\n6. The Neighbor Solicitation's target IPv6 address matches the receiving port's IPv6 address.\n7. The device updates the neighbor table with received information.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:1, Dest. IP: FEC0::4:2\nICMPv6 Neighbor Message\nType: 136")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The NDP process replies to the Neighbor Solicitation with the matching MAC Address\n2. The device encapsulates the data into an IPv6 packet.\n3. The device sets the TTL on the packet.\n4. The device looks up the destination IP address in the routing table.\n5. The routing table finds a routing entry to the destination IP address.\n6. The destination network is directly connected. The device sets destination as the next-hop.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n000C.8534.AD02 >> 0006.2A9E.C300")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is unicast address. The ND Process looks it up in the neighbor table.\n2. The next-hop IP address is in the neighbor table. The ND Process sets the frame's destination MAC address to the one found in the table.\n3. The device encapsulates the PDU into an Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/1 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Router1 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>3333.FF04.0001")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0006.2A9E.C300")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Inbound PDU at Router1 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 43")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>FF02::1:FF04:1")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Router1 - ICMPv6 Neighbor Message
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_HEADER, "ICMPv6 Neighbor Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_TYPE, "TYPE: 0x87")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_R, "R")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_S, "S")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_O, "O")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_RESERVED, "Reserved")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_TARGET_ADDR, "TARGET ADDR:<br/>FEC0::4:1")
    
    #PDU Information - Inbound PDU at Router1 - Link Layer Option
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_HEADER, "Link Layer Option")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_TYPE, "TYPE: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_LENGTH, "LENGTH: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_LINK_LAYER_ADDR, "LINK LAYER ADDR:")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_ADD, "0006.2A9E.C300")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router1 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>0006.2A9E.C300")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>000C.8534.AD02")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Outbound PDU at Router1 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 43")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:1")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router1 - ICMPv6 Neighbor Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_HEADER, "ICMPv6 Neighbor Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_TYPE, "TYPE: 0x88")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_R, "R")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_S, "S")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_O, "O")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_RESERVED, "Reserved")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_TARGET_ADDR, "TARGET ADDR:<br/>FEC0::4:1")

    #PDU Information - Outbound PDU at Router1 - Link Layer Option
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_HEADER, "Link Layer Option")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_TYPE, "TYPE: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_LENGTH, "LENGTH: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_LINK_LAYER_ADDR, "LINK LAYER ADDR:")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_ADD, "000C.8534.AD02")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    util.clickOnWorkspace(pc0.x+15, pc0.y+15)
    
    #PDU Information - OSI Model at PC0
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n000C.8534.AD02 >> 0006.2A9E.C300")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:1, Dest. IP: FEC0::4:2\nICMPv6 Neighbor Message\nType: 136")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet's destination IP address matches the device's IP address or the broadcast address. The device de-encapsulates the packet.\n2. The packet is an ICMP packet. The ICMP process processes it.\n3. The packet is an NDP packet. The device processes the packet.\n4. The ND packet is a Neighbor Advertisement.\n5. The device updates the neighbor table with received information.\n6. The device removes and sends buffered packets waiting for this Neighbor Advertisement.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)

    #PDU Information - Inbound PDU at PC0 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>0006.2A9E.C300")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>000C.8534.AD02")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Inbound PDU at PC0 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 43")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:1")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at PC0 - ICMPv6 Neighbor Message
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_HEADER, "ICMPv6 Neighbor Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_TYPE, "TYPE: 0x88")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_R, "R")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_S, "S")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_O, "O")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_RESERVED, "Reserved")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_TARGET_ADDR, "TARGET ADDR:<br/>FEC0::4:1")
    
    #PDU Information - Inbound PDU at PC0 - Link Layer Option
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_HEADER, "Link Layer Option")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_TYPE, "TYPE: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_LENGTH, "LENGTH: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_LINK_LAYER_ADDR, "LINK LAYER ADDR:")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_ADD, "000C.8534.AD02")
    
    util.clickOnWorkspace(pc0.x+40, pc0.y+15)
    
    #PDU Information - OSI Model at PC0
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device removes this packet from the buffer and resends it.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n0006.2A9E.C300 >> 000C.8534.AD02")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device encapsulates the PDU into an Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at PC0 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>000C.8534.AD02")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0006.2A9E.C300")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Outbound PDU at PC0 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 128")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at PC0 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    util.clickOnWorkspace(r1.x+15, r1.y+15)
    
    #PDU Information - OSI Model at Router1
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/1 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n0006.2A9E.C300 >> 000C.8534.AD02")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is coming from an outside network. The device looks up its NAT table for necessary translations.\n2. The device looks up the destination IP address in the routing table.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 172.16.12.1, Dest. IP: 172.16.23.3\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The routing table finds a routing entry to the destination IP address.\n2. The device decrements the TTL on the packet.\n3. The packet received on Tunnel0 needs to be encapsulated in Ipv4 Header with the protocol field set to 41.\n4. The device encapsulates the data into an IP packet.\n5. The device looks up the destination IP address in the routing table.\n6. The routing table finds a routing entry to the destination IP address.\n7. The destination routing entry is connected static route. The device sets destination as the next-hop.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nHDLC Frame\nHDLC")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device encapsulates the packet into an HDLC frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Serial0/0/0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0/0/0 sends out the frame.\n")    
        
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Router1 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>000C.8534.AD02")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0006.2A9E.C300")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Inbound PDU at Router1 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 128")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Router1 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
        
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router1 - HDLC
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_HEADER, "HDLC")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_FLG_START, "FLG:<br/>0111 1110")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_ADR, "ADR:<br/>0x8f")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_CONTROL, "CONTROL:<br/>0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_FCS, "FCS:<br/>0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_FLG_END, "FLG:<br/>0111 1110")

    #PDU Information - Outbound PDU at Router1 - IP
    util.textCheckPoint(PDUConst.OUTBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TL, "TL: 20")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PRO, "PRO: 0x29")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_SRC_IP, "SRC IP: 172.16.12.1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DST_IP, "DST IP: 172.16.23.3")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router1 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 127")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router1 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    util.clickOnWorkspace(r2.x+15, r2.y+15)
    
    #PDU Information - OSI Model at Router2
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Serial0/0/0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0/0/0 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nHDLC Frame\nHDLC")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device de-encapsulates the payload from the HDLC frame and sends it to the upper layer.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 172.16.12.1, Dest. IP: 172.16.23.3\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device looks up the destination IP address in the routing table.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 172.16.12.1, Dest. IP: 172.16.23.3\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The routing table finds a routing entry to the destination IP address.\n2. The destination network is directly connected. The device sets destination as the next-hop.\n3. The device decrements the TTL on the packet.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nHDLC Frame\nHDLC")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device encapsulates the packet into an HDLC frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Serial0/0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0/0/1 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Router2 - HDLC  
    util.textCheckPoint(PDUConst.INBOUND_HDLC_HEADER, "HDLC")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_FLG_START, "FLG:<br/>0111 1110")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_ADR, "ADR:<br/>0x8f")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_CONTROL, "CONTROL:<br/>0x0")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_FCS, "FCS:<br/>0x0")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_FLG_END, "FLG:<br/>0111 1110")

    #PDU Information - Inbound PDU at Router2 - IP
    util.textCheckPoint(PDUConst.INBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.INBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.INBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.INBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TL, "TL: 20")
    util.textCheckPoint(PDUConst.INBOUND_IP_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IP_PRO, "PRO: 0x29")
    util.textCheckPoint(PDUConst.INBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.INBOUND_IP_SRC_IP, "SRC IP: 172.16.12.1")
    util.textCheckPoint(PDUConst.INBOUND_IP_DST_IP, "DST IP: 172.16.23.3")
    util.textCheckPoint(PDUConst.INBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Router2 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 127")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Router2 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router2 - HDLC
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_HEADER, "HDLC")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_FLG_START, "FLG:<br/>0111 1110")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_ADR, "ADR:<br/>0x8f")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_CONTROL, "CONTROL:<br/>0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_FCS, "FCS:<br/>0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_HDLC_FLG_END, "FLG:<br/>0111 1110")

    #PDU Information - Outbound PDU at Router2 - IP
    util.textCheckPoint(PDUConst.OUTBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TL, "TL: 20")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_TTL, "TTL: 254")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PRO, "PRO: 0x29")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_SRC_IP, "SRC IP: 172.16.12.1")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DST_IP, "DST IP: 172.16.23.3")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router2 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 127")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router2 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    util.clickOnWorkspace(r3.x+15, r3.y+15)

    #PDU Information - OSI Model at Router3
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Serial0/0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0/0/1 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nHDLC Frame\nHDLC")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device de-encapsulates the payload from the HDLC frame and sends it to the upper layer.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 172.16.12.1, Dest. IP: 172.16.23.3\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The destination IP address matches the IP address of one of the interfaces. The device dispatches the packet to the upper layer.\n2. The protocol field in the Ip Header is 41. The IPv4 header of the packet is removed and sent to port Tunnel0.\n3. The packet received on Tunnel0 sent up to upper OSI layers.\n4. The packet is coming from an outside network. The device looks up its NAT table for necessary translations.\n5. The device looks up the destination IP address in the routing table.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The routing table finds a routing entry to the destination IP address.\n2. The destination network is directly connected. The device sets destination as the next-hop.\n3. The device decrements the TTL on the packet.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2:")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is unicast address. The ND Process looks it up in the neighbor table.\n2. The next-hop IP address is not in the neighbor table. The NDP process sends a neighbor solicitation for that IP address and buffers this packet.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Router3 - HDLC
    util.textCheckPoint(PDUConst.INBOUND_HDLC_HEADER, "HDLC")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_FLG_START, "FLG:<br/>0111 1110")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_ADR, "ADR:<br/>0x8f")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_CONTROL, "CONTROL:<br/>0x0")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_FCS, "FCS:<br/>0x0")
    util.textCheckPoint(PDUConst.INBOUND_HDLC_FLG_END, "FLG:<br/>0111 1110")

    #PDU Information - Inbound PDU at Router3 - IP
    util.textCheckPoint(PDUConst.INBOUND_IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.INBOUND_IP_VER, "4")
    util.textCheckPoint(PDUConst.INBOUND_IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.INBOUND_IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TL, "TL: 20")
    util.textCheckPoint(PDUConst.INBOUND_IP_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_TTL, "TTL: 254")
    util.textCheckPoint(PDUConst.INBOUND_IP_PRO, "PRO: 0x29")
    util.textCheckPoint(PDUConst.INBOUND_IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.INBOUND_IP_SRC_IP, "SRC IP: 172.16.12.1")
    util.textCheckPoint(PDUConst.INBOUND_IP_DST_IP, "DST IP: 172.16.23.3")
    util.textCheckPoint(PDUConst.INBOUND_IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.INBOUND_IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Router3 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 127")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Router3 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router3 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 126")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router3 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickOnWorkspace(r3.x+40, r3.y+15)
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::5:1, Dest. IP: FF02::1:FF05:2\nICMPv6 Neighbor Message\nType: 135")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The NDP process constructs a Neighbor Solicitation for the target IPv6 address.\n2. The device encapsulates the data into an IPv6 packet.\n3. The device sets the TTL on the packet.\n4. The destination IP address is a broadcast or multicast address. The device sets the destination address as the next-hop.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n0090.2BD0.8302 >> 3333.FF05.0002")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is multicast address. The ND Process sets the frame's destination MAC address to a multicast MAC address.\n2. The device encapsulates the PDU into an Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/1 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router3 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>3333.FF05.0002")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0090.2BD0.8302")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Outbound PDU at Router3 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 15")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::5:1")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FF02::1:FF05:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at Router3 - ICMPv6 Neighbor Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_HEADER, "ICMPv6 Neighbor Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_TYPE, "TYPE: 0x87")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_R, "R")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_S, "S")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_O, "O")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_RESERVED, "Reserved")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_TARGET_ADDR, "TARGET ADDR:<br/>FEC0::5:2")

    #PDU Information - Outbound PDU at Router3 - Link Layer Option
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_HEADER, "Link Layer Option")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_TYPE, "TYPE: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_LENGTH, "LENGTH: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_LINK_LAYER_ADDR, "LINK LAYER ADDR:")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_ADD, "0090.2BD0.8302")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    util.clickOnWorkspace(pc1.x+10, pc1.y+15)
    
    #PDU Information - OSI Model at PC1
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n0090.2BD0.8302 >> 3333.FF05.0002")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::5:1, Dest. IP: FF02::1:FF05:2\nICMPv6 Neighbor Message\nType: 135")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet's destination IP address matches the device's IP address or the broadcast address. The device de-encapsulates the packet.\n2. The packet is an ICMP packet. The ICMP process processes it.\n3. The packet is an NDP packet. The device processes the packet.\n4. The ND packet is a Neighbor Solicitation.\n5. The Neighbor Solicitation's target IPv6 address matches the receiving port's IPv6 address.\n6. The device updates the neighbor table with received information.\n")
    

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::5:2, Dest. IP: FEC0::5:1\nICMPv6 Neighbor Message\nType: 136")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The NDP process replies to the Neighbor Solicitation with the matching MAC Address\n2. The device sets TTL in the packet header.\n3. The destination IP address is in the same subnet. The device sets the next-hop to destination.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n0001.6329.8195 >> 0090.2BD0.8302")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is unicast address. The ND Process looks it up in the neighbor table.\n2. The next-hop IP address is in the neighbor table. The ND Process sets the frame's destination MAC address to the one found in the table.\n3. The device encapsulates the PDU into an Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)

    #PDU Information - Inbound PDU at PC1 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>3333.FF05.0002")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0090.2BD0.8302")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Inbound PDU at PC1 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 15")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::5:1")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>FF02::1:FF05:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at PC1 - ICMPv6 Neighbor Message
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_HEADER, "ICMPv6 Neighbor Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_TYPE, "TYPE: 0x87")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_R, "R")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_S, "S")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_O, "O")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_RESERVED, "Reserved")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_TARGET_ADDR, "TARGET ADDR:<br/>FEC0::5:2")
    
    #PDU Information - Inbound PDU at PC1 - Link Layer Option
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_HEADER, "Link Layer Option")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_TYPE, "TYPE: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_LENGTH, "LENGTH: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_LINK_LAYER_ADDR, "LINK LAYER ADDR:")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_ADD, "0090.2BD0.8302")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at PC1 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>0090.2BD0.8302")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0001.6329.8195")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Outbound PDU at PC1 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 43")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:1")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at PC1 - ICMPv6 Neighbor Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_HEADER, "ICMPv6 Neighbor Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_TYPE, "TYPE: 0x88")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_R, "R")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_S, "S")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_O, "O")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_RESERVED, "Reserved")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPv6_NEIGHBOR_TARGET_ADDR, "TARGET ADDR:<br/>FEC0::5:2")

    #PDU Information - Outbound PDU at PC1 - Link Layer Option
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_HEADER, "Link Layer Option")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_TYPE, "TYPE: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_LENGTH, "LENGTH: 0x1")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_LINK_LAYER_ADDR, "LINK LAYER ADDR:")
    util.textCheckPoint(PDUConst.OUTBOUND_LINK_LAYER_OPTION_ADD, "0001.6329.8195")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    util.clickOnWorkspace(r3.x+15, r3.y+15)

    #PDU Information - OSI Model at Router3
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/1 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n0001.6329.8195 >> 0090.2BD0.8302")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::5:2, Dest. IP: FEC0::5:1\nICMPv6 Neighbor Message\nType: 136")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is coming from an outside network. The device looks up its NAT table for necessary translations.\n2. The destination IP address matches the IP address of one of the interfaces. The device dispatches the packet to the upper layer.\n3. The packet is an ICMP packet. The ICMP process processes it.\n4. The packet is an NDP packet. The device processes the packet.\n5. The ND packet is a Neighbor Advertisement.\n6. The device updates the neighbor table with received information.\n7. The device removes and sends buffered packets waiting for this Neighbor Advertisement.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)

    #PDU Information - Inbound PDU at Router3 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>0090.2BD0.8302")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0001.6329.8195")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Inbound PDU at Router3 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 43")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:1")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Router3 - ICMPv6 Neighbor Message
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_HEADER, "ICMPv6 Neighbor Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_TYPE, "TYPE: 0x88")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_R, "R")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_S, "S")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_O, "O")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_RESERVED, "Reserved")
    util.textCheckPoint(PDUConst.INBOUND_ICMPv6_NEIGHBOR_TARGET_ADDR, "TARGET ADDR:<br/>FEC0::5:2")
    
    #PDU Information - Inbound PDU at Router3 - Link Layer Option
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_HEADER, "Link Layer Option")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_TYPE, "TYPE: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_LENGTH, "LENGTH: 0x1")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_LINK_LAYER_ADDR, "LINK LAYER ADDR:")
    util.textCheckPoint(PDUConst.INBOUND_LINK_LAYER_OPTION_ADD, "0001.6329.8195")
    
    util.clickOnWorkspace(r3.x+40, r3.y+15)
    
    #PDU Information - OSI Model at Router3
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device removes this packet from the buffer and resends it.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n0090.2BD0.8302 >> 0001.6329.8195")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device encapsulates the PDU into an Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/1 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at PC0 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>0001.6329.8195")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0090.2BD0.8302")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Outbound PDU at PC0 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 126")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at PC0 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    util.clickOnWorkspace(pc1.x+10, pc1.y+15)
    
    #PDU Information - OSI Model at PC1
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n0090.2BD0.8302 >> 0001.6329.8195")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::4:2, Dest. IP: FEC0::5:2\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet's destination IP address matches the device's IP address or the broadcast address. The device de-encapsulates the packet.\n2. The packet is an ICMP packet. The ICMP process processes it.\n3. The ICMP process received an Echo Request message.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: FEC0::5:2, Dest. IP: FEC0::4:2\nICMPv6 Echo Message\nType: 129")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The ICMP process replies to the Echo Request by setting ICMP type to Echo Reply.\n2. The ICMP process sends an Echo Reply.\n3. The destination IP address is not in the same subnet and is not the broadcast address.\n4. The default gateway is set. The device sets the next-hop to default gateway.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n0001.6329.8195 >> 0090.2BD0.8302")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is unicast address. The ND Process looks it up in the neighbor table.\n2. The next-hop IP address is in the neighbor table. The ND Process sets the frame's destination MAC address to the one found in the table.\n3. The device encapsulates the PDU into an Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0 sends out the frame.")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)

    #PDU Information - Inbound PDU at PC1 - Ethernet II
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>0001.6329.8195")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0090.2BD0.8302")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Inbound PDU at PC1 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 126")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at PC1 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at PC1 - Ethernet II
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DEST_MAC, "DEST MAC:<br/>0090.2BD0.8302")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_SRC_MAC, "SRC MAC:<br/>0001.6329.8195")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_TYPE, "TYPE:<br/>0x86dd")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_ETHERNETII_FCS, "FCS:<br/>0x0")
    
    #PDU Information - Outbound PDU at PC1 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 128")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>FEC0::5:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>FEC0::4:2")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Outbound PDU at PC1 - ICMPv6 Echo Message
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x81")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")