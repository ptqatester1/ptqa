from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Hide.HideConst import HideConst

util = Util()
options = Options()

r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 100, 200, "Router0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    editOptionsSetting1()
    checkpoint2()
    editOptionsSetting2()
    checkpoint3()
    editOptionsSetting3()
    checkpoint4()
    editOptionsSetting4()
    checkpoint1()
    
def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    util.clickOnSimulation()
    util.clickOnRealtime()
def checkpoint1():
    r0.select()
    snooze(2)
    test.compare(findObject(r0.squishName + ".c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab").visible, True)
    r0.clickConfigTab()
    snooze(2)
    test.compare(findObject(r0.squishName + ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab").visible, True)
    r0.clickCliTab()
    snooze(2)
    test.compare(findObject(r0.squishName + ".c_physicalTab.qt_tabwidget_stackedwidget.m_cliTab").visible, True)
    r0.clickPhysicalTab()
    snooze(2)
    # Verification Point 'VP4'
    test.compare(findObject(r0.squishName + ".c_physicalTab.qt_tabwidget_tabbar").count, 4)
    r0.close()

def editOptionsSetting1():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(HideConst.TAB_BAR, HideConst.HIDE)
    snooze(1)
    util.clickButton(HideConst.HIDE_PHYSICAL_TAB)
    snooze(1)
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def checkpoint2():
    r0.select()
    snooze(2)
    test.compare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_physicalTab").visible, False)
    test.compare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab").visible, True)

    r0.clickCliTab()
    test.compare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_tabbar").count, 3)
    r0.close()
    
def editOptionsSetting2():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(HideConst.TAB_BAR, HideConst.HIDE)
    util.clickButton(HideConst.HIDE_CONFIG_TAB)
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def checkpoint3():
    r0.select()
    test.compare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab").visible, False)
    test.compare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_cliTab").visible, True)    
    test.compare(findObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_tabbar").count, 2)
    r0.close()
    
def editOptionsSetting3():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(HideConst.TAB_BAR, HideConst.HIDE)
    util.clickButton(HideConst.HIDE_CLI_TAB)
    util.close(OptionsConst.OPTIONS_DIALOG)
    
def checkpoint4():
    util.clickOnWorkspace(r0.x, r0.y)
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "All tabs are in Hide mode")
    waitForObject(":Error")
    sendEvent("QCloseEvent", ":Error")
    
def editOptionsSetting4():
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(HideConst.TAB_BAR, HideConst.HIDE)
    util.clickButton(HideConst.HIDE_CLI_TAB)
    util.clickButton(HideConst.HIDE_CONFIG_TAB)
    util.clickButton(HideConst.HIDE_PHYSICAL_TAB)
    util.close(OptionsConst.OPTIONS_DIALOG)
