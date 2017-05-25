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

switch = MCU('LCD', 169, 162, 'IoT0')
cooler = MCU('Potentiometer', 489, 141, 'IoE2')

pc = PC(ComponentBoxConst.DeviceModel.PC, 410, 110, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('switch.pkt')
    checkSwitch()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    if object.exists(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX):
        util.clickButton(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX_YES)
    util.speedUpConvergence()

def checkSwitch():
    cooler.select()
    cooler.clickTab('Programming')
    cooler.programming.selectScript('..', 'Chiller', 'main')
    cooler.programming.insertTextAtLine(13, '\tSerial.println(input);')
    #cooler.programming.insertAfter('input = digitalRead(0)/1023;\n', '\tSerial.println(input);')
    cooler.programming.stop()
    cooler.programming.run()
    cooler.programming.clearOutputs()
    cooler.close()
    
    switch.deviceInteraction()
    
    cooler.select()
    output = cooler.programming.getConsoleOutput().splitlines()[0]
    check(float(output) == 1)
    None
