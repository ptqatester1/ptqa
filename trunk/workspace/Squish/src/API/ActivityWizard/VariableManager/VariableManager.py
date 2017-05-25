from API.Utility.Util import Util
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst 
from __builtin__ import object as Object

class PopupWarnings:
    '''Class to handle popup windows'''
    def __init__(self):
        self.util = Util()

class FileDialog:
    def __init__(self):
        self.util = Util()
    
    def dialog(self):
        try:
            return findObject(ActivityWizardConst.variableManager.FILE_DIALOG)
        except LookupError, e:
            return False
    
    def filename(self, filename):
        self.util.setText(ActivityWizardConst.variableManager.IMPORT_EXPORT_FILENAME_EDIT, filename)
    
    def saveButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.IMPORT_EXPORT_SAVE_BUTTON)
    
    def openButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.IMPORT_EXPORT_OPEN_BUTTON)
    
    def cancelButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.IMPORT_EXPORT_CANCEL_BUTTON)
        
    def importfile(self, filename):
        self.filename(filename)
        self.openButton()
    
    def exportfile(self, filename):
        self.filename(filename)
        self.saveButton()
    
class VariablesTable(Object):
    def __init__(self):
        self.util = Util()

    def variableName(self, variableName, row):
        self._setTableText(variableName, row, 0)
    
    def poolName(self, poolName, row):
        tableItem = self.tableName + '.item_' + str(row) + '/1'
        self.util.click(tableItem)
        self._selectCombo(self.tableName, 2, poolName)
        
    def valueType(self, valueType, row):
        tableItem = self.tableName + '.item_' + str(row) + '/2'
        self.util.click(tableItem)
        self._selectCombo(self.tableName, 3, valueType)
        
    def value(self, value, row):
        self._setTableText(value, row, 3)
    
    def newVariable(self, variableName, poolName, valueType, value, row):
        self.variableName(variableName, row)
        self.poolName(poolName, row)
        self.valueType(valueType, row)
        if value:
            self.value(value, row)
        
class TableInteraction(Object):
    def __init__(self):
        self.util = Util()
        
    def _setTableText(self, text, row, column):
        tableItem = self.tableName + '.item_' + str(row) + '/' + str(column)
        self.util.click(tableItem)
        text = str(text)
        if len(text) == 0 or (text.startswith('<') and text.endswith('>')):#Account for instance where <Del> <Tab> etc are passed
            initialText = text
        else:
            initialText = text[0]
        if len(text) > 1 and not (text.startswith('<') and text.endswith('>')):
            remainingText = text[1:]
        else:
            remainingText = None
        self.util.typeText(self.tableName, initialText)
        if remainingText:
            self.util.typeText(self.lineedit, remainingText)
        self.util.click(ActivityWizardConst.TITLE)#To ensure the text is saved
    
    def _selectCombo(self, tableName, column, value):
        boxname = tableName + ActivityWizardConst.variableManager.TABLE_COMBO_BOX_ENDING + str(column - 1)
        self.util.clickItem(boxname, value)
    
    def selectTableItem(self, row, column):
        self.util.click(self.tableName + '.item_' + str(row) + '/' + str(column))

class Introduction:
    def __init__(self):
        self.util = Util()
    
    def showVariableManagerInterface(self, checked = None):
        checkbox = findObject(ActivityWizardConst.variableManager.SHOW_VARIABLE_MANAGER_INTERFACE)
        self.util.checkbox(checkbox, checked)

class Seeds(TableInteraction):
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
    
    @property
    def tableName(self):
        return ActivityWizardConst.variableManager.SEEDS_TABLE
    
    @property
    def tableObject(self):
        return findObject(self.tableName)

    @property
    def lineedit(self):
        return ActivityWizardConst.variableManager.SEEDS_ENTRY_EDIT
    
    def seedName(self, name, row):
        self._setTableText(name, row, 0)
        
    def minimum(self, min, row):
        self._setTableText(str(min), row, 1)

    def maximum(self, max, row):
        self._setTableText(str(max), row, 2)
    
    def testValue(self, val, row):
        self._setTableText(str(val), row, 3)
    
    def importSeedsButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.SEEDS_IMPORT_BUTTON)
    
    def exportSeedsButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.SEEDS_EXPORT_BUTTON)
    
    def importFile(self, filename):
        self.importSeedsButton()
        self.fileDialog.importfile(filename)
    
    def exportFile(self, filename):
        self.exportSeedsButton()
        self.fileDialog.exportfile(filename)
    
    def setSeed(self, name, min, max, val, row):
        self.seedName(name, row)
        self.minimum(min, row)
        self.maximum(max, row)
        self.testValue(val, row)
    
