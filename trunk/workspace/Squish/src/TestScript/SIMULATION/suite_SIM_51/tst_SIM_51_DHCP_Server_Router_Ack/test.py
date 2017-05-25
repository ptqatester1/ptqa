#Thi
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router
from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.SimulationPanel.PDU.PDU import PDU

#Function initialization
util = Util()
eventListFilters = EventListFilters()
pdu = PDU()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 35, 233, "Router0")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 149, 237, "Router2")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 260, 226, "PC0")

def main():
    util.init()
    createTopology()
    at_router2()
    at_pc0()
    
def createTopology():
    util.open("DHCP_Req_DHCP-Server-Router.pkt", UtilConst.PROTOCOLS_TEST)

def at_router2():    
    util.clickOnSimulation()
    
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.dhcp()
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    
    snooze(10)
    
    util.clickOnWorkspace(router2.x+15, router2.y)
    
    snooze(1)
    '''pdu.checkInboundPdu(dataType, dataField, dataValue)
    util.textCheckPoint(PDUConst.OSI_HEADER_INFO, "At Device: Router2\nSource: Router0\nDestination: Broadcast")
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0/1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/1 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n00E0.F958.D202 >> 0002.4A64.2802")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 172.16.10.2, Dest. IP: 172.16.13.1")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is a reply from the helper address. The device forwards the packet back to the original sender.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 172.16.13.1, Dest. IP: 255.255.255.255")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The destination IP address is a broadcast or multicast address. The device sets the destination address as the next-hop.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_2, "Layer 2: \n\nEthernet II Header\n0002.4A64.2801 >> FFFF.FFFF.FFFF")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The next-hop IP address is a broadcast. The ARP process sets the frame's destination MAC address to the broadcast MAC address.\n2. The device encapsulates the PDU into an Ethernet frame.\n")
    

    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_OUT_LAYER_1, "Layer 1: Port\(s\): FastEthernet0/0 ")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0/0 sends out the frame.\n")'''
    
    
    util.clickTab(PDUConst.PDU_TAB_BAR, PDUConst.Inbound.INBOUND_PDU_DETAILS)

    pdu.checkInboundPdu("IP", "TL", "81")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_DEST_MAC, "DEST MAC:<br/>0002.4A64.2802")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_SRC_MAC, "SRC MAC:<br/>00E0.F958.D202")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_FCS, "FCS:<br/>0x0")
    
    util.textCheckPoint(PDUConst.Inbound.IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.Inbound.IP_VER, "4")
    util.textCheckPoint(PDUConst.Inbound.IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.Inbound.IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_TL, "TL: 81")
    util.textCheckPoint(PDUConst.Inbound.IP_ID, "ID: 0x5")
    util.textCheckPoint(PDUConst.Inbound.IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.Inbound.IP_PRO, "PRO: 0x11")
    util.textCheckPoint(PDUConst.Inbound.IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.Inbound.IP_SRC_IP, "SRC IP: 172.16.10.2")
    util.textCheckPoint(PDUConst.Inbound.IP_DST_IP, "DST IP: 172.16.13.1")
    util.textCheckPoint(PDUConst.Inbound.IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    util.textCheckPoint(PDUConst.Inbound.UDP_HEADER, "UDP")
    util.textCheckPoint(PDUConst.Inbound.UDP_SRC_PORT, "SRC PORT: 67")
    util.textCheckPoint(PDUConst.Inbound.UDP_DEST_PORT, "DEST PORT: 67")
    util.textCheckPoint(PDUConst.Inbound.UDP_LENGTH, "LENGTH: 0x3d")
    util.textCheckPoint(PDUConst.Inbound.UDP_CHECKSUM, "CHECKSUM: 0x0")
    util.textCheckPoint(PDUConst.Inbound.UDP_DATA, "DATA \(VARIABLE\)")
    
    util.textCheckPoint(PDUConst.Inbound.DHCP_HEADER, "DHCP")
    util.textCheckPoint(PDUConst.Inbound.DHCP_OP, "OP: 0x2")
    util.textCheckPoint(PDUConst.Inbound.DHCP_HW_TYPE, "HW TYPE")
    util.textCheckPoint(PDUConst.Inbound.DHCP_HW_LEN, "HW LEN")
    util.textCheckPoint(PDUConst.Inbound.DHCP_TXT_HOPS, "HOPS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_TRANSACTION_ID, "TRANSACTION ID \(4 BYTES\)") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SECS, "SECS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_FLAG, "FLAGS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_CLIENT_ADDRESS, "CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_YOUR_CLIENT_ADDRESS, "\"YOUR\" CLIENT ADDRESS:<br/>172.16.13.2") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SERVER_ADDRESS, "SERVER ADDRESS:<br/>172.16.10.2") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_RELAY_AGENT_ADDRESS, "RELAY AGENT ADDRESS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_CLIENT_HARDWARE_ADDRESS, "CLIENT HARDWARE ADDRESS:<br/>0090.214B.5165") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SERVER_HOSTNAME, "SERVER HOSTNAME \(64 BYTES\)")
    util.textCheckPoint(PDUConst.Inbound.DHCP_FILE, "FILE \(128 BYTES\)")
    util.textCheckPoint(PDUConst.Inbound.DHCP_OPTIONS, "OPTIONS \(312 BYTES\)") 
    
    
    util.clickTab(PDUConst.PDU_TAB_BAR, PDUConst.Outbound.OUTBOUND_PDU_DETAILS)
    
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_PREAMBLE, "PREAMBLE:<br/>101010...1011")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_DEST_MAC, "DEST MAC:<br/>FFFF.FFFF.FFFF")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_SRC_MAC, "SRC MAC:<br/>0002.4A64.2801")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.Outbound.ETHERNETII_FCS, "FCS:<br/>0x0")
    
    util.textCheckPoint(PDUConst.Outbound.IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.Outbound.IP_VER, "4")
    util.textCheckPoint(PDUConst.Outbound.IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.Outbound.IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_TL, "TL: 81")
    util.textCheckPoint(PDUConst.Outbound.IP_ID, "ID: 0x5")
    util.textCheckPoint(PDUConst.Outbound.IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.Outbound.IP_PRO, "PRO: 0x11")
    util.textCheckPoint(PDUConst.Outbound.IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.Outbound.IP_SRC_IP, "SRC IP: 172.16.13.1")
    util.textCheckPoint(PDUConst.Outbound.IP_DST_IP, "DST IP: 255.255.255.255")
    util.textCheckPoint(PDUConst.Outbound.IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.Outbound.IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    util.textCheckPoint(PDUConst.Outbound.UDP_HEADER, "UDP")
    util.textCheckPoint(PDUConst.Outbound.UDP_SRC_PORT, "SRC PORT: 67")
    util.textCheckPoint(PDUConst.Outbound.UDP_DEST_PORT, "DEST PORT: 68")
    util.textCheckPoint(PDUConst.Outbound.UDP_LENGTH, "LENGTH: 0x3d")
    util.textCheckPoint(PDUConst.Outbound.UDP_CHECKSUM, "CHECKSUM: 0x0")
    util.textCheckPoint(PDUConst.Outbound.UDP_DATA, "DATA \(VARIABLE\)")
    
    util.textCheckPoint(PDUConst.Outbound.DHCP_HEADER, "DHCP")
    util.textCheckPoint(PDUConst.Outbound.DHCP_OP, "OP: 0x2")
    util.textCheckPoint(PDUConst.Outbound.DHCP_HW_TYPE, "HW TYPE")
    util.textCheckPoint(PDUConst.Outbound.DHCP_HW_LEN, "HW LEN")
    util.textCheckPoint(PDUConst.Outbound.DHCP_TXT_HOPS, "HOPS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_TRANSACTION_ID, "TRANSACTION ID \(4 BYTES\)") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_SECS, "SECS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_FLAG, "FLAGS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_CLIENT_ADDRESS, "CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_YOUR_CLIENT_ADDRESS, "\"YOUR\" CLIENT ADDRESS:<br/>172.16.13.2") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_SERVER_ADDRESS, "SERVER ADDRESS:<br/>172.16.10.2") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_RELAY_AGENT_ADDRESS, "RELAY AGENT ADDRESS") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_CLIENT_HARDWARE_ADDRESS, "CLIENT HARDWARE ADDRESS:<br/>0090.214B.5165") 
    util.textCheckPoint(PDUConst.Outbound.DHCP_SERVER_HOSTNAME, "SERVER HOSTNAME \(64 BYTES\)")
    util.textCheckPoint(PDUConst.Outbound.DHCP_FILE, "FILE \(128 BYTES\)")
    util.textCheckPoint(PDUConst.Outbound.DHCP_OPTIONS, "OPTIONS \(312 BYTES\)")
    
    util.close(PDUConst.PDU_WINDOW)
    
