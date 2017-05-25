##Chris Allen

from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.Utility.Util import Util
from squish import *
import object

class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def exitTestModeDialog(self):
        try:
            return findObject(ActivityWizardConst.testActivity.EXIT_TEST_MODE_DIALOG)
        except LookupError, e:
            return False
    
    def exitTestModeYesButton(self):
        self.util.clickButton(ActivityWizardConst.testActivity.EXIT_TEST_MODE_YES)
    
    def exitTestModeNoButton(self):
        self.util.clickButton(ActivityWizardConst.testActivity.EXIT_TEST_MODE_NO)

class TestActivity:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()

    def returnToAW(self, popupYes = True):
        self.util.click(ActivityWizardConst.testActivity.ACTIVITY_WIZARD_ICON)
        if self.popups.exitTestModeDialog:
            if popupYes:
                self.popups.exitTestModeYesButton()
            else:
                self.popups.exitTestModeNoButton()