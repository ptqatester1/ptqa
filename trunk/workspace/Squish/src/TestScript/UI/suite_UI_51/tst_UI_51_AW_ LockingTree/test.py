from API.Utility.Util import Util
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
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
    util.open("UI41AnswerNetwork.pka", UtilConst.UI_TEST)
    
def goToActivityWizard():
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    if (object.exists(ActivityWizardConst.USE_AS_ANSWER_NETWORK_DIALOG)):
        util.clickButton(ActivityWizardConst.USE_AS_ANSWER_NETWORK_NO)  
        
def checkpoint():
    #Check that the Results and Connectivity Tabs are locked 
    util.clickButton(ActivityWizardConst.TEST_ACTIVITY)
    util.clickButton(TestActivityConst.CHECK_RESULTS)
    util.clickTab(TestActivityConst.ACTIVITY_RESULTS_TABBAR, TestActivityConst.ACTIVITY_RESULTS_CONNECTIVITY_TESTS)
    test.compare(findObject(TestActivityConst.ACTIVITY_RESULTS_OVERALL_FEEDBACK_TAB).enabled, True)
    test.compare(findObject(TestActivityConst.ACTIVITY_RESULTS_ASSESSMENT_ITEMS_TAB).enabled, False)
    test.compare(findObject(TestActivityConst.ACTIVITY_RESULTS_CONNECTIVITY_TESTS_TAB).enabled, False)