from API.ComponentBox import ComponentBoxConst
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Device.DeviceBase import DeviceBaseConst
from API.Utility.Util import Util
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Hide.HideConst import HideConst

util = Util()
options = Options()

linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 100, 200, "Wireless Router0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    editOptionsSetting()
    checkpoint2()
    editOptionsSetting()
    checkpoint1()
    
def createTopology():
    linksys.create()
    
def checkpoint1():
    linksys.select()
    snooze(1)
    test.compare(findObject(linksys.squishName + DeviceBaseConst.DeviceTabs.DEVICE_TAB).count, 4)
    linksys.close()

def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(HideConst.TAB_BAR, HideConst.HIDE)
    snooze(1)
    util.clickButton(HideConst.HIDE_GUI_TAB)
    snooze(1)
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def checkpoint2():
    linksys.select()
    snooze(1)
    test.compare(findObject(linksys.squishName + DeviceBaseConst.DeviceTabs.DEVICE_TAB).count, 3)