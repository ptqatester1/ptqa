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

oldcar = MCU('LCD', 187, 404, 'IoE2')
pc = PC(ComponentBoxConst.DeviceModel.SERVER, 65, 271, '1.1.1.1')

def main():
    util.init()
    util.maximizePT()
    openfile('old_car.pkt')
    checkSensor()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    if object.exists(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX):
        util.clickButton(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX_YES)
    util.speedUpConvergence()

def checkSensor():
    oldcar.deviceInteraction()
    pc.select()
    pc.clickTab('Desktop')
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse('1.1.1.1')
    pc.desktop.webBrowser.registrationServer.loginPage.signIn('cisco', 'cisco')
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('1.1.1.3')
    smokeDetectorObj = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('1.1.1.3', 2, 1)
    initVal = float(smokeDetectorObj.innerText)
    snooze(5)
    newVal = float(smokeDetectorObj.innerText)
    check(initVal < newVal)
    
    pc.minimizeDeviceWindow()
    oldcar.deviceInteraction()
    pc.restoreDeviceWindow()
    
    pc.desktop.webBrowser.registrationServer.homePage.expandItem('1.1.1.2')
    garageObj = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('1.1.1.2', 1, 1)
    util.click(garageObj)
    
    smokeDetectorObj = pc.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject('1.1.1.3', 2, 1)
    initVal = float(smokeDetectorObj.innerText)
    snooze(5)
    newVal = float(smokeDetectorObj.innerText)
    check(initVal > newVal)
    None
