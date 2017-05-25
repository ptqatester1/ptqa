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

lcd = MCU('LCD', 400, 172, 'IoT0')
pot = MCU('Potentiometer', 195, 329, 'IoE2')

pc = PC(ComponentBoxConst.DeviceModel.PC, 410, 110, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('sound_frequency_detector.pkt')
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
    lcd.programming.selectScript('LCD', 'main')
    lcd.programming.insertTextAtLine(43, '\tSerial.println(textToDisplay);')
    #lcd.programming.insertAfter('setDeviceProperty(getName(), "text", textToDisplay);\n', '\tSerial.println(textToDisplay);')
    lcd.programming.stop()
    lcd.programming.run()
    lcd.programming.clearOutputs()
    lcd.close()
    
    util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x + 15, pot.y + 5, pot.x + 30, pot.y + 10)
    
    snooze(5)
    
    lcd.select()
    output = lcd.programming.getConsoleOutput().splitlines()[0]
    check(15 < float(output) < 25)
    None
