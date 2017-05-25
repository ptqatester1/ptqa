########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.HomeGateway import HomeGatewayConst
from API.Device.HomeGateway.HomeGateway import HomeGateway
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase import DeviceBaseConst

util = Util()
hg = HomeGateway(ComponentBoxConst.DeviceModel.HOME_GATEWAY, 175, 80, 'Home Gateway0')

def main():
    util.init()
    create()
    checkPhysicalTab()
    checkGlobalConfig()
    checkIntConfig()
    checkGuiTab()
    
def create():    
    hg.create()
    hg.select()
    
def checkPhysicalTab():
    hg.physical.checkModuleText("")

    checkRange(hg.physical.imageObject.width, 250)
    checkRange(hg.physical.imageObject.height, 296)

    hg.physical.zoomIn()
    checkRange(hg.physical.imageObject.width, 500)
    checkRange(hg.physical.imageObject.height, 592)

    for i in range(2):
        hg.physical.zoomOut()
    checkRange(hg.physical.imageObject.width, 166)
    checkRange(hg.physical.imageObject.height, 197)
    
    hg.physical.zoomOut()
    checkRange(hg.physical.imageObject.width, 125)
    checkRange(hg.physical.imageObject.height, 148)

    hg.physical.zoomOriginal()
    checkRange(hg.physical.imageObject.width, 250)
    checkRange(hg.physical.imageObject.height, 296)

def checkGlobalConfig():
    hg.clickConfigTab()
    hg.config.settings.check.displayName("Home Gateway0")
    hg.config.settings.displayName('HG')
    hg.config.settings.check.displayName("HG")

    hg.config.selectInterface('Algorithm Settings')
    hg.config.algorithmSettings.check.globalSettings(True)
    hg.config.algorithmSettings.check.halfOpenSessionMultiplier(None, property='enabled', value=False)
    hg.config.algorithmSettings.check.halfOpenSessionMultiplier('1')
    hg.config.algorithmSettings.check.maxConnections(None, property='enabled', value=False)
    hg.config.algorithmSettings.check.maxConnections('100')
    hg.config.algorithmSettings.check.maxOpen(None, property='enabled', value=False)
    hg.config.algorithmSettings.check.maxOpen('1000')
    hg.config.algorithmSettings.check.maxRetransmission(None, property='enabled', value=False)
    hg.config.algorithmSettings.check.maxRetransmission('1000')
    
    hg.config.algorithmSettings.globalSettings(None)
    hg.config.algorithmSettings.halfOpenSessionMultiplier('2')
    hg.config.algorithmSettings.maxConnections('50')
    hg.config.algorithmSettings.maxOpen('1500')
    hg.config.algorithmSettings.maxRetransmission('1500')
    
    hg.config.algorithmSettings.check.globalSettings(False)
    hg.config.algorithmSettings.check.halfOpenSessionMultiplier('2')
    hg.config.algorithmSettings.check.maxConnections('50')
    hg.config.algorithmSettings.check.maxOpen('1500')
    hg.config.algorithmSettings.check.maxRetransmission('1500')
    

def checkIntConfig():
    hg.config.selectInterface('Internet')
    hg.config.interface.internet.check.dhcp(True)
    hg.config.interface.internet.check.static(False)
    hg.config.interface.internet.check.ip('')
    hg.config.interface.internet.check.gateway('')
    hg.config.interface.internet.check.subnet('')
    hg.config.interface.internet.check.dns('')
    
    hg.config.interface.internet.static()
    hg.config.interface.internet.setInternetAddress('1.1.1.1', '255.0.0.0')
    
    hg.config.interface.internet.check.ip('1.1.1.1')
    hg.config.interface.internet.check.gateway('')
    hg.config.interface.internet.check.subnet('255.0.0.0')
    hg.config.interface.internet.check.dns('')
    
    
    hg.config.selectInterface('LAN')
    hg.config.interface.lan.check.ip('192.168.25.1')
    hg.config.interface.lan.check.subnet('255.255.255.0')
    
    hg.config.selectInterface('Wireless')
    hg.config.interface.wireless.check.ssid('HomeGateway')
    hg.config.interface.wireless.check.channel('6')
    hg.config.interface.wireless.check.disabled(True)
    hg.config.interface.wireless.check.wep(False)
    hg.config.interface.wireless.check.wpa(False)
    hg.config.interface.wireless.check.wpa2(False)
    hg.config.interface.wireless.check.wpapsk(False)
    hg.config.interface.wireless.check.wpa2psk(False)
    hg.config.interface.wireless.check.wepkey('')
    hg.config.interface.wireless.check.pskPassPhrase('')
    hg.config.interface.wireless.check.ipAddress('')
    hg.config.interface.wireless.check.sharedSecret('')
    hg.config.interface.wireless.check.encryption('Disabled')
    
    hg.config.interface.wireless.wep()
    hg.config.interface.wireless.wepkey("1234567890")
    hg.config.interface.wireless.wpapsk()
    hg.config.interface.wireless.wpa2psk()
    hg.config.interface.wireless.pskPassPhrase("qwertyuiop")
    hg.config.interface.wireless.wpa()
    hg.config.interface.wireless.wpa2()
    hg.config.interface.wireless.ipAddress('1.1.1.1')
    hg.config.interface.wireless.sharedSecret('secretSecret')
    hg.config.interface.wireless.encryption('TKIP')
    
def checkGuiTab():
    hg.clickGuiTab()
    hg.gui.check.httpOn(True)
    hg.gui.check.httpOff(False)
    hg.gui.check.httpsOn(True)
    hg.gui.check.httpsOff(False)
    hg.gui.selectFile('index.php')

def checkRange(size, x):
    if size in range(x-15, x+15):
        test.passes("")
    else:
        test.fail("")