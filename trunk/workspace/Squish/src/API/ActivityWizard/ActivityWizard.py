#*********************************************************************************************************
#@author: AbbasH
#@summary: ActivityWizard handles the actions in the Activity Wizard that don't belong to other categories 
#*********************************************************************************************************
from API.ActivityWizard.ActivityWizardConst import ActivityWizardConst as AWConst


from API.ActivityWizard.Welcome.Welcome import Welcome
from API.ActivityWizard.VariableManager.VariableManager import VariableManager
from API.ActivityWizard.Instructions.Instructions import Instructions
from API.ActivityWizard.AnswerNetwork.AnswerNetwork import AnswerNetwork
from API.ActivityWizard.Scripting.Scripting import Scripting
from API.ActivityWizard.Password.Password import Password
from API.ActivityWizard.TestActivity.TestActivity import TestActivity
from API.ActivityWizard.InitialNetwork.InitialNetwork import InitialNetwork
from API.ActivityWizard.InstructionDialog.InstructionDialog import InstructionDialog
#Need to add check activity
from API.ActivityWizard.Save.Save import Save
from API.ActivityWizard.Exit.Exit import Exit

from API.Utility.Util import Util
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar

class ActivityWizard:
    def __init__(self):
        self.util = Util()
        self.welcome = Welcome()
        self.variableManager = VariableManager()
        self.instructions = Instructions()
        self.initialNetwork = InitialNetwork()
        self.answerNetwork = AnswerNetwork()
        self.scripting = Scripting()
        self.password = Password()
        self.testActivity = TestActivity()
        self.save = Save()
        self.exit = Exit()
        self.instructionDialog = InstructionDialog()
    
    def selectWelcome(self):
        self.welcome.select()
    
    def selectVariableManager(self):
        self.variableManager.select()
    
    def selectInstructions(self):
        self.instructions.select()
    
    def selectAnswerNetwork(self):
        self.util.clickButton(AWConst.ANSWER_NETWORK)
    
    def selectScripting(self):
        self.util.clickButton(AWConst.SCRIPTING)
    
    def selectInitialNetwork(self):
        self.util.clickButton(AWConst.INITIAL_NETWORK)
    
    def selectPassword(self):
        self.util.clickButton(AWConst.PASSWORD)
    
    def selectTestActivity(self):
        self.util.clickButton(AWConst.TEST_ACTIVITY)
    
    def selectCheckActivity(self):
        self.util.clickButton(AWConst.CHECK_ACTIVITY)
    
    def selectSave(self):
        self.save.saveButton()
    
    def selectSaveAs(self):
        self.save.saveAsButton()
    
    def selectSaveAsPkz(self):
        self.save.saveAsPkzButton()
    
    def selectExportAsCC(self):
        self.save.exportAsCCButton()
    
    def selectExit(self):
        self.util.clickButton(AWConst.EXIT)
    
    def goToAW(self, useNetwork = True, **kwargs):
        MainToolbar().activityWizard(useNetwork, **kwargs)
        