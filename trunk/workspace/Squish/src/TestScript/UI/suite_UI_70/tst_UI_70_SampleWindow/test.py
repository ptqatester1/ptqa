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

co = MCU('Carbon Monoxide', 370, 321, 'IoE1')
co2 = MCU('Carbon Dioxide', 397, 151, 'IoT0')
window = MCU('Window', 242, 85, 'IoE2')
stove = MCU('Stove', 593, 68, 'Stove')
switch = MCU('Rocker Switch', 574, 249, 'IoE6')
pc = PC(ComponentBoxConst.DeviceModel.PC, 74, 395, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('window.pkt')
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
    snooze(3)
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT0')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE1')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE2')
    
    covals = []
    co2vals = []
    co2vals.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 2, 1).innerText)
    covals.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE1', 2, 1).innerText)
    pc.minimizeDeviceWindow()
    switch.deviceInteraction()
    pc.restoreWindow()
    for i in range(10):
        snooze(1)
        co2vals.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 2, 1).innerText)
        covals.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE1', 2, 1).innerText)
    switch.deviceInteraction()
    
    startVal = -1
    for val in covals:
        check(startVal <= float(val))
        startVal = float(val)
    startVal = -1
    for val in co2vals:
        check(startVal <= float(val))
        startVal = float(val)
    check(float(covals[-1]) > 0)
    check(float(co2vals[-1]) > 0)
    
    pc.minimizeDeviceWindow()
    switch.deviceInteraction()
    pc.restoreWindow()
    
    windowButton = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE2', 1, 1)
    util.click(windowButton)
    
    covals = []
    co2vals = []
    co2vals.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 2, 1).innerText)
    covals.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE1', 2, 1).innerText)
    for i in range(10):
        snooze(1)
        co2vals.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoT0', 2, 1).innerText)
        covals.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE1', 2, 1).innerText)
    
    startVal = 100
    for val in covals:
        check(startVal >= float(val))
        startVal = float(val)
    startVal = 100
    for val in co2vals:
        check(startVal >= float(val))
        startVal = float(val)
    check(float(covals[-1]) < 7)
    check(float(co2vals[-1]) < 14)
    None
