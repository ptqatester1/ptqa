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
monitor = MCU('Humiture Monitor', 481, 139, 'IoT0')
sensor = MCU('Humiture Sensor', 470, 290, 'IoE4')
lcd = MCU('LCD', 144, 326, 'IoE1')
pc = PC(ComponentBoxConst.DeviceModel.PC, 101, 224, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('humiture_sensor.pkt')
    displayOutputs()
    for i in range(10):
        util.speedUpConvergence()
    checkSensor()
    checkRegistrationServer()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()
    
def displayOutputs():
    lcd.select()
    lcd.clickTab('Programming')
    lcd.programming.selectScript('LCD', 'main')
    lcd.programming.insertTextAtLine(43, '\t\tSerial.println(textToDisplay);')
    lcd.programming.stop()
    lcd.programming.run()
    lcd.programming.clearOutputs()
    lcd.close()

def checkSensor():
    lcd.select()
    output = lcd.programming.getConsoleOutput()
    output = list(set([float(l) for l in output.splitlines() if not l == '']))
    check(len(output) > 1)
    for item in output:
        check(50 < item < 80)
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
    
    value = float(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 1).innerText)
    snooze(10)
    newValue = float(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 1, 1).innerText)
    
    check(newValue != value)
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
