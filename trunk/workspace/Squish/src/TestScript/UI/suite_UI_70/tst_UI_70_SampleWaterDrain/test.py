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

level = MCU('Water Level Monitor', 392, 178, 'IoE2')
drain = MCU('Water Drain', 105, 182, 'IoT0')
sprinkler = MCU('Fire Sprinkler', 261, 53, 'IoE1')

def main():
    util.init()
    util.maximizePT()
    openfile('water_drain.pkt')
    checkDrain()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    util.speedUpConvergence()
    
def checkDrain():
    sprinkler.deviceInteraction()
    
    level.select()
    level.clickTab('Programming')
    level.programming.selectScript('..', 'Water Level Monitor', 'main')
    level.programming.insertTextAtLine(73, '\tSerial.println(level);')
    #level.programming.insertAfter('level = newLevel;\n', '\tSerial.println(level);')
    level.programming.stop()
    level.programming.run()
    level.programming.clearOutputs()
    level.close()
    
    drain.select()
    drain.clickTab('Programming')
    drain.programming.selectScript('..', 'Drain', 'main')
    drain.programming.insertTextAtLine(59, '\tSerial.println(state);')
    #drain.programming.insertAfter('state = newState;\n', '\tSerial.println(state);')
    drain.programming.stop()
    drain.programming.run()
    drain.programming.clearOutputs()
    drain.close()
    
    snooze(15)
    
    level.select()
    snooze(1)
    output = level.programming.getConsoleOutput().splitlines()
    output = [float(n) for n in output if not float(n) == 0]
    check(len(output) > 0)
    level.close()
    
    drain.select()
    snooze(1)
    output = drain.programming.getConsoleOutput()
    check('0' in output and '1' in output)
    None
