#Thi
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.PDU.PDUConst import PDUConst

#Function initialization
util = Util()
eventListFilters = EventListFilters()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 35, 233, "Router0")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 149, 237, "Router2")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 260, 226, "PC0")

def main():
    util.init()
    createTopology()
    at_pc0()
    at_router2()
    at_router0()

def createTopology():
    util.open("DHCP_Req_DHCP-Server-Router.pkt", UtilConst.PROTOCOLS_TEST)

def at_pc0():    
    util.clickOnSimulation()
    
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.dhcp()
    
    util.clickOnWorkspace(pc0.x+20, pc0.y+10)
    
    util.textCheckPoint(PDUConst.OSI_HEADER_INFO, "At Device: PC0\nSource: PC0\nDestination: 255.255.255.255")
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_7, "Layer 7: \n\nDHCP Frame\nServer: 0.0.0.0, Client: 0.0.0.0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The DHCP client constructs a Discover packet and sends it out.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_4, "Layer 4: \n\nUDP\nSrc Port: 68, Dst Port: 67")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device encapsulates the PDU into an UDP segment.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 0.0.0.0, Dest. IP: 255.255.255.255")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The port does not have an IP address.\n2. The packet payload is a DHCP UDP segment. The device sets the source address to the zero IP address.\n3. The destination IP address is in the same subnet. The device sets the next-hop to destination.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n0090.214B.5165 >> FFFF.FFFF.FFFF")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is a broadcast. The ARP process sets the frame's destination MAC address to the broadcast MAC address.\n2. The device encapsulates the PDU into an Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDU_TAB_BAR, PDUConst.Outbound.OUTBOUND_PDU_DETAILS)
    
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_2, "4")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_4, "8")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_5, "14")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_6, "19")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_UNITS_LABEL, "Bytes")

    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_DEST_MAC, "DEST MAC:<br/>FFFF.FFFF.FFFF")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_SRC_MAC, "SRC MAC:<br/>0090.214B.5165")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_FCS, "FCS:<br/>0x0")
    
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_2, "4")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_2_2, "8")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_3, "16")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_3_2, "19")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_4, "31")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Outbound.IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.Outbound.IP_VER, "4")
    util.textCheckPoint(PDUConst.Outbound.IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.Outbound.IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_TL, "TL: 77")
    util.textCheckPoint(PDUConst.Outbound.IP_ID, "ID: 0x1")
    util.textCheckPoint(PDUConst.Outbound.IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_TTL, "TTL: 128")
    util.textCheckPoint(PDUConst.Outbound.IP_PRO, "PRO: 0x11")
    util.textCheckPoint(PDUConst.Outbound.IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.Outbound.IP_SRC_IP, "SRC IP: 0.0.0.0")
    util.textCheckPoint(PDUConst.Outbound.IP_DST_IP, "DST IP: 255.255.255.255")
    util.textCheckPoint(PDUConst.Outbound.IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    util.textCheckPoint(PDUConst.Outbound.UDP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Outbound.UDP_BITS_LABEL_2, "16")
    util.textCheckPoint(PDUConst.Outbound.UDP_BITS_LABEL_3, "31")
    util.textCheckPoint(PDUConst.Outbound.UDP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Outbound.UDP_HEADER, "UDP")
    util.textCheckPoint(PDUConst.Outbound.UDP_SRC_PORT, "SRC PORT: 68")
    util.textCheckPoint(PDUConst.Outbound.UDP_DEST_PORT, "DEST PORT: 67")
    util.textCheckPoint(PDUConst.Outbound.UDP_LENGTH, "LENGTH: 0x39")
    util.textCheckPoint(PDUConst.Outbound.UDP_CHECKSUM, "CHECKSUM: 0x0")
    util.textCheckPoint(PDUConst.Outbound.UDP_DATA, "DATA \(VARIABLE\)")
    
    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_LABEL_2, "8")
    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_LABEL_3, "16")
    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_LABEL_4, "31")
    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Outbound.DHCP_HEADER, "DHCP")
    util.textCheckPoint(PDUConst.Outbound.DHCP_OP, "OP: 0x1")
    util.textCheckPoint(PDUConst.Outbound.DHCP_HW_TYPE, "HW TYPE")
    util.textCheckPoint(PDUConst.Outbound.DHCP_HW_LEN, "HW LEN")
    util.textCheckPoint(PDUConst.Outbound.DHCP_TXT_HOPS, "HOPS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_TRANSACTION_ID, "TRANSACTION ID \(4 BYTES\)") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_SECS, "SECS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_FLAG, "FLAGS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_CLIENT_ADDRESS, "CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_YOUR_CLIENT_ADDRESS, "\"YOUR\" CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_SERVER_ADDRESS, "SERVER ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_RELAY_AGENT_ADDRESS, "RELAY AGENT ADDRESS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_CLIENT_HARDWARE_ADDRESS, "CLIENT HARDWARE ADDRESS:<br/>0090.214B.5165") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_SERVER_HOSTNAME, "SERVER HOSTNAME \(64 BYTES\)")
    util.textCheckPoint(PDUConst.Outbound.DHCP_FILE, "FILE \(128 BYTES\)")
    util.textCheckPoint(PDUConst.Outbound.DHCP_OPTIONS, "OPTIONS \(312 BYTES\)")
    
    util.close(PDUConst.PDU_WINDOW)
    
def at_router2():
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    
    snooze(5)
    
    util.clickOnWorkspace(router2.x+15, router2.y)
    
    util.textCheckPoint(PDUConst.OSI_HEADER_INFO, "At Device: Router2\nSource: PC0\nDestination: 255.255.255.255")

    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0/0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/0 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)

    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n0090.214B.5165 >> FFFF.FFFF.FFFF")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)

    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 0.0.0.0, Dest. IP: 255.255.255.255")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The destination IP address is a broadcast or multicast address. The device dispatches the packet to the upper layer.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)

    util.textCheckPoint(PDUConst.OSI_IN_LAYER_4, "Layer 4: \n\nUDP\nSrc Port: 68, Dst Port: 67")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device decapsulates the PDU from the UDP segment.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)

    util.textCheckPoint(PDUConst.OSI_IN_LAYER_7, "Layer 7: \n\nDHCP Frame\nServer: 0.0.0.0, Client: 0.0.0.0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is a DHCP packet. The DHCP server processes it.\n2. The DHCP server received a DHCP Discover packet.\n3. The DHCP server does not have a pool configured for the received port. It drops the packet.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)

    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 172.16.13.1, Dest. IP: 172.16.10.2")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet matches the helper criteria. The device forwards the packet to the helper address.\n2. The device looks up the destination IP address in the routing table.\n3. The routing table finds a routing entry to the destination IP address.\n4. The destination network is directly connected. The device sets destination as the next-hop.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)

    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n0002.4A64.2802 >> 00E0.F958.D202")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is a unicast. The ARP process looks it up in the ARP table.\n2. The next-hop IP address is in the ARP table. The ARP process sets the frame's destination MAC address to the one found in the table.\n3. The device encapsulates the PDU into an Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)

    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0/1 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/1 sends out the frame.\n")
    
    util.clickTab(PDUConst.PDU_TAB_BAR, PDUConst.Inbound.INBOUND_PDU_DETAILS)
    
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_DEST_MAC, "DEST MAC:<br/>FFFF.FFFF.FFFF")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_SRC_MAC, "SRC MAC:<br/>0090.214B.5165")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_FCS, "FCS:<br/>0x0")

    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_2, "4")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_4, "8")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_5, "14")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_6, "19")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_UNITS_LABEL, "Bytes")

    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_2, "4")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_2_2, "8")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_3, "16")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_3_2, "19")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_4, "31")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Inbound.IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.Inbound.IP_VER, "4")
    util.textCheckPoint(PDUConst.Inbound.IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.Inbound.IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_TL, "TL: 77")
    util.textCheckPoint(PDUConst.Inbound.IP_ID, "ID: 0x1")
    util.textCheckPoint(PDUConst.Inbound.IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_TTL, "TTL: 128")
    util.textCheckPoint(PDUConst.Inbound.IP_PRO, "PRO: 0x11")
    util.textCheckPoint(PDUConst.Inbound.IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.Inbound.IP_SRC_IP, "SRC IP: 0.0.0.0")
    util.textCheckPoint(PDUConst.Inbound.IP_DST_IP, "DST IP: 255.255.255.255")
    util.textCheckPoint(PDUConst.Inbound.IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    util.textCheckPoint(PDUConst.Inbound.UDP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Inbound.UDP_BITS_LABEL_2, "16")
    util.textCheckPoint(PDUConst.Inbound.UDP_BITS_LABEL_3, "31")
    util.textCheckPoint(PDUConst.Inbound.UDP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Inbound.UDP_HEADER, "UDP")
    util.textCheckPoint(PDUConst.Inbound.UDP_SRC_PORT, "SRC PORT: 68")
    util.textCheckPoint(PDUConst.Inbound.UDP_DEST_PORT, "DEST PORT: 67")
    util.textCheckPoint(PDUConst.Inbound.UDP_LENGTH, "LENGTH: 0x39")
    util.textCheckPoint(PDUConst.Inbound.UDP_CHECKSUM, "CHECKSUM: 0x0")
    util.textCheckPoint(PDUConst.Inbound.UDP_DATA, "DATA \(VARIABLE\)")

    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_LABEL_2, "8")
    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_LABEL_3, "16")
    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_LABEL_4, "31")
    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Inbound.DHCP_HEADER, "DHCP")
    util.textCheckPoint(PDUConst.Inbound.DHCP_OP, "OP: 0x1")
    util.textCheckPoint(PDUConst.Inbound.DHCP_HW_TYPE, "HW TYPE")
    util.textCheckPoint(PDUConst.Inbound.DHCP_HW_LEN, "HW LEN")
    util.textCheckPoint(PDUConst.Inbound.DHCP_TXT_HOPS, "HOPS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_TRANSACTION_ID, "TRANSACTION ID \(4 BYTES\)") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SECS, "SECS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_FLAG, "FLAGS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_CLIENT_ADDRESS, "CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_YOUR_CLIENT_ADDRESS, "\"YOUR\" CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SERVER_ADDRESS, "SERVER ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_RELAY_AGENT_ADDRESS, "RELAY AGENT ADDRESS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_CLIENT_HARDWARE_ADDRESS, "CLIENT HARDWARE ADDRESS:<br/>0090.214B.5165") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SERVER_HOSTNAME, "SERVER HOSTNAME \(64 BYTES\)")
    util.textCheckPoint(PDUConst.Inbound.DHCP_FILE, "FILE \(128 BYTES\)")
    util.textCheckPoint(PDUConst.Inbound.DHCP_OPTIONS, "OPTIONS \(312 BYTES\)")
    
    util.clickTab(PDUConst.PDU_TAB_BAR, PDUConst.Outbound.OUTBOUND_PDU_DETAILS)
    
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_DEST_MAC, "DEST MAC:<br/>00E0.F958.D202")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_SRC_MAC, "SRC MAC:<br/>0002.4A64.2802")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_FCS, "FCS:<br/>0x0")

    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_2, "4")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_4, "8")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_5, "14")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_LABEL_6, "19")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_BITS_UNITS_LABEL, "Bytes")

    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_2, "4")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_2_2, "8")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_3, "16")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_3_2, "19")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_LABEL_4, "31")
    util.textCheckPoint(PDUConst.Outbound.IP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Outbound.IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.Outbound.IP_VER, "4")
    util.textCheckPoint(PDUConst.Outbound.IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.Outbound.IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_TL, "TL: 77")
    util.textCheckPoint(PDUConst.Outbound.IP_ID, "ID: 0x1")
    util.textCheckPoint(PDUConst.Outbound.IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_TTL, "TTL: 128")
    util.textCheckPoint(PDUConst.Outbound.IP_PRO, "PRO: 0x11")
    util.textCheckPoint(PDUConst.Outbound.IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.Outbound.IP_SRC_IP, "SRC IP: 172.16.13.1")
    util.textCheckPoint(PDUConst.Outbound.IP_DST_IP, "DST IP: 172.16.10.2")
    util.textCheckPoint(PDUConst.Outbound.IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    util.textCheckPoint(PDUConst.Outbound.UDP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Outbound.UDP_BITS_LABEL_2, "16")
    util.textCheckPoint(PDUConst.Outbound.UDP_BITS_LABEL_3, "31")
    util.textCheckPoint(PDUConst.Outbound.UDP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Outbound.UDP_HEADER, "UDP")
    util.textCheckPoint(PDUConst.Outbound.UDP_SRC_PORT, "SRC PORT: 68")
    util.textCheckPoint(PDUConst.Outbound.UDP_DEST_PORT, "DEST PORT: 67")
    util.textCheckPoint(PDUConst.Outbound.UDP_LENGTH, "LENGTH: 0x39")
    util.textCheckPoint(PDUConst.Outbound.UDP_CHECKSUM, "CHECKSUM: 0x0")
    util.textCheckPoint(PDUConst.Outbound.UDP_DATA, "DATA \(VARIABLE\)")

    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_LABEL_2, "8")
    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_LABEL_3, "16")
    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_LABEL_4, "31")
    util.textCheckPoint(PDUConst.Outbound.DHCP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Outbound.DHCP_HEADER, "DHCP")
    util.textCheckPoint(PDUConst.Outbound.DHCP_OP, "OP: 0x1")
    util.textCheckPoint(PDUConst.Outbound.DHCP_HW_TYPE, "HW TYPE")
    util.textCheckPoint(PDUConst.Outbound.DHCP_HW_LEN, "HW LEN")
    util.textCheckPoint(PDUConst.Outbound.DHCP_TXT_HOPS, "HOPS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_TRANSACTION_ID, "TRANSACTION ID \(4 BYTES\)") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_SECS, "SECS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_FLAG, "FLAGS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_CLIENT_ADDRESS, "CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_YOUR_CLIENT_ADDRESS, "\"YOUR\" CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_SERVER_ADDRESS, "SERVER ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_RELAY_AGENT_ADDRESS, "RELAY AGENT ADDRESS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_CLIENT_HARDWARE_ADDRESS, "CLIENT HARDWARE ADDRESS:<br/>0090.214B.5165") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_SERVER_HOSTNAME, "SERVER HOSTNAME \(64 BYTES\)")
    util.textCheckPoint(PDUConst.Outbound.DHCP_FILE, "FILE \(128 BYTES\)")
    util.textCheckPoint(PDUConst.Outbound.DHCP_OPTIONS, "OPTIONS \(312 BYTES\)")
    
    util.close(PDUConst.PDU_WINDOW)
    
def at_router0():
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    
    snooze(5)
    
    util.clickOnWorkspace(router0.x+20, router0.y+10)
    
    util.textCheckPoint(PDUConst.OSI_HEADER_INFO, "At Device: Router0\nSource: PC0\nDestination: 255.255.255.255")
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/1 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n0002.4A64.2802 >> 00E0.F958.D202")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 172.16.13.1, Dest. IP: 172.16.10.2")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The destination IP address matches the IP address of one of the interfaces. The device dispatches the packet to the upper layer.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_4, "Layer 4: \n\nUDP\nSrc Port: 68, Dst Port: 67")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device decapsulates the PDU from the UDP segment.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_7, "Layer 7: \n\nDHCP Frame\nServer: 0.0.0.0, Client: 0.0.0.0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is a DHCP packet. The DHCP server processes it.\n2. The DHCP server received a DHCP Discover packet.\n3. The DHCP server does not have an existing binding to this host. It looks up DHCP pools for a new IP address.\n4. The DHCP server finds the next available IP address in the pool.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_7, "Layer 7: \n")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The DHCP server constructs a DHCP Offer packet and prepares to send it out.\n")
    
    util.clickTab(PDUConst.PDU_TAB_BAR, PDUConst.Inbound.INBOUND_PDU_DETAILS)
    
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_DEST_MAC, "DEST MAC:<br/>00E0.F958.D202")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_SRC_MAC, "SRC MAC:<br/>0002.4A64.2802")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_FCS, "FCS:<br/>0x0")

    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_2, "4")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_4, "8")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_5, "14")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_LABEL_6, "19")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_BITS_UNITS_LABEL, "Bytes")
    
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_2, "4")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_2_2, "8")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_3, "16")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_3_2, "19")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_LABEL_4, "31")
    util.textCheckPoint(PDUConst.Inbound.IP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Inbound.IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.Inbound.IP_VER, "4")
    util.textCheckPoint(PDUConst.Inbound.IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.Inbound.IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_TL, "TL: 77")
    util.textCheckPoint(PDUConst.Inbound.IP_ID, "ID: 0x1")
    util.textCheckPoint(PDUConst.Inbound.IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_TTL, "TTL: 128")
    util.textCheckPoint(PDUConst.Inbound.IP_PRO, "PRO: 0x11")
    util.textCheckPoint(PDUConst.Inbound.IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.Inbound.IP_SRC_IP, "SRC IP: 172.16.13.1")
    util.textCheckPoint(PDUConst.Inbound.IP_DST_IP, "DST IP: 172.16.10.2")
    util.textCheckPoint(PDUConst.Inbound.IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    util.textCheckPoint(PDUConst.Inbound.UDP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Inbound.UDP_BITS_LABEL_2, "16")
    util.textCheckPoint(PDUConst.Inbound.UDP_BITS_LABEL_3, "31")
    util.textCheckPoint(PDUConst.Inbound.UDP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Inbound.UDP_HEADER, "UDP")
    util.textCheckPoint(PDUConst.Inbound.UDP_SRC_PORT, "SRC PORT: 68")
    util.textCheckPoint(PDUConst.Inbound.UDP_DEST_PORT, "DEST PORT: 67")
    util.textCheckPoint(PDUConst.Inbound.UDP_LENGTH, "LENGTH: 0x39")
    util.textCheckPoint(PDUConst.Inbound.UDP_CHECKSUM, "CHECKSUM: 0x0")
    util.textCheckPoint(PDUConst.Inbound.UDP_DATA, "DATA \(VARIABLE\)")

    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_LABEL_1, "0")
    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_LABEL_2, "8")
    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_LABEL_3, "16")
    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_LABEL_4, "31")
    util.textCheckPoint(PDUConst.Inbound.DHCP_BITS_UNITS_LABEL, "Bits")
    
    util.textCheckPoint(PDUConst.Inbound.DHCP_HEADER, "DHCP")
    util.textCheckPoint(PDUConst.Inbound.DHCP_OP, "OP: 0x1")
    util.textCheckPoint(PDUConst.Inbound.DHCP_HW_TYPE, "HW TYPE")
    util.textCheckPoint(PDUConst.Inbound.DHCP_HW_LEN, "HW LEN")
    util.textCheckPoint(PDUConst.Inbound.DHCP_TXT_HOPS, "HOPS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_TRANSACTION_ID, "TRANSACTION ID \(4 BYTES\)") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SECS, "SECS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_FLAG, "FLAGS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_CLIENT_ADDRESS, "CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_YOUR_CLIENT_ADDRESS, "\"YOUR\" CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SERVER_ADDRESS, "SERVER ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_RELAY_AGENT_ADDRESS, "RELAY AGENT ADDRESS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_CLIENT_HARDWARE_ADDRESS, "CLIENT HARDWARE ADDRESS:<br/>0090.214B.5165") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SERVER_HOSTNAME, "SERVER HOSTNAME \(64 BYTES\)")
    util.textCheckPoint(PDUConst.Inbound.DHCP_FILE, "FILE \(128 BYTES\)")
    util.textCheckPoint(PDUConst.Inbound.DHCP_OPTIONS, "OPTIONS \(312 BYTES\)")