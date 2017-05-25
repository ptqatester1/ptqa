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
sprinkler = MCU('Water Sprinkler', 611, 295, 'IoE4')
level = MCU('Water Level Monitor', 451, 168, 'IoE3')
led = MCU('LED', 208, 524, 'IoE1')
pc = PC(ComponentBoxConst.DeviceModel.PC, 183, 440, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('water_level_monitor.pkt')
    displayOutputs()
    checkLevel()
    checkSensor()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    level.select()
    level.clickTab('Programming')
    #level.programming.selectScript('Water', 'main')
    level.programming.insertTextAtLine(73, '\tSerial.println(level);')
    #level.programming.insertAfter('level = newLevel;\n', '\tSerial.println(level);')
    level.programming.stop()
    level.programming.run()
    level.programming.clearOutputs()
    level.close()
    
    led.select()
    led.clickTab('Programming')
    led.programming.selectScript('LED', 'main')
    led.programming.insertTextAtLine(14, '\tSerial.println(input);')
    #led.programming.insertAfter('input = analogRead(0);\n', '\tSerial.println(input);')
    led.programming.stop()
    led.programming.run()
    led.programming.clearOutputs()
    led.close()

def checkLevel():
    sprinkler.deviceInteraction()
    snooze(5)
    level.select()
    output = level.programming.getConsoleOutput().splitlines()[-1]
    check(float(output) == 1000)
    level.close()
    None

def checkSensor():
    led.select()
    output = led.programming.getConsoleOutput().splitlines()[-1]
    check(float(output) == 1023)
    led.close()
    
    None

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
