from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.Server.Server import Server

from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util
from API.Utility import UtilConst

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 300, 200, "Server0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    completeTopology()
    checkpoint2()

def createTopology():
    pc0.create()

def checkpoint1():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.dhcp()
    pc0.desktop.ipConfiguration.check.ip(None, property='enabled', value=False)
    pc0.desktop.ipConfiguration.check.subnet(None, property='enabled', value=False)
    pc0.desktop.ipConfiguration.check.gateway(None, property='enabled', value=False)
    pc0.desktop.ipConfiguration.check.dns(None, property='enabled', value=False)
    pc0.desktop.ipConfiguration.static()
    pc0.desktop.ipConfiguration.check.ip(None, property='enabled', value=True)
    pc0.desktop.ipConfiguration.check.subnet(None, property='enabled', value=True)
    pc0.desktop.ipConfiguration.check.gateway(None, property='enabled', value=True)
    pc0.desktop.ipConfiguration.check.dns(None, property='enabled', value=True)
    pc0.desktop.ipConfiguration.setIPConfiguration("1.1.1.2", "", "1.1.1.1", "2.1.1.1")
    pc0.desktop.ipConfiguration.check.ip("1.1.1.2")
    pc0.desktop.ipConfiguration.check.subnet("255.0.0.0")
    pc0.desktop.ipConfiguration.check.gateway("1.1.1.1")
    pc0.desktop.ipConfiguration.check.dns("2.1.1.1")
    pc0.desktop.ipConfiguration.setIPConfiguration("<Del>", "<Del>", "<Del>", "<Del>")
    pc0.desktop.ipConfiguration.ip("0.0.0.0")
    pc0.desktop.ipConfiguration.ip("<Tab>")
    snooze(2)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_LABEL, "This is an invalid IP address")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    pc0.desktop.ipConfiguration.ip("1.1.1.1")
    pc0.desktop.ipConfiguration.subnet("0.0.0.0")
    pc0.desktop.ipConfiguration.subnet("<Tab>")
    snooze(2)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_LABEL, "Invalid subnet address entered")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    pc0.desktop.ipConfiguration.gateway("0")
    pc0.desktop.ipConfiguration.gateway("<Tab>")
    snooze(2)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_LABEL, "Invalid gateway address entered")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    pc0.desktop.ipConfiguration.dns("0")
    pc0.desktop.ipConfiguration.dns("<Tab>")
    snooze(2)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_LABEL, "Invalid DNS entered")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)

def completeTopology():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, server0.model, server0.x, server0.y)
    util.connect(pc0.x, pc0.y, server0.x, server0.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    
def checkpoint2():
    util.clickOnWorkspace(server0.x, server0.y)
    server0.updateName()
    server0.clickConfigTab()
    server0.config.selectInterface("FastEthernet0")
    server0.config.interface.wired.ip("1.1.1.1")
    server0.clickServicesTab()

    server0.services.selectInterface("DHCP")
    server0.services.dhcp.on()
    server0.services.dhcp.edit('serverPool', None, '2.1.1.1', '1.1.1.1', '1.1.1.2', '255.0.0.0', '50', None)
    pc0.select()

    pc0.desktop.ipConfiguration.dhcp()
    pc0.desktop.ipConfiguration.static()
    pc0.desktop.ipConfiguration.dhcp()
    snooze(10)
    pc0.desktop.ipConfiguration.check.ip("1.1.1.[2,3]")
    pc0.desktop.ipConfiguration.check.subnet("255.0.0.0")
    pc0.desktop.ipConfiguration.check.gateway("2.1.1.1")
    pc0.desktop.ipConfiguration.check.dns("1.1.1.1")