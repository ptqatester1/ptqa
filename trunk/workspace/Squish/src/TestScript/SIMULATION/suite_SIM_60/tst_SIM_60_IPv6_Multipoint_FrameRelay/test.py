#####################
#@author: Pam Vinco
#####################
from API.ComponentBox import ComponentBoxConst
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Router.Router import Router

from API.Device.Cloud.Cloud import Cloud

#Function initialization
util = Util()

#Device initialization
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 288, 274, "Router0")
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 563, 285, "Router1")
r2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 574, 118, "Router2")
r3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 425, 69, "Router3")
r4 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 254, 90, "Router4")
cloud = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 412, 187, "Cloud0")


def main():
    util.init()
    openFile()
    
    #Ping in simulation
    ping_simulation_r0()
    
    #Ping in realtime
    ping_realtime_r0()
    ping_realtime_r1()
    ping_realtime_r2()
    ping_realtime_r3()
    ping_realtime_r4()
    
def openFile():
    util.open("SIM_60_IPv6_Multipoint_FrameRelay.pkt", UtilConst.PROTOCOLS_TEST)
    util.speedUpConvergence()
    
def ping_simulation_r0():
    util.clickOnSimulation()
    
    #Trace the PDU as it goes through the devices for the ping from Router0
    r0.select()
    r0.clickCliTab()
    r0.cli.setCliText("\r")
    r0.cli.setCliText("en")
    r0.cli.setCliText("ping 2001:0:0:1::401")
    
    #PDU Information - OSI Model at Router0
    util.clickOnWorkspace(r0.x+10, r0.y+10)

    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: 2001:0:0:1::400, Dest. IP: 2001:0:0:1::401\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The Ping process starts the next ping request.\n2. The Ping process creates an ICMP Echo Request message and sends it to the lower process.\n3. The device encapsulates the data into an IPv6 packet.\n4. The device looks up the destination IP address in the routing table.\n5. The routing table finds a routing entry to the destination IP address.\n6. The destination network is directly connected. The device sets destination as the next-hop.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nFrame Relay\nFRAME RELAY")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is unicast. The device looks up in the Frame Relay map table for the DLCI number.\n2. The packet's destination IP address is found in the Frame Relay map table.\n3. The device encapsulates the packet into a Frame Relay header.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Serial0/3/0 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0/3/0 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router0 - Frame Relay
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_HEADER, "Frame Relay")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FLG_START, "FLG:<br>0111 1110")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_ADDRESS, "ADDRESS:<br>0x191")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FCS, "FCS:<br>0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FLG_END, "FLG:<br>0111 1110")

    #PDU Information - Outbound PDU at Router0 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>2001:0:0:1::400")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>2001:0:0:1::401")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")

    #PDU Information - Outbound PDU at Router0 - ICMP Echo
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Cloud0
    util.clickOnWorkspace(cloud.x+10, cloud.y+10)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Serial0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nFrame Relay\nFRAME RELAY")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The cloud looks up the DLCI number on the frame for the connected sublink.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nFrame Relay\nFRAME RELAY")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The cloud changes the frame's DLCI number to the outgoing sublink's DLCI number.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Serial1 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial1 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Cloud0 - Frame Relay
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_HEADER, "Frame Relay")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FLG_START, "FLG:<br>0111 1110")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_ADDRESS, "ADDRESS:<br>0x191")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FCS, "FCS:<br>0x0")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FLG_END, "FLG:<br>0111 1110")
    
    #PDU Information - Inbound PDU at Cloud0 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>2001:0:0:1::400")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>2001:0:0:1::401")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Cloud0 - ICMP Echo
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Cloud0 - Frame Relay
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_HEADER, "Frame Relay")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FLG_START, "FLG:<br>0111 1110")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_ADDRESS, "ADDRESS:<br>0x19a")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FCS, "FCS:<br>0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FLG_END, "FLG:<br>0111 1110")

    #PDU Information - Outbound PDU at Cloud0 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>2001:0:0:1::400")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>2001:0:0:1::401")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")

    #PDU Information - Outbound PDU at Cloud0 - ICMP Echo
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Router1
    util.clickOnWorkspace(r1.x+10, r1.y+10)

    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Serial0/3/0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0/3/0 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nFrame Relay\nFRAME RELAY")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device de-encapsulates the Frame Relay frame and sends it to the upper layer.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: 2001:0:0:1::400, Dest. IP: 2001:0:0:1::401\nICMPv6 Echo Message\nType: 128")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is coming from an outside network. The device looks up its NAT table for necessary translations.\n2. The destination IP address matches the IP address of one of the interfaces. The device dispatches the packet to the upper layer.\n3. The packet is an ICMP packet. The ICMP process processes it.\n4. The ICMP process received an Echo Request message.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: 2001:0:0:1::401, Dest. IP: 2001:0:0:1::400\nICMPv6 Echo Message\nType: 129")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The ICMP process replies to the Echo Request by setting ICMP type to Echo Reply.\n2. The ICMP process sends an Echo Reply.\n3. The device encapsulates the data into an IPv6 packet.\n4. The device looks up the destination IP address in the routing table.\n5. The routing table finds a routing entry to the destination IP address.\n6. The destination network is directly connected. The device sets destination as the next-hop.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nFrame Relay\nFRAME RELAY")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is unicast. The device looks up in the Frame Relay map table for the DLCI number.\n2. The packet's destination IP address is found in the Frame Relay map table.\n3. The device encapsulates the packet into a Frame Relay header.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Serial0/3/0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0/3/0 sends out the frame.")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Router1 - Frame Relay
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_HEADER, "Frame Relay")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FLG_START, "FLG:<br>0111 1110")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_ADDRESS, "ADDRESS:<br>0x19a")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FCS, "FCS:<br>0x0")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FLG_END, "FLG:<br>0111 1110")
    
    #PDU Information - Inbound PDU at Router1 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 123")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>2001:0:0:1::400")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>2001:0:0:1::401")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Router1 - ICMP Echo
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x80")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Router1 - Frame Relay
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_HEADER, "Frame Relay")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FLG_START, "FLG:<br>0111 1110")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_ADDRESS, "ADDRESS:<br>0x19a")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FCS, "FCS:<br>0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FLG_END, "FLG:<br>0111 1110")

    #PDU Information - Outbound PDU at Router1 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 15")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>2001:0:0:1::401")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>2001:0:0:1::400")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")

    #PDU Information - Outbound PDU at Router1 - ICMP Echo
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x81")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Cloud0
    util.clickOnWorkspace(cloud.x+10, cloud.y+10)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Serial1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial1 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nFrame Relay\nFRAME RELAY")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The cloud looks up the DLCI number on the frame for the connected sublink.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nFrame Relay\nFRAME RELAY")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The cloud changes the frame's DLCI number to the outgoing sublink's DLCI number.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): Serial0 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Cloud0 - Frame Relay
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_HEADER, "Frame Relay")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FLG_START, "FLG:<br>0111 1110")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_ADDRESS, "ADDRESS:<br>0x19a")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FCS, "FCS:<br>0x0")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FLG_END, "FLG:<br>0111 1110")
    
    #PDU Information - Inbound PDU at Cloud0 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 15")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>2001:0:0:1::401")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>2001:0:0:1::400")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")
    
    #PDU Information - Inbound PDU at Cloud0 - ICMP Echo
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x81")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    #PDU Information - Outbound PDU at Cloud0 - Frame Relay
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_HEADER, "Frame Relay")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FLG_START, "FLG:<br>0111 1110")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_ADDRESS, "ADDRESS:<br>0x191")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FCS, "FCS:<br>0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_FRAME_RELAY_FLG_END, "FLG:<br>0111 1110")

    #PDU Information - Outbound PDU at Cloud0 - IPv6
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_PL, "PL: 15")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_SRC_IP, "SRC IP:<br/>2001:0:0:1::401")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DST_IP, "DST IP:<br/>2001:0:0:1::400")
    util.textCheckPoint(PDUConst.OUTBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")

    #PDU Information - Outbound PDU at Cloud0 - ICMP Echo
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x81")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.OUTBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    snooze(5)
    
    #PDU Information - OSI Model at Router0
    util.clickOnWorkspace(r0.x+10, r0.y+10)

    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port Serial0/3/0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. Serial0/3/0 receives the frame.")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nFrame Relay\nFRAME RELAY")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device de-encapsulates the Frame Relay frame and sends it to the upper layer.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIPv6 Header\nSrc. IP: 2001:0:0:1::401, Dest. IP: 2001:0:0:1::400\nICMPv6 Echo Message\nType: 129")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is coming from an outside network. The device looks up its NAT table for necessary translations.\n2. The destination IP address matches the IP address of one of the interfaces. The device dispatches the packet to the upper layer.\n3. The packet is an ICMP packet. The ICMP process processes it.\n4. The ICMP process received an Echo Reply message.\n5. The Ping process received an Echo Reply message.\n")
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    #PDU Information - Inbound PDU at Router0 - Frame Relay
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_HEADER, "Frame Relay")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FLG_START, "FLG:<br>0111 1110")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_ADDRESS, "ADDRESS:<br>0x191")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_DATA, "DATA: \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FCS, "FCS:<br>0x0")
    util.textCheckPoint(PDUConst.INBOUND_FRAME_RELAY_FLG_END, "FLG:<br>0111 1110")

    #PDU Information - Inbound PDU at Router0 - IPv6
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HEADER, "IPv6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_VER, "6")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_TRFC, "TRFC: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_FLOW_LABEL, "FLOW LABEL: 0")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_PL, "PL: 15")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_NEXT, "NEXT: 0x3a")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_HOP_LIMIT, "HL: 255")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_SRC_IP, "SRC IP:<br/>2001:0:0:1::401")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DST_IP, "DST IP:<br/>2001:0:0:1::400")
    util.textCheckPoint(PDUConst.INBOUND_IPV6_DATA, "DATA \(VARIABLE LENGTH\)")

    #PDU Information - Inbound PDU at Router0 - ICMP Echo
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_HEADER, "ICMPv6 Echo Message")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_TYPE, "TYPE: 0x81")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CODE, "CODE: 0x0")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_CHECKSUM, "CHECKSUM")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_ID, "ID: 0x2")
    util.textCheckPoint(PDUConst.INBOUND_ICMPV6_ECHO_SEQ_NUM, "SEQ NUMBER: 1")
    
