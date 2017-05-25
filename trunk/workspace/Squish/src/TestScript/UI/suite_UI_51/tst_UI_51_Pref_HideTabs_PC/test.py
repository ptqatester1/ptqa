from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import Util
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Hide.HideConst import HideConst

util = Util()
options = Options()

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 200, "PC0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    editOptionsSetting()
    checkpoint2()
    editOptionsSetting()
    checkpoint1()

    
def createTopology():
    pc0.create()
    
def checkpoint1():
    pc0.select()
    pc0.clickDesktopTab()
    snooze(2)
    # Verification Point 'VP1'
    test.compare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_DeskTopTab.scrollArea.qt_scrollarea_viewport.desktopScrollAreaWidgetContents.m_desktopFrame").visible, True)

    # Verification Point 'VP2'
    test.compare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_tabbar").count, 5)
    pc0.close()

def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(HideConst.TAB_BAR, HideConst.HIDE)
    snooze(1)
    util.clickButton(HideConst.HIDE_DESKTOP_TAB)
    snooze(1)
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def checkpoint2():
    pc0.select()
    snooze(2)
    # Verification Point 'VP3'
    test.xcompare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_DeskTopTab").visible, True)
    # Verification Point 'VP4'
    test.compare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_tabbar").count, 4)
    pc0.close()