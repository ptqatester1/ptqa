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

lcd = MCU('LCD', 110, 217, 'IoT0')
flex = MCU('Flex Sensor', 498, 238, 'Flex Sensor')

def main():
    util.init()
    util.maximizePT()
    openfile('flex_sensor.pkt')
    checkSensor()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
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
    
    flex.deviceInteraction()
    
    lcd.select()
    output = lcd.programming.getConsoleOutput().splitlines()
    output = [float(n) for n in output if n != '' and n != '0'][0]
    check(80 < output < 120)
    None
