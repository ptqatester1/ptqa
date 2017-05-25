#Lesley Tse

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server

from API.Device.EndDevice.PC.PC import PC

from API.Device.EndDevice.Sniffer.Sniffer import Sniffer

from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.Open.Open import Open
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.SimulationPanel.PlayControls.PlayControls import PlayControls
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from API.Device.EndDevice.Sniffer import SnifferConst
from API.functions import pathFromOS
from API import functions

util = Util()
openFile = Open()
ctb = CommonToolsBar()

pc = PC(ComponentBoxConst.DeviceModel.PC, 55, 140, 'PC0')
s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 310, 130, 'Server0')
sniffer = Sniffer(ComponentBoxConst.DeviceModel.SNIFFER, 175, 80, 'Sniffer0')

def main():
    maketop()
    sendPackets()
    checkRealtime()
    checkSimulation()
    
def maketop():
    openFile.openSamples(pathFromOS("Sniffer/sniffer_test.pkt"))
    util.speedUpConvergence()
    
def sendPackets():
    pc.select()
    pc.clickDesktopTab()
    pc.desktop.applications.webBrowser()
    pc.desktop.webBrowser.browse("10.0.0.1")
    
def checkRealtime():
    sniffer.select()
    sniffer.clickGuiTab()
    
    for i in range (0,5):
        pc.desktop.webBrowser.go()
        snooze(2)
        
    #when clicking Go, most of the time 5 packets are captured at a time. rarely, 6 packets are captured because of an extra HTTP packet.   
    functions.check(sniffer.gui.eventTable.count == 30 or sniffer.gui.eventTable.count == 31)
        
    pc.desktop.webBrowser.go()
    #This should push packet list over default buffer size of 32. Removing the first ten packets when buffer is full. Can fail depending on # of packets captured in first checkpoint.
    functions.check(sniffer.gui.eventTable.count == 25 or sniffer.gui.eventTable.count == 26)
    
    sniffer.gui.clearButton()    
    
    functions.check(sniffer.gui.eventTable.count == 0)
    
def checkSimulation():
    util.clickOnSimulation()
    pc.desktop.webBrowser.go()
    
    PlayControls().captureForward(23)
    
    #when clicking Go, most of the time 5 packets are captured at a time. rarely, 6 packets are captured because of an extra HTTP packet.   
    functions.check(sniffer.gui.eventTable.count == 6)
    
    row_1_event = sniffer.gui.eventAt(0)    
    functions.check(row_1_event.text == 'TCP')
    
    
    row_3_event = sniffer.gui.eventAt(3)    
    functions.check(row_3_event.text == 'HTTP')
    
    row_5_event = sniffer.gui.eventAt(5)    
    functions.check(row_5_event.text == 'TCP')