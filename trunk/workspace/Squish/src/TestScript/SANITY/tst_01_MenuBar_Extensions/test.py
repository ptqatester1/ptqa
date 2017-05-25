#######################
#@author: Pamela Vinco
#######################
from API.MenuBar.Extensions.Extensions import Extensions
from API.MenuBar.Extensions.ExtensionsConst import ExtensionsConst
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst
from API.Utility.Util import Util

#Function initialization
util = Util()
extensionsMenu = Extensions()

def main():
    util.init()
    extensions_activityWizard()
    util.init()
    extensions_multiuser()
    extensions_ipc()
    extensions_scripting()
    
def extensions_activityWizard():
    #Select Activity Wizard from Extensions menu and check that PT goes to Activity Wizard mode
    extensionsMenu.selectExtensionsItem(ExtensionsConst.ACTIVITY_WIZARD)
    snooze(1)
    if(object.exists(ActivityWizardConst.ACTIVITY_WIZARD_WINDOW)):
        test.passes("Activity Wizard Window found")
    else:
        test.fail("Activity Wizard Window not found")
        
def extensions_multiuser():
    #Select Multiuser Listen from Extensions menu and check that the Listen window appears
    extensionsMenu.selectExtensionsMultiuserItem(ExtensionsConst.Multiuser.LISTEN)
    snooze(1)
    if(object.exists(ExtensionsConst.Multiuser.Listen.LISTEN_WINDOW)):
        test.passes("Listen Window found")
        util.clickButton(ExtensionsConst.Multiuser.Listen.CANCEL_BUTT)
    else:
        test.fail("Listen Window not found")
        
    #Select Multiuser Port Visibility from Extensions menu and check that the Port Visibility window appears
    extensionsMenu.selectExtensionsMultiuserItem(ExtensionsConst.Multiuser.PORT_VISIBILITY)
    snooze(1)
    if(object.exists(ExtensionsConst.Multiuser.Port_Visibility.PORT_VISIBILITY_WINDOW)):
        test.passes("Port Visibility Window found")
        util.clickButton(ExtensionsConst.Multiuser.Port_Visibility.CANCEL_BUTT)
    else:
        test.fail("Port Visibility not found")
        
    #Select Multiuser Options from Extensions menu and check that the Options window appears
    extensionsMenu.selectExtensionsMultiuserItem(ExtensionsConst.Multiuser.OPTIONS)
    snooze(1)
    if(object.exists(ExtensionsConst.Multiuser.Options.OPTIONS_WINDOW)):
        test.passes("Options Window found")
        util.clickButton(ExtensionsConst.Multiuser.Options.CANCEL_BUTT)
    else:
        test.fail("Options Window not found")
        
def extensions_ipc():
    #Select IPC Configure Apps from Extensions menu and check that the Configure Apps window appears
    extensionsMenu.selectExtensionsIPCItem(ExtensionsConst.Ipc.CONFIGURE_APPS)
    snooze(1)
    if(object.exists(ExtensionsConst.Ipc.Configure_Apps.CONFIGURE_APPS_WINDOW)):
        test.passes("Configure Apps Window found")
        util.clickButton(ExtensionsConst.Ipc.Configure_Apps.OK_BUTT)
    else:
        test.fail("Configure Apps Window not found")
        
    #Select IPC Show Active Apps from Extensions menu and check that the Active Apps window appears
    extensionsMenu.selectExtensionsIPCItem(ExtensionsConst.Ipc.ACTIVE_APPS)
    snooze(1)
    if(object.exists(ExtensionsConst.Ipc.Active_Apps.ACTIVE_APPS_WINDOW)):
        test.passes("Active Apps Window found")
        util.clickButton(ExtensionsConst.Ipc.Active_Apps.CANCEL_BUTT)
    else:
        test.fail("Active Apps Window not found")
        
    #Select IPC Log from Extensions menu and check that the Log window appears
    extensionsMenu.selectExtensionsIPCItem(ExtensionsConst.Ipc.LOG)
    snooze(1)
    if(object.exists(ExtensionsConst.Ipc.Log.LOG_WINDOW)):
        test.passes("Log Window found")
        util.clickButton(ExtensionsConst.Ipc.Log.CLOSE_BUTT)
    else:
        test.fail("Log Window not found")
        
