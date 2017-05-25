##Chris Allen

from API.MenuBar.Extensions.ExtensionsConst import ExtensionsConst
from API.Utility.Util import Util
from API.MenuBar.Extensions.Scripting.ScriptingBase import ScriptingInterfaceBase
from API.MenuBar.Extensions.Scripting.ScriptingConst import ScriptingConst
from squish import *

class SecurityTab:
    def __init__(self):
        self.util = Util()
    
class SettingsTab:
    def __init__(self):
        self.util = Util()
    
    def onStartup(self):
        err()
    
    def onDemand(self):
        err()
    
    def disabled(self):
        err()

class DescriptionTab:
    def __init__(self):
        self.util = Util()
    
    @property
    def descriptionText(self):
        err()

class ConfigurePtScriptModule:
    def __init__(self):
        self.util = Util()
    
    @property
    def scriptModuleList(self):
        err()
    
    def selectScript(self):
        err()
    
    def stopButton(self):
        err()
    
    def startButton(self):
        err()
    
    def editButton(self):
        err()
    
    def addButton(self):
        Util().clickButton(ScriptingConst.ADD_BUTT)
        
    def removeButton(self):
        Util().clickButton(ScriptingConst.REMOVE_BUTT)
            
    def newButton(self):
        err()
        
    def clickTab(self, tab):
        err()
        
    def okButton(self):
        err()
    
    def addScript(self, p_item, p_location):
        self.addButton()
        Util().setText(ScriptingConst.Add_Script_Dialog.ADD_SCRIPT_FILENAME_EDIT, Util().getFilePath(p_item, p_location))
        snooze(5)
        Util().clickButton(ScriptingConst.Add_Script_Dialog.ADD_SCRIPT_FILENAME_OPEN_BUTT)
        
    def removeScript(self, p_item):
        Util().clickItem(ScriptingConst.SCRIPT_LIST, p_item)
        self.removeButton()
            
class NewPtScriptModule:
    def __init__(self):
        self.util = Util()

class EditPtScriptModule:
    def __init__(self):
        self.util = Util()

class ConfigureGlobalCustomInterfaces:
    def __init__(self):
        self.util = Util()

class ConfigureFileCustomInterfaces:
    def __init__(self):
        self.util = Util()

class ScriptingMenu:
    def __init__(self):
        self.util = Util()
    
    def selectConfigurPtScriptModule(self):
        err()
    
    def selectNewPtScriptModule(self):
        err()
    
    def selectEditPtScriptModule(self):
        err()
    
    def selectConfigureGlobalCustomInterfaces(self):
        err()
    
    def selectConfigureFileCustomInterfaces(self):
        err()


class ScriptingInterface(ScriptingInterfaceBase):
    def __init__(self):
        '''Call the super class constructor with the 'menu' parameter to tell it to use the extensions menu scripting constants'''
        super(ScriptingInterface, self).__init__('menu')
    None

'''
class Scripting:
    def __init__(self):
        self.util = Util()

    def selectScriptingItem(self, p_item):
        self.activateItem(ExtensionsConst.MENU_BAR, ExtensionsConst.EXTENSIONS)
        self.activateItem(ExtensionsConst.EXTENSIONS_MENU, ExtensionsConst.SCRIPTING)
        self.activateItem(ScriptingConst.SCRIPTING_MENU, p_item)
        

    def addScript(self, p_item, p_location):
        self.clickButton(ScriptingConst.Configure_PT_Script_Modules.ADD_BUTT)
        self.setText(ScriptingConst.Configure_PT_Script_Modules.Add_Script_Dialog.ADD_SCRIPT_FILENAME_EDIT, util.getFilePath(p_item, p_location))
        snooze(5)
        self.clickButton(ScriptingConst.Configure_PT_Script_Modules.Add_Script_Dialog.ADD_SCRIPT_FILENAME_OPEN_BUTT)
    
class ConfigurePTScriptModules:
    def __init__(self):
        self.util = Util()
        pass
    
    def selectModule(self, p_moduleName):
        self.util.click(self.getModuleInList(p_moduleName))
    
    def clickTab(self, p_tabName):
        self.util.clickTab(ScriptingConst.Configure_PT_Script_Modules.TAB_BAR, p_tabName)
    
    def stopButton(self):
        self.util.clickButton(ScriptingConst.Configure_PT_Script_Modules.STOP_BUTT)
    
    def startButton(self):
        self.util.clickButton(ScriptingConst.Configure_PT_Script_Modules.START_BUTT)
    
    def editButton(self):
        self.util.clickButton(ScriptingConst.Configure_PT_Script_Modules.EDIT_BUTT)
    
    def addButton(self):
        self.util.clickButton(ScriptingConst.Configure_PT_Script_Modules.ADD_BUTT)
    
    def newButton(self):
        self.util.clickButton(ScriptingConst.Configure_PT_Script_Modules.NEW_BUTT)
    
    def removeButton(self):
        self.util.clickButton(ScriptingConst.Configure_PT_Script_Modules.REMOVE_BUTT)
    
    def editScript(self, p_moduleName):
        self.selectModule(p_moduleName)
        self.editButton()
    
        
    
    def getModuleInList(self, p_moduleName):
        moduleList = ScriptingConst.Configure_PT_Script_Modules.SCRIPT_LIST
        for i in range(findObject(moduleList).topLevelItemCount):
            module = findObject(moduleList + '.item_' + str(i) + '/0')
            if module.text == p_moduleName:
                return module

class ScriptingInterface:
    def __init__(self):
        self.util = Util()
        pass
    
    def clickTab(self, p_tabName):
        self.util.clickTab(ScriptingConst.FileScriptModule.TAB_BAR, p_tabName)
    
class ScriptEngine:
    def __init__(self):
        self.util = Util()
        pass
    
    def chooseFile(self, p_filename):
        raise Exception('This needs implemented still')
    
    def debuggingOn(self):
        self.util.clickButton(ScriptingConst.FileScriptModule.ScriptEngine.DEBUG_BUTTON)
    
class Debugger:
    ''''''p_baseName would be the equivalent of squishname for devices''''''
    def __init__(self, p_baseName):
        self.util = Util()
        self.squishSyntax = SquishSyntax()
        self.squishName = p_baseName
        pass
    
    def checkDebuggerText(self, p_text, p_occurrenceNum = -1):
        self.squishSyntax.textCheckPoint(str(findObject(self.squishName + ScriptingConst.Debugger.DEBUGGER_TEXT).plainText), p_text, p_occurrenceNum) 
    
    def switchToFullDebugger(self):
        raise Exception('This needs implemented still')
'''