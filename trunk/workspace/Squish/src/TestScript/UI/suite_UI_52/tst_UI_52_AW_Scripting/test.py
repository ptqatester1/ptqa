######################
#@author: Pamela Vinco
######################
from API.ActivityWizard.ActivityWizard import ActivityWizard
from API.Utility.Util import Util
from API.Utility import UtilConst
from API import functions
from API.MenuBar.Extensions.Scripting.ScriptingConst import ScriptingConst

#Function initialization
util = Util()
aw = ActivityWizard()

def main():
    util.init()
    scriptEngine()
    
def scriptEngine():
    aw.goToAW()
    aw.selectScripting()
    
    aw.scripting.tabs.scriptEngine()
    functions.check(aw.scripting.engine.scriptList.count == 4)
    
    aw.scripting.engine.addScript("Test.js")
    functions.check(aw.scripting.engine.scriptList.count == 5)
    
    #Check that editing script content is working
    aw.scripting.engine.editScript('Test.js', 'Test')
    aw.scripting.engine.selectScript('Main.js')
    aw.scripting.engine.selectScript('Test.js')
    aw.scripting.engine.textCheckPoint('Test')
    
    #Check that renaming a script is working
    aw.scripting.engine.renameScript('Test.js', 'Test1.js')
    aw.scripting.engine.selectScript('Test1.js')
    
    #Check that Export script cancel button is working (Export window should not be visible after clicking on Cancel)
    aw.scripting.engine.selectScript('Test1.js')
    aw.scripting.engine.exportButton()
    aw.scripting.engine.popups.exportImportScriptCancelButton()
    if object.exists(ScriptingConst.scriptEngine.EXPORT_IMPORT_FILE_WINDOW):
        test.fail("Export Window is still visible")
    else:
        test.passes("Export Window is not visible")
    
    #Check that Export script save button is working
    aw.scripting.engine.exportScript("Test1.js", UtilConst.UI_TEST)

    #Check that removing a script is working

    aw.scripting.engine.removeScript("Test1\\.js")
    functions.check(aw.scripting.engine.scriptList.count == 4)
    
    #Check that Import script cancel button is working (Import window should not be visible after clicking on Cancel and that number of scripts remain the same)
    aw.scripting.engine.importButton()
    aw.scripting.engine.popups.exportImportScriptCancelButton()
    if object.exists(ScriptingConst.scriptEngine.EXPORT_IMPORT_FILE_WINDOW):
        test.fail("Export Window is still visible")
    else:
        test.passes("Export Window is not visible")
    functions.check(aw.scripting.engine.scriptList.count == 4)
    
    #Check that Import script open button is working (Number of scripts should increment by 1)
    aw.scripting.engine.importScript("Test1.js", UtilConst.UI_TEST)
    functions.check(aw.scripting.engine.scriptList.count == 5)
    
    #Delete the script again to keep default PT settings
    aw.scripting.engine.removeScript("Test1\\.js")
