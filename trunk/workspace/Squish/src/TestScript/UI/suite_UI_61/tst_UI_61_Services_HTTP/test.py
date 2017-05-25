##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server

from API.Device.EndDevice.PC.PC import PC

from API.ComponentBox import ComponentBoxConst
from API.functions import trace, check

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, 'Server0')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 100, 'PC1')
defaultFiles = ['copyrights.html', 'cscoptlogo177x111.jpg', 'helloworld.html', 'image.html', 'index.html']

def main():
    util.init()
    create()
    checkDefaults()
    
def create():
    s0.create()
    util.fastForwardTime()

def checkDefaults():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('HTTP')
    s0.services.http.check.httpOff(False)
    s0.services.http.check.httpOn(True)
    s0.services.http.check.httpsOff(False)
    s0.services.http.check.httpsOn(True)
    
    for i, item in enumerate(defaultFiles):
        columns = []
        for j in range(3):
            columns.append(s0.services.http.fileTableName + '.item_' + str(i) + '/' + str(j))
        check(item == findObject(columns[0]).text)
        if item.endswith('html'):
            check('(edit)' == findObject(columns[1]).text)
            util.click(columns[1])
            s0.services.http.edit.check.filename(item)
            s0.services.http.edit.check.text('[a-zA-Z]')
            s0.services.http.edit.fileManager()
        check('(delete)' == findObject(columns[2]).text)
    
    s0.services.http.newFileButton()
    s0.services.http.edit.filename('testing.html')
    s0.services.http.edit.setText('<h1>test</h1>')
    s0.services.http.edit.save()
    s0.services.http.edit.fileManager()
    
    for i, item in enumerate(defaultFiles):
        s0.services.http.deleteFile(item)
    testHtmlRow = s0.services.http.fileTableName + '.item_0/0'
    check('testing.html' == findObject(testHtmlRow).text)