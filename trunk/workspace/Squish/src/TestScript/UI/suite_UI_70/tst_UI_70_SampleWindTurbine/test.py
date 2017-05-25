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

turbine = MCU('Wind Turbine', 113, 406, 'IoE2')
battery = MCU('Battery', 607, 392, 'IoE3')
pc = PC(ComponentBoxConst.DeviceModel.PC, 295, 84, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('wind_turbine.pkt')
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
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE3')
    output0 = float(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE3', 1, 1).innerText)
    snooze(2)
    output1 = float(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE3', 1, 1).innerText)
    snooze(2)
    output2 = float(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE3', 1, 1).innerText)
    snooze(2)
    check(output0 > 0 and output1 > 0 and output2 > 0)
    check(output0 != output1 != output2)
    None
