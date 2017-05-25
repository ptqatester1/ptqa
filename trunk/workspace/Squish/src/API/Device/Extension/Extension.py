##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import DeviceBase, SquishObjectName
from API.Device.Extension.ExcensionConst import ExtensionConst
from API.ComponentBox import ComponentBoxConst
from squish import *

class PopupWarnings:
    def __init__(self):
        None
    
    def connectErrorDialog(self):
        try:
            return findObject(ExtensionConst.popup.CONNECTION_ERROR_DIALOG)
        except LookupError, e:
            return False
    
    def connectErrorOkButton(self):
        Util().clickButton(ExtensionConst.popup.CONNECTION_ERROR_OK_BUTTON)
    
    def connectErrorLabelText(self, text):
        Util().textCheckPoint(ExtensionConst.popup.CONNECTION_ERROR_TEXT, text)
        
class Incoming(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName

    def useGlobalMasterPassword(self, checked = None):
        checkbox = findObject(self.objName(ExtensionConst.incoming.USE_GLOBAL_MULTIUSER_PASSWORD_CHECKBOX))
        if checked == None:
            Util().click(checkbox)
        elif checked == True:
            if not checkbox.checked:
                Util().click(checkbox)
        elif checked == False:
            if checkbox.checked:
                Util().click(checkbox)
        else:
            raise ValueError('checked must be None, True, or False')
    
    def password(self, password):
        Util().setText(self.objName(ExtensionConst.incoming.PASS_EDIT), password)
    
    def okButton(self):
        Util().clickButton(self.objName(ExtensionConst.incoming.OK_BUTT))
    
    def cancelButton(self):
        Util().clickButton(self.objName(ExtensionConst.incoming.CANCEL_BUTT))
        
class OutgoingCheck(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def  peerAddress(self, address, **kwargs):
        if 'property' in kwargs:
            Util().checkProperty(self.objName(ExtensionConst.outgoing.PEER_ADDRESS_EDIT), **kwargs)
        else:
            Util().textCheckPoint(self.objName(ExtensionConst.outgoing.PEER_ADDRESS_EDIT), address)
    
    def peerPortNumber(self, portNumber, **kwargs):
        if 'property' in kwargs:
            Util().checkProperty(self.objName(ExtensionConst.outgoing.PEER_PORT_EDIT), **kwargs)
        else:
            Util().textCheckPoint(self.objName(ExtensionConst.outgoing.PEER_PORT_EDIT), portNumber)
    
    def peerNetworkName(self, networkName, **kwargs):
        if 'property' in kwargs:
            Util().checkProperty(self.objName(ExtensionConst.outgoing.PEER_NETWORK_NAME_EDIT), **kwargs)
        else:
            Util().textCheckPoint(self.objName(ExtensionConst.outgoing.PEER_NETWORK_NAME_EDIT), networkName)
    
    def password(self, password, **kwargs):
        if 'property' in kwargs:
            Util().checkProperty(self.objName(ExtensionConst.outgoing.PASSWORD_EDIT), **kwargs)
        else:
            Util().textCheckPoint(self.objName(ExtensionConst.outgoing.PASSWORD_EDIT), password)
    
    def connectButtonText(self, text):
        Util().textCheckPoint(self.objName(ExtensionConst.outgoing.CONNECT_BUTT), text)
        
class Outgoing(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.check = OutgoingCheck(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
    
    def  peerAddress(self, address):   
        Util().setText(self.objName(ExtensionConst.outgoing.PEER_ADDRESS_EDIT), address)
        Util().setText(self.objName(ExtensionConst.outgoing.PEER_ADDRESS_EDIT), address)
    
    def peerPortNumber(self, portNumber):
        Util().setText(self.objName(ExtensionConst.outgoing.PEER_PORT_EDIT), portNumber)
    
    def peerNetworkName(self, networkName):
        Util().setText(self.objName(ExtensionConst.outgoing.PEER_NETWORK_NAME_EDIT), networkName)
    
    def password(self, password):
        Util().setText(self.objName(ExtensionConst.outgoing.PASSWORD_EDIT), password)
    
    def connectButton(self):
        Util().clickButton(self.objName(ExtensionConst.outgoing.CONNECT_BUTT))
    
    def cancelButton(self):
        Util().clickButton(self.objName(ExtensionConst.outgoing.CANCEL_BUTT))
    
    def connect(self, address = None, portNumber = None, networkName = None, password = None):
        if address:
            self.peerAddress(address)
        if portNumber:
            self.peerPortNumber(portNumber)
        if networkName:
            self.peerNetworkName(networkName)
        if password:
            self.password(password)
        self.connectButton()
        
class Extension(DeviceBase):
    #@summary: set the x, y coordination, device model and device display name
    #to the object
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.MULTIUSER
        super(Extension, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.incoming = Incoming(self)
        self.outgoing = Outgoing(self)
        self.popups = PopupWarnings()
        
    def connectionType(self, incomingOrOutgoing):
        '''incomingOrOutoing: String - (incoming, outgoing)'''
        Util().clickItem(self.objName(ExtensionConst.CONNECTION_TYPE), incomingOrOutgoing.capitalize())
    
    @property
    def dialog(self):
        try:
            return findObject(ExtensionConst.MAIN_DIALOG)
        except LookupError, e:
            return False
    
    def close(self):
        Util().close(ExtensionConst.MAIN_DIALOG)
        