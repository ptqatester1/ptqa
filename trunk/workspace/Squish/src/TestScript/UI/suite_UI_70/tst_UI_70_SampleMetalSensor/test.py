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

obj = MCU('Light', 497, 162, 'CustomWithAlloyProperty')
mcu = MCU('MCU-PT', 251, 323, 'CustomMCU')
sensor = MCU('PhotoSensor', 449, 324, 'Sensor')
lcd = MCU('LCD', 262, 157, 'Output')

lastOutput = None
def main():
    util.init()
    util.maximizePT()
    openfile('metal_sensor.pkt')
    displayOutputs()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()

def displayOutputs():
    lcd.select()
    lcd.clickTab('Programming')
    lcd.programming.selectScript('..', 'LCD', 'main')
    lcd.programming.insertTextAtLine(30, '\tSerial.println(text);')
    #lcd.programming.insertAfter('function setText(text) {\n', '\tSerial.println(text);')
    lcd.programming.stop()
    lcd.programming.run()
    lcd.close()
    
    util.dragAndDrop(UtilConst.WORKSPACE, obj.x, obj.y, UtilConst.WORKSPACE, sensor.x, sensor.y - 10)
    
    lcd.select()
    output = str(lcd.programming.getConsoleOutput()).splitlines()[-1]
    check(output == '20')
    lcd.close()
    
    util.dragAndDrop(UtilConst.WORKSPACE, sensor.x, sensor.y - 10, UtilConst.WORKSPACE, obj.x, obj.y)
    snooze(1)
    
    lcd.select()
    output = str(lcd.programming.getConsoleOutput()).splitlines()[-1]
    check(output == '0')
    lcd.close()
    
    None
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
