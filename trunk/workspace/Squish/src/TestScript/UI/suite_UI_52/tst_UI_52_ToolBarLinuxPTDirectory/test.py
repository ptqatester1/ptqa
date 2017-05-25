######################
#@author: Pamela Vinco
######################

from API.Utility import UtilConst
from API.Utility.Util import Util
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from API.MenuBar.File.Save.SaveConst import SaveConst
import os

#Function initialization
util = Util()
mainTool = MainToolbar()

def main():
    util.init()
    if (os.name=='posix'):
        mainTool.saveFile("test.pkt")
        if (object.exists(SaveConst.NO_WRITE_PERMISSION_PROMPT)):
            test.fail("Cannot save in PT directory.")
        else:
            test.passes("Save in PT directory is successful.")
    else:
        test.log("This test is for Linux only.")