##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Server.Server import Server

from API.Device.EndDevice.PC.PC import PC

from API.ComponentBox import ComponentBoxConst

util = Util()

s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 100, 'Server0')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 100, 'PC1')

def main():
    util.init()
    create()
    setUpDns()
    checkTable()
    removeItems()
    checkDnsCacheButton()
    
def create():
    s0.create()
    util.fastForwardTime()

def setUpDns():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('DNS')
    s0.services.dns.on()
    s0.services.dns.addA('aRecord.com', '1.1.1.1')
    s0.services.dns.addCname('cname.com', 'aRecord.com')
    s0.services.dns.addNs('nsRecord.com', 'nsServer')
    s0.services.dns.addSoa('soaRecord', 'soaServer', 'soaMail', '255', '5', '5', '255')
    
def checkTable():
    fieldVals = [['0', 'arecord.com', 'A Record', '1.1.1.1'], ['1', 'cname.com', 'CNAME', 'arecord.com'],
                 ['2', 'nsrecord.com', 'NS', 'nsserver'], ['3', 'soarecord', 'SOA', 'ServerName:soaserver\n\
MailBox :soaMail\n\
Expiry :255\n\
Refresh :5\n\
Retry :5\n\
MinTTL :255']]
    for i in range(s0.services.dns.dnsTable.rowCount):
        for j,expectedText in enumerate(fieldVals[i]):
            field = s0.services.dns.dnsTableName + '.item_' + str(i) + '/' + str(j)
            util.textCheckPoint(field, expectedText)

def removeItems():
    s0.services.dns.remove('arecord.com')
    
    s0.services.dns.selectRecord('cname.com')
    s0.services.dns.cname.hostname('newCname')
    s0.services.dns.saveButton()
    
    util.textCheckPoint(s0.services.dns.dnsTableName + '.item_0/3', 'newCname')
    test.compare(s0.services.dns.dnsTable.rowCount, 3)
    
def checkDnsCacheButton():
    s0.services.dns.dnsCacheButton()
    s0.services.dns.cache.clearCacheButton()
    s0.services.dns.cache.cancelButton()