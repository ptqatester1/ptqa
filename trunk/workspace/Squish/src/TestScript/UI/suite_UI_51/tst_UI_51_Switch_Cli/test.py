from API.ComponentBox import ComponentBoxConst

from API.Device.Switch.Switch import Switch
from API.Device.Bridge.Bridge import Bridge
from API.Utility.Util import Util
from API.Utility import UtilConst
from TestScript.UI.suite_UI_51.tst_UI_51_Switch_Physical.test import createTopology
import os
from API.functions import check, Clipboard
#Function initialization
util = Util()

#Device initialization
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 200, "Switch0")
switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 200, 200, "Switch1")
switch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 300, 200, "Switch2")
switch3 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 400, 200, "Multilayer Switch0")
switch4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 500, 200, "Switch3")
switch5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 600, 200, "Switch4")

def checkCopyText(dev):
    dev.select()
    dev.clickTab('CLI')
    dev.cli.startConsole()
    Clipboard().clear()
    cli = dev.cli.cliObject
    cli.moveCursor(QTextCursor.Start)
    cli.find('Press RETURN to get started!')
    dev.cli.copyButton()
    check('Press RETURN to get started!' == Clipboard().getText(), 'Clipboard text is: ' + Clipboard().getText())
    dev.cli.pasteButton()
    cli.moveCursor(QTextCursor.Start)
    check(cli.find('>Press RETURN to get started') == 1)
    dev.close()
    None

def main():
    util.init()
    createTopology()
    copyPaste()
    
def copyPaste():
    for switch in [switch0, switch1, switch2, switch3, switch4, switch5]:
        checkCopyText(switch)
