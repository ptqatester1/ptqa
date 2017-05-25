#######################
#@author: Pamela Vinco
#######################
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.New.NewConst import NewConst
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.File.Save.SaveConst import SaveConst
from API.MenuBar.File.Print.PrintConst import PrintConst
from API.MenuBar.File.RecentFiles.RecentFilesConst import RecentFilesConst
from API.MenuBar.File.File import File
from API.MenuBar.File.Open.Open import Open
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router
import os

#Function initialization
util = Util()
fileMenu = File()
openFile = Open()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 311, 125, "Router0")

def main():
    util.init()
    file_new()
    file_open()
    file_openSamples()
    util.init()
    file_save()
    file_saveAs()
    file_saveAsPKZ()
    file_saveAsCommonCartridge()
    file_print()
    file_recentFiles()
    file_exit()
    
def file_new():
    #Create a device and check that it exists
    router0.create()    
    router0.exists()
    
    #Select New from File Menu and check that the device is not in the workspace anymore
    fileMenu.selectFileItem(FileConst.NEW)
    util.clickButton(NewConst.SAVE_NETWORK_PROMPT_NO)
    router0.doesNotExist()

def file_open():
    #Select Open from File Menu and check that the Open Dialog appears
    fileMenu.selectFileItem(FileConst.OPEN)
    snooze(1)
    if(object.exists(OpenConst.OPEN_FILE_WINDOW)):
        test.passes("Open File Window found")
        util.clickButton(OpenConst.CANCEL_OPEN_FILE)
    else:
        test.fail("Open File Window not found")
        
def file_openSamples():
    #Select Open Samples from File Menu and check that the selected pkt opens (device exists on the workspace)
    fileMenu.selectFileItem(FileConst.OPEN_SAMPLES)
    if not (os.name =='posix'):
        openFile.commonOpenFile(UtilConst.PT_PATH_WINDOWS + "\\saves\\Router\\HSRP\\Hsrp_Ping_When_Router_Priority_Is_Higher.pkt")
    else:
        openFile.commonOpenFile(UtilConst.PT_PATH_LINUX + "/saves/Router/HSRP/Hsrp_Ping_When_Router_Priority_Is_Higher.pkt") 
    router0.exists()
    
def file_save():
    #Select Save from File Menu and check that the Save Dialog appears
    fileMenu.selectFileItem(FileConst.SAVE)
    snooze(1)
    if(object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save File Window found")
        util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    else:
        test.fail("Save File Window not found")
        
def file_saveAs():
    #Select Save As from File Menu and check that the Save As Dialog appears
    fileMenu.selectFileItem(FileConst.SAVE_AS)
    snooze(1)
    if(object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save File Window found")
        util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    else:
        test.fail("Save File Window not found")

def file_saveAsPKZ():
    #Select Save As PKZ from File Menu and check that the Save As Dialog appears
    fileMenu.selectFileItem(FileConst.SAVE_AS_PKZ)
    snooze(1)
    if(object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save File Window found")
        util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    else:
        test.fail("Save File Window not found")

def file_saveAsCommonCartridge():
    #Select Save As Common Cartridge from File Menu and check that the Save As Dialog appears
    fileMenu.selectFileItem(FileConst.SAVE_AS_COMMON_CARTRIDGE)
    snooze(1)
    if(object.exists(SaveConst.SAVE_FILE_WINDOW)):
        test.passes("Save File Window found")
        util.clickButton(SaveConst.CANCEL_SAVE_FILE)
    else:
        test.fail("Save File Window not found")
        
def file_print():
    #Select Print from File Menu and check that the Print Dialog appears
    fileMenu.selectFileItem(FileConst.PRINT)
    snooze(1)
    if(object.exists(PrintConst.PRINT_DIALOG_WINDOW)):
        test.passes("Print Window found")
        util.close(PrintConst.PRINT_DIALOG_WINDOW)
    else:
        test.fail("Print Window not found")
        
def file_recentFiles():
    #Select Recent Files from File Menu and check that the selected pkt opens (device exists on the workspace)
    fileMenu.selectFileItem(FileConst.RECENT_FILES)
    if not (os.name =='posix'):
        util.activateItem(RecentFilesConst.RECENT_FILES_MENU, "C:\\\\PacketTracer\\\\saves\\\\Router\\\\Hsrp\\\\Hsrp\\_Ping\\_When\\_Router\\_Priority\\_Is\\_Higher.pkt")
    else:
        util.activateItem(RecentFilesConst.RECENT_FILES_MENU, "/home/drevil/Desktop/P/ptqa/saves/Router/HSRP/Hsrp_Ping_When_Router_Priority_Is_Higher.pkt")
    router0.exists()
    
def file_exit():
    #Select Exit from File Menu and check that Confirm Exit Window appears
    fileMenu.selectFileItem(FileConst.EXIT)
    snooze(1)
    if(object.exists(UtilConst.EXIT_PT_DIALOG)):
        test.passes("Confirm Exit Window found")
    else:
        test.fail("Confirm Exit Window not found")