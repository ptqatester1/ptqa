##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.EndDevice.PC.PC import PC
from API.Device.Router.Router import Router
from API.ComponentBox import ComponentBoxConst
from API import functions

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, 'Server0')
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 100, 100, 'Router0')

def main():
    util.init()
    create()
    checkDefaults()
    configureAAA()
    checkChanges()
    editClientAndUser()
    removeClientsAndUsers()
    
def create():
    s0.create()
    r0.create()
    s0.connect(r0)
    util.fastForwardTime()

def checkDefaults():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('AAA')
    s0.services.aaa.check.on(False)
    s0.services.aaa.check.off(True)
    s0.services.aaa.check.radiusPort('1645')
    s0.services.aaa.networkConfiguration.check.clientName('')
    s0.services.aaa.networkConfiguration.check.clientIp('')
    s0.services.aaa.networkConfiguration.check.secret('')
    s0.services.aaa.networkConfiguration.check.serverType('Radius')
    functions.check(s0.services.aaa.networkConfiguration.clientTable.rowCount == 0)
    s0.services.aaa.networkConfiguration.check.saveButton(property='enabled', value=False)
    s0.services.aaa.networkConfiguration.check.removeButton(property='enabled', value=False)
    s0.services.aaa.userSetup.check.username('')
    s0.services.aaa.userSetup.check.password('')
    functions.check(s0.services.aaa.userSetup.check.userTable.rowCount == 0)
    s0.services.aaa.userSetup.check.saveButton(property='enabled', value=False)
    s0.services.aaa.userSetup.check.removeButton(property='enabled', value=False)
    None

def configureAAA():    
    s0.services.aaa.on()
    s0.services.aaa.networkConfiguration.addClient('test', '1.1.1.1', 'testPass', 'Tacacs')
    s0.services.aaa.networkConfiguration.addClient('test2', '1.1.1.2', 'testPass2', 'Radius')
    s0.services.aaa.userSetup.addUser('tester', 'testerPass')
    s0.services.aaa.userSetup.addUser('tester2', 'tester2Pass')
    
def checkChanges():
    s0.services.aaa.check.on(True)
    s0.services.aaa.check.off(False)
    s0.services.aaa.check.radiusPort('1645')
    s0.services.aaa.networkConfiguration.check.clientName('')
    s0.services.aaa.networkConfiguration.check.clientIp('')
    s0.services.aaa.networkConfiguration.check.secret('')
    s0.services.aaa.networkConfiguration.check.serverType('Radius')
    
    functions.check(s0.services.aaa.networkConfiguration.clientTable.rowCount == 2)
    row0 = s0.services.aaa.networkConfiguration.rowObjectAt(0)
    row1 = s0.services.aaa.networkConfiguration.rowObjectAt(1)
    functions.check(row0.name.text == 'test')
    functions.check(row0.ip.text == '1.1.1.1')
    functions.check(row0.type.text == 'Tacacs')
    functions.check(row0.key.text == 'testPass')
    functions.check(row1.name.text == 'test2')
    functions.check(row1.ip.text == '1.1.1.2')
    functions.check(row1.type.text == 'Radius')
    functions.check(row1.key.text == 'testPass2')
    
    s0.services.aaa.networkConfiguration.check.saveButton(property='enabled', value=False)
    s0.services.aaa.networkConfiguration.check.removeButton(property='enabled', value=False)
    
    s0.services.aaa.userSetup.check.username('')
    s0.services.aaa.userSetup.check.password('')
    
    functions.check(s0.services.aaa.userSetup.userTable.rowCount == 2)
    row0 = s0.services.aaa.userSetup.rowObjectAt(0)
    row1 = s0.services.aaa.userSetup.rowObjectAt(1)
    functions.check(row0.username.text == 'tester')
    functions.check(row0.password.text == 'testerPass')
    functions.check(row1.username.text == 'tester2')
    functions.check(row1.password.text == 'tester2Pass')
    
    s0.services.aaa.userSetup.check.saveButton(property='enabled', value=False)
    s0.services.aaa.userSetup.check.removeButton(property='enabled', value=False)
    
def editClientAndUser():
    s0.services.aaa.networkConfiguration.selectClient('test2')
    s0.services.aaa.networkConfiguration.clientName('newTestName')
    s0.services.aaa.networkConfiguration.saveButton()
    
    s0.services.aaa.userSetup.selectUser('tester2')
    s0.services.aaa.userSetup.username('newUserName')
    s0.services.aaa.userSetup.saveButton()
    
    functions.check(s0.services.aaa.networkConfiguration.clientTable.rowCount == 2)
    row0 = s0.services.aaa.networkConfiguration.rowObjectAt(0)
    row1 = s0.services.aaa.networkConfiguration.rowObjectAt(1)
    functions.check(row0.name.text == 'test')
    functions.check(row0.ip.text == '1.1.1.1')
    functions.check(row0.type.text == 'Tacacs')
    functions.check(row0.key.text == 'testPass')
    functions.check(row1.name.text == 'newTestName')
    functions.check(row1.ip.text == '1.1.1.2')
    functions.check(row1.type.text == 'Radius')
    functions.check(row1.key.text == 'testPass2')
    
    functions.check(s0.services.aaa.userSetup.userTable.rowCount == 2)
    row0 = s0.services.aaa.userSetup.rowObjectAt(0)
    row1 = s0.services.aaa.userSetup.rowObjectAt(1)
    functions.check(row0.username.text == 'tester')
    functions.check(row0.password.text == 'testerPass')
    functions.check(row1.username.text == 'newUserName')
    functions.check(row1.password.text == 'tester2Pass')
    
def removeClientsAndUsers():
    for i in range(2):
        s0.services.aaa.networkConfiguration.selectRow(0)
        s0.services.aaa.networkConfiguration.removeButton()
    for i in range(2):
        s0.services.aaa.userSetup.selectRow(0)
        s0.services.aaa.userSetup.removeButton()
    functions.check(s0.services.aaa.networkConfiguration.clientTable.rowCount == 0)
    functions.check(s0.services.aaa.userSetup.userTable.rowCount == 0)