##Chris Allen

from API.Utility.Util import Util
from API.ActivityWizard.Exit.ExitConst import ExitConst
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.MenuBar.File.New.NewConst import NewConst
import object
from squish import *

class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def exitDialog(self):
        try:
            return findObject(ExitConst.EXIT_DIALOG_WINDOW)
        except LookupError, e:
            return False
    
    def exitYesButton(self):
        self.util.clickButton(ExitConst.EXIT_DIALOG_YES)
    
    def exitNoButton(self):
        self.util.clickButton(ExitConst.EXIT_DIALOG_NO)

    @property
    def saveNetworkDialog(self):
        try:
            return findObject(NewConst.SAVE_NETWORK_PROMPT)
        except LookupError, e:
            return False
    
    def saveNetworkYes(self):
        self.util.clickButton(NewConst.SAVE_NETWORK_PROMPT_YES)
    
    def saveNetworkNo(self):
        self.util.clickButton(NewConst.SAVE_NETWORK_PROMPT_NO)
    
    def saveNetworkCancel(self):
        self.util.clickButton(NewConst.SAVE_NETWORK_PROMPT_CANCEL)

class Exit:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
        
    def exitButton(self):
        self.util.clickButton(ActivityWizardConst.EXIT)
    
    def exit(self):
        self.exitButton()
        if self.popups.saveNetworkDialog:
            self.popups.saveNetworkNo()
        if self.popups.exitDialog:
            self.popups.exitYesButton()