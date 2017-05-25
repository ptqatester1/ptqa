##Chris Allen

from API.Utility.Util import Util
from API.MenuBar.Extensions.Scripting.ScriptingConst import ScriptingConst
from __builtin__ import object as Object
from squish import *
import object

def err(msg = ''): raise NotImplementedError(msg)

'''Below are the classes related to the actual scripting interface and not the menu items'''
class SquishObjectName(Object):
    '''Helper class that just appends the objects baseName to the object'''
    def __init__(self):
        None
    
    def objName(self, obj):
        if obj.startswith(':'):
            raise ValueError('Constants in the scriptingconst file should not contain a full name. They must be shared between AW and Menu scripting.')
        else:
            return self.baseName + obj

class InfoTabPopupWarnings(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName
    
    @property
    def selectingTemplateRemoveChangesDialog(self):
        '''Selecting a template will remove all changes made to this script module. Are you sure you want to continue?'''
        try:
            return findObject(ScriptingConst.info.WARNING_POPUP_DIALOG)
        except LookupError, e:
            return False
    
    def selectingTemplateRemoveChangesYesButton(self):
        Util().clickButton(ScriptingConst.info.WARNING_POPUP_YES_BUTTON)
    
    def selectingTemplateRemoveChangesNoButton(self):
        Util().clickButton(ScriptingConst.info.WARNING_POPUP_NO_BUTTON)
        
    def signScriptResignAndEdit(self):
        Util().clickButton(ScriptingConst.info)
        
    def signScriptReadOnly(self):
        Util().clickButton(ScriptingConst.info.WARNING_POPUP_NO_BUTTON)
        
    def signScriptEditUnsigned(self):
        Util().clickButton(ScriptingConst.info.WARNING_POPUP_NO_BUTTON)
        
class InfoTab(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName
        self.popups = InfoTabPopupWarnings(self)
    
    def selectTemplate(self, template):
        self.util.clickItem(self.objName(ScriptingConst.info.SELECT_TEMPLATE_COMBO), template)
        if self.popups.selectingTemplateRemoveChangesDialog:
            self.popups.selectingTemplateRemoveChangesYesButton()
    
    def goToGeneralInfoButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.SCRIPT_MODULE_GENERAL_INFO_GOTO_BUTTON))
    
    def goToScriptEngineButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.SCRIPT_ENGINE_FILES_GOTO_BUTTON))
    
    def goToCustomInterfaceFilesButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.CUSTOM_INTERFACE_FILES_GOTO_BUTTON))
    
    def goToDataStoreButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.DATA_STORE_GOTO_BUTTON))
    
    def saveButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.SAVE_BUTTON))
    
    def exportButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.EXPORT_BUTTON))
    
    def translateButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.TRANSLATE_BUTTON))
    
    def stopButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.STOP_BUTTON))
    
    def startButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.START_BUTTON))
    
    def debugButton(self):
        self.util.clickButton(self.objName(ScriptingConst.info.DEBUG_BUTTON))
    
