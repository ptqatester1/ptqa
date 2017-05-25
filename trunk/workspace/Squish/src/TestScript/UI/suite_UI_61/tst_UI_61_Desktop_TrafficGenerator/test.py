##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.EndDevice.PC.PC import PC

from API.Device.Switch.Switch import Switch

from API.ComponentBox import ComponentBoxConst
import time
util = Util()

sw = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 100, 200, 'Switch0')
s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 100, 100, 'Server0')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 300, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 200, 300, 'PC1')
p2 = PC(ComponentBoxConst.DeviceModel.PC, 300, 300, 'PC2')

protocols = {'DNS': 53, 'FINGER': 79, 'FTP': 21, 'HTTP': 80,
             'HTTPS': 443, 'IMAP': 143, 'NETBIOS': 137, 'PING': None,
             'POP3': 110, 'SFTP': 115, 'SMTP': 25, 'SNMP': 161, 'SSH': 22,
             'TELNET': 23, 'TFTP': 69, 'OTHER': ''}
def main():
    util.init()
    create()
    addressDevices()
    start = time.time()
    checkDefaults(p0)
    checkDefaults(s0)
    
def create():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, s0.model, s0.x, s0.y)
    util.createDevice(ComponentBoxConst.DeviceType.SWITCH, sw.model, sw.x, sw.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, p0.model, p0.x, p0.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, p1.model, p1.x, p1.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, p2.model, p2.x, p2.y)
    for dev in [s0, p0, p1, p2]:
        util.connect(sw.x, sw.y, dev.x, dev.y, ComponentBoxConst.Connection.CONN_AUTO, '', '')
    util.fastForwardTime()
    
def addressDevices():
    for i, device in enumerate([p0, p1, p2]):
        util.clickOnWorkspace(device.x, device.y)
        device.updateName()
        device.clickDesktopTab()
        device.desktop.applications.ipConfiguration()
        device.desktop.ipConfiguration.setIPConfiguration('1.1.1.' + str(i+1), '255.255.255.0', '', '')
        device.close()
    util.clickOnWorkspace(s0.x, s0.y)
    s0.updateName()
    s0.clickDesktopTab()
    s0.desktop.applications.ipConfiguration()
    s0.desktop.ipConfiguration.setIPConfiguration('1.1.1.4', '255.255.255.0', '')
    s0.close()
    
def checkDefaults(dev):
    dev.select()
    dev.clickDesktopTab()
    dev.desktop.applications.trafficGenerator()
    for key, val in protocols.items():
        p0.desktop.trafficGenerator.pduSettings.selectApplication(key)
        p0.desktop.trafficGenerator.sourceSettings.check.autoSelectPort(False)
        p0.desktop.trafficGenerator.pduSettings.check.application(key)
        p0.desktop.trafficGenerator.pduSettings.check.destinationIp('')
        p0.desktop.trafficGenerator.pduSettings.check.sourceIp('')
        p0.desktop.trafficGenerator.pduSettings.check.ttl('32')
        p0.desktop.trafficGenerator.pduSettings.check.tos('0')
        if key == 'PING':
            p0.desktop.trafficGenerator.pduSettings.check.sequenceNumber('')
        else:
            p0.desktop.trafficGenerator.pduSettings.check.sourcePort('')
            p0.desktop.trafficGenerator.pduSettings.check.destinationPort(str(val))
        p0.desktop.trafficGenerator.pduSettings.check.size('0')
        p0.desktop.trafficGenerator.simulationSettings.check.singleShot(True)
        p0.desktop.trafficGenerator.simulationSettings.check.periodic(False)
        p0.desktop.trafficGenerator.simulationSettings.check.interval('')
        
    