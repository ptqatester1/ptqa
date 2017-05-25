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

pot = MCU('MCU-PT', 542, 223, 'Blue')
led = MCU('MCU-PT', 413, 113, 'IoE2')

def main():
    util.init()
    util.maximizePT()
    openfile('rgb_led.pkt')
    displayOutputs()
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
    led.programming.selectScript('..', 'RGB LED', 'main')
    led.programming.insertTextAtLine(25, '\tSerial.println(blue)\n')
    #led.programming.insertAfter('blue = Math.round(analogRead(bluePin) * MULTIPLIER);\n', '\tSerial.println(blue)\n')
    led.programming.stop()
    led.programming.run()
    led.close()
    
    util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x, pot.y, pot.x + 15, pot.y + 5)
    
    led.select()
    output = str(led.programming.getConsoleOutput()).splitlines()[-1]
    check(50 < float(output) < 75)
    None
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
