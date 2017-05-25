##############################################################
#@author: Thi Nguyen
##############################################################
from API.ComponentBox import ComponentBoxConst

from API.Device.Router.Router import Router
from API.Utility.Util import Util
from API.Utility import UtilConst
import os
from API.functions import Clipboard, check

#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 200, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2620XM, 200, 200, "Router1")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_2621XM, 300, 200, "Router2")
router3 = Router(ComponentBoxConst.DeviceModel.ROUTER_2811, 400, 200, "Router3")
router4 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 500, 200, "Router4")
router5 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT_EMPTY, 600, 200, "Router5")

def checkCopyText(dev):
    dev.select()
    dev.clickTab('CLI')
    dev.cli.startConsole()
    Clipboard().clear()
    cli = dev.cli.cliObject
    cli.moveCursor(QTextCursor.Start)
    cli.find('Press RETURN to get started!')
    dev.cli.copyButton()
    check('Press RETURN to get started!' == Clipboard().getText(), 'Clipboard text is: ' + Clipboard().getText())
    dev.cli.pasteButton()
    cli.moveCursor(QTextCursor.Start)
    check(cli.find('Router>Press RETURN to get started') == 1)
    dev.close()
    None

def main():
    util.init()
    Clipboard().clear()
    createTopology()
    copyPaste()

def createTopology():
    router0.create()
    router1.create()
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router2.model, router2.x, router2.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router3.model, router3.x, router3.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router4.model, router4.x, router4.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, router5.model, router5.x, router5.y)
    util.fastForwardTime()
    
def copyPaste():
    for router in [router0, router1, router2, router3, router4, router5]:
        checkCopyText(router)