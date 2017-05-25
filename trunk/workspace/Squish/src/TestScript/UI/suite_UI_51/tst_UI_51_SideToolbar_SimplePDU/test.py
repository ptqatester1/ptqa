from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Device.Hub.Hub import Hub
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Utility.Util import Util
from API.Utility import UtilConst

util = Util()
utilConst = UtilConst
commonToolsBar = CommonToolsBar()

Host1 = PC(ComponentBoxConst.DeviceModel.PC, 124, 93, "PC0")
Host2 = PC(ComponentBoxConst.DeviceModel.PC, 568, 104, "PC1")
Host3 = PC(ComponentBoxConst.DeviceModel.PC, 565, 305, "PC2")
H1 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 343, 84, "Hub0")

def main():
    util.init()
    createdevice()
    connectdevices()
    addPDU()
    configIP()
    addSimplePDU()
    
def createdevice():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,Host1.model,Host1.x,Host1.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,Host2.model,Host2.x,Host2.y)
    util.createDevice(ComponentBoxConst.DeviceType.HUB, H1.model,H1.x,H1.y)
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE,Host3.model,Host3.x,Host3.y)

def connectdevices():
    util.connect(Host1.x, Host1.y, Host2.x, Host2.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.connect(Host3.x, Host3.y, H1.x, H1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    
def addPDU():
    util.clickButton(CommonToolsBarConst.ADD_SIMPLE_PDU)
    Host1.select()
    util.clickOnWorkspace(Host2.x, Host2.y)
    snooze(2)
    test.compare(findObject(CommonToolsBarConst.NO_FUNCTIONAL_PORTS_OK).visible, True)
    util.clickButton(CommonToolsBarConst.NO_FUNCTIONAL_PORTS_OK)
    util.clickButton(CommonToolsBarConst.SELECT_TOOL)

def configIP():
    Host1.select()
    Host1.clickDesktopTab()
    Host1.desktop.applications.ipConfiguration()
    Host1.desktop.ipConfiguration.setIPConfiguration("192.168.1.1", "255.255.255.0", "", "")
    Host1.desktop.ipConfiguration.close()

    util.clickOnWorkspace(Host2.x, Host2.y)
    Host2.updateName()
    Host2.clickDesktopTab()
    Host2.desktop.applications.ipConfiguration()
    Host2.desktop.ipConfiguration.setIPConfiguration("192.168.1.2", "255.255.255.0", "", "")
    Host2.desktop.ipConfiguration.close()

def addSimplePDU():
    commonToolsBar.addSimplePDU(Host1.x, Host1.y, Host2.x, Host2.y)
    util.clickButton(CommonToolsBarConst.ADD_SIMPLE_PDU)
    util.clickOnWorkspace(Host3.x, Host3.y)
    util.clickOnWorkspace(H1.x, H1.y)
    snooze(2)
    test.compare(findObject(CommonToolsBarConst.INCOMPATIBLE_DEVICE_OK).visible, True)