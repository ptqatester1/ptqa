########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Router.Router import Router
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import Modules
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase import DeviceBaseConst

util = Util()
router = Router(ComponentBoxConst.DeviceModel.ROUTER_819, 175, 80, 'Router0')

def main():
    util.init()
    create()
    checkPower()
    checkZoom()
    checkCLI()
    checkCustomizeIconButtons()    
    
def create():    
    router.create()
    router.select()  

def checkPower():
    router.physical.power(Modules.router.r819hgw.power)  
    router.clickCliTab()
    util.clickButton(waitForObject(":Error.qt_msgbox_buttonbox.OK"))
    router.physical.power(Modules.router.r819hgw.power)  
    
def checkZoom():        
    checkRange(router.physical.imageObject.width, 370)
    checkRange(router.physical.imageObject.height, 167)

    router.physical.zoomIn()
    checkRange(router.physical.imageObject.width, 741)
    checkRange(router.physical.imageObject.height, 334)

    for i in range(2):
        router.physical.zoomOut()
    checkRange(router.physical.imageObject.width, 247)
    checkRange(router.physical.imageObject.height, 111)
    
    router.physical.zoomOut()
    checkRange(router.physical.imageObject.width, 185)
    checkRange(router.physical.imageObject.height, 83)

    router.physical.zoomOriginal()
    checkRange(router.physical.imageObject.width, 370)
    checkRange(router.physical.imageObject.height, 167)

def checkCLI():
    from API.functions import Clipboard, check
    util.speedUpConvergence()
    router.clickCliTab()
    router.cli.setCliText('no')
    router.cli.setCliText(' ')
    router.cli.setCliText('enable')
    router.cli.setCliText('config t')    
    Clipboard().clear()
    cli = router.cli.cliObject
    cli.moveCursor(QTextCursor.Start)
    cli.find('Press RETURN to get started!')
    router.cli.copyButton()
    check(Clipboard().getText() == 'Press RETURN to get started!')
    router.cli.pasteButton()
    router.cli.textCheckPoint('Press RETURN to get started!', lines=1)


def checkCustomizeIconButtons():   
    router.clickPhysicalTab()
    router.physical.customizeIconInPhysicalViewButton()
    util.clickButton(waitForObject(":CBaseDeviceWidgetClass.CBaseCustomImage.m_okButton"))
    router.physical.customizeIconInLogicalViewButton() 
    # util.clickButton(waitForObject(":CBaseDeviceWidgetClass.CBaseCustomImage.m_okButton"))#object name changes time by time.  

def checkRange(size, x):
    if size in range(x-15, x+15):
        test.passes("")
    else:
        test.fail("")   
