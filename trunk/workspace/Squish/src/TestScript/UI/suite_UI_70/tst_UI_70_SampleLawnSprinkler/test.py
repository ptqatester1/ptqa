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
sprinkler = MCU('IoE0', 396, 224, 'IoE1')
mcu = MCU('MCU-PT', 597, 182, 'Controller')
pc = PC(ComponentBoxConst.DeviceModel.PC, 70, 313, 'PC')
lastOutput = None
def main():
    util.init()
    util.maximizePT()
    openfile('lawn_sprinkler.pkt')
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
    sprinkler.select()
    sprinkler.clickTab('Programming')
    sprinkler.programming.selectScript('Lawn Sprinkler', 'main')
    sprinkler.programming.insertTextAtLine(59, '\tSerial.println(newState);')
    #sprinkler.programming.insertAfter('function setState(newState)\n{\n', '\tSerial.println(newState);')
    sprinkler.programming.stop()
    sprinkler.programming.run()
    
    check(str(sprinkler.programming.getConsoleOutput()).splitlines()[-1] == '0')
    
    mcu.select()
    mcu.clickTab('Programming')
    mcu.programming.run()
    snooze(5)
    mcu.programming.stop()
    mcu.close()
    
    sprinkler.select()
    output = str(sprinkler.programming.getConsoleOutput())
    
    check('0' in output and '1' in output)
    
    global lastOutput
    lastOutput = output.splitlines()[-1]
    
def checkRegistrationServer():
    expectedOutput = str(abs(toInt(lastOutput) - 1))
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
    snooze(5)
    
    output = str(sprinkler.programming.getConsoleOutput()).splitlines()[-1]
    check(output == expectedOutput)
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
