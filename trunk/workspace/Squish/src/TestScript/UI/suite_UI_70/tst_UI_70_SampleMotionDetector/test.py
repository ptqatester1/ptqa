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

detector = MCU('Motion Detector', 506, 242, '1.1.1.2')
sensor = MCU('Motion Sensor', 465, 376, 'IoT0')
mcu = MCU('MCU-PT', 331, 372, 'MCU0')
led = MCU('LED', 141, 380, 'IoE1')
webcam = MCU('Webcam', 270, 254, '1.1.1.3')

def main():
    util.init()
    util.maximizePT()
    openfile('motion_detector.pkt')
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
    led.programming.insertTextAtLine(14, '\tSerial.println(input);')
    #led.programming.insertAfter('input = analogRead(0);\n', '\tSerial.println(input);')
    led.programming.stop()
    led.programming.run()
    led.programming.clearOutputs()
    led.close()
    
    webcam.select()
    webcam.clickTab('Programming')
    webcam.programming.selectScript('Webcam', 'main')
    webcam.programming.insertTextAtLine(95, '\tSerial.println(state);')
    #webcam.programming.insertAfter('state = newState;\n', '\tSerial.println(state);')
    webcam.programming.stop()
    webcam.programming.run()
    webcam.programming.clearOutputs()
    webcam.close()
    
def checkSensor():
    sensor.deviceInteraction(2)
    led.select()
    output = led.programming.getConsoleOutput()
    check('1023' in output)
    led.close()

def checkDetector():
    detector.deviceInteraction(2)
    webcam.select()
    output = webcam.programming.getConsoleOutput()
    check('1' in output)
    webcam.close()
    None
