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

lcd0 = MCU('LCD', 267, 158, 'IoT0')
lcd1 = MCU('LCD', 278, 376, 'IoE1')
pot = MCU('Potentiometer', 507, 171, 'IoE2')
MCU = MCU('MCU-PT', 526, 363, 'CustomMCU1')

lastOutput = None
def main():
    util.init()
    util.maximizePT()
    openfile('lcd.pkt')
    displayOutputs()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    for lcd in [lcd0, lcd1]:
        lcd.select()
        lcd.clickTab('Programming')
        lcd.programming.selectScript('LCD', 'main')
        lcd.programming.insertTextAtLine(30, '\tSerial.println(text);\n')
        #lcd.programming.insertAfter('function setText(text) {\n', '\tSerial.println(text);\n')
        lcd.programming.stop()
        lcd.programming.run()
        lcd.close()

    util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x + 10, pot.y + 10, pot.x + 30, pot.y + 20, 5)
    
    lcd0.select()
    output = str(lcd1.programming.getConsoleOutput()).splitlines()[-1]
    check(float(output) > 10)
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
