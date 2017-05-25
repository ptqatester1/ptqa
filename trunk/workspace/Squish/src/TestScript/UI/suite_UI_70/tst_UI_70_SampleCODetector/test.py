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
co = MCU('Atm Pressure', 392, 365, 'IoE2')
pc = PC(ComponentBoxConst.DeviceModel.PC, 84, 375, 'PC0')
car = MCU('Car', 445, 200, 'IoE1')

def main():
    util.init()
    openfile('CO_detector.pkt')
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
    co.select()
    co.clickTab('Programming')
    co.programming.selectScript('..', 'Carbon Monoxide', 'main')
    co.programming.insertTextAtLine(57, '\tSerial.println(level);\n')
    #co.programming.insertAfter('function sendReport()\n{\n', '\tSerial.println(level);\n')
    co.programming.stop()
    co.programming.run()
    util.fastForwardTime()
    output = co.programming.getConsoleOutput()
    check(float(output.splitlines()[-1]) == 0)
    co.close()
    
    car.deviceInteraction()
    util.speedUpConvergence()
    
    co.select()
    output = co.programming.getConsoleOutput()
    check(float(output.splitlines()[-1] > 0))
    co.close()
    
def checkRegistrationServer():
    pc.select()
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')
    value = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 2)
    check(float(value.innerText) > 0)
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))