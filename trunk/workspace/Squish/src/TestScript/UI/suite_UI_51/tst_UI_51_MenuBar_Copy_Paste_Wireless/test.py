from API.MenuBar.Edit.EditConst import EditConst
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.AccessPoint.AccessPoint import AccessPoint

from API.Device.LinksysRouter.LinksysRouter import LinksysRouter

from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar

util = Util()
editMenu = Edit()
commonToolsBar = CommonToolsBar()

CopyAccessPoint0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 100, 50, "CopyAccess Point0")
CopyLinkSysRouter0 = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 200, 50, "CopyWireless Router0")

AccessPoint0 = AccessPoint(ComponentBoxConst.DeviceModel.ACCESSPOINT, 100, 100, "Access Point0")
LinkSysRouter0 = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 200,100, "Wireless Router0")

def main():
    util.init()
    copyPaste_deviceOnWorkspace()



def copyPaste_deviceOnWorkspace():
    AccessPoint0.create()    
    LinkSysRouter0.create()    
    
    util.clickOnSimulation()
    util.clickOnRealtime()
    
    AccessPoint0.select()
    AccessPoint0.clickConfigTab()
    AccessPoint0.config.selectInterface("Port 0")
    AccessPoint0.config.interface.port0.bandwidth(None)
    AccessPoint0.config.interface.port0.duplex(None)
    AccessPoint0.config.interface.port0.portStatus(False)
    AccessPoint0.close()

    LinkSysRouter0.select()
    LinkSysRouter0.clickConfigTab()
    LinkSysRouter0.config.selectInterface("Wireless")
    LinkSysRouter0.config.interface.wireless.ssid("LinksysRouter")
    LinkSysRouter0.config.interface.wireless.wep()
    LinkSysRouter0.config.interface.wireless.wepkey("0123456789")
    LinkSysRouter0.close()

    util.selectObjectsOnWorkspace(AccessPoint0.x, AccessPoint0.y)
    util.selectObjectsOnWorkspace(LinkSysRouter0.x, LinkSysRouter0.y)
    editMenu.selectEditItem(EditConst.COPY)
    editMenu.selectEditItem(EditConst.PASTE)
    
    CopyAccessPoint0.select()
    CopyAccessPoint0.clickConfigTab()
    CopyAccessPoint0.config.settings.check.displayName("CopyAccess Point0")
    CopyAccessPoint0.config.selectInterface("Port 0")
    CopyAccessPoint0.config.interface.port0.check.bandwidth('Auto', False)
    CopyAccessPoint0.config.interface.port0.check.duplex('Auto', False)
    CopyAccessPoint0.config.interface.port0.check.portStatus(False)
    CopyAccessPoint0.close()

    CopyLinkSysRouter0.select()
    CopyLinkSysRouter0.clickConfigTab()
    CopyLinkSysRouter0.config.settings.check.displayName(CopyLinkSysRouter0.displayName)
    CopyLinkSysRouter0.config.selectInterface("Wireless")
    CopyLinkSysRouter0.config.interface.wireless.check.ssid("LinksysRouter")
    CopyLinkSysRouter0.config.interface.wireless.check.wepkey("0123456789")
    CopyLinkSysRouter0.close()