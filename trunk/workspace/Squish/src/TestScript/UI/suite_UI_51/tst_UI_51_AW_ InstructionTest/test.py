from API.ActivityWizard.Instructions.Instructions import Instructions
from API.ActivityWizard.Instructions.InstructionsConst import InstructionsConst
from API.ActivityWizard.TestActivity.TestActivityConst import TestActivityConst
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Utility.Util import Util
from API.Utility import UtilConst
instructions = Instructions()
util = Util()

def main():
    util.init()  
    checkPoint1()
    checkPoint2()
    checkPoint3()
    checkPoint4()
    checkPoint5()
    checkPoint6()
    checkPoint7()
    checkPoint8()

    
def checkPoint1():
    util.clickButton(MainToolbarConst.ACTIVITY_WIZARD)
    util.clickButton(InstructionsConst.INSTRUCTIONS)
    util.clickButton(InstructionsConst.INSERT_PAGE)
    util.textCheckPoint(InstructionsConst.PAGE_NUMBER, "2/2")

def checkPoint2():
    util.clickButton(InstructionsConst.PREVIOUS_PAGE)
    util.textCheckPoint(InstructionsConst.PAGE_NUMBER, "1/2")

def checkPoint3():
    util.clickButton(InstructionsConst.NEXT_PAGE)
    util.textCheckPoint(InstructionsConst.PAGE_NUMBER, "2/2")

def checkPoint4():
    util.clickButton(InstructionsConst.REMOVE_PAGE)
    util.textCheckPoint(InstructionsConst.PAGE_NUMBER, "1/1")

def checkPoint5():
    instructions.importPage(util.getFilePath("UI14_Instructions_Import.htm", UtilConst.UI_TEST))
    snooze(2)
    util.textCheckPoint(InstructionsConst.INSTRUCTIONS_TEXT_FIELD, "Testing Import Instructions")

def checkPoint6():
    util.clickButton(InstructionsConst.EXPORT_PAGE)
    util.setText(InstructionsConst.EXPORT_PAGE_DIALOG, util.getFilePath("UI14_Instructions_Export.htm", UtilConst.UI_TEST))
    util.clickButton(InstructionsConst.EXPORT_PAGE_DIALOG_SAVE)
    snooze(1)
    util.clickButton(InstructionsConst.EXPORT_PAGE_DIALOG_OVERWRITE_YES)

def checkPoint7():
    util.clickButton(InstructionsConst.INSERT_PAGE)
    instructions.edit.setText("Page 2")
    util.clickButton(InstructionsConst.PREVIOUS_PAGE)
    instructions.edit.setText("Page 1")
    instructions.exportAll(util.getFilePath("", UtilConst.UI_TEST))

def checkPoint8():
    instructions.edit.setText("  ")
    util.clickButton(InstructionsConst.NEXT_PAGE)
    util.clickButton(InstructionsConst.REMOVE_PAGE)
    instructions.importAll(util.getFilePath("", UtilConst.UI_TEST))
    util.clickButton(InstructionsConst.PREVIOUS_PAGE)
    util.textCheckPoint(InstructionsConst.INSTRUCTIONS_TEXT_FIELD, "Page 1")

    util.clickTab(InstructionsConst.TAB_BAR, InstructionsConst.PREVIEW_AS_HTML)
    util.textCheckPoint(InstructionsConst.PREVIEW_AS_HTML_TEXT, "Page 1")
    
    util.clickTab(InstructionsConst.TAB_BAR, InstructionsConst.EDIT)
    util.clickButton(InstructionsConst.NEXT_PAGE)

    util.textCheckPoint(InstructionsConst.INSTRUCTIONS_TEXT_FIELD, "Page 2")
    util.clickTab(InstructionsConst.TAB_BAR, InstructionsConst.PREVIEW_AS_HTML)
    util.textCheckPoint(InstructionsConst.PREVIEW_AS_HTML_TEXT, "Page 2")
