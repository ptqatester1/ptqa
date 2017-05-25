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

motor = MCU('Motion Sensor', 460, 146, 'IoT0')
pot = MCU('Potentiometer', 140, 161, 'MCU0')

def main():
    util.init()
    util.maximizePT()
    openfile('motor.pkt')
    displayOutputs()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    motor.select()
    motor.clickTab('Programming')
    motor.programming.selectScript('Motor', 'main')
    motor.programming.insertTextAtLine(35, '\n\tSerial.println(rotation);\n')
    #motor.programming.insertAfter('rotation += (rotationToCapacity *(workCapacity/100));', '\n\tSerial.println(rotation);\n')
    motor.programming.stop()
    motor.programming.run()
    motor.close()
    
    util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x, pot.y, pot.x + 10, pot.y - 5)
    
    motor.select()
    output = str(motor.programming.getConsoleOutput()).splitlines()[-2:]
    check(float(output[0]) < float(output[1]))
    None
    

def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
