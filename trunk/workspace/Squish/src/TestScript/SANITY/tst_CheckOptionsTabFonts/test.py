##Chris Allen
##Sanity check to make sure that all the options tabs are there and functioning

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.PreferencesConst import PreferencesConst as pConst
from API.MenuBar.Options.Preferences.Font.FontConst import FontConst as fConst
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst

util = Util()
opt = Options()

fonts = [fConst.CLI_FONT_NAME]

fontSize = [fConst.CLI_FONT_SIZE]

fontColors = [fConst.ROUTER_IOS_TEXT, fConst.PC_CONSOLE_TEXT]
bgColors = [fConst.ROUTER_IOS_BACKGROUND, fConst.PC_CONSOLE_BACKGROUND]

r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")


def main():
    changeFonts()
    changeSize()
    changeCLIBGColor()
    changeCLITextColor()
    check()

def cleanup():
    resetDefaults()
    test.log("Cleanup Finished")
    
def changeFonts():
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(pConst.TAB_BAR, pConst.FONT)
    for item in fonts:
        util.clickItem(item, "Courier")
        
def changeSize():
    for item in fontSize:
        util.clickItem(item, "16")
        
def changeCLIBGColor():
    for item in bgColors:
        util.clickItem(item, "Black")
        
def changeCLITextColor():
    for item in fontColors:
        util.clickItem(item, "White")
        
def check():
    util.clickButton(fConst.APPLY_BUTTON)
    util.close(OptionsConst.PREFERENCES_WINDOW)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r1.model, r1.x, r1.y)
    util.fastForwardTime()
    r1.select()
    r1.clickCliTab()
    
    r1Properties = findObject(r1.squishName + RouterConst.DeviceBaseConst.Cli.CLI_CONSOLE)
    if(r1Properties.font.family == "Courier"):
        test.passes("The font was correctly changed")
    else:
        test.fail("The font was not correctly changed")
    if(r1Properties.font.pointSize == 16):
        test.passes("The font size is correct")
    else:
        test.fail("The font size is not correct")
        
def resetDefaults():
    if(object.exists(OptionsConst.PREFERENCES_WINDOW)):
        util.close(OptionsConst.PREFERENCES_WINDOW)
    util.init()
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(pConst.TAB_BAR, pConst.FONT)
    util.clickButton(fConst.RESET_BUTTON)
    util.clickButton(fConst.APPLY_BUTTON)
    util.close(OptionsConst.PREFERENCES_WINDOW)