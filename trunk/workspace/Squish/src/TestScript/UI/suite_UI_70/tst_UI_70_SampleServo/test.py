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

pot = MCU('MCU-PT', 241, 169, 'IoT0')
servo = MCU('MCU-PT', 357, 336, 'IoE1')

def main():
    util.init()
    util.maximizePT()
    openfile('servo.pkt')
    displayOutputs()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    servo.select()
    servo.clickTab('Programming')
    servo.programming.selectScript('..', 'Servo', 'main')
    servo.programming.insertTextAtLine(52, '\tSerial.println(angle)\n')
    #servo.programming.insertAfter('setProperty(angle);\n', '\tSerial.println(angle)\n')
    servo.programming.stop()
    servo.programming.run()
    servo.close()
    
    util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x, pot.y, pot.x + 15, pot.y + 5)
    
    servo.select()
    output = str(servo.programming.getConsoleOutput()).splitlines()[-1]
    check(20 < float(output) < 30)
    None
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
