#Thi
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router
from API.Device.EndDevice.PC.PC import PC

from API.Device.EndDevice.Server.Server import Server
from API.Utility.Util import Util
from API.Utility import UtilConst
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.SimulationPanel.EventListFilters.EventListFilters import EventListFilters
from API.SimulationPanel.PDU.PDUConst import PDUConst

#Function initialization
util = Util()
eventListFilters = EventListFilters()

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
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.OUTBOUND_PDU_DETAILS)
    
    router1_initiator_cookie = str(findObject(PDUConst.Outbound.ISAKMP_INITIATOR_COOKIE).text)
    router1_responder_cookie = str(findObject(PDUConst.Outbound.ISAKMP_RESPONDER_COOKIE).text)
    
    util.textCheckPoint(PDUConst.Outbound.ISAKMP_HEADER, "ISAKMP")
    util.textCheckPoint(PDUConst.Outbound.ISAKMP_INITIATOR_COOKIE, router1_initiator_cookie)
    util.textCheckPoint(PDUConst.Outbound.ISAKMP_RESPONDER_COOKIE, router1_responder_cookie)
    util.textCheckPoint(PDUConst.Outbound.ISAKMP_NEXT_PAYLOAD, "NEXT PAYLOAD: 1")
    util.textCheckPoint(PDUConst.Outbound.ISAKMP_VERSION, "VERSION: 1")
    util.textCheckPoint(PDUConst.Outbound.ISAKMP_EXCHANGE_TYPE, "EXCHANGE TYPE: 2")
    util.textCheckPoint(PDUConst.Outbound.ISAKMP_FLAG, "FLAG: 0x0")
    util.textCheckPoint(PDUConst.Outbound.ISAKMP_MESSAGE_ID, "MESSAGE ID: 0x[0-9A-F]*")
    util.textCheckPoint(PDUConst.Outbound.ISAKMP_LENGTH, "LENGTH: 28") 
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    
    snooze(10)
    
    util.clickOnWorkspace(router1.x + 15, router1.y)
    
    snooze(1)
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_HEADER, "ISAKMP")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_INITIATOR_COOKIE, router1_initiator_cookie)
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_RESPONDER_COOKIE, router1_responder_cookie)
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_NEXT_PAYLOAD, "NEXT PAYLOAD: 8")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_VERSION, "VERSION: 1")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_EXCHANGE_TYPE, "EXCHANGE TYPE: 32")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_FLAG, "FLAG: 0x1")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_MESSAGE_ID, "MESSAGE ID: 0x[0-9A-F]*")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_LENGTH, "LENGTH: 28")
    
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_ENCRYPTED_PAYLOAD_HEADER, "ISAKMP ENCRYPTED PAYLOAD")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_ENCRYPTED_PAYLOAD, "ENCRYPTED DATA")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    
    snooze(10)
    
    util.clickOnWorkspace(router1.x + 15, router1.y)
    
    snooze(1)
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_HEADER, "ISAKMP")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_INITIATOR_COOKIE, router1_initiator_cookie)
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_RESPONDER_COOKIE, router1_responder_cookie)
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_NEXT_PAYLOAD, "NEXT PAYLOAD: 8")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_VERSION, "VERSION: 1")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_EXCHANGE_TYPE, "EXCHANGE TYPE: 32")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_FLAG, "FLAG: 0x1")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_MESSAGE_ID, "MESSAGE ID: 0x[0-9A-F]*")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_LENGTH, "LENGTH: 28")
    
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_ENCRYPTED_PAYLOAD_HEADER, "ISAKMP ENCRYPTED PAYLOAD")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_ENCRYPTED_PAYLOAD, "ENCRYPTED DATA")
    
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)
    util.clickButton(PlayControlsConst.CAPTURE_FORWARD)

    snooze(10)
    
    util.clickOnWorkspace(router1.x + 15, router1.y)
    
    snooze(1)
    
    util.clickTab(PDUConst.PDUINFO_TAB_BAR, PDUConst.INBOUND_PDU_DETAILS)
    
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_HEADER, "ISAKMP")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_INITIATOR_COOKIE, router1_initiator_cookie)
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_RESPONDER_COOKIE, router1_responder_cookie)
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_NEXT_PAYLOAD, "NEXT PAYLOAD: 8")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_VERSION, "VERSION: 1")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_EXCHANGE_TYPE, "EXCHANGE TYPE: 32")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_FLAG, "FLAG: 0x1")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_MESSAGE_ID, "MESSAGE ID: 0x[0-9A-F]*")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_LENGTH, "LENGTH: 28")
    
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_ENCRYPTED_PAYLOAD_HEADER, "ISAKMP ENCRYPTED PAYLOAD")
    util.textCheckPoint(PDUConst.Inbound.ISAKMP_ENCRYPTED_PAYLOAD, "ENCRYPTED DATA")