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

util = Util()
sprinkler = MCU('Fire Sprinkler', 174, 119, 'Sprinkler')
mcu = MCU('MCU-PT', 400, 105, 'CustomMCU')
fire = MCU('MCU-PT', 174, 272, 'IoT0')
sensor = MCU('Fire Sensor', 469, 271, 'Sensor')

def main():
    util.init()
    util.maximizePT()
    openfile('fire_monitor_sprinkler.pkt')
    displayOutputs()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    if object.exists(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX):
        util.clickButton(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX_YES)
    util.speedUpConvergence()

def displayOutputs():
    sprinkler.select()
    sprinkler.clickTab('Programming')
    sprinkler.programming.selectScript('..', 'Fire Sprinkler', 'main')
    sprinkler.programming.insertTextAtLine(45, '\tSerial.println(state);')
    #sprinkler.programming.insertAfter('function setState(newState)\n{\n', '\tSerial.println(state);')
    sprinkler.programming.stop()
    sprinkler.programming.run()
    sprinkler.close()
    
    util.dragAndDrop(UtilConst.WORKSPACE, fire.x, fire.y, UtilConst.WORKSPACE, sensor.x - 100, sensor.y)
    
    sprinkler.select()
    output = str(sprinkler.programming.getConsoleOutput()).splitlines()[-1]
    check(output == '0')
    sprinkler.close()
    
    util.dragAndDrop(UtilConst.WORKSPACE, sensor.x - 100, sensor.y, UtilConst.WORKSPACE, fire.x, fire.y)
    
    sprinkler.select()
    output = str(sprinkler.programming.getConsoleOutput()).splitlines()[-1]
    check(output == '1')
    sprinkler.close()
    
def check(condition, msg = ''):
    if condition:
        test.passes('Pass', trace('test.py'))
    else:
        test.fail('Fail: ' + msg, trace('test.py'))
