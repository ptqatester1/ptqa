##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.EndDevice.PC.PC import PC
from API.Device.Switch.Switch import Switch
from API.ComponentBox import ComponentBoxConst
from API import functions

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 100, 100, 'Server0')
sw = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 100, 200, 'Switch0')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 300, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 200, 300, 'PC1')
p2 = PC(ComponentBoxConst.DeviceModel.PC, 300, 300, 'PC2')

def main():
    util.init()
    create()
    addressDevices()
    checkEmailDefaults()
    configureEmail()
    removeUsers()
    
def create():
    s0.create()
    sw.create()
    p0.create()
    p1.create()
    p2.create()
    for dev in [s0, p0, p1, p2]:
        sw.connect(dev)
    util.fastForwardTime()
    
def addressDevices():
    for i, device in enumerate([p0, p1, p2]):
        device.select()
        device.clickDesktopTab()
        device.desktop.applications.ipConfiguration()
        device.desktop.ipConfiguration.setIPConfiguration('1.1.1.' + str(i+1), '255.255.255.0')
        device.close()
    
    s0.select()
    s0.clickDesktopTab()
    s0.desktop.applications.ipConfiguration()
    s0.desktop.ipConfiguration.setIPConfiguration('1.1.1.4', '255.255.255.0')
    s0.close()
    
def checkEmailDefaults():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('EMAIL')
    s0.services.email.check.smtpOn(True)
    s0.services.email.check.smtpOff(False)
    s0.services.email.check.pop3On(True)
    s0.services.email.check.pop3Off(False)
    s0.services.email.check.domainName('')
    s0.services.email.check.setButton(property='enabled', value=True)
    s0.services.email.check.user('')
    s0.services.email.check.password('')
    functions.check(s0.services.email.userTable.count == 0)
    
def configureEmail():
    s0.services.email.domainName('test.com')
    s0.services.email.addUser('pc0', 'pc0Pass')
    s0.services.email.addUser('pc1', 'pc1Pass')
    s0.services.email.addUser('pc2', 'pc2Pass')
    s0.services.email.check.smtpOn(True)
    s0.services.email.check.smtpOff(False)
    s0.services.email.check.pop3On(True)
    s0.services.email.check.pop3Off(False)
    s0.services.email.check.domainName('test.com')
    s0.services.email.check.setButton(property='enabled', value=True)
    s0.services.email.check.user('')
    s0.services.email.check.password('')
    functions.check(s0.services.email.userTable.count == 3)
    functions.check(findObject(s0.services.email.userTableName + '.item_0/0').text  == 'pc0')
    functions.check(findObject(s0.services.email.userTableName + '.item_1/0').text  == 'pc1')
    functions.check(findObject(s0.services.email.userTableName + '.item_2/0').text  == 'pc2')
    
def removeUsers():
    s0.services.email.removeUser('pc1')
    functions.check(s0.services.email.userTable.count == 2)