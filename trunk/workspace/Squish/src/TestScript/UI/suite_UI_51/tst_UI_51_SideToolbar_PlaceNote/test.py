from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Utility.Util import Util

util = Util()
commonToolsBar = CommonToolsBar()

def main():
    util.init()
    checkPoint()

def checkPoint():
    commonToolsBar.addPlaceNote("test", 200, 100)
    util.clickOnWorkspace(100, 100)
    util.clickOnWorkspace(200, 100)
    util.textCheckPoint(CommonToolsBarConst.PLACENOTE_TEXT_EDIT, "test")