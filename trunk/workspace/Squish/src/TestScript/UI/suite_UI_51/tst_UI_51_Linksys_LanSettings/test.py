from API.ComponentBox import ComponentBoxConst
from API.ComponentBox import ComponentBox
from API.Utility.Util import Util
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter


Linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 150, 100, "Wireless Router0")
util = Util()

def main():
    util.init()
    createTopology()
    LanSettings()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.WIRELESS_DEVICE, Linksys.model, Linksys.x, Linksys.y)

def LanSettings():
    Linksys.select()
    Linksys.clickConfigTab()
    Linksys.config.selectInterface("LAN")
    Linksys.config.interface.lan.ip("1.1.1.1")
    Linksys.config.interface.lan.subnet("255.0.0.0")
    Linksys.close()
    
    Linksys.select()
    Linksys.config.selectInterface("LAN")
    Linksys.config.interface.lan.check.ip("1.1.1.1")
    Linksys.config.interface.lan.check.subnet("255.0.0.0")