class GeneralTabPopupWarnings(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName
    
    def signScriptResignAndEdit(self):
        Util().clickButton(ScriptingConst.general.SIGN_SCRIPT_RESIGN_AND_EDIT)
        
    def signScriptReadOnly(self):
        Util().clickButton(ScriptingConst.general.SIGN_SCRIPT_READ_ONLY)
        
    def signScriptEditUnsigned(self):
        Util().clickButton(ScriptingConst.general.SIGN_SCRIPT_EDIT_UNSIGNED)
        
class GeneralTab(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName
        self.popups = GeneralTabPopupWarnings(self)

    def name(self, name):
        self.util.setText(self.objName(ScriptingConst.general.info.NAME), name)
    
    def idEdit(self, idEdit):
        self.util.setText(self.objName(ScriptingConst.general.info.ID), idEdit)
    
    def version(self, version):
        self.util.setText(self.objName(ScriptingConst.general.info.VERSION), version)
    
    def author(self, author):
        self.util.setText(self.objName(ScriptingConst.general.info.AUTHOR), author)
    
    def contact(self, contact):
        self.util.setText(self.objName(ScriptingConst.general.info.CONTACT), contact)
    
    def description(self, description):
        self.util.setText(self.objName(ScriptingConst.general.info.DESCRIPTION), description)
    
    def browseButton(self):
        self.util.clickButton(self.objName(ScriptingConst.general.publisherSigning.BROWSE_BUTTON))
    
    def clearButton(self):
        self.util.clickButton(self.objName(ScriptingConst.general.publisherSigning.CLEAR_BUTTON))
    
    def password(self, password):
        self.util.setText(self.objName(ScriptingConst.general.password.PASSWORD), password)
        
    def confirmedPassword(self, password):
        self.util.setText(self.objName(ScriptingConst.general.password.CONFIRM_PASSWORD), password)
    
    def enabledPassowrdButton(self):
        self.util.clickButton(self.objName(ScriptingConst.general.password.ENABLE_BUTTON))
    
    def disabledPassowrdButton(self):
        self.util.clickButton(self.objName(ScriptingConst.general.password.DISABLE_BUTTON))
    
    def onStartupRadio(self):
        self.util.clickButton(self.objName(ScriptingConst.general.startup.ON_STARTUP_RADIO))
    
    def onDemandRadio(self):
        self.util.clickButton(self.objName(ScriptingConst.general.startup.ON_DEMAND_RADIO))
    
    def disabledRadio(self):
        self.util.clickButton(self.objName(ScriptingConst.general.startup.DISABLED_RADIO))
        
    def preventThisScriptModuleFromBeingRemoted(self, checked = None):
        checkbox = findObject(self.objName(ScriptingConst.general.securityPrivileges.ALLOW_OPENING_FILE_EVEN_IF_SECURITY_PRIVILEGES_NOT_GRANTED_CHECKBOX))
        self.util.checkbox(checkbox, checked)
    
    def selectSecurityPriveleges(self, privilege, *morePrivileges, **kwargs):
        '''
        Takes a list of privileges and then iterates of the checkboxes in the groupbox to see if the checkbox text is in the list. If so
        it will add that to the boxes list. When finished iterating the checkboxes it will iterate over the boxes list and check/uncheck
        each box in the list accordingly
        
        PARAMETERS:
            privilege: String (Name of a privilege to check
            morePriviliges: String (More names of privileges to check separated by a comma)
            kwargs:
                checked: None || Boolean (If None toggle. If True check. If False uncheck. Default is toggle)
        '''
        privilegeList = list((privilege,) + morePrivileges)
        boxes = []
        groupbox = findObject(self.objName(ScriptingConst.general.securityPrivileges.GROUP_BOX))
        for item in object.children(groupbox):
            try:
                if item.checkable:
                    if item.text in privilegeList:
                        boxes.append(item)
            except AttributeError, e:
                print(e)
        for checkbox in boxes:
            self.util.checkbox(checkbox, checked)

class ScriptEnginePopups(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName
    
    def enterScriptIdDialog(self):
        try:
            return findObject(self.objName(ScriptingConst.scriptEngine.ENTER_SCRIPT_ID_DIALOG))
        except LookupError, e:
            return False
    
    def enterScriptIdFilename(self, filename):
        self.util.setText(self.objName(ScriptingConst.scriptEngine.ENTER_SCRIPT_ID_FILENAME), filename)
    
    def enterScriptIdOkButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.ENTER_SCRIPT_ID_OK_BUTTON))
        
    def enterScriptIdCancelButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.ENTER_SCRIPT_ID_CANCEL_BUTTON))
    
    def exportImportScriptCancelButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.EXPORT_SCRIPT_CANCEL_BUTTON))
        
    
