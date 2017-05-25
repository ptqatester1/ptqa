from API.Utility.Util import Util
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.ViewCommandLog.ViewCommandLogConst import ViewCommandLogConst
util = Util()
options = Options()


def main():
    util.init()
    editOptionsSetting()
    checkpoint1()


def editOptionsSetting():
    options.selectOptionsItem(OptionsConst.VIEW_COMMAND_LOG)

def checkpoint1():
    if(object.exists(ViewCommandLogConst.COMMAND_LOG_WINDOW)):
        test.passes("View Log Window found")
    else:
        test.fail("View Log Window not found")