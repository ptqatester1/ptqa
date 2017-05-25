from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Extensions.ExtensionsConst import ExtensionsConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst
from API.MenuBar.Options.Preferences.Administrative.AdministrativeConst import AdministrativeConst
from API.MenuBar.Options.Preferences.Hide.HideConst import HideConst
from API.MenuBar.Options.Preferences.CustomInterfaces.CustomInterfacesConst import CustomInterfacesConst
from API.MenuBar.Extensions.Multiuser.MultiuserConst import MultiuserConst
util = Util()
options = Options()

def main():
    util.init()
    editOptionsSetting()
    checkpoint()
    uncheckInterfaceLocks()

def editOptionsSetting():

    options.selectOptionsItem(OptionsConst.PREFERENCES)
    options.clickTab(AdministrativeConst.TAB_BAR, AdministrativeConst.ADMINISTRATIVE)
    util.clickButton(AdministrativeConst.HIDE_TAB)
    util.clickButton(AdministrativeConst.MULTIUSER_MENU)
    util.clickButton(AdministrativeConst.IPC_MENU)
    util.clickButton(AdministrativeConst.CUSTOM_INTERFACES_TAB)
    util.clickButton(AdministrativeConst.SCRIPTING_MENU)
    util.clickButton(AdministrativeConst.INTERFACE_TAB)
    util.close(OptionsConst.OPTIONS_DIALOG)

def checkpoint():
    #can't find a way to test menu items being locked
    options.selectOptionsItem(OptionsConst.PREFERENCES)
    snooze(2)
    test.compare(findObject(InterfaceConst.INTERFACE_WINDOW).enabled, False)
    options.clickTab(HideConst.TAB_BAR, HideConst.HIDE)
    snooze(2)
    test.compare(findObject(HideConst.HIDE_WINDOW).enabled, False)
    options.clickTab(HideConst.TAB_BAR, CustomInterfacesConst.CUSTOM_INTERFACES)
    snooze(2)
    test.compare(findObject(CustomInterfacesConst.CUSTOM_INTERFACES_WINDOW).enabled, False)


def uncheckInterfaceLocks():
    options.clickTab(AdministrativeConst.TAB_BAR, AdministrativeConst.ADMINISTRATIVE)
    util.clickButton(AdministrativeConst.INTERFACE_TAB)
    util.clickButton(AdministrativeConst.HIDE_TAB)
    util.clickButton(AdministrativeConst.MULTIUSER_MENU)
    util.clickButton(AdministrativeConst.IPC_MENU)
    util.clickButton(AdministrativeConst.CUSTOM_INTERFACES_TAB)
    util.clickButton(AdministrativeConst.SCRIPTING_MENU)
    util.close(OptionsConst.OPTIONS_DIALOG)
