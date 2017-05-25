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

lcd = MCU('LCD', 108, 178, 'IoE2')
membrane = MCU('Membrane Potentiometer', 548, 171, 'IoE3')

def main():
    util.init()
    util.maximizePT()
    openfile('membrane_sensor.pkt')
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
    lcd.select()
    lcd.clickTab('Programming')
    lcd.programming.selectScript('..', 'LCD', 'main')
    lcd.programming.insertTextAtLine(43, '\tSerial.println(textToDisplay);')
    lcd.programming.insertAfter('setDeviceProperty(getName(), "text", textToDisplay);\n', '\tSerial.println(textToDisplay);')
    lcd.programming.stop()
    lcd.programming.run()
    lcd.programming.clearOutputs()
    lcd.close()
    
    membrane.deviceInteraction(1)
    
    lcd.select()
    output = lcd.programming.getConsoleOutput().splitlines()[0]
    check(80 < float(output) < 120)
    None
