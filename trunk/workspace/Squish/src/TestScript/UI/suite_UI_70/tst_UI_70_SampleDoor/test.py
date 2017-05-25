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

util = Util()
door = MCU('Door', 470, 327, 'IoT0')
pc = PC(ComponentBoxConst.DeviceModel.PC, 142, 350, 'PC')
sbc = SBC('SBC-PT', 457, 174, 'SBC0')
def main():
    util.init()
    openfile('door.pkt')
    checkSbcDoor()
    checkRegistrationServer()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def checkSbcDoor():
    door.select()
    door.clickTab('Programming')
    door.programming.selectScript('..', 'Door', 'main')
    outputs = door.programming.getConsoleOutput()
    check('0,0' in outputs)
    check('0,1' in outputs)
    check('1,0' in outputs)
    check('1,1' in outputs)
    check('can\'t open locked door' in outputs)
    door.close()
    
    sbc.select()
    sbc.clickTab('Programming')
    sbc.programming.selectScript('door', 'main')
    sbc.programming.removeTextAtLines(8, 9, 10, 11, 12, 13)
    sbc.programming.stop()
    sbc.programming.run()
    sbc.programming.stop()
    sbc.close()
    
def checkRegistrationServer():
    pc.select()
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')
    lockButton = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 2, 2)
    util.click(lockButton)
    
    snooze(1)
    
    door.select()
    currentOutput = str(door.programming.getConsoleOutput()).splitlines()[-1]
    check(currentOutput == '0,1')
    
    unlockButton = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 2, 1)
    util.click(unlockButton)
    
    snooze(1)
    
    currentOutput = str(door.programming.getConsoleOutput()).splitlines()[-1]
    check(currentOutput == '0,0')
    
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
