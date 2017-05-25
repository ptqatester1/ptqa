######################
#@author: Pamela Vinco
######################

from API.ActivityWizard.ActivityWizard import ActivityWizard
from API.Utility.Util import Util
from API.Utility import UtilConst

util = Util()
aw = ActivityWizard()

def main():
    util.init()  
    activityCreationExperience()
    authorInformation()
    
def activityCreationExperience():
    aw.goToAW()
    aw.selectAnswerNetwork()
    aw.answerNetwork.tabs.assessmentTree()
    aw.answerNetwork.tabs.connectivityTest()
    aw.answerNetwork.tabs.overallFeedback()
    aw.answerNetwork.tabs.scoringModel()
    aw.answerNetwork.tabs.settings()
     
def authorInformation():
    aw.selectWelcome()
    aw.welcome.editAuthorInformation('Test') 
    aw.selectAnswerNetwork()
    aw.selectWelcome()
    aw.save.saveAs(util.getFilePath("AuthorInfo.pka", UtilConst.UI_TEST), overwrite=True)
    aw.exit.exit()
    
    util.open("AuthorInfo.pka", UtilConst.UI_TEST)
    
    aw.goToAW()
    aw.selectWelcome()
    aw.welcome.textCheckPoint("Test")