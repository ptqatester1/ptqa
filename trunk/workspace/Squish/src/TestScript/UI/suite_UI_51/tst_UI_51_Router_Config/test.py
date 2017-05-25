##################################################################
#@author: Thi Nguyen
##############################################################
from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Utility.Util import Util
from API.Utility import UtilConst
#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 200, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2620XM, 200, 200, "Router1")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 300, 200, "Router2")
router3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 400, 200, "Router3")
router4 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 500, 200, "Router4")
router5 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT_EMPTY, 600, 200, "Router5")

hostnames = ['ROUTER_1841', 'ROUTER_2620XM', 'ROUTER_2621XM', 'ROUTER_2811', 'ROUTER_PT', 'ROUTER_PT_EMPTY']
paths = ['UI15_Router1841_running-config.txt', 'UI15_Router2620XM_running-config.txt', 'UI15_Router2621XM_running-config.txt',
         'UI15_Router2811_running-config.txt', 'UI15_RouterPT_running-config.txt', 'UI15_RouterPT_Empty_running-config.txt']

def main():
    util.init()
    createTopology()
    exportRunningConfig()
    mergeConfig()

def createTopology():
    router0.create()
    router1.create()
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router2.model, router2.x, router2.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router3.model, router3.x, router3.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router4.model, router4.x, router4.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router5.model, router5.x, router5.y)
    util.clickOnSimulation()
    util.clickOnRealtime()
 
def exportRunningConfig():
    for i, rtr in enumerate([router0, router1, router2, router3, router4, router5]):
        rtr.select()
        rtr.clickConfigTab()
        rtr.config.settings.hostname(hostnames[i])
        rtr.config.settings.exportRunningConfigButton()
        rtr.config.settings.fileDialog.cancelButton()
        rtr.config.settings.exportRunningConfig(util.getFilePath(paths[i], UtilConst.UI_TEST))
        
        rtr.clickCliTab()
        rtr.cli.setCliText("end")
        rtr.cli.setCliText("show running-config")
        snooze(1)
        rtr.cli.textCheckPoint("hostname " + hostnames[i], 2)
        rtr.cli.setCliText(" ")
        rtr.cli.setCliText(" ")
        rtr.cli.setCliText(" ")
        rtr.close()
        
def mergeConfig():
    for i, rtr in enumerate([router0, router1, router2, router3, router4, router5]):
        rtr.select()
        rtr.cli.setCliText("conf t")
        rtr.cli.setCliText("hostname Test")
        rtr.cli.setCliText("end")
        rtr.cli.setCliText("show run")
        rtr.cli.textCheckPoint("hostname Test", 2)
        rtr.cli.setCliText(" ")
        rtr.cli.setCliText(" ")
        rtr.cli.setCliText(" ")
        rtr.clickConfigTab()
        rtr.config.settings.mergeButton()
        rtr.config.settings.fileDialog.cancelButton()
        rtr.config.settings.mergeRunningConfig(util.getFilePath(paths[i], UtilConst.UI_TEST))

        rtr.clickCliTab()
        rtr.cli.setCliText("show run")
        rtr.cli.textCheckPoint("hostname " + hostnames[i], 3)
        rtr.close()
        