#Thi
from API.ComponentBox import ComponentBoxConst
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.Device.Router.Router import Router
from API.Device.DeviceBase.WirelessGuiBase.WirelessGuiBaseConst import WirelessGuiConst

#Function initialization
util = Util()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 563, 252, "PC0")
wirelessRouter0 = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 313, 251, "Wireless Router0")
Router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 450, 252, "Router1")

def main():
    createTopology()
    advancedWirelessSettings()
    
def createTopology():
    #a.    Create and connect devices according to diagram.
    #a.    On PC0, remove ethernet interface and insert Linksys WRT-300N.
    util.open("UI20_Improved_Linksys.pkt", UtilConst.UI_TEST)

def advancedWirelessSettings():
    wirelessRouter0.select()
    wirelessRouter0.clickGuiTab()
    wirelessRouter0.gui.tabs.wireless()
    wirelessRouter0.gui.tabs.advancdedWirelessSettings()
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.advancedWirelessSettings.AUTHENTICATION_TYPE).currentText, "Shared Key")
    wirelessRouter0.gui.tabs.wirelessSecurity()
    wirelessRouter0.gui.wireless.wirelessSecurity.securityMode("Disabled")
    wirelessRouter0.gui.wireless.wirelessSecurity.saveSettingsButton()
    wirelessRouter0.gui.tabs.advancdedWirelessSettings()
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.advancedWirelessSettings.AUTHENTICATION_TYPE).enabled, False)
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.advancedWirelessSettings.AUTHENTICATION_TYPE).currentText, "Auto")
