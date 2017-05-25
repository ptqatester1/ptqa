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

siren = MCU('Siren', 105, 184, 'IoT0')
trip = MCU('Trip Sensor', 384, 181, 'IoE1')
pc = PC(ComponentBoxConst.DeviceModel.PC, 405, 105, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('siren.pkt')
    checkSiren()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    if object.exists(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX):
        util.clickButton(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX_YES)
    util.speedUpConvergence()

def checkSiren():
    siren.select()
    siren.clickTab('Programming')
    siren.programming.selectScript('Siren', 'main')
    siren.programming.insertTextAtLine(38, '\tSerial.println(state);')
    siren.programming.stop()
    siren.programming.run()
    siren.programming.clearOutputs()
    siren.close()
    
    trip.deviceInteraction()
    
    siren.select()
    output = siren.programming.getConsoleOutput().splitlines()[-1]
    check(float(output) == 1)
    siren.close()
    
    trip.y = trip.y + 15
    trip.deviceInteraction()
        
    pc.select()
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('Siren')
    sirenButton = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('Siren', 1, 1)
    util.click(sirenButton)
    snooze(1)
    pc.close()
    
    siren.select()
    output = siren.programming.getConsoleOutput().splitlines()[-1]
    check(float(output) == 0)
    siren.close()
    None
