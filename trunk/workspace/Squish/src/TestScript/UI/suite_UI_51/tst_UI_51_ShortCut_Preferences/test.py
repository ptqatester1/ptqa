from API.Utility.Util import Util
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.File import File
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.File.Open.OpenConst import OpenConst
util = Util()
fileMenu = File()

def main():
    util.init()
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(2)
    util.clickButton(OpenConst.CANCEL_OPEN_FILE)
    nativeType("<Ctrl+r>")
    snooze(2)
    if (object.exists(OptionsConst.OPTIONS_DIALOG)):
        test.passes("Preference window found")
        util.close(OptionsConst.OPTIONS_DIALOG)
    else:
        test.fail("Preference window not found")
