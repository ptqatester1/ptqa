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

led = MCU('LED', 57, 294, 'IoE3')
tripwire = MCU('Trip Wire', 372, 298, 'IoE2')
sensor = MCU('Trip Sensor', 396, 205, 'IoE1')
light = MCU('Light', 59, 170, 'IoT0')
pc = PC(ComponentBoxConst.DeviceModel.PC, 415, 110, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('trip_sensor.pkt')
    checkSensor()
    checkTripwire()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def checkSensor():
    light.select()
    light.clickTab('Programming')
    light.programming.selectScript('Light', 'main')
    light.programming.insertTextAtLine(72, '\tSerial.println(state);')
    #light.programming.insertAfter('state = newState;\n', '\tSerial.println(state);')
    light.programming.stop()
    light.programming.run()
    light.programming.clearOutputs()
    light.close()
    
    sensor.deviceInteraction()
    snooze(2)
    
    light.select()
    output = light.programming.getConsoleOutput()
    check('2' in output)
    light.close()
    None
    
def checkTripwire():
    led.select()
    led.clickTab('Programming')
    led.programming.selectScript('LED', 'main')
    led.programming.insertTextAtLine(14, '\tSerial.println(input);')
    #led.programming.insertAfter('input = analogRead(0);\n', '\tSerial.println(input);')
    led.programming.stop()
    led.programming.run()
    led.programming.clearOutputs()
    led.close()
    
    tripwire.deviceInteraction()
    snooze(2)
    
    led.select()
    output = led.programming.getConsoleOutput()
    check('1023' in output)
    None
