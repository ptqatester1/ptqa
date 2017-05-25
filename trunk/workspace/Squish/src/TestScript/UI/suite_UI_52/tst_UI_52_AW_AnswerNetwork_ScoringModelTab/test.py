######################
#@author: Pamela Vinco
######################
from API.ActivityWizard.ActivityWizard import ActivityWizard
from API.Utility.Util import Util
from API import functions
#Function initialization
util = Util()
aw = ActivityWizard()

def main():
    util.init()
    activitywizard()
    workproduct()
    evidence()
   
def activitywizard():
    aw.goToAW()
    aw.selectAnswerNetwork()
    aw.answerNetwork.tabs.scoringModel()
    
def workproduct():
    aw.answerNetwork.scoringModel.workProductFeatures.addButton()
    functions.check(aw.answerNetwork.scoringModel.workProductFeatures.editDialog.dialogWindow)
    aw.answerNetwork.scoringModel.workProductFeatures.editDialog.cancelButton()
    
    #Check that the Work Product table is empty
    test.compare(aw.answerNetwork.scoringModel.workProductFeatures.featureList.rowCount, 0)
    
    aw.answerNetwork.scoringModel.workProductFeatures.addButton()
    aw.answerNetwork.scoringModel.workProductFeatures.editDialog.name('A')
    aw.answerNetwork.scoringModel.workProductFeatures.editDialog.description('Test')
    aw.answerNetwork.scoringModel.workProductFeatures.editDialog.okButton()
    test.compare(aw.answerNetwork.scoringModel.workProductFeatures.featureList.rowCount, 1)

    aw.answerNetwork.scoringModel.workProductFeatures.addButton()
    aw.answerNetwork.scoringModel.workProductFeatures.editDialog.name('B')
    aw.answerNetwork.scoringModel.workProductFeatures.editDialog.description('Test2')
    aw.answerNetwork.scoringModel.workProductFeatures.editDialog.okButton()
    test.compare(aw.answerNetwork.scoringModel.workProductFeatures.featureList.rowCount, 2)

    aw.answerNetwork.scoringModel.workProductFeatures.selectRow(0)
    aw.answerNetwork.scoringModel.workProductFeatures.editButton()
    if aw.answerNetwork.scoringModel.workProductFeatures.editDialog.dialogWindow:
        aw.answerNetwork.scoringModel.workProductFeatures.editDialog.name('A1')
        aw.answerNetwork.scoringModel.workProductFeatures.editDialog.okButton()
    else:
        test.fail("Work Product Feature Window not found")
    
    name = findObject(aw.answerNetwork.scoringModel.workProductFeatures.featureListName + '.item_0/0')
    functions.check(name.text == 'A1')
    
    aw.answerNetwork.scoringModel.workProductFeatures.selectRow(0)
    aw.answerNetwork.scoringModel.workProductFeatures.downButton()
    name = findObject(aw.answerNetwork.scoringModel.workProductFeatures.featureListName + '.item_1/0')
    functions.check(name.text == 'A1')
    
    aw.answerNetwork.scoringModel.workProductFeatures.selectRow(1)
    aw.answerNetwork.scoringModel.workProductFeatures.upButton()
    name = findObject(aw.answerNetwork.scoringModel.workProductFeatures.featureListName + '.item_0/0')
    functions.check(name.text == 'A1')
    
    aw.answerNetwork.scoringModel.workProductFeatures.selectRow(0)
    aw.answerNetwork.scoringModel.workProductFeatures.removeButton()
    name = findObject(aw.answerNetwork.scoringModel.workProductFeatures.featureListName + '.item_0/0')
    functions.check(name.text == 'B')
    
def evidence():
    aw.answerNetwork.scoringModel.scoringRules.addButton()
    
    if aw.answerNetwork.scoringModel.scoringRules.editDialog.editDialog:
        test.passes("Evidence Window found")
        aw.answerNetwork.scoringModel.scoringRules.editDialog.cancelButton()
    else:
        test.fail("Evidence Window not found")
    
    test.compare(aw.answerNetwork.scoringModel.scoringRules.scoringList.rowCount, 0)
    
    aw.answerNetwork.scoringModel.scoringRules.addButton()
    aw.answerNetwork.scoringModel.scoringRules.editDialog.name('A')
    aw.answerNetwork.scoringModel.scoringRules.editDialog.description('Test')
    aw.answerNetwork.scoringModel.scoringRules.editDialog.okButton()
    
    test.compare(aw.answerNetwork.scoringModel.scoringRules.scoringList.rowCount, 1)
    
    for ch in ['B', 'C', 'D']:
        aw.answerNetwork.scoringModel.scoringRules.addButton()
        aw.answerNetwork.scoringModel.scoringRules.editDialog.name(ch)
        aw.answerNetwork.scoringModel.scoringRules.editDialog.description('Test')
        aw.answerNetwork.scoringModel.scoringRules.editDialog.okButton()
    test.compare(aw.answerNetwork.scoringModel.scoringRules.scoringList.rowCount, 4)
    
    aw.answerNetwork.scoringModel.scoringRules.selectRow(0)
    aw.answerNetwork.scoringModel.scoringRules.editButton()
    if aw.answerNetwork.scoringModel.scoringRules.editDialog.editDialog:
        aw.answerNetwork.scoringModel.scoringRules.editDialog.name('A1')
        aw.answerNetwork.scoringModel.scoringRules.editDialog.okButton()
    else:
        test.fail("Evidence Window not found")
    
    name = findObject(aw.answerNetwork.scoringModel.scoringRules.scoringListName + '.item_0/1')
    functions.check(name.text == 'A1')
    
    aw.answerNetwork.scoringModel.scoringRules.selectRow(0)
    aw.answerNetwork.scoringModel.scoringRules.downButton()
    name = findObject(aw.answerNetwork.scoringModel.scoringRules.scoringListName + '.item_1/1')
    functions.check(name.text == 'A1')
    
    aw.answerNetwork.scoringModel.scoringRules.selectRow(1)
    aw.answerNetwork.scoringModel.scoringRules.upButton()
    name = findObject(aw.answerNetwork.scoringModel.scoringRules.scoringListName + '.item_0/1')
    functions.check(name.text == 'A1')
    
    for i in range(3):
        aw.answerNetwork.scoringModel.scoringRules.selectRow(0)
        aw.answerNetwork.scoringModel.scoringRules.removeButton()
    name = findObject(aw.answerNetwork.scoringModel.scoringRules.scoringListName + '.item_0/1')
    functions.check(name.text == 'D')