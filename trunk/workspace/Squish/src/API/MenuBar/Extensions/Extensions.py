#**************************************************************************
#@author: Tuan Hoang
#@summary: Extensions handles the Extensions menu
#**************************************************************************
from API.MenuBar.Extensions.ExtensionsConst import ExtensionsConst
from API.SquishSyntax import SquishSyntax

class Scripting:
    def __init__(self):
        self.sq = SquishSyntax()
    
    def _selectExtensions(self):
        self.sq.activateItem(ExtensionsConst.MENU_BAR, "Extensions")
    
    def _selectExtensionsScriptingItem(self, item):
        self._selectExtensions()
        self.sq.activateItem(ExtensionsConst.EXTENSIONS_MENU, ExtensionsConst.SCRIPTING)
        self.sq.activateItem(ExtensionsConst.EXTENSIONS_SCRIPTING_MENU, item)
    
    def configurePtScriptModules(self):
        self._selectExtensionsScriptingItem(ExtensionsConst.Scripting.CONFIGURE_PT_SCRIPT_MODULES)
        
    def newPtScriptModule(self):
        self._selectExtensionsScriptingItem(ExtensionsConst.Scripting.NEW_PT_SCRIPT_MODULE)
        
    def editFileScriptModule(self):
        self._selectExtensionsScriptingItem(ExtensionsConst.Scripting.EDIT_FILE_SCRIPT_MODULE)
        
    def configureGlabalCustomInterfaces(self):
        self._selectExtensionsScriptingItem(ExtensionsConst.Scripting.CONFIGURE_GLOBAL_CUSTOM_INTERFACES)
        
    def configureFileCustomInterfaces(self):
        self._selectExtensionsScriptingItem(ExtensionsConst.Scripting.CONFIGURE_FILE_CUSTOM_INTERFACES)
        
class Extensions:
    def __init__(self):
        self.sq = SquishSyntax()
        self.scripting = Scripting()
        
    def selectExtensions(self):
        self.sq.activateItem(ExtensionsConst.MENU_BAR, "Extensions")
    #@summary: Selects p_item from the Extensions menu
    #@param p_item: IPC, Multiuser, or Activity Wizard
    def selectExtensionsItem(self, p_item):
        self.selectExtensions()
        self.sq.activateItem(ExtensionsConst.EXTENSIONS_MENU, p_item)
        
    def selectExtensionsMultiuserItem(self, p_item):       
        self.selectExtensions()
        self.sq.activateItem(ExtensionsConst.EXTENSIONS_MENU, ExtensionsConst.MULTIUSER)
        self.sq.activateItem(ExtensionsConst.EXTENSION_MULTIUSER_MENU, p_item)
        
    def selectExtensionsIPCItem(self, p_item):       
        self.sq.selectExtensions()
        self.sq.activateItem(ExtensionsConst.EXTENSIONS_MENU, ExtensionsConst.IPC)
        self.sq.activateItem(ExtensionsConst.EXTENSIONS_IPC_MENU, p_item)
        
    def selectExtensionsScriptingItem(self, p_item):
        self.selectExtensions()
        self.sq.activateItem(ExtensionsConst.EXTENSIONS_MENU, ExtensionsConst.SCRIPTING)
        self.sq.activateItem(ExtensionsConst.EXTENSIONS_SCRIPTING_MENU, p_item)
        
        