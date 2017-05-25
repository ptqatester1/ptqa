from API.MenuBar.Edit.EditConst import EditConst
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Device.EndDevice.Printer.Printer import Printer

from API.Device.EndDevice.Server.Server import Server

from API.Device.EndDevice.IPPhone.IPPhone import IPPhone
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.MenuBar.File.New.NewConst import NewConst

util = Util()
editMenu = Edit()
commonToolsBar = CommonToolsBar()


PC0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, "PC0")
Printer0 = Printer(ComponentBoxConst.DeviceModel.PRINTER, 200, 100,"Printer0")
Server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 300, 100, "Server0")
IPPhone0 = IPPhone(ComponentBoxConst.DeviceModel.IPPHONE, 400, 100, "IP Phone0")

CopyPC0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 50, "PC0")
CopyPrinter0 = Printer(ComponentBoxConst.DeviceModel.PRINTER, 200, 50, "CopyPrinter1")
CopyServer0 = Server(ComponentBoxConst.DeviceModel.SERVER, 300, 50, "CopyServer1")
CopyIPPhone0 = IPPhone(ComponentBoxConst.DeviceModel.IPPHONE, 400, 50, "CopyIP Phone1")

def main():
    util.init()
    copyPaste_noItemOnWorkspace()
    copyPaste_deviceOnWorkspace()


def copyPaste_noItemOnWorkspace():
    snooze(2)
    editMenu.selectEditItem(EditConst.COPY)
    editMenu.selectEditItem(EditConst.PASTE)
    util.clickButton(MainToolbarConst.NEW)
    snooze(2)
    if (not object.exists(NewConst.SAVE_NETWORK_PROMPT)):
        test.passes("no item was copied")
    else:
        test.fail("some item was copied")

def copyPaste_deviceOnWorkspace():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, PC0.model, PC0.x, PC0.y)    
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, Printer0.model, Printer0.x, Printer0.y)    
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, Server0.model, Server0.x, Server0.y)    
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, IPPhone0.model, IPPhone0.x, IPPhone0.y)
    

    PC0.select()
    PC0.clickConfigTab()
    PC0.config.settings.dns("10.1.1.1")
    PC0.config.settings.gateway("10.1.1.1")
    PC0.config.selectInterface("FastEthernet0")
    PC0.config.interface.wired.ip("10.1.1.2")     
    PC0.config.interface.wired.bandwidth('auto')
    PC0.config.interface.wired.duplex(None)
    PC0.config.interface.wired.portStatus(None)
    PC0.close()

    Printer0.select()
    Printer0.clickConfigTab()
    Printer0.config.settings.dns("10.1.1.1")
    Printer0.config.settings.gateway("10.1.1.1")
    Printer0.config.selectInterface("FastEthernet0")
    Printer0.config.interface.wired.ip("10.1.1.2")     
    Printer0.config.interface.wired.bandwidth('auto')
    Printer0.config.interface.wired.duplex(None)
    Printer0.config.interface.wired.portStatus(None)
    Printer0.close()
    
    
    Server0.select()
    Server0.clickConfigTab()
    Server0.config.settings.gateway("10.1.1.1")
    Server0.config.selectInterface("FastEthernet0")
    Server0.config.interface.wired.ip("10.1.1.2")
    Server0.config.interface.wired.bandwidth(None) 
    Server0.config.interface.wired.duplex(None)
    Server0.config.interface.wired.portStatus(None)
    Server0.clickServicesTab()
    Server0.services.selectInterface("DHCP")
    Server0.services.dhcp.off()
    Server0.services.selectInterface("DNS")
    Server0.services.dns.off()
    Server0.services.selectInterface('HTTP')
    Server0.services.http.httpOff()
    Server0.services.http.httpsOff()
    Server0.services.selectInterface("TFTP")
    Server0.services.tftp.off()
    Server0.close()

    util.selectObjectsOnWorkspace(PC0.x, PC0.y)
    util.selectObjectsOnWorkspace(Server0.x, Server0.y)
    util.selectObjectsOnWorkspace(Printer0.x, Printer0.y)
    util.selectObjectsOnWorkspace(IPPhone0.x, IPPhone0.y)
    editMenu.selectEditItem(EditConst.COPY)
    editMenu.selectEditItem(EditConst.PASTE)

    
    CopyPC0.select()
    CopyPC0.clickConfigTab()
    CopyPC0.config.settings.check.displayName("CopyPC0")
    CopyPC0.config.settings.check.dns("10.1.1.1")
    CopyPC0.config.settings.check.gateway("10.1.1.1")
    CopyPC0.config.selectInterface("FastEthernet0")
    CopyPC0.config.settings.check.gateway("10.1.1.1")
    CopyPC0.config.interface.wired.check.ip("10.1.1.2")
    CopyPC0.config.interface.wired.check.bandwidth('Auto', False)
    CopyPC0.config.interface.wired.check.duplex('Auto', False)
    CopyPC0.config.interface.wired.check.portStatus(False)
    CopyPC0.close()

    CopyPrinter0.select()
    CopyPrinter0.clickConfigTab()
    CopyPrinter0.config.settings.check.displayName("CopyPrinter0")
    CopyPrinter0.config.settings.check.dns("10.1.1.1")
    CopyPrinter0.config.settings.check.gateway("10.1.1.1")
    CopyPrinter0.config.selectInterface("FastEthernet0")
    CopyPrinter0.config.settings.check.gateway("10.1.1.1")
    CopyPrinter0.config.interface.wired.check.ip("10.1.1.2")
    CopyPrinter0.config.interface.wired.check.bandwidth('Auto', False)
    CopyPrinter0.config.interface.wired.check.duplex('Auto', False)
    CopyPrinter0.config.interface.wired.check.portStatus(False)
    CopyPrinter0.close()
    
    
    CopyServer0.select()
    CopyServer0.clickConfigTab()
    CopyServer0.config.settings.check.displayName("CopyServer0")
    CopyServer0.config.settings.check.gateway("10.1.1.1")
    CopyServer0.config.selectInterface("FastEthernet0")
    CopyServer0.config.interface.wired.check.ip("10.1.1.2")     
    CopyServer0.config.interface.wired.check.bandwidth('Auto', True)
    CopyServer0.config.interface.wired.check.duplex('Auto', True)
    CopyServer0.config.interface.wired.check.portStatus(False)
    CopyServer0.clickServicesTab()
    CopyServer0.services.selectInterface("DHCP")
    CopyServer0.services.dhcp.check.off(True)
    CopyServer0.services.selectInterface("DNS")
    CopyServer0.services.dns.check.off(True)
    CopyServer0.services.selectInterface('HTTP')
    CopyServer0.services.http.check.httpOff(True)
    CopyServer0.services.http.check.httpsOff(True)
    CopyServer0.services.selectInterface("TFTP")
    CopyServer0.services.tftp.check.off(True)
    CopyServer0.close()