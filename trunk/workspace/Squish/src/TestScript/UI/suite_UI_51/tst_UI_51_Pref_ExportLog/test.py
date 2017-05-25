from API.ComponentBox import ComponentBoxConst
from API.Device.Router.Router import Router

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Preferences import Preferences

util = Util()
pref = Preferences()


r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 100, 200, "Router0")

def main():
    util.init()
    #Manually check if the log was successfully saved")
    createTopology()
    configureRouter()
    editOptionsSetting()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
  
def configureRouter():
    snooze(10)
    r0.select()
    r0.clickCliTab()
    r0.cli.startConsole()
    r0.cli.setCliText("en")   
    
def editOptionsSetting():
    pref.goToPreferences()
    pref.interface.exportLog(util.getFilePath("UI13Log.txt", UtilConst.UI_TEST))
    pref.close()
    
    test.passes("If no error occurs, export works as expected.")