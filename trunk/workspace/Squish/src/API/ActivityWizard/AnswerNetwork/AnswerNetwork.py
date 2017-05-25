##Chris Allen

from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.Utility.Util import Util
from squish import *
import re
import object
from __builtin__ import object as Object#importing object means this has to be import as Object

class AssessmentTreeRowItem:
    def __init__(self, squishName, assessmentItem, points, components, feedback, itemName):
        self.squishName = squishName
        self.assessmentItem = assessmentItem
        self.points = points
        self.components = components
        self.feedback = feedback
        self.itemName = itemName#Name in "Network.Device.Attribute" format
        
class AssessmentTree(Object):#Must import object for inheritance
    def __init__(self):
        self.util = Util()
    
    @property
    def treeName(self):
        return ActivityWizardConst.answerNetwork.ASSESSMENT_ITEMS_TREE
    
    @property
    def treeObject(self):
        return findObject(self.treeName)
    
    def _setTreeItemText(self, text):
        lineedit = self.treeName + '.qt_scrollarea_viewport.QExpandingLineEdit1'
        self.util.setText(lineedit, text)
        self.util.click(ActivityWizardConst.TITLE)#To ensure the text is saved
    
    def _expandViewArea(self):
        awWindow = findObject(ActivityWizardConst.ACTIVITY_WIZARD_WINDOW)
        if not awWindow.windowState() == Qt.WindowMaximized:
            self.util.maximizeWindow(awWindow)
        findObject(ActivityWizardConst.answerNetwork.ASSESSMENT_ITEMS_TREE_HEADER).setResizeMode(0, QHeaderView.Stretch)#Make the tree stretch
    
    def _expandItem(self, currentItem, squishName):
        if currentItem.collapsed:
            self.util.clickItem_x_y(self.treeObject, squishName, p_x=-10, p_y=5)
    
    def _findItemInTree(self, *children):
        self._expandViewArea()#Make the window and header area larger
        itemStrings = []
        currentSquishName = ''
        parentObj = self.treeObject
        parentName = self.treeName
        counter = 0
        for child in children:
            childFound = False
            for item in object.children(parentObj):
                try:
                    currentItem = findObject(parentName + '.item_' + str(counter) + '/0')
                except LookupError, e:
                    print(e)
                if 'text' in object.properties(currentItem):
                    if currentItem.text == child or (re.search(child, str(currentItem.text)) and child is children[-1]) and currentItem.column == 0: 
                        if child is children[-1]:
                            None
                        childFound = True
                        parentObj = currentItem
                        parentName += '.item_' + str(counter) + '/0'
                        itemStrings.append(currentItem.text)
                        currentSquishName = '.'.join(itemStrings)
                        counter = 0#Reset counter once object is found
                        if not child is children[-1]:#Last object shows as always shows as collapsed 
                            self._expandItem(currentItem, currentSquishName)
                        break
                    elif currentItem.column == 0:
                        counter += 1
            if not childFound:
                raise ValueError('Could not find child: %s'%(child,))
        assessmentItemsObj = parentObj
        pointsObj = findObject(parentName[:-1] + '1')
        componentsObj = findObject(parentName[:-1] + '2')
        feedbackObj = findObject(parentName[:-1] + '3')
        rowItem = AssessmentTreeRowItem(parentName, assessmentItemsObj, pointsObj, componentsObj, feedbackObj, '.'.join(itemStrings))
        return rowItem
    
    def getItem(self, parentItem = 'Network', *children):
        children = (parentItem,) + children
        return self._findItemInTree(*children)
        
    def checkItem(self, checked, parentItem = 'Network', *children):
        children = (parentItem,) + children
        item = self._findItemInTree(*children)
        self.util.checkbox(item.assessmentItem, checked)
    
    def changeItemValue(self, value, parentItem = 'Network', *children):
        children = (parentItem,) + children
        item = self._findItemInTree(*children)
        #Below item.itemName had to be used for squish to click the correct place
        valueObject = item.itemName
        ipRegex = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        if re.search(ipRegex, valueObject):
            startOfString = item.itemName[:item.itemName.find(':')]
            ip = item.itemName[item.itemName.find(':'):]
            valueObject = startOfString + '\\.'.join(ip.split('.'))
            
        self.util.doubleClickItem_x_y(self.treeName, valueObject, 60, 5)#60 and 5 are just arbitrary numbers that should click about half way in the edit box
        self._setTreeItemText(value)
        
    def changeItemComponentValue(self, value, parentItem = 'Network', *children):
        children = (parentItem,) + children
        item = self._findItemInTree(*children)
        self.util.doubleClick(item.components)
        self._setTreeItemText(str(value))
    
    def changeItemPoints(self, points, parentItem = 'Network', *children):
        children = (parentItem,) + children
        item = self._findItemInTree(*children)
        self.util.doubleClick(item.points)
        self._setTreeItemText(str(points))

