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
pc = PC(ComponentBoxConst.DeviceModel.PC, 85, 364, 'PC')
therm = MCU('Thermostat', 378, 243, 'IoE5')

def main():
    util.init()
    util.maximizePT()
    openfile('temperature_monitor.pkt')
    checkRegistrationServer()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def checkRegistrationServer():
    pc.select()
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE2')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE5')
    
    heatingButton = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE5', 1, 3)
    util.click(heatingButton)
    snooze(45)
    temp = float(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE2', 1, 1).innerText)
    check(temp == 100)
    
    coolingButton = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE5', 1, 2)
    util.click(coolingButton)
    snooze(30)
    temp = float(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE2', 1, 1).innerText)
    check(temp <= 0)
    None
