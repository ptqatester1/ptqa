from API.MenuBar.Edit.EditConst import EditConst
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.Hub.Hub import Hub

from API.Device.Repeater.Repeater import Repeater


from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar

util = Util()
editMenu = Edit()
commonToolsBar = CommonToolsBar()


CopyHub0 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 100, 50, "CopyHub0")
CopyRepeater0 = Repeater(ComponentBoxConst.DeviceModel.REPEATER_PT, 200, 50, "CopyRepeater0")
Hub0 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 100, 100, "Hub0")
Repeater0 = Repeater(ComponentBoxConst.DeviceModel.REPEATER_PT, 200,100, "Repeater0")

def main():
    util.init()
    copyPaste_deviceOnWorkspace()



def copyPaste_deviceOnWorkspace():
    util.createDevice(ComponentBoxConst.DeviceType.HUB, Hub0.model, Hub0.x, Hub0.y)    
    util.createDevice(ComponentBoxConst.DeviceType.HUB, Repeater0.model, Repeater0.x, Repeater0.y)    

    util.selectObjectsOnWorkspace(Hub0.x, Hub0.y)
    util.selectObjectsOnWorkspace(Repeater0.x, Repeater0.y)
    snooze(2)
    editMenu.selectEditItem(EditConst.COPY)
    editMenu.selectEditItem(EditConst.PASTE)

    util.clickOnWorkspace(CopyHub0.x, CopyHub0.y)
    CopyHub0.updateName()
    CopyHub0.clickConfigTab()
    CopyHub0.config.settings.check.displayName("CopyHub0")

    util.clickOnWorkspace(CopyRepeater0.x, CopyRepeater0.y)
    CopyRepeater0.updateName()
    CopyRepeater0.clickConfigTab()
    CopyRepeater0.config.settings.check.displayName("CopyRepeater0")

