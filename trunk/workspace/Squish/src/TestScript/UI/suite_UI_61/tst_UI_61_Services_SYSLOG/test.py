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

def main():
    util.init()
    create()
    checkDefaults()
    addressServer()
    configureRouter()
    checkSyslog()
    
def create():
    s0.create()
    r0.create()
    s0.connect(r0)
    util.fastForwardTime()

def checkDefaults():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('SYSLOG')
    s0.services.syslog.check.on(True)
    s0.services.syslog.check.off(False)

def addressServer():    
    s0.clickDesktopTab()
    s0.desktop.applications.ipConfiguration()
    s0.desktop.ipConfiguration.setIPConfiguration('192.168.1.5', '255.255.255.0', '')
    s0.close()
    
def configureRouter():
    r0.select()
    r0.clickCliTab()
    r0.cli.startConsole()
    r0.cli.setCliText('enable')
    r0.cli.setCliText('configure terminal')
    r0.cli.setCliText('int fa0/0')
    r0.cli.setCliText('ip address 192.168.1.4 255.255.255.0')
    r0.cli.setCliText('no shut')
    r0.cli.setCliText('end')
    r0.cli.setCliText('ping 192.168.1.5')
    util.fastForwardTime()
    r0.cli.setCliText('configure terminal')
    r0.cli.setCliText('logging host 192.168.1.5')
    r0.cli.setCliText('logging trap debug')
    r0.cli.setCliText('end')
    r0.close()
    
def checkSyslog():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('SYSLOG')
    functions.check(s0.services.syslog.table.rowCount == 2)
    functions.check(s0.services.syslog.table.columnCount == 3)
    
    row1 = ['Jan 01 00:00:00.000', '192.168.1.4', '%SYS-5-CONFIG_I: Configured from console by console']
    row2 = ['Jan 01 00:00:00.000', '192.168.1.4', '%SYS-6-LOGGINGHOST_STARTSTOP: Logging to host 192.168.1.5 port 514 started - CLI initiated']
    for i, text in enumerate(row1):
        util.textCheckPoint(s0.services.syslog.tableName + '.item_0/' + str(i), text)
    for i, text in enumerate(row2):
        util.textCheckPoint(s0.services.syslog.tableName + '.item_1/' + str(i), text)
    s0.services.syslog.clearLog()
    
    functions.check(s0.services.syslog.table.rowCount == 0)