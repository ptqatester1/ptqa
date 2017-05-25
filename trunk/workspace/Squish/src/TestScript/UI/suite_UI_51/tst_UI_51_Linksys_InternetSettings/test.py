from API.ComponentBox import ComponentBoxConst

from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Utility import UtilConst
from API.Utility.Util import Util
from API.Device.DeviceBase import DeviceBase
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst 

Linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 150, 100, "Wireless Router0")
util = Util()


def main():
    util.init()
    createTopology()
    checkPoint1()
    checkPoint2()
    checkPoint3()
    checkPoint4()
    checkPoint5()
    checkPoint6()
    checkPoint7()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, Linksys.model, Linksys.x, Linksys.y)

def checkPoint1():
    Linksys.select()
    Linksys.clickConfigTab()
    Linksys.config.selectInterface("Internet")
    Linksys.config.interface.internet.dhcp()
    
    test.compare(findObject(Linksys.objName(ConfigConst.interface.GATEWAY_EDIT)).enabled, False)
    test.compare(findObject(Linksys.objName(ConfigConst.interface.IP_ADDRESS_EDIT)).enabled, False)
    test.compare(findObject(Linksys.objName(ConfigConst.interface.SUBNET_MASK_EDIT)).enabled, False)
    test.compare(findObject(Linksys.objName(ConfigConst.interface.DNS_EDIT)).enabled, False)

def checkPoint2():
    Linksys.config.interface.internet.static()
    test.compare(findObject(Linksys.objName(ConfigConst.interface.GATEWAY_EDIT)).enabled, True)
    test.compare(findObject(Linksys.objName(ConfigConst.interface.IP_ADDRESS_EDIT)).enabled, True)
    test.compare(findObject(Linksys.objName(ConfigConst.interface.SUBNET_MASK_EDIT)).enabled, True)
    test.compare(findObject(Linksys.objName(ConfigConst.interface.DNS_EDIT)).enabled, True)

def checkPoint3():
    Linksys.config.interface.internet.setInternetAddress("1.1.1.2", "255.0.0.0", "1.1.1.1", "2.2.2.2")
    
    Linksys.config.interface.internet.check.gateway("1.1.1.1")
    Linksys.config.interface.internet.check.dns("2.2.2.2")
    Linksys.config.interface.internet.check.ip("1.1.1.2")
    Linksys.config.interface.internet.check.subnet("255.0.0.0")

def checkPoint4():
    Linksys.config.interface.internet.dhcp()
    Linksys.config.interface.internet.static()
    Linksys.config.interface.internet.gateway('1.1.1')
    Linksys.config.interface.internet.gateway('<Tab>')
    
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Invalid IP address entered")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)

def checkPoint5():
    Linksys.config.interface.internet.ip("1.1.1")
    Linksys.config.interface.internet.ip("<Tab>")

    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "This is an invalid IP address.")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)

def checkPoint6():
    Linksys.config.interface.internet.dns("1.1.1")
    Linksys.config.interface.internet.dns("<Tab>")

    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Invalid IP address entered")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    
def checkPoint7():
    Linksys.config.interface.internet.ip("1.1.1.1")
    Linksys.config.interface.internet.subnet("1.1.1")
    Linksys.config.interface.internet.subnet("<Tab>")
    snooze(2)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Invalid subnet address entered.")