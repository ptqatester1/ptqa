from API.ComponentBox import ComponentBoxConst
from API.ComponentBox import ComponentBox
from API.Utility.Util import Util
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter

Linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 150, 100, "Wireless Router0")
util = Util()

def main():
    util.init()
    createTopology()
    WirelessSettings()

def createTopology():
    Linksys.create()
    
def WirelessSettings():
    Linksys.select()
    Linksys.clickConfigTab()
    Linksys.config.selectInterface("Wireless")
    Linksys.config.interface.wireless.ssid("1000")   
    Linksys.config.interface.wireless.wep()
    Linksys.config.interface.wireless.wepkey("1234567891")
    Linksys.close()
    
    Linksys.select()
    Linksys.config.selectInterface("Wireless")
    Linksys.config.interface.wireless.check.ssid("1000")
    Linksys.config.interface.wireless.check.wepkey("1234567891")
    Linksys.config.interface.wireless.check.disabled(False)
    Linksys.config.interface.wireless.disabled()
    Linksys.config.interface.wireless.check.wepkey('')
    Linksys.config.interface.wireless.check.disabled(True)