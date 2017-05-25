from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.Utility.Util import Util

class Welcome:
    def __init__(self):
        self.util = Util()

    def select(self):
        '''Click welcome button'''
        self.util.clickButton(ActivityWizardConst.WELCOME)
    
    def editAuthorInformation(self, text):
        self.util.setText(ActivityWizardConst.welcome.AUTHOR_INFO_CONTENT, text)
    
    def textCheckPoint(self, expected, **kwargs):
        self.util.textCheckPoint(ActivityWizardConst.welcome.AUTHOR_INFO_CONTENT, expected, **kwargs)