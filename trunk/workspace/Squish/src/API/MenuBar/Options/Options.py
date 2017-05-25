#**************************************************************************
#@author: Tuan Hoang
#@summary: Options handles the Options menu
#**************************************************************************
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Interface.InterfaceConst import InterfaceConst
from API.MenuBar.Options.Preferences.Miscellaneous.MiscellaneousConst import MiscellaneousConst
from API.MenuBar.Options.Preferences.PreferencesConst import PreferencesConst
from API.SquishSyntax import SquishSyntax
from squish import *

class Options(SquishSyntax):
    #@summary: Selects p_item from the Options menu
    #@param p_item: Preferences
    def selectOptionsItem(self, p_item):
        self.activateItem(OptionsConst.MENU_BAR, "Options")
        self.activateItem(OptionsConst.OPTIONS, p_item)
        
    def turnOnLinkLights(self):
        self.selectOptionsItem(OptionsConst.PREFERENCES)
        snooze(1)
        if (findObject(InterfaceConst.SHOW_LINK_LIGHTS).checked):
            pass
        else:
            self.clickButton(InterfaceConst.SHOW_LINK_LIGHTS)        
        self.close(OptionsConst.PREFERENCES_WINDOW)
        
    def autoClearEventList(self):
        self.selectOptionsItem(OptionsConst.PREFERENCES)
        self.clickTab(PreferencesConst.TAB_BAR, PreferencesConst.MISCELLANEOUS)
        snooze(1)
        if (findObject(MiscellaneousConst.AUTO_CLEAR_EVENT_LIST).checked):
            pass
        else:
            self.clickButton(MiscellaneousConst.AUTO_CLEAR_EVENT_LIST)        
        self.close(OptionsConst.PREFERENCES_WINDOW)
        
    def promptEventList(self):
        self.selectOptionsItem(OptionsConst.PREFERENCES)
        self.clickTab(PreferencesConst.TAB_BAR, PreferencesConst.MISCELLANEOUS)
        snooze(1)
        if (findObject(MiscellaneousConst.PROMPT).checked):
            pass
        else:
            self.clickButton(MiscellaneousConst.PROMPT)        
        self.close(OptionsConst.PREFERENCES_WINDOW)