class NumberPools(TableInteraction):
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
        
    @property
    def tableName(self):
        return ActivityWizardConst.variableManager.NUMBERS_POOLS_TABLE
    
    @property
    def tableObject(self):
        return findObject(self.tableName)
    
    @property
    def lineedit(self):
        return ActivityWizardConst.variableManager.NUMBERS_POOLS_EDIT
    
    def name(self, name, row):
        self._setTableText(name, row, 0)
    
    def min(self, min, row):
        self._setTableText(min, row, 1)
    
    def max(self, max, row):
        self._setTableText(max, row, 2)
    
    def newPool(self, name, min, max, row):
        self.name(name, row)
        self.min(min, row)
        self.max(max, row)
    
    def importNumberPoolsButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.NUMBERS_POOLS_IMPORT_BUTTON)
    
    def exportNumberPoolsButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.NUMBERS_POOLS_EXPORT_BUTTON)
    
    def importFile(self, filename):
        self.importNumberPoolsButton()
        self.fileDialog.importfile(filename)
    
    def exportFile(self, filename):
        self.exportNumberPoolsButton()
        self.fileDialog.exportfile(filename)
    
    
class NumberVariables(TableInteraction, VariablesTable):
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
        
    @property
    def tableName(self):
        return ActivityWizardConst.variableManager.NUMBERS_VARIABLES_TABLE
    
    @property
    def tableObject(self):
        return findObject(self.tableName)
    
    @property
    def lineedit(self):
        return ActivityWizardConst.variableManager.NUMBERS_VARIABLES_EDIT
    
    def importNumberVariablesButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.NUMBERS_VARIABLES_IMPORT_BUTTON)
    
    def exportNumberVariablesButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.NUMBERS_VARIABLES_EXPORT_BUTTON)
    
    def importFile(self, filename):
        self.importNumberVariablesButton()
        self.fileDialog.importfile(filename)
    
    def exportFile(self, filename):
        self.exportNumberVariablesButton()
        self.fileDialog.exportfile(filename)
    
    
class Number:
    def __init__(self):
        self.util = Util()
        self.numberPools = NumberPools()
        self.numberVariables = NumberVariables()
    
class StringPools(TableInteraction):
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
        
    @property
    def tableName(self):
        return ActivityWizardConst.variableManager.STRINGS_POOLS_TABLE
    
    @property
    def tableObject(self):
        return findObject(self.tableName)
    
    @property
    def lineedit(self):
        return ActivityWizardConst.variableManager.STRINGS_POOLS_EDIT
    
    def stringPoolName(self, name, row):
        self._setTableText(name, row, 0)
    
    def text(self, text, row):
        self._setTableText(text, row, 1)
    
    def newPool(self, name, text, row):
        self.stringPoolName(name, row)
        self.text(text, row)
    
    def importStringPoolsButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.STRINGS_POOLS_IMPORT_BUTTON)
    
    def exportStringPoolsButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.STRINGS_POOLS_EXPORT_BUTTON)
    
    def importFile(self, filename):
        self.importStringPoolsButton()
        self.fileDialog.importfile(filename)
    
    def exportFile(self, filename):
        self.exportStringPoolsButton()
        self.fileDialog.exportfile(filename)
    
