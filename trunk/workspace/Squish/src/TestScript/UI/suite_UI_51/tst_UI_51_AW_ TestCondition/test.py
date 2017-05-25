from API.Utility import UtilConst
from API.Utility.Util import Util
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.ActivityWizard.AnswerNetwork.AnswerNetworkConst import AnswerNetworkConst
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.Utility.Util import UtilConst
from API.ActivityWizard.TestActivity.TestActivityConst import TestActivityConst

#Function initialization
util = Util()

def main():
    util.init()
    openFile()
    goToActivityWizard()
    checkpoint()
 
def openFile():
    util.open("UI41AnswerNetwork.pka", "UI")
    
def goToActivityWizard():
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    if (object.exists(ActivityWizardConst.USE_AS_ANSWER_NETWORK_DIALOG)):
        util.clickButton(ActivityWizardConst.USE_AS_ANSWER_NETWORK_NO)    
    
def checkpoint():
    util.clickButton(ActivityWizardConst.ANSWER_NETWORK)
    util.clickTab(AnswerNetworkConst.TAB_BAR, AnswerNetworkConst.CONNECTIVITY_TEST)
    util.clickItem(AnswerNetworkConst.CONNECTIVITY_COMBO_BOX, "Successful")
    util.clickButton(ActivityWizardConst.CHECK_ACTIVITY)
    util.clickButton(TestActivityConst.CHECK_RESULTS)
    snooze(1)
    util.textCheckPoint(TestActivityConst.ACTIVITY_RESULTS_OVERALL_FEEDBACK_TEXT, "This activity is incomplete, please try again")

    util.clickButton(TestActivityConst.ACTIVITY_RESULTS_CLOSE)
    util.mousePress(TestActivityConst.ACTIVITY_WIZARD_ICON, 50, 50)
    snooze(3)
    util.clickButton(TestActivityConst.EXIT_TEST_MODE_YES)
    
    util.clickButton(ActivityWizardConst.ANSWER_NETWORK)
    util.clickTab(AnswerNetworkConst.TAB_BAR, AnswerNetworkConst.CONNECTIVITY_TEST)
    util.clickItem(AnswerNetworkConst.CONNECTIVITY_COMBO_BOX, "Fail")
    util.clickButton(ActivityWizardConst.CHECK_ACTIVITY)
    util.clickButton(TestActivityConst.CHECK_RESULTS)
    snooze(1)
    util.textCheckPoint(TestActivityConst.ACTIVITY_RESULTS_OVERALL_FEEDBACK_TEXT, "Well Done")

    util.clickButton(TestActivityConst.ACTIVITY_RESULTS_CLOSE)
    util.mousePress(TestActivityConst.ACTIVITY_WIZARD_ICON, 50, 50)
    snooze(3)
    util.clickButton(TestActivityConst.EXIT_TEST_MODE_YES)
    
    util.clickButton(ActivityWizardConst.ANSWER_NETWORK)
    util.clickTab(AnswerNetworkConst.TAB_BAR, AnswerNetworkConst.CONNECTIVITY_TEST)
    util.clickItem(AnswerNetworkConst.CONNECTIVITY_COMBO_BOX, "Do Not Test")
    util.clickButton(ActivityWizardConst.CHECK_ACTIVITY)
    util.clickButton(TestActivityConst.CHECK_RESULTS)
    snooze(1)
    util.textCheckPoint(TestActivityConst.ACTIVITY_RESULTS_OVERALL_FEEDBACK_TEXT, "Well Done")