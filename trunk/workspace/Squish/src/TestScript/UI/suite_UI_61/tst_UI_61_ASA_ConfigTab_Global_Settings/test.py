##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Security.Asa import Asa

from API.ComponentBox import ComponentBoxConst

util = Util()
a0 = Asa(ComponentBoxConst.DeviceModel.ASA_5505, 100, 100, 'Asa0')

def main():
    util.init()
    create()
    
def create():
    a0.create()
    a0.select()
    a0.clickConfigTab()
    if object.exists(UtilConst.DEVICE_IS_BOOTING_POPUP):
        test.passes('The pop up showed')
        util.clickButton(UtilConst.DEVICE_IS_BOOTING_POPUP_OK_BUTT)
    else:
        test.fail('The popup did not show')
    util.fastForwardTime()
    a0.clickConfigTab()
    a0.config.settings.displayName('TestDisplayName')
    a0.config.settings.hostname('TestHostName')
    a0.config.settings.saveButton()
    a0.config.equivalentIosCommands.textCheckPoint('copy running-config startup-config')
    a0.config.settings.eraseNvram()
    a0.config.equivalentIosCommands.textCheckPoint('Erase configuration in flash memory')
    a0.config.settings.exportStartupConfig(util.getFilePath('ui_61_ASA_startup-config.txt', UtilConst.UI_TEST))
    a0.config.settings.loadStartupConfig(util.getFilePath('ui_61_ASA_startup-config.txt', UtilConst.UI_TEST))
    a0.config.settings.exportRunningConfig(util.getFilePath('ui_61_ASA_running-config.txt', UtilConst.UI_TEST))
    a0.config.settings.mergeRunningConfig(util.getFilePath('ui_61_ASA_running-config.txt', UtilConst.UI_TEST))