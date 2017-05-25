from API.Android.AddPdu.AddPduConst import AddPduConst
from API.Android.Utility.Util import Util
from API.Android.Workspace.WorkspaceConst import WorkspaceConst
from squish import *
import test
import object

class ComplexPdu:
	def __init__(self):
		self.util = Util()
		
	def toggleAutoSelectPort(self):
		self.util.tap(AddPduConst.AUTO_SELECT_PORT)

	def selectPort(self, p_portName):
		pass
	
	def selectApplication(self, p_application):
		pass
	
	def setDestinationIp(self, p_destinationIp):
		self.util.tap(AddPduConst.DESTINATION_IP_ADDRESS)
		snooze(2)
		self.util.typeText(AddPduConst.DESTINATION_IP_ADDRESS, p_destinationIp)
	
	def setSourceIp(self, p_sourceIp):
		self.util.typeText(AddPduConst.SOURCE_IP_ADDRESS, p_sourceIp)
	
	def setTos(self, p_tos):
		self.util.typeText(AddPduConst.TOS, p_tos)
	
	def setTtl(self, p_ttl):
		self.util.typeText(AddPduConst.TTL, p_ttl)
	
	def setSequenceNumber(self, p_sequenceNumber):
		self.util.tap(AddPduConst.SEQUENCE_NUMBER)
		snooze(2)
		self.util.typeText(AddPduConst.SEQUENCE_NUMBER, p_sequenceNumber)
	
	def setSize(self, p_size):
		self.util.typeText(AddPduConst.SIZE, p_size)
	
	def setOneShot(self):
		self.util.tap(AddPduConst.ONE_SHOT_TIME_RADIO)
	
	def setPeriodic(self):
		self.util.tap(AddPduConst.PERIODIC_RADIO)
	
	def setOneShotSeconds(self, p_seconds):
		self.util.touchAndDrag(WorkspaceConst.MAIN_APPLICATION, 888, 1032, 12, -292)
		snooze(5)
		self.util.tap(AddPduConst.SECONDS_ONE_SHOT)
		snooze(1)
		self.util.typeText(AddPduConst.SECONDS_ONE_SHOT, p_seconds)
	
	def setPeriodicSeconds(self, p_seconds):
		self.util.touchAndDrag(WorkspaceConst.MAIN_APPLICATION, 888, 1032, 12, -292)
		snooze(5)
		self.util.tap(AddPduConst.SECONDS_PERIODIC)
		snooze(1)
		self.util.typeText(AddPduConst.SECONDS_PERIODIC, p_seconds)
	
	def setSourcePort(self, p_sourcePort):
		self.util.typeText(AddPduConst.SOURCE_PORT, p_sourcePort)
	
	def setDestinationPort(self, p_destinationPort):
		self.util.typeText(AddPduConst.DESTINATION_PORT, p_destinationPort)
	
	def createPdu(self):
		self.util.tap(AddPduConst.CREATE_PDU_BUTTON)
	
	def addComplexPdu(self, p_device, p_application = None, p_destinationIp = None, p_sourceIp = None, p_tos = None, p_ttl = None, p_sequenceNumber = None,
					p_size = None, p_oneShot = True, p_seconds = None, p_sourcePort = None, p_destinationPort = None, p_portName = 'Auto', p_send = True):
		p_device.select()
		snooze(5)
		p_device.menu.selectAddComplexPdu()
		snooze(10)
		if not p_portName == 'Auto':
			self.toggleAutoSelectPort()
			self.selectPort(p_portName)
		if p_application:
			self.selectApplication(p_application)
		if p_destinationIp:
			self.setDestinationIp(p_destinationIp)
		if p_sourceIp:
			self.setSourceIp(p_sourceIp)
		if p_destinationPort:
			self.setDestinationPort(p_destinationPort)
		if p_sourcePort:
			self.setSourcePort(p_sourcePort)
		if p_tos:
			self.setTos(p_tos)
		if p_ttl:
			self.setTtl(p_ttl)
		if p_sequenceNumber:
			self.setSequenceNumber(p_sequenceNumber)
		if p_size:
			self.setSize(p_size)
		if p_oneShot:
			self.setOneShot()
			if not p_seconds == '':
				self.setOneShotSeconds(p_seconds)
		else:
			self.setPeriodic()
			if not p_seconds == '':
				self.setPeriodicSeconds(p_seconds)
		if p_send:
			self.createPdu()
		
		
			

class SimplePdu:
	def __init__(self):
		self.util = Util()
		
	def addSimplePdu(self, p_sourceDevice, p_destinationDevice):
		p_sourceDevice.select()
		snooze(2)
		p_sourceDevice.menu.selectAddPdu()
		snooze(2)
		self.util.tapOnDevice(p_destinationDevice)
