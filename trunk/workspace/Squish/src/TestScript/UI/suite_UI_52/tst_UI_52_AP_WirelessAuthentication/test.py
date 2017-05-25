##Chris Allen

from API.Utility.Util import Util
from API.Device.EndDevice.PC.PC import PC
from API.Device.AccessPoint.AccessPoint import AccessPoint
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.ComponentBox import ComponentBoxConst

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 100, 100, 'PC0')
pc1 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 300, 100, 'PC0')

ap0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 200, 200, 'Access Point0')
ap1 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT_A, 200, 200, 'Access Point1')
ap2 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT_N, 200, 200, 'Access Point2')

def main():
    util.init()
    createDevices()
    configureIps()
    for ap in [ap0, ap1, ap2]:
        ap.create()
        disabled()
        wep(ap)
        wpa(ap)
        wpa2(ap)
        ap.delete()

def createDevices():
    pc0.create()
    pc1.create()

def configureIps():
    for i, pc in enumerate([pc0, pc1]):
        pc.select()
        pc.clickDesktopTab()
        pc.desktop.applications.ipConfiguration()
        pc.desktop.ipConfiguration.setIPConfiguration('1.1.1.%s'%(i+1,), '255.255.255.0')
        pc.close()

def disabled():
    for pc in [pc0, pc1]:
        pc.select()
        pc.clickConfigTab()
        pc.config.selectInterface('Wireless0')
        pc.config.interface.wireless.disabled()
        pc.close()
    util.speedUpConvergence()
    checkPing(success=True)

def wep(ap):
    ap.select()
    ap.clickConfigTab()
    ap.config.selectInterface('Port 1')
    ap.config.interface.port1.wep()
    ap.config.interface.port1.wepkey('0123456789')
    ap.close()
    
    util.speedUpConvergence()
    checkPing(success=False)
    
    for pc in [pc0, pc1]:
        pc.select()
        pc.clickConfigTab()
        pc.config.selectInterface('Wireless0')
        pc.config.interface.wireless.wep()
        pc.config.interface.wireless.wepkey('0123456789')
        pc.close()
        
    util.speedUpConvergence()
    checkPing(success=True)

def wpa(ap):
    ap.select()
    ap.clickConfigTab()
    ap.config.selectInterface('Port 1')
    ap.config.interface.port1.wpapsk()
    ap.config.interface.port1.pskPassPhrase('testPassPhrase')
    ap.close()
    
    util.speedUpConvergence()
    checkPing(success=False)
    
    for pc in [pc0, pc1]:
        pc.select()
        pc.clickConfigTab()
        pc.config.selectInterface('Wireless0')
        pc.config.interface.wireless.wpapsk()
        pc.config.interface.wireless.pskPassPhrase('testPassPhrase')
        pc.close()
        
    util.speedUpConvergence()
    checkPing(success=True)

def wpa2(ap):
    ap.select()
    ap.clickConfigTab()
    ap.config.selectInterface('Port 1')
    ap.config.interface.port1.wpa2psk()
    ap.config.interface.port1.pskPassPhrase('testPassPhrase')
    ap.close()
    
    util.speedUpConvergence()
    checkPing(success=False)
    
    for pc in [pc0, pc1]:
        pc.select()
        pc.clickConfigTab()
        pc.config.selectInterface('Wireless0')
        pc.config.interface.wireless.wpa2psk()
        pc.config.interface.wireless.pskPassPhrase('testPassPhrase')
        pc.close()
        
    util.speedUpConvergence()
    checkPing(success=True)
    
def checkPing(success=True):
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText('ping 1.1.1.2')
    util.speedUpConvergence()
    if success:
        pc0.desktop.commandPrompt.textCheckPoint('Received = [1234]', lines=5)
    else:
        pc0.desktop.commandPrompt.textCheckPoint('Received = 0', lines=5)
    pc0.close()
    