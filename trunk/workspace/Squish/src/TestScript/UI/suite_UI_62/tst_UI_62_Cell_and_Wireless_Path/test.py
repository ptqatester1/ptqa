##Chris Allen

from API.Utility.Util import Util
from API.Workspace.Physical import Physical
from API.Device.EndDevice.PC.PC import PC
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.Open.Open import Open
from API.functions import pathFromOS

util = Util()
openFile = Open()
smartphone = PC(ComponentBoxConst.DeviceModel.PC, 115, 265, 'Smartphone0')

def main():
    util.init()
    openFile.openSamples(pathFromOS('Cellular/Cell and Wireless Path.pkt'))

    moveSmartphoneInRange()
    checkConnectionIsOnWireless()
    moveOutOfRange()
    checkConnectionIsCell()
    
def moveSmartphoneInRange():
    util.clickOnPhysical()
    util.maximizePT()
    Physical().goTo('Home City')
    Physical().scrollVertical(450)
    pda = Physical().getObject(smartphone.displayName)
    util.dragAndDrop(pda, 10, 10, Physical().getObject('Corporate Office'), 10, 10)
    util.clickOnLogical()
    None
    
def checkConnectionIsOnWireless():
    util.speedUpConvergence()
    smartphone.select()
    smartphone.clickTab('Desktop')
    smartphone.desktop.applications.commandPrompt()
    smartphone.desktop.commandPrompt.setText('tracert 20.1.1.1')#Trace to wireless router
    util.speedUpConvergence()
    smartphone.desktop.commandPrompt.textCheckPoint('''1\s+\d{1,} ms\s+\d{1,} ms\s+\d{1,} ms\s+192.168.0.1
\s+2\s+\*\s+\d{1,} ms\s+\d{1,} ms\s+20.1.1.1''')
    smartphone.close()
    None
    
def moveOutOfRange():
    util.clickOnPhysical()
    pda = Physical().getObject(smartphone.displayName)
    util.dragAndDrop(pda, 10, 10, Physical().workspace, 100, 100)
    util.clickOnLogical()
    None
    
def checkConnectionIsCell():
    util.speedUpConvergence()
    smartphone.select()
    smartphone.clickTab('Desktop')
    smartphone.desktop.applications.commandPrompt()
    smartphone.desktop.commandPrompt.setText('tracert 20.1.1.1')#Trace to wireless router
    util.speedUpConvergence()
    smartphone.desktop.commandPrompt.textCheckPoint('''1\s+\d{1,} ms\s+\d{1,} ms\s+\d{1,} ms\s+172.16.1.1
\s+2\s+\*\s+\d{1,} ms\s+\d{1,} ms\s+20.1.1.1''')
    smartphone.close()
    None
    