def extensions_scripting():
    #Select Scripting Configure PT Script Modules from Extensions menu and check that the Configure PT Script Modules window appears
    extensionsMenu.selectExtensionsScriptingItem(ExtensionsConst.Scripting.CONFIGURE_PT_SCRIPT_MODULES)
    snooze(1)
    if(object.exists(ExtensionsConst.Scripting.Configure_PT_Script_Modules.CONFIGURE_PT_SCRIPT_MODULE_WINDOW)):
        test.passes("Configure PT Script Modules Window found")
        util.clickButton(ExtensionsConst.Scripting.Configure_PT_Script_Modules.OK_BUTT)
    else:
        test.fail("Configure PT Script Modules Window not found")
        
    #Select Scripting New PT Script Module from Extensions menu and check that the New PT Script Module window appears
    extensionsMenu.selectExtensionsScriptingItem(ExtensionsConst.Scripting.NEW_PT_SCRIPT_MODULE)
    snooze(1)
    if(object.exists(ExtensionsConst.Scripting.New_PT_Script_Module.NEW_PT_SCRIPT_MODULE_WINDOW)):
        test.passes("New PT Script Module Window found")
        util.close(ExtensionsConst.Scripting.New_PT_Script_Module.NEW_PT_SCRIPT_MODULE_WINDOW)
        util.clickButton(ExtensionsConst.Scripting.New_PT_Script_Module.CONFIRM_EXIT_YES)
    else:
        test.fail("New PT Script Module Window not found")
        
    #Select Scripting Edit File Script Module from Extensions menu and check that the Edit File Script Module window appears
    extensionsMenu.selectExtensionsScriptingItem(ExtensionsConst.Scripting.EDIT_FILE_SCRIPT_MODULE)
    snooze(1)
    if(object.exists(ExtensionsConst.Scripting.Edit_File_Script_Module.EDIT_FILE_SCRIPT_MODULE_WINDOW)):
        test.passes("Edit File Script Module Window found")
        util.close(ExtensionsConst.Scripting.Edit_File_Script_Module.EDIT_FILE_SCRIPT_MODULE_WINDOW)
    else:
        test.fail("Edit File Script Module Window not found")
        
    #Select Scripting Configure Global Custom Interfaces from Extensions menu and check that the Configure Global Custom Interfaces window appears
    extensionsMenu.selectExtensionsScriptingItem(ExtensionsConst.Scripting.CONFIGURE_GLOBAL_CUSTOM_INTERFACES)
    snooze(1)
    if(object.exists(ExtensionsConst.Scripting.Configure_Global_Custom_Interfaces.CONFIGURE_GLOBAL_CUSTOM_INTERFACES_WINDOW)):
        test.passes("Configure Global Custom Interfaces Window found")
        util.close(ExtensionsConst.Scripting.Configure_Global_Custom_Interfaces.CONFIGURE_GLOBAL_CUSTOM_INTERFACES_WINDOW)
    else:
        test.fail("Configure Global Custom Interfaces Window not found")
        
    #Select Scripting Configure File Custom Interfaces from Extensions menu and check that the Configure File Custom Interfaces window appears
    extensionsMenu.selectExtensionsScriptingItem(ExtensionsConst.Scripting.CONFIGURE_FILE_CUSTOM_INTERFACES)
    snooze(1)
    if(object.exists(ExtensionsConst.Scripting.Configure_File_Custom_Interfaces.CONFIGURE_FILE_CUSTOM_INTERFACES_WINDOW)):
        test.passes("Configure File Custom Interfaces Window found")
        util.close(ExtensionsConst.Scripting.Configure_File_Custom_Interfaces.CONFIGURE_FILE_CUSTOM_INTERFACES_WINDOW)
    else:
        test.fail("Configure File Custom Interfaces Window not found")