class AssessmentTreeTab:
    def __init__(self):
        self.util = Util()
        self.assessmentItems = AssessmentTree()
        
    def keyword(self, keyword):
        self.util.setText(ActivityWizardConst.answerNetwork.KEYWORD_TEXTFIELD, keyword)
    
    def filterButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.FILTER_BUTTON)
        
    def expandCollapseAllButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.EXPAND_COLLAPSE_ALL_BUTTON)
    
    def showCheckedOnly(self, checked = None):
        checkbox = findObject(ActivityWizardConst.answerNetwork.SHOW_CHECKED_ONLY_CHBOX)
        self.util.checkbox(checkbox, checked)
    
class ConnectivityTestTab:
    def __init__(self):
        self.util = Util()
    
    @property
    def tableName(self):
        return ActivityWizardConst.answerNetwork.CONNECTIVITY_TABLE
    
    @property
    def tableObject(self):
        return findObject(self.tableName)
    
    def _setTableItemText(self, text, row, column):
        item = self.tableName + '.item_' + str(row) + '/' + str(column)
        self.util.doubleClick(item)
        self.util.setText(ActivityWizardConst.answerNetwork.CONNECTIVITY_LINE_EDIT, text)
        if not column == 1:
            self.util.click(item[:-1] + '1')#Click in the 1st column to clear
        else:
            self.util.click(item[:-1] + '2')#If it is the 1st column click in the 2nd to clear
    
    def _setTableComboValue(self, value, row):
        row += 1#Combo box numbering starts at 1
        self.util.clickItem(ActivityWizardConst.answerNetwork.CONNECTIVITY_COMBO_BOX[:-1] + str(row), value)
    
    def testCondition(self, condition, row):
        self._setTableComboValue(condition, row)
    
    def point(self, points, row):
        self._setTableItemText(points, row, 1)
    
    def lastStatus(self, status, row):
        self._setTableItemText(status, row, 2)
    
    def source(self, src, row):
        self._setTableItemText(src, row, 3)
    
    def destination(self, dst, row):
        self._setTableItemText(dst, row, 4)
    
    def type(self, type, row):
        self._setTableItemText(type, row, 5)
    
    def color(self, color, row):
        self._setTableItemText(color, row, 6)
    
    def time(self, time, row):
        self._setTableItemText(time, row, 7)
    
    def periodic(self, val, row):
        self._setTableItemText(val, row, 8)
    
    def num(self, num, row):
        self._setTableItemText(num, row, 9)
    
    def newTest(self, condition, points, lastStatus, source, destination, type, color, time, periodic, num, row):
        self.testCondition(condition, row)
        self.point(points, row)
        self.lastStatus(status, row)
        self.source(src, row)
        self.destination(dst, row)
        self.type(type, row)
        self.color(color, row)
        self.time(time, row)
        self.periodic(val, row)
        self.num(num, row)
    
