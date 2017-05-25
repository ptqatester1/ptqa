##Chris Allen

from API.Utility.Util import Util
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.ActivityWizard.AnswerNetwork.AnswerNetwork import AssessmentTree
from squish import *
import re
import object

class TreeItem:
    def __init__(self, squishName, item, itemName):
        self.squishName = squishName
        self.item = item
        self.itemName = itemName#Name in "Network.Device.Attribute" format
        
class LockingTree:
    def __init__(self):
        self.util = Util()
    
    @property
    def treeName(self):
        return ActivityWizardConst.initialNetwork.LOCKING_ITEMS_TREE
    
    @property
    def treeObject(self):
        return findObject(self.treeName)
    
    def _expandItem(self, currentItem, squishName):
        if currentItem.collapsed:
            self.util.clickItem_x_y(self.treeObject, squishName, p_x=-10, p_y=5)
                
    def _findItemInTree(self, *children):
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
        itemObj = parentObj
        return TreeItem(parentName, itemObj, '.'.join(itemStrings))
    
    def checkItem(self, checked, parentItem = 'Locking', *children):
        children = (parentItem,) + children
        item = self._findItemInTree(*children)
        self.util.checkbox(item.item, checked)
    

class LockingOptionsTab:
    def __init__(self):
        self.util = Util()
        self.lockingTree = LockingTree()
    
    def expandCollapseAllButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.LOCKING_OPTIONS_EXPAND_COLLAPSE_ALL_BUTTON)
    
class InitialNetworkTree(AssessmentTree):
    def __init__(self):
        super(InitialNetworkTree, self).__init__()
    
    @property
    def treeName(self):
        '''Overwride the assessmentTree name'''
        return ActivityWizardConst.initialNetwork.INITIAL_NETWORK_SETUP_TREE
    
    @property
    def treeObject(self):
        return findObject(self.treeName)
    
    def _setTreeItemText(self, text):
        lineedit = self.treeName + '.qt_scrollarea_viewport.QExpandingLineEdit1'
        self.util.setText(lineedit, text)
    
    def _expandViewArea(self):
        awWindow = findObject(ActivityWizardConst.ACTIVITY_WIZARD_WINDOW)
        if not awWindow.windowState() == Qt.WindowMaximized:
            self.util.maximizeWindow(awWindow)
        findObject(ActivityWizardConst.answerNetwork.ASSESSMENT_ITEMS_TREE_HEADER).setResizeMode(0, QHeaderView.Stretch)#Make the tree stretch
    
    def _expandItem(self, currentItem, squishName):
        if currentItem.collapsed:
            self.util.clickItem_x_y(self.treeObject, squishName, p_x=-10, p_y=5)
            
    def _findItemInTree(self, *children):
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
        return TreeItem(parentName, parentObj, '.'.join(itemStrings))
    
    def checkItem(self, checked, parentItem = 'Network', *children):
        children = (parentItem,) + children
        item = self._findItemInTree(*children)
        self.util.checkbox(item.item, checked)
    
    def changeItemValue(self, value, parentItem = 'Network', *children):
        children = (parentItem,) + children
        item = self._findItemInTree(*children)
        #Below item.itemName had to be used for squish to click the correct place
        self.util.doubleClickItem_x_y(self.treeName, item.itemName, 50, 5)#50 and 5 are just arbitrary numbers that should click about half way in the edit box
        self._setTreeItemText(value)

class InitialNetworkSetupTab:
    def __init__(self):
        self.util = Util()
        self.initialNetworkTree = InitialNetworkTree()
        
    def expandCollapseAllButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.InitialNetworkSetup.EXPAND_COLLAPSE_ALL)
        
class ObjectLocationsTab:
    def __init__(self):
        self.util = Util()    
    
    @property
    def tableName(self):
        return ActivityWizardConst.initialNetwork.OBJECT_LOCATIONS_TABLE
    
    @property
    def tableObject(self):
        try:
            return findObject(self.tableName)
        except LookupError, e:
            return False
    
    def editSet(self, text):
        self.util.setText(ActivityWizardConst.initialNetwork.EDIT_SET, text)
    
    def overwriteSelectedLocationsButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.OVERWRITE_SELECTED_LOCATION)
    
    def appendCurrentLocationsButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.APPEND_CURRENT_LOCATIONS)
    
    def loadLocationsButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.LOAD_LOCATIONS)
    
    def deleteSelectedLocationsButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.DELETE_SELECTED_LOCATIONS)
    
    def indexVariable(self, var):
        self.util.setText(ActivityWizardConst.initialNetwork.INDEX_VARIABLE, var)

