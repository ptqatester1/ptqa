##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.HomeGateway.HomeGatewayConst import HomeGatewayConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from squish import *
import object

def err(msg = ''):
    raise NotImplementedError(msg)

class FileRow:
    def __init__(self, filename, edit, delete):
        self.filename = filename
        self.edit = edit
        self.delete = delete

class FileEdit(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName        
        
    def updateName(self, squishName):
        self.squishName = squishName

    def filename(self, filename):
        Util().setText(self.objName(HomeGatewayConst.gui.fileEdit.FILE_NAME_EDIT), filename)
    
    def setText(self, text):
        Util().setText(self.objName(HomeGatewayConst.gui.fileEdit.HTML_CONTENT), text)
    
    def fileManagerButton(self):
        Util().clickButton(self.objName(HomeGatewayConst.gui.fileEdit.FILE_MANAGER_BUTTON))
    
    def saveButton(self):
        Util().clickButton(self.objName(HomeGatewayConst.gui.fileEdit.SAVE_BUTTON))
    
class GuiCheck(DeviceBase):
    def __init__(self, parent):
        self.squishName = parent.squishName        
        
    def updateName(self, squishName):
        self.squishName = squishName
        
    def httpOn(self, checked=True):
        Util().isChecked(self.objName(HomeGatewayConst.gui.HTTP_ON_RADIO), checked)
    
    def httpOff(self, checked=True):
        Util().isChecked(self.objName(HomeGatewayConst.gui.HTTP_OFF_RADIO), checked)
    
    def httpsOn(self, checked=True):
        Util().isChecked(self.objName(HomeGatewayConst.gui.HTTPS_ON_RADIO), checked)
    
    def httpsOff(self, checked=True):
        Util().isChecked(self.objName(HomeGatewayConst.gui.HTTPS_OFF_RADIO), checked)

class Gui(DeviceBase):
    def __init__(self, parent):
        self.squishName = parent.squishName        
        self.fileEdit = FileEdit(self)
        self.check = GuiCheck(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
        self.fileEdit.updateName(squishName)
        self.check.updateName(squishName)
    def httpOn(self):
        Util().clickButton(self.objName(HomeGatewayConst.gui.HTTP_ON_RADIO))
    
    def httpOff(self):
        Util().clickButton(self.objName(HomeGatewayConst.gui.HTTP_OFF_RADIO))
    
    def httpsOn(self):
        Util().clickButton(self.objName(HomeGatewayConst.gui.HTTPS_ON_RADIO))
    
    def httpsOff(self):
        Util().clickButton(self.objName(HomeGatewayConst.gui.HTTPS_OFF_RADIO))
    
    @property
    def fileTable(self):
        return findObject(self.objName(HomeGatewayConst.gui.FILE_MANAGER_TABLE))

    
    def getFile(self, filename):
        '''Returns a FileRow instance holding the object for filename, edit, and delete fields'''
        for i in range(self.fileTable.rowCount):
            row = self.objName(HomeGatewayConst.gui.FILE_MANAGER_TABLE + '.item_' + str(i))
            filenameBox = row + '/0'
            editBox = row + '/1'
            deleteBox = row + '/2'
            if findObject(filenameBox).text == filename:
                return FileRow(findObject(filenameBox),
                               findObject(editBox),
                               findObject(deleteBox))
        raise ValueError('Could not find file: ' + filename)
    
    def selectFile(self, filename):
        Util().click(self.getFile(filename).filename)
    
    def editFile(self, filename):
        Util().click(self.getFile(filename).edit)
    
    def deleteFile(self, filename):
        Util().click(self.getFile(filename).delete)
    
    def newFileButton(self):
        Util().clickButton(self.objName(HomeGatewayConst.gui.NEW_FILE_BUTTON))
    
    def importFileButton(self):
        Util().clickButton(self.objName(HomeGatewayConst.gui.IMPORT_BUTTON))