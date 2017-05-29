from API.Device.DeviceBase.DeviceBase import DeviceBase, SquishObjectName
from API.Device.DeviceBase.ConfigBase.ConfigBase import Config
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.ComponentBox import ComponentBoxConst
from API.Device.Ioe.IOEBase.ThingEditor import ThingEditor
from API.Device.Ioe.IOEBase.Programming import Programming
from API.Device.Ioe.IOEBase.Specifications import Specifications
from API.Device.Ioe.IOEBase.IOConfig import IOConfig
from API.Device.DeviceBase.AttributeBase.AttributesBase import Attributes
from API.Utility import UtilConst
from squish import *
import object

#Can remove the following imports when this gets refactored
from API.Device.Ioe.IoeBaseConst import IoeBaseConst
from API.Utility.Util import Util

def err(msg = ''): raise NotImplementedError(msg)

class Settings(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def displayName(self, displayName):
        Util().setText(self.objName(IoeBaseConst.config.settings.DISPLAY_NAME_EDIT), displayName)
    
    @property
    def serialNumber(self):
        return str(findObject(self.objName(IoeBaseConst.config.settings.SERIAL_NUMBER)).text)

    def noneRadio(self):
        Util().clickButton(self.objName(IoeBaseConst.config.settings.NONE_RADIO))
    
    def homeGatewayRadio(self):
        Util().clickButton(self.objName(IoeBaseConst.config.settings.HOME_GATEWAY_RADIO))
    
    def remoteServerRadio(self):
        Util().clickButton(self.objName(IoeBaseConst.config.settings.REMOTE_SERVER_RADIO))
    
    def serverAddress(self, address):
        Util().setText(self.objName(IoeBaseConst.config.settings.SERVER_ADDRESS_EDIT), address)
    
    def username(self, username):
        Util().setText(self.objName(IoeBaseConst.config.settings.USER_NAME_EDIT), username)
    
    def password(self, password):
        Util().setText(self.objName(IoeBaseConst.config.settings.PASSWORD_EDIT), password)
    
    def connectButton(self):
        Util().clickButton(self.objName(IoeBaseConst.config.settings.CONNECT_BUTTON))
    
    def connect(self, address, username, password):
        self.serverAddress(address)
        self.username(username)
        self.password(password)
        self.connectButton()

class IoeBase(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = None
        self.deviceModel = p_model#Actual model of device. 'Fan' instead of squishname
        super(IoeBase, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)   
        self.config = Config(self)
        self.config.settings = Settings(self)
        self.physical = Physical(self)
        self.thingEditor = ThingEditor(self)
        self.specifications = Specifications(self)
        self.programming = Programming(self)
        self.ioConfig = IOConfig(self)
        self.attribute = Attributes(self)
        
    def updateName(self):
        self.squishName = self.util.getCurrentDeviceName(self.displayName)
        super(IoeBase, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        self.thingEditor.updateName(self.squishName)
        self.programming.updateName(self.squishName)
        self.specifications.updateName(self.squishName)
        self.ioConfig.updateName(self.squishName)
        self.attribute.updateName(self.squishName)
    
    def create(self, *args):
        self.getDeviceModel()
        super(IoeBase, self).create(*args)
        
    def getDeviceModel(self):
        
        mainTypes = {'End Devices':ComponentBoxConst.DeviceGroup.END_DEVICES,
                     'Components':ComponentBoxConst.DeviceGroup.COMPONENTS}
        ComponentBoxConst.DeviceType.SMART_CITY
        
        endDeviceIoeType =  {
                             10:ComponentBoxConst.DeviceType.HOME,
                             11:ComponentBoxConst.DeviceType.SMART_CITY,
                             12:ComponentBoxConst.DeviceType.INDUSTRIAL,
                             13:ComponentBoxConst.DeviceType.POWER_GRID,
                           } 
        componentsIoeType = {
                             5:ComponentBoxConst.DeviceType.BOARDS,
                             14:ComponentBoxConst.DeviceType.ACTUATORS,
                             15:ComponentBoxConst.DeviceType.SENSORS
                             }
        allIoeTypes = {}
        allIoeTypes.update(endDeviceIoeType)
        allIoeTypes.update(componentsIoeType)
        
        for numberKey, componentNameValue in allIoeTypes.items():
            componentBoxString = '.'.join(ComponentBoxConst.DeviceModel.IOE_MCU.split('.')[:-1])
            componentBoxString = componentBoxString.replace('QScrollArea5', 'QScrollArea' + str(numberKey))
            componentBox = findObject(componentBoxString)
            for i, ioeDevice in enumerate(object.children(componentBox)):
                if i == 0:
                    continue
                if self.model == ioeDevice.windowIconText:
                    self.deviceType = componentNameValue
                    self.model = '.'.join((componentBoxString, 'CDeviceButton' + str(i)))
                    return [self.deviceType, self.model]
    
    
    def deviceInteraction(self, p_holdTime = 0.2, p_workspace = 'logical'):
        if p_workspace == 'physical':
            workspace = self.util.currentWorkspace
        elif p_workspace == 'logical':
            workspace = self.util.currentWorkspace
        self.util.mousePressAltButton(workspace, self.x, self.y)
        snooze(p_holdTime)
        self.util.mouseReleaseAltButton(workspace, self.x, self.y)
    
    def deviceDragInteraction(self, xoffset1, yoffset1, xoffset2, yoffset2, p_hold_time = 0.2):
        workspace = self.util.currentWorkspace
        x1, y1 = self.x + xoffset1, self.y + yoffset1
        x2, y2 = self.x + xoffset2, self.y + yoffset2
        self.util.mouseDragAltButton(workspace, x1, y1, x2, y2, p_hold_time)

    def clickTab(self, *args):        
        if object.exists(self.squishName + IoeBaseConst.ADVANCED_BUTTON):
            advancedButton = findObject(self.squishName + IoeBaseConst.ADVANCED_BUTTON)
            if advancedButton.visible and not advancedButton.checked:
                self.util.click(advancedButton)
        super(IoeBase, self).clickTab(*args)#Call devicebase clicktab function    