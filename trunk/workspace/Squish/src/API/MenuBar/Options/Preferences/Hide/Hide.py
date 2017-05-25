##Chris Allen

from API.MenuBar.Options.Preferences.Hide.HideConst import HideConst
from API import functions
from API.Utility.Util import Util
from squish import *

class Hide:
    def __init__(self):
        self.util = Util()
    
    def physicalTabToggle(self, checked = None):
        checkbox = findObject(HideConst.HIDE_PHYSICAL_TAB)
        self.util.checkbox(checkbox, checked)
    
    def allDevicesConfigTabToggle(self, checked = None):
        checkbox = findObject(HideConst.HIDE_CONFIG_TAB)
        self.util.checkbox(checkbox, checked)
    
    def allDevicesCliToggle(self, checked = None):
        checkbox = findObject(HideConst.HIDE_CLI_TAB)
        self.util.checkbox(checkbox, checked)
    
    def routerSwitchConfigToggle(self, checked = None):
        checkbox = findObject(HideConst.HIDE_ROUTER_SWITCH_CONFIG_TAB)
        self.util.checkbox(checkbox, checked)
        
    def routerSwitchCliToggle(self, checked = None):
        checkbox = findObject(HideConst.HIDE_ROUTER_SWITCH_CLI_TAB)
        self.util.checkbox(checkbox, checked)
    
    def servicesTab(self, checked = None):
        checkbox = findObject(HideConst.HIDE_SERVICES_TAB)
        self.util.checkbox(checkbox, checked)
    
    def desktopTab(self, checked = None):
        checkbox = findObject(HideConst.HIDE_DESKTOP_TAB)
        self.util.checkbox(checkbox, checked)
    
    def guiTab(self, checked = None):
        checkbox = findObject(HideConst.HIDE_GUI_TAB)
        self.util.checkbox(checkbox, checked)
    
    def wirelessCellConnection(self, checked = None):
        checkbox = (HideConst.HIDE_WIRELESS_CELLULAR_CONNECTION)
        self.util.checkbox(checkbox, checked)
    
    def legacyEquipment(self, checked = None):
        checkbox = findObject(HideConst.HIDE_LEGACY_EQUIPMENT)
        self.util.checkbox(checkbox, checked)
    
    def showAdvancedModeByDefaultForThingsToggle(self, checked = None):
        checkbox = findObject(HideConst.SHOW_ADVANCED_MODE_BY_DEFAULT_FOR_THINGS)
        self.util.checkbox(checkbox, checked)