##Chris Allen
##Sanity check to make sure that all the options tabs are there and functioning

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.PreferencesConst import PreferencesConst as pConst
from API.MenuBar.Options.Preferences.CustomInterfaces.CustomInterfacesConst import CustomInterfacesConst as intConst
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst

util = Util()
opt = Options()

customIntTabList = [intConst.ROUTER_COMBOBOX, intConst.SWITCH_COMBOBOX, intConst.MULTILAYERSWITCH_COMBOBOX, intConst.BRIDGE_COMBOBOX,
                    intConst.HUB_COMBOBOX, intConst.REPEATER_COMBOBOX, intConst.COAXIALSPLITTER_COMBOBOX, intConst.ACCESSPOINT_COMBOBOX,
                    intConst.WIRELESSROUTER_COMBOBOX, intConst.PC_COMBOBOX, intConst.LAPTP_COMBOBOX, intConst.SERVER_COMBOBOX,
                    intConst.PRINTER_COMBOBOX, intConst.IPPHONE_COMBOBOX, intConst.HOMEVOIP_COMBOBOX, intConst.ANALOGPHONE_COMBOBOX,
                    intConst.TV_COMBOBOX, intConst.TABLETPC_COMBOBOX, intConst.PDA_COMBOBOX, intConst.WIRELESSENDDEVICE_COMBOBOX,
                    intConst.WIREDENDDEVICE_COMBOBOX, intConst.CLOUD_COMBOBOX, intConst.DSLMODEM_COMBOBOX, intConst.CABLEMODEM_COMBOBOX]

def main():
    setDevices()
    check()
    
def setDevices():
    opt.selectOptionsItem(OptionsConst.PREFERENCES)
    util.clickTab(pConst.TAB_BAR, pConst.CUSTOM_INTERFACES)
    for item in customIntTabList:
        util.clickItem(item, "net\\.netacad\\.cisco\\.clearTerminalAgent:terminal\\.html")
    
def check():
    def checkCurrentText(p_item):
        if(findObject(item).currentText == "net.netacad.cisco.clearTerminalAgent:terminal.html"):
            test.passes("The combo box works")
        else:
            test.fail("The combo box does not work")
    for item in customIntTabList:
        checkCurrentText(item)
    