class ScoringModelWorkProductFeaturesDialog:
    def __init__(self):
        self.util = Util()
    
    @property
    def dialogWindow(self):
        try:
            return findObject(ActivityWizardConst.answerNetwork.WORKPRODUCT_WINDOW)
        except LookupError, e:
            return False
    
    def name(self, name):
        self.util.setText(ActivityWizardConst.answerNetwork.WORKPRODUCT_NAME, name)
    
    def description(self, description):
        self.util.setText(ActivityWizardConst.answerNetwork.WORKPRODUCT_DESCRIPTION, description)
    
    def limitAssessmentItmes(self, checked = None):
        checkbox = findObject(ActivityWizardConst.answerNetwork.WORKPRODUCT_LIMIT_CHECKBOX)
        self.util.checkbox(checkbox, checked)
    
    def expressions(self, expressions):
        self.util.setText(ActivityWizardConst.answerNetwork.WORKPRODUCT_EXPRESSION)
    
    def okButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.WORKPRODUCT_OK)
    
    def cancelButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.WORKPRODUCT_CANCEL)

class ScoringModelWorkProductFeatures:
    def __init__(self):
        self.util = Util()
        self.editDialog = ScoringModelWorkProductFeaturesDialog()
    
    def addButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.WORKPRODUCT_ADD)
    
    def removeButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.WORKPRODUCT_DELETE)
    
    def downButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.WORKPRODUCT_DOWN)
    
    def upButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.WORKPRODUCT_UP)
    
    def editButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.WORKPRODUCT_EDIT)
    
    @property
    def featureListName(self):
        return ActivityWizardConst.answerNetwork.WORKPRODUCT_LIST
    
    @property
    def featureList(self):
        return findObject(self.featureListName)

    def selectRow(self, row):
        self.util.click(self.featureListName + '.item_%s/0'%(row,))

class ScoringModelScoringRulesDialog:
    def __init__(self):
        self.util = Util()
    
    def type(self, type):
        self.util.clickItem(ActivityWizardConst.answerNetwork.SCORING_RULE_TYPE_DROPDOWN, type)
    
    def name(self, name):
        self.util.setText(ActivityWizardConst.answerNetwork.SCORING_RULE_NAME, name)
    
    def description(self, description):
        self.util.setText(ActivityWizardConst.answerNetwork.SCORING_RULE_DESCRIPTION, description)
    
    def expressions(self, expressions):
        self.util.setText(ActivityWizardConst.answerNetwork.SCORING_RULE_EXPRESSION, expressions)
    
    def okButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SCORING_RULE_OK)
    
    def cancelButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SCORING_RULE_CANCEL)
    
    @property
    def editDialog(self):
        try:
            return findObject(ActivityWizardConst.answerNetwork.SCORING_RULE_WINDOW)
        except LookupError, e:
            return False

class ScoringModelScoringRules:
    def __init__(self):
        self.util = Util()
        self.editDialog = ScoringModelScoringRulesDialog()
    
    def addButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SCORING_RULE_ADD)
    
    def removeButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SCORING_RULE_DELETE)
    
    def downButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SCORING_RULE_DOWN)
    
    def upButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SCORING_RULE_UP)
    
    def editButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SCORING_RULE_EDIT)
    
    @property
    def scoringListName(self):
        return ActivityWizardConst.answerNetwork.SCORING_RULE_LIST
    
    @property
    def scoringList(self):
        return findObject(self.scoringListName)

    def selectRow(self, row):
        self.util.click(self.scoringListName + '.item_%s/0'%(row,))
        
class ScoringModelTab:
    def __init__(self):
        self.util = Util()
        self.workProductFeatures = ScoringModelWorkProductFeatures()
        self.scoringRules = ScoringModelScoringRules()
    
class OverallFeedbackTabCheck:
    def __init__(self):
        self.util = Util()
    
    def completedFeedback(self, text):
        self.util.textCheckPoint(ActivityWizardConst.answerNetwork.COMPLETED_FEEDBACK_TEXTFIELD, text)
    
    def incompleteFeedback(self, text):
        self.util.textCheckPoint(ActivityWizardConst.answerNetwork.INCOMPLETE_FEEDBACK_TEXTFIELD, text)
    