class ScriptEngineTab(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName
        self.popups = ScriptEnginePopups(self)
        
    @property
    def scriptList(self):
        '''Returns the scriptlist object'''
        return findObject(self.objName(ScriptingConst.scriptEngine.SCRIPT_LIST))

    @property
    def scriptObjectsList(self):
        '''Returns a list of all the objects in the script list'''
        objList = []
        for i in range(self.scriptList.count):
            objList.append(findObject(self.objName(ScriptingConst.scriptEngine.SCRIPT_LIST + '.item_' + str(i) + '/0')))
        return objList

    def selectScript(self, scriptName):
        for script in self.scriptObjectsList:
            if script.text == scriptName:
                self.util.click(script)
                return True
        raise ValueError('Unable to find script: ' + scriptName)
            
    def setScriptText(self, text):
        self.util.setText(self.objName(ScriptingConst.scriptEngine.SCRIPT_TEXT), text)
    
    def editScript(self, scriptName, newText):
        self.selectScript(scriptName)
        self.setScriptText(newText)
        
    @property
    def scriptText(self):
        return str(findObject(self.objName(ScriptingConst.scriptEngine.SCRIPT_TEXT)).toPlainText())
    
    def textCheckPoint(self, text, **kwargs):
        self.util.textCheckPoint(self.objName(ScriptingConst.scriptEngine.SCRIPT_TEXT), text, **kwargs)
    
    def addButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.ADD_BUTTON))
    
    def removeButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.REMOVE_BUTTON))
    
    def renameButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.RENAME_BUTTON))
    
    def importButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.IMPORT_BUTTON))

    def importScript(self, script, path):
        self.importButton()
        self.util.setText(self.objName(ScriptingConst.scriptEngine.FILE_DIALOG_NAME_EDIT), self.util.getFilePath(script, path))
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.FILE_DIALOG_OPEN))
    
    def importDirButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.IMPORT_DIR_BUTTON))
    
    def exportButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.EXPORT_BUTTON))
    
    def exportScript(self, script, path):
        self.selectScript(script)
        self.exportButton()
        self.util.setText(self.objName(ScriptingConst.scriptEngine.FILE_DIALOG_NAME_EDIT), self.util.getFilePath(script, path))
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.EXPORT_FILE_SAVE_BTN))
        if object.exists(ScriptingConst.scriptEngine.EXPORT_FILE_OVERWRITE_MESSAGE):
            self.util.clickButton(self.objName(ScriptingConst.scriptEngine.EXPORT_FILE_OVERWRITE_YES_BTN))
    
    def removeScript(self, script):
        self.util.clickItem(self.objName(ScriptingConst.scriptEngine.SCRIPT_LIST), script)
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.REMOVE_BUTTON))
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.REMOVE_SCRIPT_YES_BTN))
    
    def runFileButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.RUN_FILE_BUTTON))
    
    def stopButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.STOP_BUTTON))
    
    def startButton(self):
        '''Same as stop button but named for clarity in scripts'''
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.STOP_BUTTON))
        
    def debugButton(self):
        self.util.clickButton(self.objName(ScriptingConst.scriptEngine.DEBUG_BUTTON))
    
    def addScript(self, filename):
        self.addButton()
        self.popups.enterScriptIdFilename(filename)
        self.popups.enterScriptIdOkButton()
    
    def renameScript(self, script, newName):
        self.selectScript(script)
        self.renameButton()
        self.popups.enterScriptIdFilename(newName)
        self.popups.enterScriptIdOkButton()

