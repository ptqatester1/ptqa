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
gar = MCU('Garage Door', 323, 214, 'IoT0')
mcu = MCU('MCU-PT', 380, 359, 'Local Door Control')
pc = PC(ComponentBoxConst.DeviceModel.PC, 64, 373, 'PC')

lastOutput = None

def main():
    util.init()
    util.maximizePT()
    openfile('garage_door.pkt')
    displayOutputs()
    checkRegistrationServer()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    gar.select()
    gar.clickTab('Programming')
    gar.programming.selectScript('Garage Door', 'main')
    gar.programming.insertTextAtLine(88, '\tSerial.println(newState);')
    #gar.programming.insertAfter('function setState(newState) {\n', '\tSerial.println(newState);')
    gar.programming.stop()
    gar.programming.run()
    gar.close()
    
    mcu.select()
    mcu.clickTab('Programming')
    mcu.programming.run()
    snooze(5)
    mcu.programming.stop()
    mcu.close()
    
    gar.select()
    output = str(gar.programming.getConsoleOutput())
    check(output.count('0') > 1 and output.count('1') > 1)
    gar.close()
    
    global lastOutput
    lastOutput = output.splitlines()[-1]
    None
    
    
def checkRegistrationServer():
    expectedOutput = abs(toInt(lastOutput) - 1)
    pc.select()
    snooze(1)
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')    
    snooze(2)
    
    button = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 1)
    
    util.click(button)
    snooze(1)
    gar.select()
    snooze(1)
    currentOutput = str(gar.programming.getConsoleOutput()).splitlines()[-1]
    check(currentOutput == str(expectedOutput))
    
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
