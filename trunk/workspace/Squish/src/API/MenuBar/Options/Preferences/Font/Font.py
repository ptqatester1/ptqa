##Chris Allen

from API.MenuBar.Options.Preferences.Font.FontConst import FontConst
from API.Utility.Util import Util
from squish import *

class Font:
    def __init__(self):
        self.util = Util()
        
    def setCLIFontName(self, p_squishName):
        self.util.clickItem(FontConst.CLI_FONT_NAME_SELECT, p_squishName)

    def setCLIFontSize(self, p_size):
        self.util.clickItem(FontConst.CLI_FONT_SIZE_SELECT, p_size)

    def setHeadersFontName(self, p_squishName):
        self.util.clickItem(FontConst.HEADERS_FONT_NAME_SELECT, p_squishName)

    def setHeadersFontSize(self, p_size):
        self.util.clickItem(FontConst.HEADERS_FONT_SIZE_SELECT, p_size)

    def setWorkspaceFontName(self, p_squishName):
        self.util.clickItem(FontConst.WORKSPACE_FONT_NAME_SELECT, p_squishName)

    def setWorkspaceFontSize(self, p_size):
        self.util.clickItem(FontConst.WORKSPACE_FONT_SIZE_SELECT, p_size)

    def setActivityWizardFontName(self, p_squishName):
        self.util.clickItem(FontConst.ACTIVITY_WIZARD_FONT_NAME_SELECT, p_squishName)

    def setActivityWizardFontSize(self, p_size):
        self.util.clickItem(FontConst.ACTIVITY_WIZARD_FONT_SIZE_SELECT, p_size)

    def setFileMenuFontName(self, p_squishName):
        self.util.clickItem(FontConst.FILE_MENU_FONT_NAME_SELECT, p_squishName)

    def setFileMenuFontSize(self, p_size):
        self.util.clickItem(FontConst.FILE_MENU_FONT_SIZE_SELECT, p_size)

    def setTabSwitchesFontName(self, p_squishName):
        self.util.clickItem(FontConst.TAB_SWITCHES_FONT_NAME_SELECT, p_squishName)

    def setTabSwitchesFontSize(self, p_size):
        self.util.clickItem(FontConst.TAB_SWITCHES_FONT_SIZE_SELECT, p_size)

    def setTooltipsFontName(self, p_squishName):
        self.util.clickItem(FontConst.TOOLTIPS_FONT_NAME_SELECT, p_squishName)

    def setTooltipsFontSize(self, p_size):
        self.util.clickItem(FontConst.TOOLTIPS_FONT_SIZE_SELECT, p_size)

    def setButtonLabelsFontName(self, p_squishName):
        self.util.clickItem(FontConst.BUTTON_LABELS_FONT_NAME_SELECT, p_squishName)

    def setButtonLabelsFontSize(self, p_size):
        self.util.clickItem(FontConst.BUTTON_LABELS_FONT_SIZE_SELECT, p_size)

    def setButtonLabelsFontSize(self, p_size):
        self.util.clickItem(FontConst.BUTTON_LABELS_FONT_SIZE_SELECT, p_size)

    def setRouterIosTextColor(self, p_color):
        self.util.clickItem(FontConst.ROUTER_IOS_TEXT, p_color)

    def setRouterIosBackgroundColor(self, p_color):
        self.util.clickItem(FontConst.ROUTER_IOS_BACKGROUND, p_color)

    def setPCIosTextColor(self, p_color):
        self.util.clickItem(FontConst.PC_CONSOLE_TEXT, p_color)

    def setPCIosBackgroundColor(self, p_color):
        self.util.clickItem(FontConst.PC_CONSOLE_BACKGROUND, p_color)
        
    def setApplicationScale(self, p_size):
        if not float(p_size) in range(8, 21):
            raise ValueError('Must be and integer between 8 and 20')
        fontSize = float(str(findObject(FontConst.SCALE_SLIDER_CURRENT_SIZE).text))
        slider = findObject(FontConst.SCALE_SLIDER)
        if float(p_size) > fontSize:
            while (p_size) > fontSize:
                slider.value = slider.value + 1
                fontSize = float(str(findObject(FontConst.SCALE_SLIDER_CURRENT_SIZE).text))
        elif float(p_size) < fontSize:
            while (p_size) < fontSize:
                slider.value = slider.value - 1
                fontSize = float(str(findObject(FontConst.SCALE_SLIDER_CURRENT_SIZE).text))
            
    def apply(self):
        self.util.clickButton(FontConst.APPLY_BUTTON)
    
    def reset(self):
        self.util.clickButton(FontConst.RESET_BUTTON)