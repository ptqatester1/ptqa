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

led = MCU('LED', 449, 139, 'IoE2')
detector = MCU('Wind Detector', 241, 297, 'IoT0')
pc = PC(ComponentBoxConst.DeviceModel.PC, 113, 492, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('wind_sensor.pkt')
    displayOutputs()
    checkSensor()
    checkDetector()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    led.select()
    led.clickTab('Programming')
    led.programming.selectScript('LED', 'main')
    led.programming.insertTextAtLine(14, '\tSerial.println(input);\n')
    #led.programming.insertAfter('input = analogRead(0);\n', '\tSerial.println(input);\n')
    led.programming.stop()
    led.programming.run()
    led.programming.clearOutputs()
    led.close()
    
    detector.select()
    detector.clickTab('Programming')
    detector.programming.selectScript('..', 'Wind Detector', 'main')
    detector.programming.insertTextAtLine(75, '\tSerial.println(state);')
    #detector.programming.insertAfter('state = newState;\n', '\tSerial.println(state);')
    detector.programming.stop()
    detector.programming.run()
    detector.programming.clearOutputs()
    detector.close()
    
def checkSensor():
    util.speedUpConvergence()
    led.select()
    output = str(led.programming.getConsoleOutput())
    check('1023' in output)
    led.close()
    
def checkDetector():
    detector.select()
    output = detector.programming.getConsoleOutput()
    check('1\n' in output)
    detector.close()
    None
