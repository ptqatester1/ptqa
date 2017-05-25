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
fan = MCU('Fan', 364, 204, 'IoE2')
pc = PC(ComponentBoxConst.DeviceModel.PC, 76, 256, 'PC')
sbc = SBC('SBC-PT', 480, 103, 'SBC0')
switch = MCU('Switch', 507, 266, 'IoE1')
def main():
    util.init()
    util.maximizePT()
    openfile('fan.pkt')
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
    fan.select()
    fan.clickTab('Programming')
    fan.programming.selectScript('Ceiling Fan', 'main')
    fan.programming.insertTextAtLine(70, '\tSerial.println(state);')
    #fan.programming.insertAfter('function sendReport()\n{\n', '\tSerial.println(state);')
    fan.programming.stop()
    fan.programming.run()
    fan.close()
    
    snooze(1)
    switch.deviceInteraction(1)
    
    fan.select()
    check(str(fan.programming.getConsoleOutput()).splitlines()[-1] == '2')
    fan.close()
    
    switch.deviceInteraction(1)
    
    fan.select()
    check(str(fan.programming.getConsoleOutput()).splitlines()[-1] == '0')
    fan.close()
    
    fan.deviceInteraction(1)
    
    fan.select()
    check(str(fan.programming.getConsoleOutput()).splitlines()[-1] == '1')
    
    
def checkRegistrationServer():
    pc.select()
    snooze(1)
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')    
    snooze(2)
    
    #offButton = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE2', 1, 1)
    #lowButton = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE2', 1, 2)
    #highButton = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE2', 1, 3)
    
    util.click(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 1))
    snooze(1)
    currentOutput = str(fan.programming.getConsoleOutput()).splitlines()[-1]
    check(currentOutput == '0')
    
    util.click(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 2))
    snooze(1)
    currentOutput = str(fan.programming.getConsoleOutput()).splitlines()[-1]
    check(currentOutput == '1')
    
    util.click(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 3))
    snooze(1)
    currentOutput = str(fan.programming.getConsoleOutput()).splitlines()[-1]
    check(currentOutput == '2')
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