def at_pc0():
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    
    snooze(5)
    
    util.clickOnWorkspace(pc0.x+20, pc0.y+10)
    
    snooze(1)

    util.textCheckPoint(PDUConst.OSI_HEADER_INFO, "At Device: PC0\nSource: Router0\nDestination: Broadcast")
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_1, "Layer 1: Port FastEthernet0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. FastEthernet0 receives the frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_2, "Layer 2: \n\nEthernet II Header\n0002.4A64.2801 >> FFFF.FFFF.FFFF")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The frame's destination MAC address matches the receiving port's MAC address, the broadcast address, or a multicast address.\n2. The device decapsulates the PDU from the Ethernet frame.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_3, "Layer 3: \n\nIP Header\nSrc. IP: 172.16.13.1, Dest. IP: 255.255.255.255")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet's destination IP address matches the device's IP address or the broadcast address. The device de-encapsulates the packet.\n")
    
    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_4, "Layer 4: \n\nUDP\nSrc Port: 67, Dst Port: 68")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The device decapsulates the PDU from the UDP segment.\n")

    util.clickButton(PDUConst.NEXT_LAYER)
    
    util.textCheckPoint(PDUConst.OSI_IN_LAYER_7, "Layer 7: \n\nDHCP Frame\nServer: 172.16.10.2, Client: 0.0.0.0")
    util.textCheckPoint(PDUConst.OSI_EXPLANATION, "1. The packet is a DHCP packet. The DHCP client processes it.\n2. The DHCP client received a DHCP acknowledge packet.\n3. The DHCP client receives an Ack packet and sets its IP address configuration.\n")
    
    util.clickTab(PDUConst.PDU_TAB_BAR, PDUConst.Inbound.INBOUND_PDU_DETAILS)

    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_HEADER, "Ethernet II")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_PREAMBLE, "PREAMBLE:\<br/>101010...1011")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_DEST_MAC, "DEST MAC:<br/>FFFF.FFFF.FFFF")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_SRC_MAC, "SRC MAC:<br/>0002.4A64.2801")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_TYPE, "TYPE:<br/>0x800")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_DATA, "DATA \(VARIABLE LENGTH\)")
    util.textCheckPoint(PDUConst.Inbound.ETHERNETII_FCS, "FCS:<br/>0x0")
        
    util.textCheckPoint(PDUConst.Inbound.IP_HEADER, "IP")
    util.textCheckPoint(PDUConst.Inbound.IP_VER, "4")
    util.textCheckPoint(PDUConst.Inbound.IP_IHL, "IHL")
    util.textCheckPoint(PDUConst.Inbound.IP_DSCP, "DSCP: 0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_TL, "TL: 81")
    util.textCheckPoint(PDUConst.Inbound.IP_ID, "ID: 0x5")
    util.textCheckPoint(PDUConst.Inbound.IP_FLAG, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_FRAG_OFFSET, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_TTL, "TTL: 255")
    util.textCheckPoint(PDUConst.Inbound.IP_PRO, "PRO: 0x11")
    util.textCheckPoint(PDUConst.Inbound.IP_CHKSUM, "CHKSUM")
    util.textCheckPoint(PDUConst.Inbound.IP_SRC_IP, "SRC IP: 172.16.13.1")
    util.textCheckPoint(PDUConst.Inbound.IP_DST_IP, "DST IP: 255.255.255.255")
    util.textCheckPoint(PDUConst.Inbound.IP_OPT, "OPT: 0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_PADDING, "0x0")
    util.textCheckPoint(PDUConst.Inbound.IP_DATA, "DATA \(VARIABLE LENGTH\)")
    
    util.textCheckPoint(PDUConst.Inbound.UDP_HEADER, "UDP")
    util.textCheckPoint(PDUConst.Inbound.UDP_SRC_PORT, "SRC PORT: 67")
    util.textCheckPoint(PDUConst.Inbound.UDP_DEST_PORT, "DEST PORT: 68")
    util.textCheckPoint(PDUConst.Inbound.UDP_LENGTH, "LENGTH: 0x3d")
    util.textCheckPoint(PDUConst.Inbound.UDP_CHECKSUM, "CHECKSUM: 0x0")
    util.textCheckPoint(PDUConst.Inbound.UDP_DATA, "DATA \(VARIABLE\)")
    
    util.textCheckPoint(PDUConst.Inbound.DHCP_HEADER, "DHCP")
    util.textCheckPoint(PDUConst.Inbound.DHCP_OP, "OP: 0x2")
    util.textCheckPoint(PDUConst.Inbound.DHCP_HW_TYPE, "HW TYPE")
    util.textCheckPoint(PDUConst.Inbound.DHCP_HW_LEN, "HW LEN")
    util.textCheckPoint(PDUConst.Inbound.DHCP_TXT_HOPS, "HOPS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_TRANSACTION_ID, "TRANSACTION ID \(4 BYTES\)") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SECS, "SECS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_FLAG, "FLAGS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_CLIENT_ADDRESS, "CLIENT ADDRESS:<br/>0.0.0.0") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_YOUR_CLIENT_ADDRESS, "\"YOUR\" CLIENT ADDRESS:<br/>172.16.13.2") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SERVER_ADDRESS, "SERVER ADDRESS:<br/>172.16.10.2") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_RELAY_AGENT_ADDRESS, "RELAY AGENT ADDRESS") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_CLIENT_HARDWARE_ADDRESS, "CLIENT HARDWARE ADDRESS:<br/>0090.214B.5165") 
    util.textCheckPoint(PDUConst.Inbound.DHCP_SERVER_HOSTNAME, "SERVER HOSTNAME \(64 BYTES\)")
    util.textCheckPoint(PDUConst.Inbound.DHCP_FILE, "FILE \(128 BYTES\)")
    util.textCheckPoint(PDUConst.Inbound.DHCP_OPTIONS, "OPTIONS \(312 BYTES\)")    

    router0.select()
    router0.clickCliTab()
    router0.cli.setCliText(" ")
    router0.cli.setCliText("enable")
    router0.cli.setCliText("show ip dhcp binding")
    router0.cli.textCheckPoint("172.16.13.2      0090.214B.5165           --                     Automatic")