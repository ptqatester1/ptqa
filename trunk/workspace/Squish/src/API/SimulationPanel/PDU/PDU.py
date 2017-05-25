##Chris Allen

from API.SimulationPanel.PDU.PDUConst import PDUConst
from API.SimulationPanel.EventList.EventList import EventList
from API.SquishSyntax import SquishSyntax
from API.Utility.Util import Util
from squish import *
import object
import test

class PduTabs:
    def __init__(self):
        self.util = Util()
    
    def _clickTab(self, tabName):
        self.util.clickTab(PDUConst.PDUINFO_TAB_BAR, tabName)
    
    def osiModel(self):
        self._clickTab('OSI Model')
    
    def inbound(self):
        self._clickTab('Inbound PDU Details')
    
    def outbound(self):
        self._clickTab('Outbound PDU Details')
    
class Challenge:
    def __init__(self):
        self.util = Util()
        self.tabs = PduTabs()
        
    def selectAnswer(self, answer):
        self.util.click(PDUConst.challenge.ANSWER_BASE + answer)

class OsiModel:
    def __init__(self):
        self.util = Util()
        self.tabs = PduTabs()
        self.check = OsiModelCheck()
        self.challenge = Challenge()
        
    def challengeMeButton(self):
        self.util.clickButton(PDUConst.CHALLENGE_BUTT)
    
    def nextLayerButton(self):
        self.util.clickButton(PDUConst.NEXT_LAYER)
    
    def previousLayButton(self):
        self.util.clickButton(PDUConst.PREVIOUS_LAYER)
    
    def selectInLayer(self, layer):
        layer_name_base = PDUConst.OSI_IN_LAYER_1[:-1]
        self.util.click(layer_name_base + str(layer))
    
    def selectOutLayer(self, layer):
        layer_name_base = PDUConst.OSI_OUT_LAYER_1[:-1]
        self.util.click(layer_name_base + str(layer))

class OsiModelCheck:
    def __init__(self):
        self.util = Util()
        self.tabs = PduTabs()
        
    def explanation(self, text, **kwargs):
        self.util.textCheckPoint(PDUConst.OSI_EXPLANATION, text, **kwargs)
    
    def inLayerOsiExplanation(self, layer, text, **kwargs):
        self.tabs.osiModel()
        OsiModel().selectInLayer(layer)
        self.explanation(text, **kwargs)
    
    def outLayerOsiExplanation(self, layer, text, **kwargs):
        self.tabs.osiModel()
        OsiModel().selectOutLayer(layer)
        self.explanation(text)
    
    def inLayerInformation(self, layer, text, **kwargs):
        self.tabs.osiModel()
        OsiModel().selectInLayer(layer)
        self.util.textCheckPoint(PDUConst.OSI_IN_LAYER_BASE + str(layer), text, **kwargs)
        
    def outLayerInformation(self, layer, text, **kwargs):
        self.tabs.osiModel()
        OsiModel().selectOutLayer(layer)
        self.util.textCheckPoint(PDUConst.OSI_OUT_LAYER_BASE + str(layer), text, **kwargs)
        
    def headerInfo(self, text, **kwargs):
        self.util.textCheckPoint(PDUConst.OSI_HEADER_INFO, text, **kwargs)
    
class PDU:
    def __init__(self):
        self.util = Util()
        self.tabs = PduTabs()
        self.osiModel = OsiModel()
        
    def waitForPdu(self, lastDevice, atDevice, type, maxTries, **kwargs):
        return EventList().waitForEvent(lastDevice, atDevice, type, maxTries, **kwargs)
    
    def selectPdu(self, lastDevice, atDevice, type, **kwargs):
        '''Select a pdu based on the last device, current device, and type
        See EventList.selectEvent documentation for kwargs details'''
        EventList().selectEvent(lastDevice, atDevice, type, **kwargs)
    
    def _getPduObject(self, inboundOrOutbound):
        main_outbound_object_name = ':CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.PDU Info.CBasePDUInfoClass.m_PDUInfoTabWidget.qt_tabwidget_stackedwidget.m_OutPDUDetailsPage.m_OutPDUGroupBox.m_outPDUScrollArea.qt_scrollarea_viewport.outPduWidget'                                          
        main_indbound_object_name = ':CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.PDU Info.CBasePDUInfoClass.m_PDUInfoTabWidget.qt_tabwidget_stackedwidget.m_InPDUDetailsPage.m_InPDUGroupBox.m_PDUScrollArea.qt_scrollarea_viewport.inPduWidget'
        #Determine the parent object based on whether it is inbound or outbound
        if inboundOrOutbound.lower().startswith('i'):
            main_pdu_object_name = main_indbound_object_name
        elif inboundOrOutbound.lower().startswith('o'):
            main_pdu_object_name = main_outbound_object_name
        return findObject(main_pdu_object_name)
        
    def _getSection(self, header_data_type, pdu_obj):
        main_pdu_object = pdu_obj
        #Each section is a child of the main_pdu_object
        section_objects_list = object.children(main_pdu_object)
        for obj in section_objects_list:
            section_child_objects = object.children(obj)
            try:
                if len(section_child_objects) > 1:
                    section_header_text = str(section_child_objects[1].text)#section_child_objects[1] should be the main header text
                else:
                    continue#If there are not children then continue to the next iteration
            except AttributeError, e:
                section_header_text = None
            if section_header_text:
                if section_header_text == header_data_type:
                    return obj
        raise ValueError('Unable to find dataType:%s'%(header_data_type,))
    
    def _getField(self, field_value, section_object):
        section_child_objects = object.children(section_object)
        #Iterate through all the child object until the right one is found. Throw an error if not found
        for field_object in section_child_objects:
            #Convert the object name to a string and then split it so it can check for the correct field without the data mattering
            object_name = str(field_object.objectName)
            field_text = object_name.split(':')[0]
