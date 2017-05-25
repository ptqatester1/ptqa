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
lcd = MCU('lcd', 559, 183, 'IoE5')
pot = MCU('Potentiometer', 286, 353, 'IoE2')
speaker = MCU('Home Speaker', 293, 202, 'IoE6')
pc = PC(ComponentBoxConst.DeviceModel.PC, 500, 45, 'PC0')

def main():
    util.init()
    util.maximizePT()
    openfile('sound_sensor.pkt')
    displayOutputs()
    checkSensor()
    checkSpeaker()
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
    lcd.programming.insertTextAtLine(30, '\tSerial.println(text);\n')
    #lcd.programming.insertAfter('function setText(text) {\n', '\tSerial.println(text);\n')
    lcd.programming.stop()
    lcd.programming.run()
    lcd.programming.clearOutputs()
    lcd.close()
    
    speaker.select()
    speaker.clickTab('Programming')
    speaker.programming.selectScript('..', 'Home Speaker', 'main')
    speaker.programming.insertTextAtLine(19, '\tSerial.println(g_currSound);')
    #speaker.programming.insertAfter('setDeviceProperty(getName(), "Signal", g_currSound);\n', '\tSerial.println(g_currSound);')
    speaker.programming.stop()
    speaker.programming.run()
    speaker.programming.clearOutputs()
    speaker.close()
    
def checkSensor():
    util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x, pot.y, pot.x + 25, pot.y + 5)
    snooze(5)
    lcd.select()
    output = lcd.programming.getConsoleOutput().splitlines()[-1]
    check(15 < float(output) < 30)
    lcd.close()
    
def checkSpeaker():
    speaker.select()
    output = speaker.programming.getConsoleOutput().splitlines()[-1]
    check(float(output) == 1)
    speaker.close()
    None
