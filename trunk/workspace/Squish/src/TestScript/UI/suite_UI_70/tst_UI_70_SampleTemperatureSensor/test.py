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
from API.functions import toInt

util = Util()
lcd = MCU('LCD', 352, 223, 'Custom LCD')
temp = MCU('Temperature Monitor', 577, 213, 'IoE8=7')

def main():
    util.init()
    util.maximizePT()
    openfile('temperature_sensor.pkt')
    displayOutputs()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    temp.select()
    temp.clickTab('Programming')
    temp.programming.selectScript('..', 'Temperature Monitor', 'main')
    temp.programming.insertTextAtLine(36, '\tSerial.println(value);\n')
    temp.programming.stop()
    temp.programming.run()
    temp.close()

    lcd.select()
    lcd.clickTab('Programming')
    lcd.programming.selectScript('LCD', 'main')
    lcd.programming.insertTextAtLine(38, '\tSerial.println(text);\n')
    lcd.programming.stop()
    lcd.programming.run()
    lcd.close()
    
    lcd.select()
    temp.select()
    snooze(10)
    for i in range(30):
        val = str(temp.programming.getConsoleOutput()).splitlines()[-1]
        if val != '0':
            break
        snooze(1)
    lcdVal = str(temp.programming.getConsoleOutput()).splitlines()[-1]
    check(float(lcdVal)-1 <= float(val) <= float(lcdVal)+1)
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
