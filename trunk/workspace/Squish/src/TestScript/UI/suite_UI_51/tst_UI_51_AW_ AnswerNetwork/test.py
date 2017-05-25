from API.ActivityWizard.AnswerNetwork.AnswerNetwork import AnswerNetwork
from API.ActivityWizard.AnswerNetwork.AnswerNetworkConst import AnswerNetworkConst
from API.ActivityWizard.Save.SaveConst import SaveConst
from API.ComponentBox import ComponentBoxConst

from API.Device.EndDevice.PC.PC import PC
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Utility.Util import Util
from API.Utility import UtilConst

#Function initialization
answerNetwork = AnswerNetwork()
util = Util()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 52, 119, "PC0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 168, 117, "PC1")

def main():
    util.init()  
    checkPoint1()
    checkPoint2()
    checkPoint3()

def checkPoint1():
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    util.clickButton(AnswerNetworkConst.ANSWER_NETWORK)
    util.clickButton(AnswerNetworkConst.SHOW_ANSWER_NETWORK)
    if (object.exists(AnswerNetworkConst.ACTIVITY_WIZARD_ICON)):
        test.passes("Show Answer Network works")
    else:
        test.fail("Show Answer Network does not work")
    util.click(AnswerNetworkConst.ACTIVITY_WIZARD_ICON)

def checkPoint2():
    answerNetwork.importAnswerNetwork(util.getFilePath("UI14_ImportAnswerNetwork.pkt", "UI"))
    util.clickButton(AnswerNetworkConst.SHOW_ANSWER_NETWORK)
    snooze(2)
    pc0.select()
    pc0.physical.checkModuleText("The WMP300N module provides one 2.4GHz wireless interface suitable for connection to wireless networks. The module supports protocols that use Ethernet for LAN access.")
    util.click(AnswerNetworkConst.ACTIVITY_WIZARD_ICON)

def checkPoint3():
    util.clickButton(AnswerNetworkConst.EXPORT_ANSWER_NETWORK_TO_FILE)
    util.setText(AnswerNetworkConst.EXPORT_ANSWER_NETWORK_TO_FILE_DIALOG, util.getFilePath("UI14_ExportAnswerNetwork.pkt", "UI"))
    util.clickButton(AnswerNetworkConst.EXPORT_ANSWER_NETWORK_TO_FILE_DIALOG_OK)
    util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)