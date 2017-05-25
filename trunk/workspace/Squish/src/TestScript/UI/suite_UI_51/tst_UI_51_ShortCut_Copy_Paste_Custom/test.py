from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router

from API.Device.EndDevice.PC.PC import PC

from API.Utility import UtilConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File

util = Util()
editMenu = Edit()
commonToolsBar = CommonToolsBar() 
fileMenu = File()
CopyRouter0 = Router(ComponentBoxConst.DeviceModel.CUSTOM_1841, 100, 50, "CopyRouter0")
CopyRouter1 = Router(ComponentBoxConst.DeviceModel.CUSTOM_2621XM, 200, 50, "CopyRouter1")
CopyRouter2 = Router(ComponentBoxConst.DeviceModel.CUSTOM_2811,300, 50, "CopyRouter2")
CopyPC0 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC,400, 50, "CopyPC0")


Router0 = Router(ComponentBoxConst.DeviceModel.CUSTOM_1841, 100, 100, "Router0")
Router1 = Router(ComponentBoxConst.DeviceModel.CUSTOM_2621XM, 200, 100, "Router1")
Router2 = Router(ComponentBoxConst.DeviceModel.CUSTOM_2811,300, 100, "Router2")
PC0 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 400, 100, "PC0")

def main():
    util.init()
    copyPaste_deviceOnWorkspace()

def copyPaste_deviceOnWorkspace():

    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, Router0.model, Router0.x, Router0.y)    
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, Router1.model, Router1.x, Router1.y)    
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, PC0.model, PC0.x, PC0.y) 
    util.createDevice(ComponentBoxConst.DeviceType.MISCELLANEOUS, Router2.model, Router2.x, Router2.y)   
    
    util.clickOnSimulation()
    util.clickOnRealtime()
    for rtr in [Router0, Router1, Router2]:
        rtr.select()
        rtr.clickConfigTab()
        rtr.config.settings.hostname("RouterCopy")
        rtr.config.selectInterface('Static')
        rtr.config.routing.static.addRoute("10.0.0.0", "255.0.0.0", "10.1.1.1")
        rtr.config.selectInterface('RIP')
        rtr.config.routing.rip.addRoute("10.0.0.0")
        rtr.config.selectInterface("FastEthernet0/0")
        rtr.config.interface.ethernet.ip("10.1.1.2")
        rtr.config.interface.ethernet.subnet("255.0.0.0")
        rtr.config.interface.ethernet.bandwidth(None)    
        rtr.config.interface.ethernet.duplex(None)
        rtr.config.interface.ethernet.portStatus(True)
        rtr.close()
        
    PC0.select()
    PC0.clickConfigTab()
    PC0.config.selectInterface("Wireless0")
    PC0.config.interface.wireless.ssid("LinksysRouter")   
    PC0.config.interface.wireless.wep()
    PC0.config.interface.wireless.wepkey("0123456789")   
    PC0.close()

    util.selectObjectsOnWorkspace(Router0.x, Router0.y)
    util.selectObjectsOnWorkspace(Router1.x, Router1.y)
    util.selectObjectsOnWorkspace(Router2.x, Router2.y)
    util.selectObjectsOnWorkspace(PC0.x, PC0.y)
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+C>")
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+V>")
    
    for i, rtr in enumerate([CopyRouter0, CopyRouter1, CopyRouter2]):
        rtr.select()
        rtr.clickConfigTab()
        rtr.config.settings.check.hostname("RouterCopy")
        rtr.config.settings.check.displayName("CopyRouter%s"%(i,))
        rtr.config.selectInterface('Static')
        rtr.config.routing.static.removeRow(0)
        rtr.config.selectInterface('RIP')
        rtr.config.routing.rip.removeRow(0)
        rtr.cli.textCheckPoint("no ip route 10.0.0.0 255.0.0.0 10.1.1.1")       
        rtr.cli.textCheckPoint("no network 10.0.0.0")
        rtr.config.selectInterface("FastEthernet0/0")
        rtr.config.interface.ethernet.check.ip("10.1.1.2")
        rtr.config.interface.ethernet.check.subnet("255.0.0.0")
        rtr.config.interface.ethernet.check.bandwidth('Auto', False)
        rtr.config.interface.ethernet.check.duplex('Auto', False)
        rtr.config.interface.ethernet.check.portStatus(True)
        rtr.close()

    CopyPC0.select()
    CopyPC0.clickConfigTab()
    CopyPC0.config.settings.check.displayName("CopyPC0")
    CopyPC0.config.selectInterface("Wireless0") 
    CopyPC0.config.interface.wireless.check.ssid("LinksysRouter")
    CopyPC0.config.interface.wireless.check.wepkey("0123456789")
    CopyPC0.close()
