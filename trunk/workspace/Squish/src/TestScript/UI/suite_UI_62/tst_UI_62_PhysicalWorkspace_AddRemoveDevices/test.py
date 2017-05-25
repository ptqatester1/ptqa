########################
##Author: AbbasH
########################

from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst
from API.Utility import UtilConst
from API.Utility.Util import Util
from API.Device.Router.Router import Router
from API.ComponentBox import ComponentBoxConst
from API.ComponentBox.ComponentBox import ComponentBox
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Workspace.Physical import Physical, Closet

#Function initialization
util = Util()
componentBox = ComponentBox()

r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 500, 300, "Router0")

def main():
    util.init()
    util.clickOnPhysical()
    checkAddToIntercity()
    checkAddToHomeCity()
    checkAddToCorporateOffice()
    checkAddToWiringCloset()

def checkAddToIntercity():
    homecity = Physical().getObject('Home City')
    util.dragAndDrop(homecity, 10, 10, UtilConst.PHYSICAL_WORKSPACE, 0, 0)
    r0.create('physical')
    r0.select('physical')
    r0.clickTab('CLI')
    r0.close()
    test.passes('Router was added into the home city')

def checkAddToHomeCity():
    homecity = Physical().getObject('Home City')
    r0.x, r0.y = homecity.x + 50, homecity.y + 50
    r0.create('physical')
    Physical().goTo('Home City')
    r0.select('physical')
    r0.clickTab('CLI')
    r0.close()
    test.passes('Router was added into the home city')

def checkAddToCorporateOffice():
    coprporateoffice = Physical().getObject('Corporate Office')
    r0.x, r0.y = coprporateoffice.x + 50, coprporateoffice.y + 50
    r0.create('physical')
    Physical().goTo('Corporate Office')
    r0.select('physical')
    r0.clickTab('CLI')
    r0.close()
    test.passes('Router was added into the Corporate Office')

def checkAddToWiringCloset():
    wiringcloset = Physical().getObject('Main Wiring Closet')
    r0.x, r0.y = wiringcloset.x + 50, wiringcloset.y + 50
    r0.create('physical')
    Physical().goTo('Main Wiring Closet')
    snooze(5)
    devs = Closet().rackDeviceDict
    util.click(devs['rack1']['dev1'])
    r0.clickTab('CLI')
    r0.close()
    test.passes('Router was added into the main wiring closet')    
    None