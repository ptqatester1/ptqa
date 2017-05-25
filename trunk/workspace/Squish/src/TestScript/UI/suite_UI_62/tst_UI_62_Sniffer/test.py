##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Sniffer.Sniffer import Sniffer
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.Open.Open import Open
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Device.EndDevice.Sniffer import SnifferConst
from API import functions

util = Util()
openFile = Open()
ctb = CommonToolsBar()

pc = PC(ComponentBoxConst.DeviceModel.PC, 55, 140, 'PC0')
s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 310, 130, 'Server0')
sniffer = Sniffer(ComponentBoxConst.DeviceModel.SNIFFER, 175, 80, 'Sniffer0')

def main():
    util.init()
    #openfile('C:/PT61/saves/6.2/Sniffer/', 'sniffer_test.pkt')
    openfile('Sniffer/', 'sniffer_test.pkt')
    checkGui()
    None

def openfile(path, filename):
    openFile.openSamples(functions.pathFromOS(path + filename))
        
def checkGui():
    sniffer.select()
    sniffer.clickGuiTab()
    sniffer.gui.off()
    #Check on off buttons
    sniffer.gui.check.off(True)
    sniffer.gui.check.on(False)
    sniffer.gui.on()
    sniffer.gui.check.on(True)
    sniffer.gui.check.off(False)
    #Check Port buttons
    sniffer.gui.port1()
    sniffer.gui.check.port1(True)
    sniffer.gui.check.port0(False)
    sniffer.gui.port0()
    
    #Check slider
    #Minimum should be 32
    #Max should be 512
    sniffer.gui.bufferSize(0)
    sniffer.gui.check.bufferSize(32)
    sniffer.gui.bufferSize(32)
    sniffer.gui.check.bufferSize(32)
    sniffer.gui.bufferSize(256)
    sniffer.gui.check.bufferSize(256)
    sniffer.gui.bufferSize(512)
    sniffer.gui.check.bufferSize(512)
    sniffer.gui.bufferSize(1000)
    sniffer.gui.check.bufferSize(512)
    
    #Check Adding/removing filters
    for filter in ['HTTP', 'HTTPS', 'TCP']:
        functions.check(filter in sniffer.gui.filters.currentFiltersList)
    sniffer.gui.filters.checkFilters('ICMP', clearFilters=True)
    functions.check(len(sniffer.gui.filters.currentFiltersList) == 1)
    functions.check(sniffer.gui.filters.currentFiltersText == 'ICMP')
    
    sniffer.gui.filters.checkFilters('ICMP', 'TCP', clearFilters=True)
    for filter in sniffer.gui.filters.currentFiltersList:
        functions.check(filter in ['ICMP', 'TCP'])
    sniffer.gui.filters.checkFilters('ARP')    
    
    ctb.addSimplePDU(pc.x, pc.y, s0.x, s0.y)
    functions.check(sniffer.gui.eventTable.count == 2)
    
    functions.check(sniffer.gui.eventAt(0).text == 'ARP')
    
    functions.check(sniffer.gui.eventAt(1).text == 'ICMP')
    
    ##Check PDU Info
    sniffer.gui.selectEventType('ICMP')
    util.checkObjectExist(SnifferConst.GuiConst.PacketInformation + 'TYPE: 0x8 ')
    util.checkObjectExist(SnifferConst.GuiConst.PacketInformation + 'CODE: 0x0 ')
    util.checkObjectExist(SnifferConst.GuiConst.PacketInformation + 'CHECKSUM ')
    util.checkObjectExist(SnifferConst.GuiConst.PacketInformation + 'ID: 0x2 ')
    util.checkObjectExist(SnifferConst.GuiConst.PacketInformation + 'SEQ NUMBER: 1 ')
