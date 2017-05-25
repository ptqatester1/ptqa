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
co2 = MCU('Atm Pressure', 480, 320, 'IoE1')
pc = PC(ComponentBoxConst.DeviceModel.PC, 140, 355, 'PC0')
car = MCU('Car', 490, 120, 'IoT0')

def main():
    util.init()
    openfile('CO2_detector.pkt')
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
    co2.select()
    co2.clickTab('Programming')
    co2.programming.selectScript('Carbon Dioxide', 'main')
    co2.programming.insertTextAtLine(56, '\tSerial.println(level);\n')
    #co2.programming.insertAfter('function sendReport()\n{\n', '\tSerial.println(level);\n')
    co2.programming.stop()
    co2.programming.run()
    util.fastForwardTime()
    output = co2.programming.getConsoleOutput()
    check(float(output.splitlines()[-1]) < 1)
    co2.close()
    
    car.deviceInteraction()
    util.speedUpConvergence()
    
    co2.select()
    output = co2.programming.getConsoleOutput()
    check(float(output.splitlines()[-1] > 0))
    co2.close()
    
def checkRegistrationServer():
    pc.select()
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE1')
    value = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE1', 2)
    check(float(value.innerText) > 1)
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))