##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.EndDevice.PC.PC import PC
from API.ComponentBox import ComponentBoxConst
from API import functions

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, 'Server0')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 100, 'PC1')
defaultFtpFiles = []

def main():
    util.init()
    create()
    checkDefaults()
    addFtpUsers()
    changeUsersAttributes()
    removeUsers()
    removeFile()
    
def create():
    s0.create()
    util.fastForwardTime()

def checkDefaults():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('FTP')
    s0.services.ftp.check.on(True)
    s0.services.ftp.check.off(False)
    s0.services.ftp.check.writeCheckbox(False)
    s0.services.ftp.check.readCheckbox(False)
    s0.services.ftp.check.deleteCheckbox(False)
    s0.services.ftp.check.renameCheckbox(False)
    s0.services.ftp.check.listCheckbox(False)
    
    s0.services.ftp.check.username('')
    s0.services.ftp.check.password('')
    
    functions.check(findObject(s0.services.ftp.userTableName + '.item_0/0').text == 'cisco')
    functions.check(findObject(s0.services.ftp.userTableName + '.item_0/1').text == 'cisco')
    functions.check(findObject(s0.services.ftp.userTableName + '.item_0/2').text == 'RWDNL')
    
    s0.services.ftp.check.addButton(property='enabled', value=True)
    s0.services.ftp.check.removeUserButton(property='enabled', value=False)
    s0.services.ftp.check.saveButton(property='enabled', value=False)
    
    global defaultFtpFiles
    defaultFtpFiles = ['asa842-k8.bin',
                       'asa923-k8.bin',
                       'c1841-advipservicesk9-mz.124-15.T1.bin',
                       'c1841-ipbase-mz.123-14.T7.bin',
                       'c1841-ipbasek9-mz.124-12.bin',
                       'c1900-universalk9-mz.SPA.155-3.M4a.bin',
                       'c2600-advipservicesk9-mz.124-15.T1.bin',
                       'c2600-i-mz.122-28.bin',
                       'c2600-ipbasek9-mz.124-8.bin',
                       'c2800nm-advipservicesk9-mz.124-15.T1.bin',
                       'c2800nm-advipservicesk9-mz.151-4.M4.bin',
                       'c2800nm-ipbase-mz.123-14.T7.bin',
                       'c2800nm-ipbasek9-mz.124-8.bin',
                       'c2900-universalk9-mz.SPA.155-3.M4a.bin',
                       'c2950-i6q4l2-mz.121-22.EA4.bin',
                       'c2950-i6q4l2-mz.121-22.EA8.bin',
                       'c2960-lanbase-mz.122-25.FX.bin',
                       'c2960-lanbase-mz.122-25.SEE1.bin',
                       'c2960-lanbasek9-mz.150-2.SE4.bin',
                       'c3560-advipservicesk9-mz.122-37.SE1.bin',
                       'c3560-advipservicesk9-mz.122-46.SE.bin',
                       'c800-universalk9-mz.SPA.152-4.M4.bin',
                       'c800-universalk9-mz.SPA.154-3.M6a.bin',
                       'cat3k_caa-universalk9.16.03.02.SPA.bin',
                       'cgr1000-universalk9-mz.SPA.154-2.CG',
                       'cgr1000-universalk9-mz.SPA.156-3.CG',
                       'ir800-universalk9-bundle.SPA.156-3.M.bin',
                       'ir800-universalk9-mz.SPA.155-3.M',
                       'ir800-universalk9-mz.SPA.156-3.M',
                       'ir800_yocto-1.7.2.tar',
                       'ir800_yocto-1.7.2_python-2.7.3.tar',
                       'pt1000-i-mz.122-28.bin',
                       'pt3000-i6q4l2-mz.121-22.EA4.bin']
    
    functions.check(s0.services.ftp.fileTable.rowCount == len(defaultFtpFiles))
    filesInList = []
    for i in range(s0.services.ftp.fileTable.rowCount):
        filesInList.append(findObject(s0.services.ftp.fileTableName + '.item_%s/0'%(i,)).text)
    if len(filesInList) == len(defaultFtpFiles):
        for file in filesInList:
            if file in defaultFtpFiles:
                test.passes('The file is there')
            else:
                test.fail(file + ' is not in the list')
    else:
        test.fail('The number of files is not correct')
        
def addFtpUsers():
    s0.services.ftp.addUser('tester', 'tester', write=True, read=True, delete=True, rename=True, list=True)
    s0.services.ftp.addUser('user', 'password', write=False, read=True, delete=False, rename=False, list=False)
    
    functions.check(findObject(s0.services.ftp.userTableName + '.item_0/0').text, 'cisco')
    functions.check(findObject(s0.services.ftp.userTableName + '.item_0/1').text, 'cisco')
    functions.check(findObject(s0.services.ftp.userTableName + '.item_0/2').text, 'RWDNL')
    
    functions.check(findObject(s0.services.ftp.userTableName + '.item_1/0').text, 'tester')
    functions.check(findObject(s0.services.ftp.userTableName + '.item_1/1').text, 'tester')
    functions.check(findObject(s0.services.ftp.userTableName + '.item_1/2').text, 'RWDNL')
    
    functions.check(findObject(s0.services.ftp.userTableName + '.item_2/0').text, 'user')
    functions.check(findObject(s0.services.ftp.userTableName + '.item_2/1').text, 'password')
    functions.check(findObject(s0.services.ftp.userTableName + '.item_2/2').text, 'R')
    
def changeUsersAttributes():
    s0.services.ftp.selectUser('user')
    s0.services.ftp.writeCheckbox(True)
    s0.services.ftp.deleteCheckbox(True)
    s0.services.ftp.renameCheckbox(True)
    s0.services.ftp.listCheckbox(True)
    s0.services.ftp.saveButton()
    functions.check(findObject(s0.services.ftp.userTableName + '.item_2/2').text, 'RWDNL')
    None

def removeUsers():
    s0.services.ftp.removeUser('tester')
    functions.check(s0.services.ftp.userTable.rowCount == 2)
    None
    
def removeFile():
    filesToRemove = ['c2600-i-mz.122-28.bin',
                     'c2600-ipbasek9-mz.124-8.bin',
                     'c2800nm-advipservicesk9-mz.124-15.T1.bin',
                     'c2800nm-advipservicesk9-mz.151-4.M4.bin',
                     'c2800nm-ipbase-mz.123-14.T7.bin']
    for file in filesToRemove:
        s0.services.ftp.removeFile(file)
    
    functions.check(s0.services.ftp.fileTable.rowCount == (len(defaultFtpFiles)-len(filesToRemove)))