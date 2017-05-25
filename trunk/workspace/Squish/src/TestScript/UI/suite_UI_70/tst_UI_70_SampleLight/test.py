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

light = MCU('Light', 295, 312, 'IoT0')
mcu = MCU('MCU-PT', 119, 313, 'MCU0')
sensor = MCU('PhotoSensor', 617, 194, 'IoE1')
pc = PC(ComponentBoxConst.DeviceModel.PC, 291, 58, 'PC0')

lastOutput = None
def main():
    util.init()
    util.maximizePT()
    openfile('light-photo_sensor.pkt')
    displayOutputs()
    checkRegistrationServer()
    None
    
def openfile(filename):
    path = '7.0/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    light.select()
    light.clickTab('Programming')
    light.programming.selectScript('..', 'Light', 'main')
    light.programming.insertTextAtLine(69, '\tSerial.println(newState);')
    #light.programming.insertAfter('function setState(newState) {\n', '\tSerial.println(newState);')
    light.programming.stop()
    light.programming.run()
    light.close()
    
    sensor.select()
    sensor.clickTab('Programming')
    sensor.programming.selectScript('..', 'Photo Sensor', 'main')
    sensor.programming.insertTextAtLine(11, '\tSerial.println(value);')
    #sensor.programming.insertAfter('var value = Environment.get(ENVIRONMENT_NAME);\n', '\tSerial.println(value);')
    sensor.programming.stop()
    sensor.programming.run()
    sensor.close()
    
    mcu.select()
    mcu.clickTab('Programming')
    mcu.programming.run()
    for i in range(5):
        util.speedUpConvergence()#Give a chance for the mcu to change the light values a few times
    mcu.programming.stop()
    mcu.close()
    
    light.select()
    outputs = str(light.programming.getConsoleOutput())
    check('0' in outputs and '1' in outputs and '2' in outputs)
    light.close()
    
    sensor.select()
    outputs = str(sensor.programming.getConsoleOutput())
    outputs = outputs.splitlines()[3:]#All numeric outputs
    outputs = list(set(outputs))
    outputs = [float(o) for o in outputs]
    bOffFound = False
    bLowFound = False
    bHighFound = False
    for num in outputs:
        if 0 == num:
            bOffFound = True
        elif 10 <= num <= 12:
            bLowFound = True
        elif 20 <= num <= 22:
            bHighFound = True
    check(bOffFound)
    check(bLowFound)
    check(bHighFound)
    sensor.close()  
    None
    
def checkRegistrationServer():
    pc.select()
    snooze(1)
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('cisco', 'cisco')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')    
    snooze(2)
    
    
    util.click(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 1))
    snooze(2)
    pc.close()
    light.select()
    output = str(light.programming.getConsoleOutput()).splitlines()[-1]
    check(output == '0')
    
    pc.select()
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('cisco', 'cisco')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')    
    snooze(2)
    util.click(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 2))
    snooze(2)
    pc.close()
    
    light.select()
    output = str(light.programming.getConsoleOutput()).splitlines()[-1]
    check(output == '1')
    
    pc.select()
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('cisco', 'cisco')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')    
    snooze(2)
    util.click(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 3))
    snooze(2)
    pc.close()
    
    light.select()
    output = str(light.programming.getConsoleOutput()).splitlines()[-1]
    check(output == '2')
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
