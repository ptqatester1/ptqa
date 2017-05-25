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

button = MCU('LCD', 103, 167, 'IoT0')
speaker = MCU('Piezo Speaker', 445, 150, 'IoE1')

def main():
    util.init()
    util.maximizePT()
    openfile('piezo_speaker.pkt')
    checkSpeaker()
    None
    
def openfile(filename):
    path = 'IoT/IoE_Devices/' + filename
    if not os.name == 'posix':
        path = path.replace('/', '\\')
    Open().openSamples(path)
    if object.exists(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX):
        util.clickButton(UtilConst.UPDATE_IOE_DEVICE_MESSAGE_BOX_YES)
    util.speedUpConvergence()

def checkSpeaker():
    speaker.select()
    speaker.clickTab('Programming')
    speaker.programming.selectScript('Speaker', 'main')
    speaker.programming.insertTextAtLine(48, '\tSerial.println(g_currSound);')
    #speaker.programming.insertAfter('updateEnvironment();\n', '\tSerial.println(g_currSound);')
    speaker.programming.stop()
    speaker.programming.run()
    speaker.programming.clearOutputs()
    speaker.close()
    
    button.deviceInteraction()
    
    speaker.select()
    outputs = speaker.programming.getConsoleOutput().splitlines()
    outputs = [float(n) for n in outputs if float(n) > 0]
    
    check(len(outputs) > 0)
    None
