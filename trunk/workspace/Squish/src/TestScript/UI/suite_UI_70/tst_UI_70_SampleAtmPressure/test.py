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
atm = MCU('Atm Pressure', 325, 235, 'IoT0')
pc = PC(ComponentBoxConst.DeviceModel.PC, 25, 340, 'PC0')

def main():
    util.init()
    openfile('atm_pressure.pkt')
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
    atm.select()
    atm.clickTab('Programming')
    atm.programming.selectScript('Atm', 'main')
    atm.programming.insertAfter('function setLevel(newLevel)\n{\n', '\tSerial.println(newLevel);')
    atm.programming.stop()
    atm.programming.run()
    util.fastForwardTime()
    output = atm.programming.getConsoleOutput()
    check(float(output.splitlines()[-1] > 0))
    atm.close()
    
def checkRegistrationServer():
    pc.select()
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')
    value = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0')
    check(float(value.innerText) > 0)
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))