#            field_text = split_field_text[0]
#             if len(split_field_text) > 1:
#                 field_value_text = ':'.join(split_field_text[1:])#This needs to be here to account for IPv6 address and other items that might contain a : that isn't for separating the field/value
#             else:
#                 field_value_text = ''
            if field_text == field_value:
                return field_object
        raise ValueError('Unable to find dataField:%s'%(field_value,))
    
    def checkPdu(self, dataType, dataField, dataValue, inboundOrOutbound, **kwargs):
        '''
        dataType: String (The header for the section of the PDU that is to be checked
                          Example: To check the ICMP section of a PDU the value of
                                   dataType should be "ICMP")
        dataField: String (The field inside a specific dataType to be checked.
                           Example: To check the ID of an ICMP packet the dataField
                                    should be "ID" and the dataType should be "ICMP")
        dataValue: String (The expected value of the dataField in dataType.
                           Example: To check if the ID of an ICMP packet is Ox2 the 
                                    dataValue should be "Ox2" the dataField should be
                                    "ID" and the dataType should be "ICMP"
        inboundOrOutbound: String ('in' or 'out')
        kwargs: Keyword arguments for the textCheckPoint
        Example usage: checkPdu("ICMP", "ID", "Ox2")#Check the ID field in the ICMP
                                                     section of the PDU for the value
                                                     of Ox2
        '''
        if dataValue == None:
            dataValue = ''#Set to empty string if not provided
        main_pdu_object = self._getPduObject(inboundOrOutbound)
        section = self._getSection(dataType, main_pdu_object)
        field = self._getField(dataField, section)  
        #If the field is correct then rejoin the text so that it can be checked as a whole
        text = str(field.objectName)
        searchText = ':'.join([val for val in [dataField, dataValue] if val])
        return self.util.checkText(text, searchText, escape=True, **kwargs)
        
    def checkPduHeaderExists(self, dataType, inboundOrOutbound, **kwargs):
        main_pdu_object = self._getPduObject(inboundOrOutbound)
        section = self._findSection(dataType, main_pdu_object)
        if section:
            test.passes(dataType + ' header is found')
        else:
            test.fail(dataType + ' header is not found')
            
    def checkInboundPduHeaderExists(self, dataType, **kwargs):
        main_pdu_object = self._getPduObject('Inbound')
        section = self._findSection(dataType, main_pdu_object)
        if section:
            test.passes(dataType + ' header is found')
        else:
            test.fail(dataType + ' header is not found')
            
    def checkOutboundPduHeaderExists(self, dataType, **kwargs):
        main_pdu_object = self._getPduObject('Outbound')
        section = self._findSection(dataType, main_pdu_object)
        if section:
            test.passes(dataType + ' header is found')
        else:
            test.fail(dataType + ' header is not found')
            
    def _findSection(self, header_data_type, pdu_obj):
        #Same as _getSection but with no error so tests can continue running
        main_pdu_object = pdu_obj
        #Each section is a child of the main_pdu_object
        section_objects_list = object.children(main_pdu_object)
        for obj in section_objects_list:
            section_child_objects = object.children(obj)
            try:
                if len(section_child_objects) > 1:
                    section_header_text = str(section_child_objects[1].text)#section_child_objects[1] should be the main header text
                else:
                    continue#If there are not children then continue to the next iteration
            except AttributeError, e:
                section_header_text = None
            if section_header_text:
                if section_header_text == header_data_type:
                    return obj    
        
    def checkInboundPdu(self, dataType, dataField, dataValue, **kwargs):
        self.tabs.inbound()
        self.checkPdu(dataType, dataField, dataValue, 'in', **kwargs)
    
    def checkOutboundPdu(self, dataType, dataField, dataValue, **kwargs):
        self.tabs.outbound()
        self.checkPdu(dataType, dataField, dataValue, 'out', **kwargs)
    
    def getInboundFieldObject(self, dataType, dataField):
        self.tabs.inbound()
        return self._getField(dataField, self._getSection(dataType, self._getPduObject('in')))
    
    def getOutboundFieldObject(self, dataType, dataField):
        self.tabs.outbound()
        return self._getField(dataField, self._getSection(dataType, self._getPduObject('out')))
    
    def getInboundSectionHeaderObject(self, dataType):
        self.tabs.inbound()
        return object.children(self._getSection(dataType, self._getPduObject('in')))[1]
    
    def getOutboundSectionHeaderObject(self, dataType):
        self.tabs.outbound()
        return object.children(self._getSection(dataType, self._getPduObject('out')))[1]
    
    def close(self):
        self.util.close(PDUConst.PDU_WINDOW)