class OverallFeedbackTab:
    def __init__(self):
        self.util = Util()
        self.check = OverallFeedbackTabCheck()
    
    def completedFeedback(self, text):
        self.util.setText(ActivityWizardConst.answerNetwork.COMPLETED_FEEDBACK_TEXTFIELD, text)
    
    def incompleteFeedback(self, text):
        self.util.setText(ActivityWizardConst.answerNetwork.INCOMPLETE_FEEDBACK_TEXTFIELD, text)
    
class SettingsTabCheck:
    def __init__(self):
        self.util = Util()
    
    def timeElapsedRadio(self, checked=True):
        self.util.isChecked(ActivityWizardConst.answerNetwork.TIME_ELAPSED, checked)
    
    def countdownRadio(self, checked=True):
        self.util.isChecked(ActivityWizardConst.answerNetwork.COUNTDOWN, checked)
    
    def noneRadio(self, checked=True):
        self.util.isChecked(ActivityWizardConst.answerNetwork.NONE, checked)

    def hour(self, hour):
        self.util.textCheckPoint(ActivityWizardConst.answerNetwork.COUNTDOWN_HOURS, hour)
    
    def minute(self, minute):
        self.util.textCheckPoint(ActivityWizardConst.answerNetwork.COUNTDOWN_MINUTES, minute)
    
    def second(self, second):
        self.util.textCheckPoint(ActivityWizardConst.answerNetwork.COUNTDOWN_SECONDS, second)
    
    def noDynamicFeedbackRadio(self, checked=True):
        self.util.isChecked(ActivityWizardConst.answerNetwork.NO_DYNAMIC_PERCENTAGE_FEEDBACK, checked)
    
    def showScoreRadio(self, checked=True):
        self.util.isChecked(ActivityWizardConst.answerNetwork.SHOW_SCORE, checked)
    
    def showItemCountPercentageRadio(self, checked=True):
        self.util.isChecked(ActivityWizardConst.answerNetwork.SHOW_ITEM_COUNT_PERCENTAGE, checked)
    
    def showItemCountRadio(self, checked=True):
        self.util.isChecked(ActivityWizardConst.answerNetwork.SHOW_ITEM_COUNT, checked)
    
    def showScorePercentageRadio(self, checked=True):
        self.util.isChecked(ActivityWizardConst.answerNetwork.SHOW_SCORE_PERCENTAGE, checked)
    
    def userProfileLocking(self, checked=True):
        checkbox = findObject(ActivityWizardConst.answerNetwork.USER_PROFILE_LOCKING)
        self.util.isChecked(checkbox, checked)
        
    def noGuestProfile(self, checked=True):
        checkbox = findObject(ActivityWizardConst.answerNetwork.NO_GUEST_PROFILE)
        self.util.isChecked(checkbox, checked)
    
    def timeToForwardAnswerNetwork(self, timeInMS):
        self.util.textCheckPoint(ActivityWizardConst.answerNetwork.TIME_TO_FORWARD_ANSWER_NETWORK, timeInMS)


class SettingsTab:
    def __init__(self):
        self.util = Util()
        self.check = SettingsTabCheck()
    
    def timeElapsedRadio(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.TIME_ELAPSED)
    
    def countdownRadio(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.COUNTDOWN)
    
    def noneRadio(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.NONE)

    def setCountdownTimer(self, hour, minute, second):
        self.countdownRadio()
        self.hour(hour)
        self.minute(minute)
        self.second(second)
        
    def hour(self, hour):
        self.util.setText(ActivityWizardConst.answerNetwork.COUNTDOWN_HOURS, hour)
    
    def minute(self, minute):
        self.util.setText(ActivityWizardConst.answerNetwork.COUNTDOWN_MINUTES, minute)
    
    def second(self, second):
        self.util.setText(ActivityWizardConst.answerNetwork.COUNTDOWN_SECONDS, second)
    
    def noDynamicFeedbackRadio(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.NO_DYNAMIC_PERCENTAGE_FEEDBACK)
    
    def showScoreRadio(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SHOW_SCORE)
    
    def showItemCountPercentageRadio(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SHOW_ITEM_COUNT_PERCENTAGE)
    
    def showItemCountRadio(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SHOW_ITEM_COUNT)
    
    def showScorePercentageRadio(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SHOW_SCORE_PERCENTAGE)
    
    def userProfileLocking(self, checked = None):
        checkbox = findObject(ActivityWizardConst.answerNetwork.USER_PROFILE_LOCKING)
        self.util.checkbox(checkbox, checked)
        
    def noGuestProfile(self, checked = None):
        checkbox = findObject(ActivityWizardConst.answerNetwork.NO_GUEST_PROFILE)
        self.util.checkbox(checkbox, checked)
    
    def timeToForwardAnswerNetwork(self, timeInMS):
        self.util.setText(ActivityWizardConst.answerNetwork.TIME_TO_FORWARD_ANSWER_NETWORK, timeInMS)
        
