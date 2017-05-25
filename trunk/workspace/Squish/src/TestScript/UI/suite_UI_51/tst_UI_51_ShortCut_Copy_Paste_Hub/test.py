from API.MenuBar.Edit.EditConst import EditConst
from API.MenuBar.Edit.Edit import Edit
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.Hub.Hub import Hub

from API.Device.Repeater.Repeater import Repeater

from API.Utility import UtilConst
from API.MenuBar.File.File import File
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.File.FileConst import FileConst
util = Util()
editMenu = Edit()
commonToolsBar = CommonToolsBar()
fileMenu = File()
 
CopyHub0 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 100, 50, "CopyHub0")
CopyRepeater0 = Repeater(ComponentBoxConst.DeviceModel.REPEATER_PT, 200, 50, "CopyRepeater0")
Hub0 = Hub(ComponentBoxConst.DeviceModel.HUB_PT, 100, 100, "Hub0")
Repeater0 = Repeater(ComponentBoxConst.DeviceModel.REPEATER_PT, 200,100, "Repeater0")

def main():
    util.init()
    copyPaste_deviceOnWorkspace()



def copyPaste_deviceOnWorkspace():
    Hub0.create()    
    Repeater0.create()    

    util.selectObjectsOnWorkspace(Hub0.x, Hub0.y)
    util.selectObjectsOnWorkspace(Repeater0.x, Repeater0.y)
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.SAVE_NETWORK_PROMPT_CANCEL)
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+C>")
    util.typeText(UtilConst.WORKSPACE, "<Ctrl+V>")

    CopyHub0.select()
    CopyHub0.clickConfigTab()
    CopyHub0.config.settings.check.displayName("CopyHub0")

    CopyRepeater0.select()
    CopyRepeater0.clickConfigTab()
    CopyRepeater0.config.settings.check.displayName("CopyRepeater0")