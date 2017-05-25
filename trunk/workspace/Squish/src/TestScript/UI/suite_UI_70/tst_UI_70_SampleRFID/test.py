##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.Open import Open
from API.functions import trace
import os
from API.Device.Ioe.SBC import SBC
from API.Device.Ioe.MCU import MCU
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch
from API.Device.EndDevice.PC.PC import PC
from API.ComponentBox import ComponentBoxConst
from API.functions import toInt

util = Util()

valid = MCU('RFID Card', 61, 316, 'Valid Card')
invalid = MCU('RFID Card', 56, 448, 'Invalid Card')
reader = MCU('RFID Reader', 171, 207, 'RFID Reader')
pc = PC(ComponentBoxConst.DeviceModel.PC, 60, 142, 'PC0')

lastOutput = None
def main():
    util.init()
    util.maximizePT()
    openfile('rfid_reader.pkt')
    displayOutputs()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    util.dragAndDrop(UtilConst.WORKSPACE, valid.x, valid.y, UtilConst.WORKSPACE, reader.x, reader.y - 25)
    
    pc.select()
    snooze(1)
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.0.0.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('Reader')    
    snooze(2)
    output = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('Reader', 1, 1)
    check('1001' in str(output.innerText))
    
    util.dragAndDrop(UtilConst.WORKSPACE, reader.x, reader.y - 25, UtilConst.WORKSPACE, valid.x, valid.y)
    snooze(1)
    util.dragAndDrop(UtilConst.WORKSPACE, invalid.x, invalid.y, UtilConst.WORKSPACE, reader.x, reader.y - 25)
    
    pc.select()
    snooze(1)
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    snooze(2)
    pc.desktop.webBrowser.browse('1.0.0.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('Reader')    
    snooze(2)
    output = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('Reader', 1, 1)
    check('2001' in str(output.innerText))
    None
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
