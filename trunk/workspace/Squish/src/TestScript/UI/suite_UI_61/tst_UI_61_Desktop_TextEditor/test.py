##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.PC.PC import PC
from API.ComponentBox import ComponentBoxConst

util = Util()

pcNew = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'PC0')
pcSave = PC(ComponentBoxConst.DeviceModel.PC, 150, 100, 'PC1')
pcOpen = PC(ComponentBoxConst.DeviceModel.PC, 200, 100, 'PC2')
pcExit = PC(ComponentBoxConst.DeviceModel.PC, 250, 100, 'PC3')

def main():
    util.init()
    create()
    checkTextEditorNew()
    checkTextEditorSave()
    checkTextEditorOpen()
    checkTextEditorExit()
    
def create():
    pcNew.create()
    pcSave.create()
    pcOpen.create()
    pcExit.create()
    
def checkTextEditorNew():
    pcNew.select()
    pcNew.clickDesktopTab()
    pcNew.desktop.applications.textEditor()
    pcNew.desktop.textEditor.setText('testing')
    pcNew.desktop.textEditor.checkText('testing')
    pcNew.desktop.textEditor.newFile('cancel')
    pcNew.desktop.textEditor.checkText('testing')
    pcNew.desktop.textEditor.newFile('save', 'saveTest')
    pcNew.desktop.textEditor.checkText('testing', 0)
    pcNew.desktop.textEditor.newFile()
    pcNew.desktop.textEditor.checkText('testing', 0)
    pcNew.close()

def checkTextEditorSave():
    pcSave.select()
    pcSave.clickDesktopTab()
    pcSave.desktop.applications.textEditor()
    pcSave.desktop.textEditor.setText('testingSave')
    pcSave.desktop.textEditor.saveFile('cancel', '')
    pcSave.desktop.textEditor.saveFile('save', 'saveTestFile')
    pcSave.close()
    
def checkTextEditorOpen():
    pcOpen.select()
    pcOpen.clickDesktopTab()
    pcOpen.desktop.applications.textEditor()
    pcOpen.desktop.textEditor.setText('testingOpen')
    pcOpen.desktop.textEditor.openFile('cancel', '0/0')
    pcOpen.desktop.textEditor.openFile('discard', '0/0')
    pcOpen.desktop.textEditor.openFile('save', '0/0', 'openSaveTest')
    pcOpen.desktop.textEditor.checkText('This is a sample text file')
    pcOpen.close()
    
def checkTextEditorExit():
    pcExit.select()
    pcExit.clickDesktopTab()
    pcExit.desktop.applications.textEditor()
    pcExit.desktop.textEditor.setText('testingExit')
    pcExit.desktop.textEditor.exit('cancel')
    pcExit.desktop.textEditor.exit('save', 'exitSaveTest')
    pcExit.desktop.applications.textEditor()
    pcExit.desktop.textEditor.setText('testingExit')
    pcExit.desktop.textEditor.exit()
    pcExit.close()
