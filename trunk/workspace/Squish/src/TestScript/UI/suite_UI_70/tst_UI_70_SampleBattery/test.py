##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Ioe.MCU import MCU
from API.Device.Ioe.MCUConst import MCUConst
from API.MenuBar.File.Open.Open import Open
from API.Device.EndDevice.PC.PC import PC

from API.Device.EndDevice.Server.Server import Server

from API.functions import toInt, check, pathFromOS
from API.ComponentBox import ComponentBoxConst

util = Util()

pc = PC(ComponentBoxConst.DeviceModel.PC, 260, 230, 'PC0')
server = Server(ComponentBoxConst.DeviceModel.SERVER, 475, 240, 'Server0')
battery = MCU('Battery', 555, 335, 'IoE3')
power = MCU('Power Meter', 285, 445, 'IoE2')
solar = MCU('Solar Panel', 55, 340, 'IoE1')
leds = [MCU('LED', 730, 210, 'Custom LED 1'),
        MCU('LED', 805, 310, 'Custom LED 2'),
        MCU('LED', 790, 415, 'Custom LED 3'),
        MCU('LED', 685, 485, 'Custom LED 4')]

def main():
    util.init()
    Open().openSamples(pathFromOS('IoT/IoE_Devices/battery-solar_panel-power_meter.pkt'))
    util.speedUpConvergence()
    addOutputDisplay()
    util.speedUpConvergence()
    checkDeviceOutputChanging()
    checkDevicesOnRegistrationServer()
    
def addOutputDisplay():
    solar.select()
    solar.clickTab('Programming')
    solar.programming.selectScript('main')
    solar.programming.insertTextAtLine(49, '\t\tSerial.println(electricity);')
    #solar.programming.insertAfter is not working for this script. Unable to figure out why -Chris
    #solar.programming.insertAfter('electricity = Math.round(getElectricityProduction());', 'Serial.println(electricity);')
    solar.programming.stop()
    solar.programming.run()
    solar.programming.clearOutputs()
    solar.close()
    
    power.select()
    power.clickTab('Programming')
    power.programming.selectScript('main')
    power.programming.insertTextAtLine(42, '\tSerial.println(makeDisplayText(electricity));')
    power.programming.stop()
    power.programming.run()
    power.programming.clearOutputs()
    power.close()
    
    battery.select()
    battery.clickTab('Programming')
    battery.programming.selectScript('main')
    battery.programming.insertTextAtLine(77, '\n\tSerial.println(availablePower);')
    battery.programming.stop()
    battery.programming.run()
    battery.programming.clearOutputs()
    battery.close()
    
    for led in leds:
        led.select()
        led.clickTab('Programming')
        led.programming.selectScript('main')
        led.programming.insertTextAtLine(14, '\tSerial.println(input);')
        led.programming.stop()
        led.programming.run()
        led.programming.clearOutputs()
        led.close()
    None
    
def checkDeviceOutputChanging():
    for device in [solar, power, battery]:
        device.select()
        output = str(device.programming.getConsoleOutput())
        output = output.splitlines()
        if device is battery:
            check(len(list(set(output))) > 2)
        else:
            check(len(list(set(output))) > 1)
        device.close()
    None
    
def checkDevicesOnRegistrationServer():
    pc.select()
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.0.0.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE1')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE2')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoE3')
    ioe1 = []
    ioe2 = []
    ioe3 = []
    for i in range(15):
        ioe1.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE1', 0).innerText)
        ioe2.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE2', 0).innerText)
        ioe3.append(pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('IoE3', 0).innerText)
    ioe1 = list(set(ioe1))
    ioe2 = list(set(ioe2))
    ioe3 = list(set(ioe3))
    check(len(ioe1) > 1)
    check(len(ioe2) > 1)
    check(len(ioe3) > 1)
    None