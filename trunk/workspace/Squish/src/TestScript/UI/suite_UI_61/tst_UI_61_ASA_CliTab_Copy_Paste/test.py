##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Security.Asa import Asa
from API.Device.EndDevice.PC.PC import PC
from API.ComponentBox import ComponentBoxConst
from API import functions

util = Util()
a0 = Asa(ComponentBoxConst.DeviceModel.ASA_5505, 100, 100, 'Asa0')
pc = PC(ComponentBoxConst.DeviceModel.PC, 200, 100, 'PC0')

def main():
    util.init()
    create()
    checkPaste()
    checkCopy()
    
def create():    
    a0.create()
    pc.create()
    a0.connect(pc)
    util.fastForwardTime()
    
def checkPaste():
    pc.select()
    pc.clickDesktopTab()
    pc.desktop.applications.ipConfiguration()
    pc.desktop.ipConfiguration.setIPConfiguration('10.1.1.2', '255.255.255.0', '10.1.1.1', '')
    functions.Clipboard().setText('10.1.1.1')
    pc.close()
    
    util.clickOnWorkspace(a0.x, a0.y)
    a0.updateName()
    a0.clickCliTab()
    a0.cli.setCliText('enable')
    a0.cli.setCliText('')
    a0.cli.setCliText('configure terminal')
    a0.cli.setCliText('interface vlan 2')
    a0.cli.typeText('ip address ')
    a0.cli.pasteButton()
    a0.cli.setCliText('')
    
    util.clickOnWorkspace(pc.x, pc.y)
    pc.updateName()
    pc.desktop.applications.commandPrompt()
    pc.desktop.commandPrompt.setText('ping 10.1.1.1')
    util.fastForwardTime()
    pc.desktop.commandPrompt.textCheckPoint('Received = [1234]')
    pc.close()

def checkCopy():
    a0.select()
    functions.Clipboard().clear()
    cli = a0.cli.cliObject
    cli.moveCursor(QTextCursor.Start)
    cli.find('ciscoasa>enable')
    a0.cli.copyButton()
    a0.cli.pasteButton()
    a0.cli.textCheckPoint('ciscoasa>enable', lines=2)
    None
