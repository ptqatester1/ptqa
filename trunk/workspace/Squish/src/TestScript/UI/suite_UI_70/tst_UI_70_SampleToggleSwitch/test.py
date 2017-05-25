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
pot = MCU('Potentiometer', 93, 256, 'POT')
button = MCU('Toggle Push Button', 320, 247, 'TSW')
lcd = MCU('LCD', 364, 382, 'LCD')
led = MCU('LED', 615, 281, 'L1')

def main():
    util.init()
    util.maximizePT()
    openfile('toggle_switch.pkt')
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
    led.programming.selectScript('LED', 'main')
    led.programming.insertTextAtLine(14, '\tSerial.println(input);\n')
    #led.programming.insertAfter('input = analogRead(0);\n', '\tSerial.println(input);\n')
    led.programming.stop()
    led.programming.run()
    led.close()
    
    lcd.select()
    lcd.clickTab('Programming')
    lcd.programming.selectScript('..', 'LCD', 'main')
    lcd.programming.insertTextAtLine(30, '\tSerial.println(text);\n')
    #lcd.programming.insertAfter('function setText(text) {\n', '\tSerial.println(text);\n')
    lcd.programming.stop()
    lcd.programming.run()
    lcd.close()
    
    util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x, pot.y, pot.x + 15, pot.y + 5)
    button.deviceInteraction()
    
    lcd.select()
    output = str(lcd.programming.getConsoleOutput()).splitlines()[-1]
    check(50 < float(output) < 75)
    lcd.close()
    
    led.select()
    output = str(led.programming.getConsoleOutput()).splitlines()[-1]
    check(250 < float(output) < 275)
    led.close()
    None
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
