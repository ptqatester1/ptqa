##Chris Allen

from API.Utility.Util import Util
from API.MenuBar.File.Open.Open import Open
from API.functions import trace
from API.Device.Ioe.SBC import SBC
from API.Device.Ioe.MCU import MCU
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch
from API.Device.EndDevice.PC.PC import PC
from API.ComponentBox import ComponentBoxConst
from API import functions

util = Util()
sbc = SBC('SBC-PT', 130, 155, 'Custom SBC')
iot1 = MCU('Appliance', 76, 244, 'IoT1')
iot2 = MCU('Appliance', 579, 406, 'IoT2')
iot3 = MCU('Appliance', 808, 159, 'IoT3')
ioe1 = MCU('Switch', 183, 258, 'IoE1')
se = Server(ComponentBoxConst.DeviceModel.SERVER, 270, 225, 'Server0')
sw = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 395, 255, 'Switch0')
pc = PC(ComponentBoxConst.DeviceModel.PC, 428, 433, 'PC0')

def main():
    util.init()
    openfile('appliance.pkt')
    util.maximizePT()
    addDebugInformationToIoeDevices()
    togglePower()
    checkDeviceOn(iot1)
    checkDeviceOn(iot2)
    checkDeviceOn(iot3)
    togglePower()
    checkDeviceOff(iot1)
    checkDeviceOff(iot2)
    checkDeviceOff(iot3)

def openfile(filename):
    path = functions.pathFromOS('IoT/IoE_Devices/' + filename)
    Open().openSamples(path)
    util.speedUpConvergence()

def addDebugInformationToIoeDevices():
    for dev in [iot1, iot2, iot3]:
        dev.select()
        dev.clickProgrammingTab()
        if dev == iot3:
            dev.programming.selectScript('..')
        dev.programming.selectScript('Appliance', 'main')
        dev.programming.insertAfter('setDeviceProperty(getName(), "state", state);\n', '\tSerial.println(state);')
        dev.programming.stop()
        dev.programming.run()
        dev.close()

def togglePower():
    pc.select()
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('IoT2')
    snooze(1)
    pc.desktop.webBrowser.registrationServer.homePage.toggleButton('IoT2')
    pc.close()
    
    iot1.deviceInteraction(1)
    iot3.deviceInteraction(1)

def checkDeviceOn(dev):
    dev.select()
    snooze(1)
    dev.clickProgrammingTab()
    value = dev.programming.getConsoleOutput().splitlines()[-1]
    if float(value) > 0:
        test.passes('Device is on', trace('test.py'))
    else:
        test.fail('Device is off', trace('test.py'))
    dev.close()

def checkDeviceOff(dev):
    dev.select()
    dev.clickProgrammingTab()
    value = dev.programming.getConsoleOutput().splitlines()[-1]
    if not float(value) > 0:
        test.passes('Device is off', trace('test.py'))
    else:
        test.fail('Device is on', trace('test.py'))
    dev.close()