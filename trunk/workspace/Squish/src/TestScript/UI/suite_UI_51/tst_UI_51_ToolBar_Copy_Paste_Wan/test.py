from API.MenuBar.Edit.EditConst import EditConst
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.Modem.Modem import Modem

from API.Device.Cloud.Cloud import Cloud

from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
util = Util()
editMenu = Edit()
commonToolsBar = CommonToolsBar()
 
CopyCableModem0 = Modem(ComponentBoxConst.DeviceModel.CABLE_MODEM, 100, 50, "CopyCable Modem0")
CopyDSLModem0 = Modem(ComponentBoxConst.DeviceModel.DSL_MODEM, 200, 50, "CopyDSL Modem0")
CopyCloud0 = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 300, 50, "CopyCloud0")
CopyCloud1 = Cloud(ComponentBoxConst.DeviceModel.CLOUD_EMPTY, 400, 50, "CopyCloud1")

CableModem0 = Modem(ComponentBoxConst.DeviceModel.CABLE_MODEM, 100, 100, "Cable Modem0")
DSLModem0 = Modem(ComponentBoxConst.DeviceModel.DSL_MODEM, 200, 100, "DSL Modem0")
Cloud0 = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 300, 100, "Cloud0")
Cloud1 = Cloud(ComponentBoxConst.DeviceModel.CLOUD_EMPTY, 400, 100, "Cloud1")

def main():
    util.init()
    copyPaste_deviceOnWorkspace()


def copyPaste_deviceOnWorkspace():
    for dev in [Cloud0, Cloud1, CableModem0, DSLModem0]:
        dev.create()
        
    Cloud0.select()
    Cloud0.clickConfigTab()
    Cloud0.config.selectInterface('DSL')
    Cloud0.config.connections.dsl.add("Modem4", "Ethernet6")
    Cloud0.config.selectInterface("Serial0")
    Cloud0.config.interface.serial.add("100", "100")  
    Cloud0.config.selectInterface("Modem4")
    Cloud0.config.interface.modem.phoneNumber("555")
    Cloud0.close()
    
    for dev in [Cloud0, Cloud1, CableModem0, DSLModem0]:
        util.selectObjectsOnWorkspace(dev.x, dev.y)
    
    util.clickButton(MainToolbarConst.COPY)
    util.clickButton(MainToolbarConst.PASTE)

    

    CopyCableModem0.select()
    CopyCableModem0.clickConfigTab()
    CopyCableModem0.config.settings.check.displayName("CopyCable Modem0")
    CopyCableModem0.close()
    
    CopyDSLModem0.select()
    CopyDSLModem0.clickConfigTab()
    CopyDSLModem0.config.settings.check.displayName("CopyDSL Modem0")
    CopyDSLModem0.close()
    
    CopyCloud0.select()
    CopyCloud0.clickConfigTab()
    CopyCloud0.config.settings.check.displayName(CopyCloud0.displayName)
    CopyCloud0.config.selectInterface("Modem4")
    CopyCloud0.config.interface.modem.check.phoneNumber("555")
    CopyCloud0.close()
    
    CopyCloud1.select()
    CopyCloud1.clickConfigTab()
    CopyCloud1.config.settings.check.displayName(CopyCloud1.displayName)