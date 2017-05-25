#######################
#@author: Pamela Vinco
#######################
from API.MenuBar.Tools.Tools import Tools
from API.MenuBar.Tools.ToolsConst import ToolsConst
from API.Toolbar.MainToolBar.CustomDeviceWindowConst import CustomDeviceWindowConst
from API.Toolbar.MainToolBar.PaletteWindowConst import PaletteWindowConst
from API.Utility.Util import Util

#Function initialization
util = Util()
toolsMenu = Tools()

def main():
    util.init()
    tools_drawingPalette()
    tools_customDevicesDialog()
    
def tools_drawingPalette():
    #Select Drawing Palette from the Tools Menu and check that the Drawing Palette Window appears
    toolsMenu.selectToolsItem(ToolsConst.DRAWING_PALETTE)
    snooze(1)
    if(object.exists(PaletteWindowConst.PALETTE_WINDOW)):
        test.passes("Palette Window found")
        util.close(PaletteWindowConst.PALETTE_WINDOW)
    else:
        test.fail("Palette Window not found")
        
def tools_customDevicesDialog():
    #Select Custom Devices Dialog from the Tools Menu and check that the Custom Devices Dialog appears
    toolsMenu.selectToolsItem(ToolsConst.CUSTOM_DEVICE_DIALOG)
    snooze(1)
    if(object.exists(CustomDeviceWindowConst.CUSTOM_DEVICE_WINDOW)):
        test.passes("Custom Device Window found")
        util.close(CustomDeviceWindowConst.CUSTOM_DEVICE_WINDOW)
    else:
        test.fail("Custom Device Window not found")