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
from API.functions import toInt, check

util = Util()
car = MCU('Car', 124, 125, 'IoE2')
detector = MCU('Smoke Detector', 243, 125, 'IoT0')
sensor = MCU('Smoke Sensor', 126, 395, 'IoE7')
led = MCU('LED', 458, 376, 'IoE6')
pc = PC(ComponentBoxConst.DeviceModel.PC, 510, 48, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('smoke_detector.pkt')
    displayOutputs()
    activateCar()
    checkRegistrationServer()
    checkDetector()
    checkSensor()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    detector.select()
    detector.clickTab('Programming')
    detector.programming.selectScript('Smoke Detector', 'main')
    detector.programming.insertTextAtLine(76, '\tSerial.println(newState);\n')
    #detector.programming.insertAfter('function setState(newState) {\n', '\tSerial.println(newState);\n')
    detector.programming.stop()
    detector.programming.run()
    detector.programming.clearOutputs()
    detector.close()
    
    led.select()
    led.clickTab('Programming')
    led.programming.selectScript('LED', 'main')
    led.programming.insertTextAtLine(14, '\tSerial.println(input);')
    #led.programming.insertAfter('input = analogRead(0);\n', '\tSerial.println(input);')
    led.programming.stop()
    led.programming.run()
    led.programming.clearOutputs()
    led.close()
    
def activateCar():
    car.deviceInteraction()

def checkRegistrationServer():
    pc.select()
    snooze(1)
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')    
    snooze(2)
    
    value = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 2, 1)
    for i in range(15):
        if float(value.innerText) >= 40:
            break
        snooze(1)
    check(40 < float(value.innerText) < 60)
    pc.close()
    
def checkDetector():
    detector.select()
    output = detector.programming.getConsoleOutput()
    check('1\n' in output)
    detector.close()
    None

def checkSensor():
    led.select()
    output = led.programming.getConsoleOutput()
    check('1023' in output)
    led.close()