class Tabs:
    def __init__(self):
        self.util = Util()
        
    def _clickTab(self, tab):
        self.util.clickTab(ActivityWizardConst.answerNetwork.TAB_BAR, tab)
    
    def assessmentTree(self):
        self._clickTab('Assessment Tree')
    
    def connectivityTest(self):
        self._clickTab('Connectivity Test')
    
    def scoringModel(self):
        self._clickTab('Scoring Model')
    
    def overallFeedback(self):
        self._clickTab('Overall Feedback')
    
    def settings(self):
        self._clickTab('Settings')
    
class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def replaceFileDialog(self):
        try:
            return findObject(ActivityWizardConst.answerNetwork.REPLACE_FILE_DIALOG)
        except LookupError, e:
            return False
    
    def replaceFileYesButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.REPLACE_FILE_YES_BUTTON)
        
    def replaceFileNoButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.REPLACE_FILE_NO_BUTTON)
    
    @property
    def overwriteDialog(self):
        try:
            return findObject(ActivityWizardConst.answerNetwork.OVERWRITE_DIALOG)
        except LookupError, e:
            return False
    
    def overwriteYesButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.OVERWRITE_YES_BUTTON)
    
    def overwriteNoButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.OVERWRITE_NO_BUTTON)
    
class FileDialog:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
    
    def filename(self, filename):
        self.util.setText(ActivityWizardConst.answerNetwork.IMPORT_FILE_TO_ANSWER_NETWORK_DIALOG, filename)
    
    def saveButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.EXPORT_ANSWER_NETWORK_TO_FILE_DIALOG_OK)
    
    def cancelButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.IMPORT_FILE_TO_ANSWER_NETWORK_DIALOG_CANCEL)
    
    def openButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.IMPORT_FILE_TO_ANSWER_NETWORK_DIALOG_OK)
    
    def importFile(self, filename, overwrite = True):
        self.filename(filename)
        self.openButton()
    
    def exportFile(self, filename, overwrite = True):
        self.filename(filename)
        self.saveButton()
        if self.popups.replaceFileDialog:
            if overwrite:
                self.popups.replaceFileYesButton()
            else:
                self.popups.replaceFileNoButton()
        if self.popups.overwriteDialog:
            if overwrite:
                self.popups.overwriteYesButton()
            else:
                self.popups.overwriteNoButton()

class AnswerNetwork:
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
        self.assessmentTree = AssessmentTreeTab()
        self.connectivityTest = ConnectivityTestTab()
        self.scoringModel = ScoringModelTab()
        self.overallFeedback = OverallFeedbackTab()
        self.settings = SettingsTab()
        self.tabs = Tabs()
        
    def showAnswerNetworkButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.SHOW_ANSWER_NETWORK)
    
    def importFileToAnswerNetworkButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.IMPORT_FILE_TO_ANSWER_NETWORK)
    
    def exportAnswerNetworkToFileButton(self):
        self.util.clickButton(ActivityWizardConst.answerNetwork.EXPORT_ANSWER_NETWORK_TO_FILE)
    
    def importAnswerNetwork(self, filename, overwrite = True):
        self.importFileToAnswerNetworkButton()
        self.fileDialog.importFile(filename, overwrite)
        
    def exportAnswerNetwork(self, filename, overwrite = True):
        self.exportAnswerNetworkToFileButton()
        self.fileDialog.exportFile(filename, overwrite)