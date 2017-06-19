from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.Open import Open
from API import functions
from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Device.EndDevice.Server.Server import Server

util = Util()

r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1941, 30, 105, 'Router0')
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2901, 260, 225, 'Router1')
r2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2911, 180, 315, 'Router2')

server = Server(ComponentBoxConst.DeviceModel.SERVER, 25, 190, 'Server1')

files = ['c1900-universalk9-mz.SPA.155-3.M4a.bin',
         'c2900-universalk9-mz.SPA.155-3.M4a.bin']

def main():
    open_sample('7.1/Upgrade/upgrading_to_ios15_3.pkt')
    verify_files_on_server()
    upgrade_router(r0, files[0])
    upgrade_router(r1, files[1])
    upgrade_router(r2, files[1])
    

def open_sample(file_path):
    util.init()
    Open().openSamples(functions.pathFromOS(file_path))
    util.speedUpConvergence()

def verify_files_on_server():
    server.select()
    server.clickServicesTab()
    server.services.selectInterface('TFTP')
    for f in files:
        condition = server.services.tftp.has_file(f)
        msg = 'Expected %s to be in files. Got %s' % (f, condition)
        functions.check(condition, msg)
    server.close()
    
def upgrade_router(router, ios):
    router.select()
    router.clickCliTab()
    router.cli.startConsole()
    router.cli.setCliText('enable',
                      'copy tftp flash',
                      '1.1.1.1',
                      ios,
                      ios)
    util.speedUpConvergence()
    router.cli.setCliText('configure terminal',
                          'boot system %s' % (ios),
                          'do reload',
                          'yes',
                          '\r')
    util.speedUpConvergence()
    check_upgrade(router, ios)
    router.close()

def check_upgrade(router, ios):
    router.cli.startConsole()
    router.cli.setCliText('enable',
                      'show version')
    router.cli.textCheckPoint('System image file is "flash0:%s"' % (ios))