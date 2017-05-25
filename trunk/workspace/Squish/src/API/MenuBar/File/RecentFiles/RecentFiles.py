#*******************************************
#@author: Tuan Hoang
#@summary: RecentFiles handles the Recent Files menu
#*******************************************
from API.SquishSyntax import SquishSyntax
from API.MenuBar.File.RecentFiles.RecentFilesConst import RecentFilesConst
from API.MenuBar.File.FileConst import FileConst 
from API.MenuBar.File.File import File
from API.Utility import UtilConst
from API.Utility.Util import Util
from squish import *
import os
filemenu = File()

class RecentFiles(SquishSyntax):
    #@summary: Opens up a file from Recent Files
    #@param p_fileName: File name
    #@param p_testType: Test suite
    def openRecentFile(self, p_fileName, p_testType):
        util = Util()
        filemenu.selectFileItem(FileConst.RECENT_FILES)
        if(os.name =='posix'):
            p_filePath = "/home/drevil/Desktop/P/ptqa/trunk/workspace/Squish/Pkt_Pka_ForTesting/" + p_testType + "/" + p_fileName
        else:
        #    p_filePath = "P:\\ptqa\\trunk\\workspace\\Squish\\Pkt\\_Pka\\_ForTesting\\" + p_testType + "\\" + p_fileName
            p_filePath = util.getFilePath(p_fileName, p_testType)
        self.activateItem(RecentFilesConst.RECENT_FILES_MENU, p_filePath)
