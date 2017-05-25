from API.ActivityWizard.Welcome.WelcomeConst import WelcomeConst
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Utility.Util import Util

util = Util()

def main():
    util.init()  
    welcome()
    
def welcome():
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    util.textCheckPoint(WelcomeConst.WELCOME_TEXT, "Welcome to the Activity Wizard!")