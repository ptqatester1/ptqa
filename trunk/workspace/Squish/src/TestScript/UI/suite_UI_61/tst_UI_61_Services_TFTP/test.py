##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.EndDevice.PC.PC import PC
from API.Device.Router.Router import Router
from API.ComponentBox import ComponentBoxConst
from API import functions

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, 'Server0')
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 100, 100, 'Router0')
defaultFileList = []

def main():
    util.init()
    create()
    checkDefaults()
    removeFiles()
    
def create():
    s0.create()
    r0.create()
    s0.connect(r0)
    util.fastForwardTime()

def checkDefaults():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('TFTP')
    s0.services.tftp.check.on(True)
    s0.services.tftp.check.off(False)
    
    global defaultFileList
    defaultFileList = ['asa842-k8.bin',
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
    
    currentFiles = []
    for i in range(findObject(s0.services.tftp.fileListName).rowCount):
        currentFiles.append(findObject(s0.services.tftp.fileListName + '.item_' + str(i) + '/0').text)
    if len(defaultFileList) == len(currentFiles):
        for file in defaultFileList:
            if file in currentFiles:
                test.passes('File is in the list')
            else:
                test.fail('The file is not in the list')
    else:
        test.fail('The current file list does not match the default file list')

def removeFiles():
    filesToRemove = ['asa842-k8.bin',
                     'c1841-advipservicesk9-mz.124-15.T1.bin',
                     'c2800nm-ipbasek9-mz.124-8.bin',
                     'c2950-i6q4l2-mz.121-22.EA4.bin',
                     'c2950-i6q4l2-mz.121-22.EA8.bin']
    for file in filesToRemove:
        s0.services.tftp.remove(file)
    
    functions.check(s0.services.tftp.fileList.rowCount ==  (len(defaultFileList)-len(filesToRemove)))