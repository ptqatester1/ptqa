from API.MenuBar.Extensions.IPC.IPC import IPC
from API.MenuBar.Extensions.IPC.IPCConst import IPCConst
from API.Utility.Util import Util

IPCMenu = IPC()
util = Util()


def main():
    util.init()
    configureCEPWindow()
    activeCEPWindowOpen()
    optionsWindowOpen()
    logCEPWindow()

def configureCEPWindow(): 
    IPCMenu.selectIPC_ConfigureApps()
    if (object.exists(IPCMenu.Configure_Apps_Window + IPCConst.Configure_Apps.APPS_LIST)):
        test.passes("Configure Apps window found")
    else:
        test.fail("Configure Apps window not found")


def activeCEPWindowOpen(): 
    IPCMenu.selectIPC_ActiveApps()
    if (object.exists(IPCMenu.Active_Apps_Window + IPCConst.Active_Apps.APPS_LIST)):
        test.passes("Active Apps window found")
    else:
        test.fail("Active Apps window not found")
    util.clickButton(IPCMenu.Active_Apps_Window + IPCConst.Active_Apps.CANCEL_BUTT)

def optionsWindowOpen(): 
    IPCMenu.selectIPC_Options()
    if (object.exists(IPCMenu.Options_Window + IPCConst.Options.PORT_NUM_EDIT)):
        test.passes("Options window found")
    else:
        test.fail("Options window not found")
    util.clickButton(IPCMenu.Options_Window + IPCConst.Options.CANCEL_BUTT)
    
def logCEPWindow(): 
    IPCMenu.selectIPC_Log()
    if (object.exists(IPCMenu.Log_Window + IPCConst.Log.IPC_LOG)):
        test.passes("Log window found")
    else:
        test.fail("Log window not found")

    util.clickButton(IPCMenu.Log_Window + IPCConst.Log.CLOSE_BUTT)
