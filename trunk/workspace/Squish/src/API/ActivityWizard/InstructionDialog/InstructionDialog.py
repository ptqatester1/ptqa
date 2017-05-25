from API.Utility.Util import Util
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from squish import *
def err(msg = ''): raise NotImplementedError(msg)

class OverallFeedback:
    def __init__(self):
        self.util = Util()
    
    def textCheckPoint(self, expected, **kwargs):
        self.util.textCheckPoint(ActivityWizardConst.instructionsDialog.checkResults.overallFeedback.FEEDBACK_TEXT, expected, **kwargs)

class AssessmentItems:
    def __init__(self):
        self.util = Util()
    
    def score(self, expected, **kwargs):
        self.util.textCheckPoint(ActivityWizardConst.instructionsDialog.checkResults.assessmentItems.SCORE_TEXT, expected, **kwargs)
    
    def itemCount(self, expected, **kwargs):
        self.util.textCheckPoint(ActivityWizardConst.instructionsDialog.checkResults.assessmentItems.ITEM_COUNT_TEXT, expected, **kwargs)
    
    def pointsOverview(self, expected, **kwargs):
        self.util.textCheckPoint(ActivityWizardConst.instructionsDialog.checkResults.assessmentItems.SCORE_BREAKDOWN_TEXT, expected, **kwargs)
    
    @property
    def assessmentTreeName(self):
        return ActivityWizardConst.instructionsDialog.checkResults.assessmentItems.ASSESSMENT_TREE
    
class ConnectivityTests:
    def __init__(self):
        self.util = Util()
    
    @property
    def tableName(self):
        return ActivityWizardConst.instructionsDialog.checkResults.connectivityTests.TABLE
    
    @property
    def tableObj(self):
        return findObject(self.tableName)

    def _textCheckPoint(self, text, row, column):
        self.util.textCheckPoint(self.tableName + '.item_%s/%s'%(row, column), text)
        
    def status(self, status, row):
        self._textCheckPoint(status, row, 0)
    
    def testCondition(self, testCondition, row):
        self._textCheckPoint(testCondition, row, 1)
    
    def points(self, points, row):
        self._textCheckPoint(points, row, 2)
    
    def source(self, source, row):
        self._textCheckPoint(source, row, 3)
    
    def destination(self, destination, row):
        self._textCheckPoint(destination, row, 4)
    
    def type(self, type, row):
        self._textCheckPoint(type, row, 5)
        
class Tabs():
    def __init__(self):
        self.util = Util()
    
    def _clickTab(self, tab):
        self.util.clickTab(ActivityWizardConst.instructionsDialog.checkResults.TABBAR, tab)
    
    def overallFeedback(self):
        self._clickTab('Overall Feedback')
    
    def assessmentItems(self):
        self._clickTab('Assessment Items')
    
    def connnectivityTests(self):
        self._clickTab('Connectivity Tests')

class CheckResults:
    def __init__(self):
        self.util = Util()
        self.overallFeedback = OverallFeedback()
        self.assessmentItems = AssessmentItems()
        self.connectivityTests = ConnectivityTests()
        self.tabs = Tabs()
    
    def closeButton(self):
        self.util.clickButton(ActivityWizardConst.instructionsDialog.checkResults.CLOSE_BUTTON)

class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def resetActivityDialog(self):
        return findObject(ActivityWizardConst.instructionsDialog.popups.RESET_ACTIVITY_DIALOG)
    
    def resetActivityOkButton(self):
        self.util.clickButton(ActivityWizardConst.instructionsDialog.popups.RESET_ACTIVITY_OK_BUTTON)
    
    def resetActivityCancelButton(self):
        self.util.clickButton(ActivityWizardConst.instructionsDialog.popups.RESET_ACTIVITY_CANCEL_BUTTON)

class InstructionDialog:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
        self.results = CheckResults()
    
    def waitForCompletionText(self, completionText, maxWaitTime=60):
        for i in range(maxWaitTime):
            obj = findObject(ActivityWizardConst.instructionsDialog.COMPLETION_TEXT)
            if self.util.hasText(str(obj.text), completionText):
                return True
            snooze(1)
        return False
    
    def checkCompletion(self, completionText):
        self.util.textCheckPoint(ActivityWizardConst.instructionsDialog.COMPLETION_TEXT, completionText)
    
    def checkResultsButton(self):
        self.util.clickButton(ActivityWizardConst.instructionsDialog.CHECK_RESULTS_BUTTON)
    
    def resetActivityButton(self):
        self.util.clickButton(ActivityWizardConst.instructionsDialog.RESET_ACTIVITY_BUTTON)
    
    def resetActivity(self):
        self.resetActivityButton()
        if self.popups.resetActivityDialog:
            self.popups.resetActivityOkButton()
    
    def previousPageButton(self):
        self.util.clickButton(ActivityWizardConst.instructionsDialog.PREVIOUS_PAGE_BUTTON)
       
    def nextPageButton(self):
        self.util.clickButton(ActivityWizardConst.instructionsDialog.NEXT_PAGE_BUTTON)
    
    def topCheckbox(self, checked = None):
        checkbox = findObject(ActivityWizardConst.instructionsDialog.TOP_CHECKBOX)
        self.util.checkbox(checkbox, checked)
    
    def textCheckPoint(self, expected, **kwargs):
        self.util.textCheckPoint(ActivityWizardConst.instructionsDialog.INSTRUCTIONS_TEXT, expected, **kwargs)
    
    def getText(self):
        self.util.clearCache(ActivityWizardConst.instructionsDialog.INSTRUCTIONS_WEBVIEW)
        return str(findObject(ActivityWizardConst.instructionsDialog.INSTRUCTIONS_TEXT).innerText)
    
    def close(self):
        self.util.close(ActivityWizardConst.instructionsDialog.DIALOG_WINDOW)