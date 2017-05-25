#Thi
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Device.Router.Router import Router
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.Utility import UtilConst
from API.Utility.Util import Util
from API.SimulationPanel.PDU.PDU import PDU

#Function initialization
util = Util()
eventListFilters = EventListFilters()
pdu = PDU()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 151, 136, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 263, 34, "Router1")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 368, 148, "Router2")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 57, 236, "PC0")
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 452, 248, "Server0")
server1 = Server(ComponentBoxConst.DeviceModel.SERVER, 515, 48, "Server1")

def main():
    util.init()
    createTopology()
    ping()
    checkpoint()
    
def createTopology():
    util.open("ipsec_sim.pkt", UtilConst.PROTOCOLS_TEST)

def ping():    
    util.clickOnSimulation()
    
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()  
    pc0.desktop.commandPrompt.setText("ping 2.1.1.2") 
    
def checkpoint():
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    
    snooze(10)
    
    util.clickOnWorkspace(router2.x + 15, router2.y)
    
    snooze(1)

    pdu.tabs.outbound()

    router2_initiator_cookie = str(pdu.getOutboundFieldObject('ISAKMP', 'INITIATOR COOKIE').plainText).split(':')[1]
    router2_responder_cookie = str(pdu.getOutboundFieldObject('ISAKMP', 'RESPONDER COOKIE').plainText).split(':')[1]
        
    pdu.checkPduHeaderExists('ISAKMP', 'Outbound')
    pdu.checkOutboundPdu('ISAKMP', 'INITIATOR COOKIE', router2_initiator_cookie)
    pdu.checkOutboundPdu('ISAKMP', 'RESPONDER COOKIE', router2_responder_cookie)
    pdu.checkOutboundPdu('ISAKMP', 'NEXT PAYLOAD', "1")
    pdu.checkOutboundPdu('ISAKMP', 'VERSION', "1")
    pdu.checkOutboundPdu('ISAKMP', 'EXCHANGE TYPE', "2")
    pdu.checkOutboundPdu('ISAKMP', 'FLAGS', "0")
    pdu.checkOutboundPdu('ISAKMP', 'MESSAGE ID', "0x[0-9A-F]*")
    pdu.checkOutboundPdu('ISAKMP', 'LENGTH', "28") 
    
    test.xcompare(router2_initiator_cookie, "-0000000000000000")
    
    pdu.tabs.inbound()
    
    pdu.checkPduHeaderExists('ISAKMP', 'Inbound')
    pdu.checkInboundPdu('ISAKMP', 'INITIATOR COOKIE', router2_initiator_cookie)
    pdu.checkInboundPdu('ISAKMP', 'RESPONDER COOKIE', "0000000000000000")
    pdu.checkInboundPdu('ISAKMP', 'NEXT PAYLOAD', "1")
    pdu.checkInboundPdu('ISAKMP', 'VERSION', "1")
    pdu.checkInboundPdu('ISAKMP', 'EXCHANGE TYPE', "2")
    pdu.checkInboundPdu('ISAKMP', 'FLAGS', "0")
    pdu.checkInboundPdu('ISAKMP', 'MESSAGE ID', "0x[0-9A-F]*")
    pdu.checkInboundPdu('ISAKMP', 'LENGTH', "28")
    
    pdu.checkPduHeaderExists("ISAKMP Security Association", 'Inbound')
    pdu.checkInboundPdu('ISAKMP Security Association', 'Next Payload', "13")
    pdu.checkInboundPdu('ISAKMP Security Association', 'Reserved', "")
    pdu.checkInboundPdu('ISAKMP Security Association', 'Payload Length', "57")
    pdu.checkInboundPdu('ISAKMP Security Association', 'Domain of Interpretation', "1")
    pdu.checkInboundPdu('ISAKMP Security Association', 'Situation (Variable Length)', "1")
    
    pdu.checkPduHeaderExists("ISAKMP Proposal", 'Inbound')
    pdu.checkInboundPdu('ISAKMP Proposal', 'Next Payload', "0")
    pdu.checkInboundPdu('ISAKMP Proposal', 'Reserved', "")
    pdu.checkInboundPdu('ISAKMP Proposal', 'Payload Length', "49")
    pdu.checkInboundPdu('ISAKMP Proposal', 'Proposal', "1")
    pdu.checkInboundPdu('ISAKMP Proposal', 'Protocol ID', "1")
    pdu.checkInboundPdu('ISAKMP Proposal', 'SPI Size', "0")  
    pdu.checkInboundPdu('ISAKMP Proposal', '#Of Transforms', "1")
    pdu.checkInboundPdu('ISAKMP Proposal', 'SPI (Variable Length)', "0")
    
    pdu.checkPduHeaderExists("ISAKMP Transform", 'Inbound')
    pdu.checkInboundPdu('ISAKMP Transform', 'Next Payload', "0")
    pdu.checkInboundPdu('ISAKMP Transform', 'Payload Length', "33")
    pdu.checkInboundPdu('ISAKMP Transform', 'Transform ID', "10")
    pdu.checkInboundPdu('ISAKMP Transform', 'Transform ID', "KEY_IKE")
    pdu.checkInboundPdu('ISAKMP Transform', 'Encryption Algorithm', "AES-CBC")
    pdu.checkInboundPdu('ISAKMP Transform', 'Key Length', "128")
    pdu.checkInboundPdu('ISAKMP Transform', 'Hash Algorithm', "SHA")
    pdu.checkInboundPdu('ISAKMP Transform', 'Group Description', "5")
    pdu.checkInboundPdu('ISAKMP Transform', 'Authentication Method', "PSK")
    pdu.checkInboundPdu('ISAKMP Transform', 'Life Type', "SECONDS")
    pdu.checkInboundPdu('ISAKMP Transform', 'Life Duration', "900")
        
    pdu.checkPduHeaderExists("ISAKMP VENDOR ID PAYLOAD", 'Inbound')
    pdu.checkInboundPdu('ISAKMP VENDOR ID PAYLOAD', 'NEXT PAYLOAD', "0")
    pdu.checkInboundPdu('ISAKMP VENDOR ID PAYLOAD', 'Reserved', "RESERVED")
    pdu.checkInboundPdu('ISAKMP VENDOR ID PAYLOAD', 'PAYLOAD LENGTH', "49")
    pdu.checkInboundPdu('ISAKMP VENDOR ID PAYLOAD', 'VENDOR ID', "439B59F8BA676C4C")    
        
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    
    snooze(10)
    
    util.clickOnWorkspace(router2.x + 15, router2.y)
    
    snooze(1)

    pdu.tabs.outbound()
    
    pdu.checkPduHeaderExists('ISAKMP', 'Outbound')
    pdu.checkOutboundPdu('ISAKMP', 'INITIATOR COOKIE', router2_initiator_cookie)
    pdu.checkOutboundPdu('ISAKMP', 'RESPONDER COOKIE', router2_responder_cookie)
    pdu.checkOutboundPdu('ISAKMP', 'NEXT PAYLOAD', "4")
    pdu.checkOutboundPdu('ISAKMP', 'VERSION', "1")
    pdu.checkOutboundPdu('ISAKMP', 'EXCHANGE TYPE', "2")
    pdu.checkOutboundPdu('ISAKMP', 'FLAG', "0x0")
    pdu.checkOutboundPdu('ISAKMP', 'MESSAGE ID', "0x[0-9A-F]*")
    pdu.checkOutboundPdu('ISAKMP', 'LENGTH', "28")     
    
    pdu.tabs.inbound()
    
    pdu.checkPduHeaderExists('ISAKMP', 'Inbound')
    pdu.checkInboundPdu('ISAKMP', 'INITIATOR COOKIE', router2_initiator_cookie)
    pdu.checkInboundPdu('ISAKMP', 'RESPONDER COOKIE', router2_responder_cookie)
    pdu.checkInboundPdu('ISAKMP', 'NEXT PAYLOAD', "4")
    pdu.checkInboundPdu('ISAKMP', 'VERSION', "1")
    pdu.checkInboundPdu('ISAKMP', 'EXCHANGE TYPE', "2")
    pdu.checkInboundPdu('ISAKMP', 'FLAG', "0x0")
    pdu.checkInboundPdu('ISAKMP', 'MESSAGE ID', "0x[0-9A-F]*")
    pdu.checkInboundPdu('ISAKMP', 'LENGTH', "28")
    
    pdu.checkPduHeaderExists("KEY EXCHANGE PAYLOAD", 'Inbound')
    pdu.checkInboundPdu('ISAKMP', "NEXT PAYLOAD", "10")
    pdu.checkInboundPdu('ISAKMP', "RESERVED", "")
    pdu.checkInboundPdu('ISAKMP', "PAYLOAD LENGTH", "9")
    pdu.checkInboundPdu('ISAKMP', "KEY EXCHANGE PAYLOAD")
    
    pdu.checkPduHeaderExists("NONCE PAYLOAD", 'Inbound')    
    pdu.checkInboundPdu('ISAKMP', "NEXT PAYLOAD", "0")
    pdu.checkInboundPdu('ISAKMP', "RESERVED", "")
    pdu.checkInboundPdu('ISAKMP', "PAYLOAD LENGTH", "5")
    pdu.checkInboundPdu('ISAKMP', "NONCE PAYLOAD", "")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    
    snooze(10)
    
    util.clickOnWorkspace(router2.x + 15, router2.y)
    
    snooze(1)
    
    pdu.tabs.outbound()
    
    pdu.checkPduHeaderExists('ISAKMP', 'Outbound')
    pdu.checkOutboundPdu('ISAKMP', 'INITIATOR COOKIE', router2_initiator_cookie)
    pdu.checkOutboundPdu('ISAKMP', 'RESPONDER COOKIE', router2_responder_cookie)
    pdu.checkOutboundPdu('ISAKMP', 'NEXT PAYLOAD', "5")
    pdu.checkOutboundPdu('ISAKMP', 'VERSION', "1")
    pdu.checkOutboundPdu('ISAKMP', 'EXCHANGE TYPE', "2")
    pdu.checkOutboundPdu('ISAKMP', 'FLAG', "0x1")
    pdu.checkOutboundPdu('ISAKMP', 'MESSAGE ID', "0x[0-9A-F]*")
    pdu.checkOutboundPdu('ISAKMP', 'LENGTH', "28")     
    
    pdu.tabs.inbound()
    
    pdu.checkPduHeaderExists('ISAKMP', 'Inbound')
    pdu.checkInboundPdu('ISAKMP', 'INITIATOR COOKIE', router2_initiator_cookie)
    pdu.checkInboundPdu('ISAKMP', 'RESPONDER COOKIE', router2_responder_cookie)
    pdu.checkInboundPdu('ISAKMP', 'NEXT PAYLOAD', "5")
    pdu.checkInboundPdu('ISAKMP', 'VERSION', "1")
    pdu.checkInboundPdu('ISAKMP', 'EXCHANGE TYPE', "2")
    pdu.checkInboundPdu('ISAKMP', 'FLAG', "0x1")
    pdu.checkInboundPdu('ISAKMP', 'MESSAGE ID', "0x[0-9A-F]*")
    pdu.checkInboundPdu('ISAKMP', 'LENGTH', "28")