def ping_realtime_r0():
    #Check that all the pings from Router0 are successful ("Success rate is 0 percent" should not be found)
    util.clickOnRealtime()
    r0.select()
    r0.cli.setCliText("ping 2001:0:0:1::401")
    util.fastForwardTime()
    r0.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r0.cli.setCliText("ping 2001:0:0:1::402")
    util.fastForwardTime()
    r0.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r0.cli.setCliText("ping 2001:0:0:1::403")
    util.fastForwardTime()
    r0.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r0.cli.setCliText("ping 2001:0:0:1::408")
    util.fastForwardTime()
    r0.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r0.close()
    
def ping_realtime_r1():
    #Check that all the pings from Router1 are successful ("Success rate is 0 percent" should not be found)
    r1.select()
    r1.clickCliTab()
    r1.cli.setCliText("\r")
    r1.cli.setCliText("en")
    
    r1.cli.setCliText("ping 2001:0:0:1::400")
    util.fastForwardTime()
    r1.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r1.cli.setCliText("ping 2001:0:0:1::402")
    util.fastForwardTime()
    r1.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r1.cli.setCliText("ping 2001:0:0:1::403")
    util.fastForwardTime()
    r1.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r1.cli.setCliText("ping 2001:0:0:1::408")
    util.fastForwardTime()
    r1.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r1.close()
    
