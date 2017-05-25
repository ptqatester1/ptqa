##Chris Allen

from API.Utility.Util import Util
from API.Toolbar.CommonToolsBar.ComplexPDUWindowConst import ComplexPDUWindowConst
from squish import *

class PopupWarnings():
    def __init__(self):
        None
    
    @property
    def incorrectPduSizeDialog(self):
        try:
            return findObject(ComplexPDUWindowConst.ERROR_INCORRECT_PDU_SIZE)
        except LookupError, e:
            return False
    
    def incorrectPduSizeOkButton(self):
        Util().clickButton(ComplexPDUWindowConst.ERROR_INCORRECT_PDU_SIZE_OK)

class SourceSettings:
    def __init__(self):
        pass

    def autoSelectPort(self, checked=None):
        auto_select_checkbox = findObject(ComplexPDUWindowConst.AUTO_SELECT_PORT)
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
        Util().clickItem(ComplexPDUWindowConst.OUTGOING_PORT_LIST, portName)



class PduSettings:
    def __init__(self):
        pass

    def selectApplication(self, application):
        Util().clickItem(ComplexPDUWindowConst.APPLICATION_TYPE_LIST, application)
        snooze(1)

    def destinationIp(self, destinationIp):
        Util().setText(ComplexPDUWindowConst.DESTINATION_IP, destinationIp)

    def sourceIp(self, sourceIp):
        Util().setText(ComplexPDUWindowConst.SOURCE_IP, sourceIp)

    def ttl(self, ttl):
        Util().setText(ComplexPDUWindowConst.TIME_TO_LIVE, ttl)

    def tos(self, tos):
        Util().setText(ComplexPDUWindowConst.TOS, tos)
    
    def startingSourcePort(self, sourcePort):
        Util().setText(ComplexPDUWindowConst.SOURCE_PORT, sourcePort)
    
    def destinationPort(self, destinationPort):
        Util().setText(ComplexPDUWindowConst.DESTINATION_PORT, destinationPort)

    def sequenceNumber(self, sequenceNumber):
        Util().setText(ComplexPDUWindowConst.SEQUENCE_NUMBER, sequenceNumber)

    def size(self, size):
        Util().setText(ComplexPDUWindowConst.SIZE, size)

class SimulationSettings:
    def __init__(self):
        pass
    
    def singleShot(self):
        Util().clickButton(ComplexPDUWindowConst.ONE_SHOT)

    def periodic(self):
        Util().clickButton(ComplexPDUWindowConst.PERIODIC)

    def time(self, seconds):
        Util().setText(ComplexPDUWindowConst.ONE_SHOT_TIME, seconds)

    def interval(self, seconds):
        Util().setText(ComplexPDUWindowConst.PERIODIC_INTERVAL, seconds)

class ComplexPDUWindow:
    def __init__(self):
        self.sourceSettings = SourceSettings()
        self.pduSettings = PduSettings()
        self.simulationSettings = SimulationSettings()
        self.popups = PopupWarnings()

    def send(self):
        Util().clickButton(ComplexPDUWindowConst.CREATE_PDU)

    def generatePacket(self, application = None, destinationIp = None, sourceIp = None,
                       ttl = None, tos = None, sequence = None, sourcePort = None, destinationPort = None,
                       sequenceNumber = None, size = None, oneShotOrPeriodic = None,
                       timeOrInterval = None, outgoingPort = None):
        if outgoingPort:
            self.sourceSettings.autoSelectPort(False)
            self.sourceSettings.outgoingPort(outgoingPort)
        else:
            self.sourceSettings.autoSelectPort(True)
        if application:
            self.pduSettings.selectApplication(application) 
        if destinationIp:
            self.pduSettings.destinationIp(destinationIp)
        if sourceIp:
            self.pduSettings.sourceIp(sourceIp)
        if ttl:
            self.pduSettings.ttl(ttl)
        if tos:
            self.pduSettings.tos(tos)
        if sequence:
            self.pduSettings.sequenceNumber(sequence)
        if sourcePort:
            self.pduSettings.startingSourcePort(sourcePort)
        if destinationPort:
            self.pduSettings.destinationPort(destinationPort)
        if sequenceNumber:
            self.pduSettings.sequenceNumber(sequenceNumber)
        if size:
            self.pduSettings.size(size)
        if oneShotOrPeriodic.lower() == 'one shot':
            self.simulationSettings.singleShot()
            self.simulationSettings.time(timeOrInterval)
        elif oneShotOrPeriodic.lower() == 'periodic':
            self.simulationSettings.periodic()
            self.simulationSettings.interval(timeOrInterval)
        else:
            raise ValueError('oneShotOrPeriodic must be "one shot" or "periodic"')
        self.send()

    def ping(self, destinationIp, sourceIp, **kwargs):
        '''Default function will just require source and destination IP but any other
        parameters can be added using keyword arguments.
        example:
            ping(1.1.1.1, 1.1.1.2)
            ping(1.1.1.1, 1.1.1.2, singleOrPeriodic = 'periodic', interval = 1)'''
        self.generatePacket('PING', destinationIp, sourceIp, **kwargs)
        
    def complexPDU(self, application, destinationIp, sourceIp, ttl, tos, sequence, sourcePort, destinationPort, size, oneShotOrPeriodic, timeOrInterval, outgoingPort):
        self.generatePacket(application, destinationIp, sourceIp, ttl, tos, sequence, sourcePort, destinationPort, None, size, oneShotOrPeriodic, timeOrInterval, outgoingPort)
    
    def selectOutgoingPort(self, portName):
        self.sourceSettings.autoSelectPort(False)
        self.sourceSettings.outgoingPort(portName)
        
    def selectAppType(self, p_item):
        self.pduSettings.selectApplication(p_item)