class StringVariables(TableInteraction, VariablesTable):
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
        
    @property
    def tableName(self):
        return ActivityWizardConst.variableManager.STRINGS_VARIABLES_TABLE
    
    @property
    def tableObject(self):
        return findObject(self.tableName)
    
    @property
    def lineedit(self):
        return ActivityWizardConst.variableManager.STRINGS_VARIABLES_EDIT
    
    def importStringVariablesButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.STRINGS_VARIABLES_IMPORT_BUTTON)
            
    def exportStringVariablesButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.STRINGS_VARIABLES_EXPORT_BUTTON)
    
    def importFile(self, filename):
        self.importStringVariablesButton()
        self.fileDialog.importfile(filename)
    
    def exportFile(self, filename):
        self.exportStringVariablesButton()
        self.fileDialog.exportfile(filename)
    
class Strings:
    def __init__(self):
        self.util = Util()
        self.stringPools = StringPools()
        self.stringVariables = StringVariables()

class IpAddressPools(TableInteraction):
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
        
    @property
    def tableName(self):
        return ActivityWizardConst.variableManager.IP_POOLS_TABLE
    
    @property
    def tableObject(self):
        return findObject(self.tableName)
    
    @property
    def lineedit(self):
        return ActivityWizardConst.variableManager.IP_POOLS_EDIT
    
    def ipPoolName(self, name, row):
        self._setTableText(name, row, 0)
    
    def network(self, network, row):
        self._setTableText(network, row, 1)
    
    def mask(self, mask, row):
        self._setTableText(mask, row, 2)
    
    def firstIpAddr(self, firstIp, row):
        self._setTableText(firstIp, row, 3)
    
    def lastIpAddr(self, lastIp, row):
        self._setTableText(lastIp, row, 4)
    
    def newPool(self, name, network, mask, firstAddress, lastAddress, row):
        self.ipPoolName(name, row)
        self.network(network, row)
        self.mask(mask, row)
        self.firstIpAddr(firstAddress, row)
        self.lastIpAddr(lastAddress, row)
    
    def importIpAddressPoolsButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.IP_POOLS_IMPORT_BUTTON)
    
    def exportIpAddressPoolsButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.IP_POOLS_EXPORT_BUTTON)
    
    def importFile(self, filename):
        self.importIpAddressPoolsButton()
        self.fileDialog.importfile(filename)
    
    def exportFile(self, filename):
        self.exportIpAddressPoolsButton()
        self.fileDialog.exportfile(filename)
    
class IpAddressVariables(TableInteraction, VariablesTable):
    def __init__(self):
        self.util = Util()
        self.fileDialog = FileDialog()
        
    @property
    def tableName(self):
        return ActivityWizardConst.variableManager.IP_VARIABLES_TABLE
    
    @property
    def tableObject(self):
        return findObject(self.tableName)
    
    @property
    def lineedit(self):
        return ActivityWizardConst.variableManager.IP_VARIABLES_EDIT
    
    def importIpAddressVariablesButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.IP_VARIABLES_IMPORT_BUTTON)
    
    def exportIpAddressVariablesButton(self):
        self.util.clickButton(ActivityWizardConst.variableManager.IP_VARIABLES_EXPORT_BUTTON)
    
    def importFile(self, filename):
        self.importIpAddressVariablesButton()
        self.fileDialog.importfile(filename)
    
    def exportFile(self, filename):
        self.exportIpAddressVariablesButton()
        self.fileDialog.exportfile(filename)
    
class IpAddresses:
    def __init__(self):
        self.util = Util()
        self.ipPools = IpAddressPools()
        self.ipVariables = IpAddressVariables()
    
class Tabs:
    def __init__(self):
        self.util = Util()
    
    def _clickTab(self, tab):
        self.util.clickTab(ActivityWizardConst.variableManager.TAB_BAR, tab)
    
    def introduction(self):
        self._clickTab('Introduction')
    
    def seeds(self):
        self._clickTab('Seeds')
    
    def number(self):
        self._clickTab('Number')
    
    def strings(self):
        self._clickTab('Strings')
    
    def ipAddresses(self):
        self._clickTab('IP Addresses')
        
class VariableManager:
    def __init__(self):
        self.util = Util()
        self.introduction = Introduction()
        self.seeds = Seeds()
        self.number = Number()
        self.strings = Strings()
        self.ipAddresses = IpAddresses()
        self.tabs = Tabs()
        
    def select(self):
        self.util.clickButton(ActivityWizardConst.VARIABLE_MANAGER)