class CustomInterfacesTab(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName

    @property
    def interfaceList(self):
        '''Returns the scriptlist object'''
        return findObject(self.objName(ScriptingConst.customInterfaces.INTERFACE_LIST))

    @property
    def interfaceObjectsList(self):
        '''Returns a list of all the objects in the script list'''
        objList = []
        for i in range(self.interfaceList.count):
            objList.append(findObject(self.objName(ScriptingConst.customInterfaces.INTERFACE_LIST + '.item' + str(i) + '/0')))
        return objList

    def selectInterface(self, interfaceName):
        for interface in self.interfaceObjectsList:
            if interface.text == interfaceName:
                self.util.click(interface)
                return True
        raise ValueError('Unable to find script: ' + interfaceName)
            
    def setInterfaceText(self, text):
        self.util.setText(self.objName(ScriptingConst.customInterfaces.INTERFACE_TEXT), text)
    
    def editInterface(self, interfaceName, newText):
        self.selectInterface(interfaceName)
        self.setInterfaceText(newText)
    
    def addButton(self):
        self.util.clickButton(self.objName(ScriptingConst.customInterfaces.ADD_BUTTON))
    
    def removeButton(self):
        self.util.clickButton(self.objName(ScriptingConst.customInterfaces.REMOVE_BUTTON))
    
    def renameButton(self):
        self.util.clickButton(self.objName(ScriptingConst.customInterfaces.RENAME_BUTTON))
    
    def importButton(self):
        self.util.clickButton(self.objName(ScriptingConst.customInterfaces.IMPORT_BUTTON))
    
    def importDirButton(self):
        self.util.clickButton(self.objName(ScriptingConst.customInterfaces.IMPORT_DIR_BUTTON))
    
    def exportButton(self):
        self.util.clickButton(self.objName(ScriptingConst.customInterfaces.EXPORT_BUTTON))
    
    def debugButton(self):
        self.util.clickButton(self.objName(ScriptingConst.customInterfaces.DEBUG_BUTTON))
    
class DataStoreTab(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName
    
    @property
    def dataStoreList(self):
        '''Returns the scriptlist object'''
        return findObject(self.objName(ScriptingConst.dataStore.INTERFACE_LIST))

    @property
    def dataStoreObjectsList(self):
        '''Returns a list of all the objects in the script list'''
        objList = []
        for i in range(self.dataStoreList.count):
            objList.append(findObject(self.objName(ScriptingConst.dataStore.INTERFACE_LIST + '.item' + str(i) + '/0')))
        return objList

    def selectDataStore(self, dataStoreName):
        for dataStore in self.dataStoreObjectsList:
            if dataStore.text == dataStoreName:
                self.util.click(dataStore)
                return True
        raise ValueError('Unable to find script: ' + dataStoretName)
            
    def setDataStoreText(self, text):
        self.util.setText(self.objName(ScriptingConst.dataStore.INTERFACE_TEXT), text)
    
    def editDataStore(self, dataStoreName, newText):
        self.selectDataStore(dataStoreName)
        self.setDataStoreText(newText)
    
    def addButton(self):
        self.util.clickButton(self.objName(ScriptingConst.dataStore.ADD_BUTTON))
    
    def removeButton(self):
        self.util.clickButton(self.objName(ScriptingConst.dataStore.REMOVE_BUTTON))
    
    def renameButton(self):
        self.util.clickButton(self.objName(ScriptingConst.dataStore.RENAME_BUTTON))
    
    def importButton(self):
        self.util.clickButton(self.objName(ScriptingConst.dataStore.IMPORT_BUTTON))
    
    def importDirButton(self):
        self.util.clickButton(self.objName(ScriptingConst.dataStore.IMPORT_DIR_BUTTON))
    
    def exportButton(self):
        self.util.clickButton(self.objName(ScriptingConst.dataStore.EXPORT_BUTTON))
    
    def debugButton(self):
        self.util.clickButton(self.objName(ScriptingConst.dataStore.DEBUG_BUTTON))

class DebuggerBasic(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName
        
    def updateName(self, baseName):
        self.baseName = baseName
    
    def switchToFullDebuggerButton(self):
        self.util.clickButton(self.objName(ScriptingConst.debugger.basic.SWITCH_TO_FULL_DEBUGGER_BUTTON))
    
    def textCheckPoint(self, text, occurrenceNum = 0, **kwargs):
        self.util.textCheckPoint(self.objName(ScriptingConst.debugger.basic.OUTPUT_FIELD), text, occurrenceNum, **kwargs)
    
    def setText(self, text):
        self.util.setText(self.objName(ScriptingConst.debugger.basic.INPUT_FIELD), text)

class DebuggerAdvanced(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName

    def updateName(self, baseName):
        self.baseName = baseName
    
    def playButton(self):
        self.util.clickButton(self.objName(ScriptingConst.debugger.advanced.PLAY_BUTTON))

class Debugger:    
    def __init__(self):
        self.util = Util()
        self.baseName = ':BaseDebugDialog'
        self.basic = DebuggerBasic(self)
        self.advanced = DebuggerAdvanced(self)
        
    def updateName(self, baseName):
        self.squishName = baseName
        self.basic.updateName(baseName)
        self.advanced.updateName(baseName)
    
    def close(self):
        Util().close(self.baseName)

class Tabs(SquishObjectName):
    def __init__(self, parent):
        self.util = Util()
        self.baseName = parent.baseName
    
    def _clickTab(self, tab):
        self.util.clickTab(self.objName(ScriptingConst.tabs.TABBAR), tab)
    
    def info(self):   
        self._clickTab('Info')
    
    def general(self):
        self._clickTab('General')
    
    def scriptEngine(self):
        self._clickTab('Script Engine')
    
    def customInterfaces(self):
        self._clickTab('Custom Interfaces')
    
    def dataStore(self):
        self._clickTab('Data Store')

class ScriptingInterfaceBase(SquishObjectName):
    '''
    To construct a new SCriptingInterface object either 'aw' or 'menu' needs to be passed as a parameter.
    If 'aw' is passed then it will append the base name for ActivityWizard Scripting objects.
    If 'menu' is passed then it will append the base name for Scripting objects accessed from the menu bar
    '''
    def __init__(self, awOrMenuScripting):
        if awOrMenuScripting == 'aw':
            self.baseName = ':Activity_Wizard.m_contents.ScriptingInterface'
        elif awOrMenuScripting == 'menu':
            self.baseName = ':ScriptingInterface'
        else:
            raise ValueError('Must pass in aw or menu to load the constants for Activity Wizard or Menubar scripting')
        self.util = Util()
        self.info = InfoTab(self)
        self.general = GeneralTab(self)
        self.engine = ScriptEngineTab(self)
        self.customInterfaces = CustomInterfacesTab(self)
        self.dataStore = DataStoreTab(self)
        self.tabs = Tabs(self)
        self.debugger = Debugger()