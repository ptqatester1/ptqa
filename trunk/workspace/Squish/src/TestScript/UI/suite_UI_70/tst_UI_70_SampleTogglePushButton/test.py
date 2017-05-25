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
led = MCU('LED', 452, 96, 'LED')
button = MCU('Toggle Push Button', 197, 100, 'IoE8=7')

def main():
    util.init()
    util.maximizePT()
    openfile('toggle_push_button.pkt')
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
    led.programming.insertTextAtLine(14, '\tSerial.println(input);')
    #led.programming.insertAfter('input = analogRead(0);\n', '\tSerial.println(input);')
    led.programming.stop()
    led.programming.run()
    led.programming.clearOutputs()
    led.close()
    
    button.deviceInteraction()
    
    led.select()
    output = led.programming.getConsoleOutput().splitlines()[-1]
    check(output == '1023')
    led.close()
    
    button.deviceInteraction()
    led.select()
    output = led.programming.getConsoleOutput().splitlines()[-1]
    check(output == '0')
    led.close()
    
