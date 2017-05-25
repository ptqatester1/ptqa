##Chris Allen
##Santity test to check opening a file, editing it, saving it, reopening it, saving it as different file
##reopening the previous file and checking it has the expected behavior

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.Save.Save import Save
from API.MenuBar.File.Save.SaveConst import SaveConst
from API.MenuBar.File.Open.Open import Open
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.Toolbar.CommonToolsBar.CommonToolsBar import CommonToolsBar
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst

util = Util()
save = Save()
fileOpen = Open()
ctb = CommonToolsBar()
fileMenu = File()

r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
r2 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 100, "Router1")
r3 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 300, 100, "Router2")
r4 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 200, "Router3")
r5 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 200, "Router4")
r6 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 300, 200, "Router5")

def main():
    createTopology()
    saveFile()
    openFile()
    editFile()
    reSaveFile()
    openFile()
    check()
    
def createTopology():
    def createRtr(dev):
        util.createDevice(ComponentBoxConst.DeviceType.ROUTER, dev.model, dev.x, dev.y)
    createRtr(r1)
    createRtr(r2)
    createRtr(r3)
    createRtr(r4)
    createRtr(r5)
    createRtr(r6)
    
    def connect(dev1, dev2):
        util.connect(dev1.x, dev1.y, dev2.x, dev2.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    connect(r1, r2)
    connect(r2, r3)
    connect(r3, r4)
    connect(r4, r5)
    connect(r5, r6)
    None
    
def saveFile():
    save.saveFile(util.getFilePath("editingFileTest.pkt", UtilConst.SANITY_TEST))
    if(object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
    None
    
def openFile():
    fileOpen.openFileNoSave(util.getFilePath("editingFileTest.pkt", UtilConst.SANITY_TEST))
    
def editFile():
    ctb.deleteItem(r1.x, r1.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r1.model, r1.x, r1.y + 200)
    util.connect(r6.x, r6.y, r1.x, r1.y + 200, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    None
    
def reSaveFile():
    fileMenu.selectFileItem(FileConst.SAVE_AS)
    util.setText(SaveConst.SAVE_FILE_NAME, util.getFilePath("editingFileTestPart2.pkt", UtilConst.SANITY_TEST))
    util.clickButton(SaveConst.CONFIRM_SAVE_FILE)
    if(object.exists(SaveConst.OVERWRITE_FILE_PROMPT)):
        util.clickButton(SaveConst.OVERWRITE_FILE_PROMPT_YES)
        
def check():
    r1.select()
    r1.clickCliTab()
    test.passes("If the router is present there will be no errors and the test will pass.")
    None
    