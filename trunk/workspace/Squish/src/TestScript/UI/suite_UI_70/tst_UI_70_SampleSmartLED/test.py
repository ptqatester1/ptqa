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
pot = MCU('Humidifier', 508, 262, 'IoE2')
led = MCU('Smart LED', 346, 264, 'IoE3')
pc = PC(ComponentBoxConst.DeviceModel.PC, 90, 339, 'PC')
lastOutput = None
def main():
    util.init()
    util.maximizePT()
    openfile('smart_LED.pkt')
    displayOutputs()
    checkRegistrationServer()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    if object.exists(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX):
        util.clickButton(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX_YES)
    util.speedUpConvergence()

def displayOutputs():
    led.select()
    led.clickTab('Programming')
    led.programming.selectScript('..', 'Smart LED', 'main')
    led.programming.insertTextAtLine(24, '\tSerial.println(input);\n')
    #led.programming.insertAfter('input = analogRead(A0);\n', '\tSerial.println(input);\n')
    led.programming.stop()
    led.programming.run()
    led.close()
    
    util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x, pot.y, pot.x + 15, pot.y + 5)
    
    led.select()
    output = str(led.programming.getConsoleOutput()).splitlines()[-1]
    check(250 < float(output) < 275)
    None
    
def checkRegistrationServer():
    pc.select()
    snooze(1)
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')    
    snooze(2)
    
    value = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 1)
    
    check(250 < float(value.innerText) < 275)
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
