########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.COServer.COServer import COServer
from API.Device.COServer import COServerConst
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase import DeviceBaseConst

util = Util()
server = COServer(ComponentBoxConst.DeviceModel.CO_SERVER, 175, 80, 'Central Office Server0')

def main():
    util.init()
    create()
    checkGlobalConfig()
    checkInterfaceConfig()
    checkZoom()
    checkCustomizeIconButtons()
    
def create():    
    server.create()
    server.select()

def checkGlobalConfig():
    server.clickConfigTab()
    server.config.settings.displayName("COS")
    server.config.settings.domainName("COS-D")
    server.config.settings.check.displayName("COS")
    server.config.settings.check.domainName("COS-D")
    
    server.config.selectInterface('Algorithm Settings')
    server.config.algorithmSettings.check.globalSettings(True)
    server.config.algorithmSettings.check.halfOpenSessionMultiplier(None, property='enabled', value=False)
    server.config.algorithmSettings.check.halfOpenSessionMultiplier('1')
    server.config.algorithmSettings.check.maxConnections(None, property='enabled', value=False)
    server.config.algorithmSettings.check.maxConnections('100')
    server.config.algorithmSettings.check.maxOpen(None, property='enabled', value=False)
    server.config.algorithmSettings.check.maxOpen('1000')
    server.config.algorithmSettings.check.maxRetransmission(None, property='enabled', value=False)
    server.config.algorithmSettings.check.maxRetransmission('1000')
    
    server.config.algorithmSettings.globalSettings(None)
    server.config.algorithmSettings.halfOpenSessionMultiplier('2')
    server.config.algorithmSettings.maxConnections('50')
    server.config.algorithmSettings.maxOpen('1500')
    server.config.algorithmSettings.maxRetransmission('1500')
    
    server.config.algorithmSettings.check.globalSettings(False)
    server.config.algorithmSettings.check.halfOpenSessionMultiplier(None, property='enabled', value=True)
    server.config.algorithmSettings.check.halfOpenSessionMultiplier('2')
    server.config.algorithmSettings.check.maxConnections(None, property='enabled', value=True)
    server.config.algorithmSettings.check.maxConnections('50')
    server.config.algorithmSettings.check.maxOpen(None, property='enabled', value=True)
    server.config.algorithmSettings.check.maxOpen('1500')
    server.config.algorithmSettings.check.maxRetransmission(None, property='enabled', value=True)
    server.config.algorithmSettings.check.maxRetransmission('1500')
    
def checkInterfaceConfig():
    server.config.selectInterface('Backbone')
    server.config.interface.backbone.check.dhcp(True)
    server.config.interface.backbone.check.static(False)
    server.config.interface.backbone.check.gateway('')
    server.config.interface.backbone.check.ip('')
    server.config.interface.backbone.check.subnet('')
    server.config.interface.backbone.check.dns('')
    
    server.config.interface.backbone.ipconfig('1.1.1.1', '255.0.0.0')
    
    server.config.interface.backbone.check.ip('1.1.1.1')
    server.config.interface.backbone.check.subnet('255.0.0.0')
    
    server.config.selectInterface('Cell Tower')
    server.config.interface.cellTower.check.ip("172.16.1.1")
    server.config.interface.cellTower.check.subnet("255.255.255.0")
    server.config.interface.cellTower.check.ipv6("2001::1")
    server.config.interface.cellTower.check.subnetv6("64")
    server.config.interface.cellTower.check.linkLocal('FE80::')
    
def checkZoom():
    server.clickPhysicalTab()    
    checkRange(server.physical.imageObject.width, 309)
    checkRange(server.physical.imageObject.height, 73)

    server.physical.zoomIn()
    checkRange(server.physical.imageObject.width, 618)
    checkRange(server.physical.imageObject.height, 146)

    for i in range(2):
        server.physical.zoomOut()
    checkRange(server.physical.imageObject.width, 206)
    checkRange(server.physical.imageObject.height, 48)
    
    server.physical.zoomOut()
    checkRange(server.physical.imageObject.width, 154)
    checkRange(server.physical.imageObject.height, 36)

    server.physical.zoomOriginal()
    checkRange(server.physical.imageObject.width, 309)
    checkRange(server.physical.imageObject.height, 73)

def checkRange(size, x):
    if size in range(x-15, x+15):
        test.passes("")
    else:
        test.fail("")


def checkCustomizeIconButtons():
    server.physical.customizeIconInPhysicalViewButton()
    clickButton(waitForObject(":CBaseDeviceWidgetClass.CBaseCustomImage.m_okButton"))
    
    server.physical.customizeIconInLogicalViewButton() 
    clickButton(waitForObject(":CBaseDeviceWidgetClass.Customize Images in Logical and Physical View.m_okButton")) # the object name changes time by time. 
