from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.Utility.Util import Util
optionsMenu = Options()
util = Util()


def main():
    util.init()
    optionsMenu.selectOptionsItem(OptionsConst.PREFERENCES)
    if (object.exists(OptionsConst.OPTIONS_DIALOG)):
        test.passes("Preference window found")
        util.close(OptionsConst.OPTIONS_DIALOG)
    else:
        test.fail("Preference window not found")