class Tabs:
    def __init__(self):
        self.util = Util()
    
    def _clickTab(self, tab):
        self.util.clickTab(ActivityWizardConst.initialNetwork.TAB_BAR, tab)
    
    def lockingOptions(self):
        self._clickTab('Locking Options')
    
    def initialNetworkSetup(self):
        self._clickTab('Initial Network Setup')
    
    def objectLocations(self):
        self._clickTab('Object Locations')

class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def replaceFileDialog(self):
        try:
            return findObject(ActivityWizardConst.initialNetwork.EXPORT_INITIAL_NETWORK_REPLACE_BOX)
        except LookupError, e:
            return False
    
    def replaceFileYesButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.EXPORT_INITIAL_NETWORK_REPLACE_BOX_YES)
    
    def replaceFileNoButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.EXPORT_INITIAL_NETWORK_REPLACE_BOX_NO)
    
    @property
    def overwriteDialog(self):
        try:
            return findObject(ActivityWizardConst.initialNetwork.EXPORT_OVERWRITE_FILE_DIALOG)
        except LookupError, e:
            return False
    
    def overwriteYesButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.EXPORT_OVERWRITE_FILE_DIALOG_YES)
    
    def overwriteNoButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.EXPORT_OVERWRITE_FILE_DIALOG_NO)

    @property
    def copyFromAnswerNetworkReplaceDialog(self):
        try:
            return findObject(ActivityWizardConst.initialNetwork.COPY_FROM_ANSWER_NETWORK_DIALOG)
        except LookupError, e:
            return False
    
    def copyFromAnswerNetworkReplaceYesButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.COPY_FROM_ANSWER_NETWORK_DIALOG_YES)
    
    def copyFromAnswerNetworkReplaceNoButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.COPY_FROM_ANSWER_NETWORK_DIALOG_NO)
    
    

class FileDialog:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
    
    def filename(self, filename):
        self.util.setText(ActivityWizardConst.initialNetwork.IMPORT_FILE_TO_INITIAL_NETWORK_DIALOG, filename)
    
    def openButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.IMPORT_FILE_TO_INITIAL_NETWORK_DIALOG_OK)
    
    def saveButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.EXPORT_INITIAL_NETWORK_TO_FILE_DIALOG_OK)
    
    def cancelButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.IMPORT_FILE_TO_INITIAL_NETWORK_DIALOG_CANCEL)
    
    def importFile(self, filename):
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
        
class InitialNetwork:
    def __init__(self):
        self.util = Util()
        self.lockingOptions = LockingOptionsTab()
        self.initialNetworkSetup = InitialNetworkSetupTab()
        self.objectLocations = ObjectLocationsTab()
        self.tabs = Tabs()
        self.fileDialog = FileDialog()
        self.popups = PopupWarnings()
        
    def showInitialNetworkButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.SHOW_INITIAL_NETWORK)
    
    def importFileToInitialNetworkButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.IMPORT_FILE_TO_INITIAL_NETWORK)
    
    def copyFromAnswerNetworkButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.COPY_FROM_ANSWER_NETWORK)
    
    def exportInitialNetworkToFileButton(self):
        self.util.clickButton(ActivityWizardConst.initialNetwork.EXPORT_INITIAL_NETWORK_TO_FILE)
    
    def importInitialNetwork(self, filename):
        self.importFileToInitialNetworkButton()
        self.fileDialog.importFile(filename)
    
    def exportInitialNetwork(self, filename, overwrite = True):
        self.exportInitialNetworkToFileButton()
        self.fileDialog.exportFile(filename, overwrite)
        
    def copyFromAnswerNetwork(self):
        self.copyFromAnswerNetworkButton()
        if self.popups.copyFromAnswerNetworkReplaceDialog:
            self.popups.copyFromAnswerNetworkReplaceYesButton()
        
    def returnToAW(self):
        self.util.click(ActivityWizardConst.initialNetwork.ACTIVITY_WIZARD_ICON)