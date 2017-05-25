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
hum = MCU('Humidifier', 422, 409, 'IoE2')
sensor = MCU('Humidity Sensor', 431, 266, 'IoT0')
pc = PC(ComponentBoxConst.DeviceModel.PC, 72, 405, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('humidifier_and_monitor.pkt')
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
    sensor.select()
    sensor.clickTab('Programming')
    sensor.programming.selectScript('Humidity Monitor', 'main')
    sensor.programming.insertTextAtLine(40, '\tSerial.println(newLevel);')
    #sensor.programming.insertAfter('function setLevel(newLevel)\n{\n', '\tSerial.println(newLevel);')
    sensor.programming.stop()
    sensor.programming.run()
    for i in range(5):
        util.speedUpConvergence()
    check(str(sensor.programming.getConsoleOutput()).splitlines()[-1] <= '75')
    
    
def checkRegistrationServer():
    pc.select()
    snooze(1)
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE2')    
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE1')    
    snooze(2)
    
    button = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE2', 1, 1)
    
    util.click(button)
    snooze(15)
    value = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE1', 1, 1)
    test.log(value.innerText)
    check(float(value.innerText) > 90)
    
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
