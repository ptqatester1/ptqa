from API.MenuBar.File.Save.SaveConst import SaveConst
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.Device.Router.Router import Router
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from API.ComponentBox import ComponentBoxConst
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst

#Function initialization
util = Util()
mainToolbar = MainToolbar()

#Device intialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 200, 100, "Router1")

def main():
    util.init()
    addNewDescriptionText()
    removeDescriptionText()

def addNewDescriptionText():
    util.clickButton(MainToolbarConst.NETWORK_DESCRIPTION)
    mainToolbar.addNetworkDescription("This is an empty file")

    util.clickButton(MainToolbarConst.SAVE)
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("UI2_InfoBox.pkt", UtilConst.UI_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
        
    util.newWorkspace()
    util.open("UI2_InfoBox.pkt", UtilConst.UI_TEST)
    snooze(5)
    mouseDrag(waitForObject(MainToolbarConst.NETWORK_DESCRIPTION_TEXT), 172, 18, -183, -17, 1, Qt.LeftButton)
    test.compare(findObject(MainToolbarConst.NETWORK_DESCRIPTION_TEXT).selectedText, "This is an empty file")

def removeDescriptionText():
    mainToolbar.addNetworkDescription(" ")
    util.clickButton(MainToolbarConst.SAVE)
    snooze(2)
    if (object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    util.newWorkspace()
    util.open("UI2_InfoBox.pkt", UtilConst.UI_TEST)
    util.clickButton(MainToolbarConst.NETWORK_DESCRIPTION)
    mouseDrag(waitForObject(MainToolbarConst.NETWORK_DESCRIPTION_TEXT), 172, 18, -183, -17, 1, Qt.LeftButton)
    snooze(2)
    test.compare(findObject(MainToolbarConst.NETWORK_DESCRIPTION_TEXT2).selectedText, " ")