def ping_realtime_r2():
    #Check that all the pings from Router2 are successful ("Success rate is 0 percent" should not be found)
    r2.select()
    r2.clickCliTab()
    r2.cli.setCliText("\r")
    r2.cli.setCliText("en")
    
    r2.cli.setCliText("ping 2001:0:0:1::400")
    util.fastForwardTime()
    r2.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r2.cli.setCliText("ping 2001:0:0:1::401")
    util.fastForwardTime()
    r2.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r2.cli.setCliText("ping 2001:0:0:1::403")
    util.fastForwardTime()
    r2.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r2.cli.setCliText("ping 2001:0:0:1::408")
    util.fastForwardTime()
    r2.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r2.close()
    
def ping_realtime_r3():
    #Check that all the pings from Router3 are successful ("Success rate is 0 percent" should not be found)
    r3.select()
    r3.clickCliTab()
    r3.cli.setCliText("\r")
    r3.cli.setCliText("en")
    
    r3.cli.setCliText("ping 2001:0:0:1::400")
    util.fastForwardTime()
    r3.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r3.cli.setCliText("ping 2001:0:0:1::401")
    util.fastForwardTime()
    r3.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r3.cli.setCliText("ping 2001:0:0:1::402")
    util.fastForwardTime()
    r3.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r3.cli.setCliText("ping 2001:0:0:1::408")
    util.fastForwardTime()
    r3.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r3.close()
    
def ping_realtime_r4():
    #Check that all the pings from Router4 are successful ("Success rate is 0 percent" should not be found)
    r4.select()
    r4.clickCliTab()
    r4.cli.setCliText("\r")
    r4.cli.setCliText("en")
    
    r4.cli.setCliText("ping 2001:0:0:1::400")
    util.fastForwardTime()
    r4.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r4.cli.setCliText("ping 2001:0:0:1::401")
    util.fastForwardTime()
    r4.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r4.cli.setCliText("ping 2001:0:0:1::402")
    util.fastForwardTime()
    r4.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r4.cli.setCliText("ping 2001:0:0:1::403")
    util.fastForwardTime()
    r4.cli.textCheckPoint("Success rate is 0 percent", 0)
    
    r4.close()