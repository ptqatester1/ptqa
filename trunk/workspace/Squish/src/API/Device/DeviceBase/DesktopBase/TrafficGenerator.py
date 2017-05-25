##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from squish import snooze
def err(msg = ''):
	raise NotImplementedError(msg)

class PopupWarnings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	@property
	def incorrectPduSizeDialog(self):
		try:
			return findObject(self.objName(DesktopConst.trafficGenerator.PDUSIZE_ERROR_DIALOG))
		except LookupError, e:
			return False
	
	def incorrectPduSizeOkButton(self):
		Util().clickButton(self.objName(DesktopConst.trafficGenerator.PDUSIZE_ERROR_OK))

class SourceSettingsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def autoSelectPort(self, checked=True):
		Util().isChecked(self.objName(DesktopConst.trafficGenerator.AUTO_SELECT_PORT), checked)

	def portName(self, name):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.OUTGOING_PORT_LIST), name)

class SourceSettings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = SourceSettingsCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)

	def autoSelectPort(self, checked=None):
		auto_select_checkbox = findObject(self.objName(DesktopConst.trafficGenerator.AUTO_SELECT_PORT))
		if checked == None:
			Util().click(auto_select_checkbox)
		else:
			if checked == True:
				if not auto_select_checkbox.checked:
					Util().click(auto_select_checkbox)
			elif checked == False:
				if auto_select_checkbox.checked:
					Util().click(auto_select_checkbox)
			else:
				raise ValueError('Must pass None, True, or False')
			
	def outgoingPort(self, portName):
		Util().clickItem(self.objName(DesktopConst.trafficGenerator.OUTGOING_PORT_LIST), portName)

class PduSettingsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	def application(self, application):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.APPLICATION_TYPE_LIST), application)

	def destinationIp(self, destinationIp):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.DESTINATION_IP), destinationIp)

	def sourceIp(self, sourceIp):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.SOURCE_IP), sourceIp)

	def ttl(self, ttl):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.TIME_TO_LIVE), ttl)

	def tos(self, tos):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.TOS), tos)
	
	def sourcePort(self, sourcePort):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.SOURCE_PORT), sourcePort)
	
	def destinationPort(self, destinationPort):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.DESTINATION_PORT), destinationPort)

	def sequenceNumber(self, sequenceNumber):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.SEQUENCE_NUMBER), sequenceNumber)

	def size(self, size):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.SIZE), size)

class PduSettings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = PduSettingsCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def selectApplication(self, application):
		Util().clickItem(self.objName(DesktopConst.trafficGenerator.APPLICATION_TYPE_LIST), application)

	def destinationIp(self, destinationIp):
		Util().setText(self.objName(DesktopConst.trafficGenerator.DESTINATION_IP), destinationIp)

	def sourceIp(self, sourceIp):
		Util().setText(self.objName(DesktopConst.trafficGenerator.SOURCE_IP), sourceIp)

	def ttl(self, ttl):
		Util().setText(self.objName(DesktopConst.trafficGenerator.TIME_TO_LIVE), ttl)

	def tos(self, tos):
		Util().setText(self.objName(DesktopConst.trafficGenerator.TOS), tos)
	
	def sourcePort(self, sourcePort):
		Util().setText(self.objName(DesktopConst.trafficGenerator.SOURCE_PORT), sourcePort)
	
	def destinationPort(self, destinationPort):
		Util().setText(self.objName(DesktopConst.trafficGenerator.DESTINATION_PORT), destinationPort)

	def sequenceNumber(self, sequenceNumber):
		Util().setText(self.objName(DesktopConst.trafficGenerator.SEQUENCE_NUMBER), sequenceNumber)

	def size(self, size):
		Util().setText(self.objName(DesktopConst.trafficGenerator.SIZE), size)

class SimulationSettingsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def singleShot(self, checked=True):
		Util().isChecked(self.objName(DesktopConst.trafficGenerator.ONE_SHOT), checked)

	def periodic(self, checked=True):
		Util().isChecked(self.objName(DesktopConst.trafficGenerator.PERIODIC), checked)

	def interval(self, seconds):
		Util().textCheckPoint(self.objName(DesktopConst.trafficGenerator.PERIODIC_INTERVAL), seconds)
	
class SimulationSettings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = SimulationSettingsCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def singleShot(self):
		Util().clickButton(self.objName(DesktopConst.trafficGenerator.ONE_SHOT))

	def periodic(self):
		Util().clickButton(self.objName(DesktopConst.trafficGenerator.PERIODIC))

	def interval(self, seconds):
		Util().setText(self.objName(DesktopConst.trafficGenerator.PERIODIC_INTERVAL), seconds)

class TrafficGenerator(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.sourceSettings = SourceSettings(self)
		self.pduSettings = PduSettings(self)
		self.simulationSettings = SimulationSettings(self)
		self.popups = PopupWarnings(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.sourceSettings.updateName(squishName)
		self.pduSettings.updateName(squishName)
		self.simulationSettings.updateName(squishName)
		self.popups.updateName(squishName)

	def send(self):
		Util().clickButton(self.objName(DesktopConst.trafficGenerator.SEND))

	def close(self):
		Util().clickButton(self.objName(DesktopConst.trafficGenerator.CLOSE_BUTTON))

	def generatePacket(self, application = None, destinationIp = None, sourceIp = None,
					   ttl = None, tos = None, sourcePort = None, destinationPort = None,
					   sequenceNumber = None, size = None, oneShotOrPeriodic = None,
					   interval = None, outgoingPort = None):
		if outgoingPort:
			self.sourceSettings.outgoingPort(outgoingPort)
		if application:
			self.pduSettings.selectApplication(application)
			snooze(1)
		if destinationIp:
			self.pduSettings.destinationIp(destinationIp)
		if sourceIp:
			self.pduSettings.sourceIp(sourceIp)
		if ttl:
			self.pduSettings.ttl(ttl)
		if tos:
			self.pduSettings.tos(tos)
		if sourcePort:
			self.pduSettings.sourcePort(sourcePort)
		if destinationPort:
			self.pduSettings.destinationPort(destinationPort)
		if sequenceNumber:
			self.pduSettings.sequenceNumber(sequenceNumber)
		if size:
			self.pduSettings.size(size)
		if oneShotOrPeriodic:
			if oneShotOrPeriodic.lower() == 'one shot':
				self.simulationSettings.singleShot()
			elif oneShotOrPeriodic.lower() == 'periodic':
				self.simulationSettings.periodic()
				self.simulationSettings.interval(interval)
			else:
				raise ValueError('oneShotOrPeriodic must be "one shot" or "periodic"')
		self.send()
			

	def ping(self, destinationIp, sourceIp, **kwargs):
		'''Default function will just require soure and destination IP but any other
		parameters can be added using keyword arguments.
		example:
			ping(1.1.1.1, 1.1.1.2)
			ping(1.1.1.1, 1.1.1.2, singleOrPeriodic = 'periodic', interval = 1)'''
		if 'sequenceNumber' in kwargs:
			self.generatePacket('PING', destinationIp, sourceIp, **kwargs)
		else:
			self.generatePacket('PING', destinationIp, sourceIp, sequenceNumber=0, **kwargs)
			
	def size(self, size):
		self.pduSettings.size(size)