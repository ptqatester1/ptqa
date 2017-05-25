#**************************************************************************
#@author: Tuan Hoang, Thi Nguyen
#@summary: IPC handles the IPC submenu in Extensions menu
#**************************************************************************

from API.MenuBar.Extensions.IPC.IPCConst import IPCConst
from API.SquishSyntax import SquishSyntax
from API.MenuBar.Extensions.ExtensionsConst import ExtensionsConst
import object
class IPC(SquishSyntax):
    def __init__(self):
        self.Configure_Apps_Window_Num = 0
        self.Active_Apps_Window_Num = 0
        self.Log_Window_Num = 0
        self.Options_Window_Num = 0
        self.Configure_Apps_Window = ":BaseCEPListDialog"
        self.Active_Apps_Window = ":BaseCEPActiveDialog"
        self.Log_Window = ":CBaseCEPMessageDlg"
        self.Options_Window = ":CBaseOptionsDialog"

    def set_Configure_Apps_Window_Name(self, p_name):
        self.Configure_Apps_Window = p_name
    #@summary: Selects Configure Apps from the IPC menu
    def selectIPC_ConfigureApps(self):
        self.activateItem(ExtensionsConst.MENU_BAR, "Extensions")
        self.activateItem(ExtensionsConst.EXTENSIONS_MENU, ExtensionsConst.IPC)
        self.activateItem(IPCConst.IPC_MENU, IPCConst.CONFIGURE_APPS)
        if (not object.exists(self.Configure_Apps_Window)):
            if(object.exists(":Configure Apps")):
                self.Configure_Apps_Window = ":Configure Apps"
            else:
                self.Configure_Apps_Window_Num = self.Configure_Apps_Window_Num+1
                self.Configure_Apps_Window = ":CAppsListDlg" + str(self.Configure_Apps_Window_Num)

    #@summary: Selects Configure Apps from the IPC menu
    def selectIPC_ActiveApps(self):
        self.activateItem(ExtensionsConst.MENU_BAR, "Extensions")
        self.activateItem(ExtensionsConst.EXTENSIONS_MENU, ExtensionsConst.IPC)
        self.activateItem(IPCConst.IPC_MENU, IPCConst.ACTIVE_APPS)
        if (not object.exists(self.Configure_Apps_Window)):
            if(object.exists(":Show Active Apps")):
                self.Configure_Apps_Window = ":Show Active Apps"
            else:
                self.Configure_Apps_Window_Num = self.Configure_Apps_Window_Num+1
                self.Configure_Apps_Window = ":CCEPListDlg" + str(self.Configure_Apps_Window_Num)

    #@summary: Selects Configure Apps from the IPC menu
    def selectIPC_Log(self):
        self.activateItem(ExtensionsConst.MENU_BAR, "Extensions")
        self.activateItem(ExtensionsConst.EXTENSIONS_MENU, ExtensionsConst.IPC)
        self.activateItem(IPCConst.IPC_MENU, IPCConst.LOG)
        if (not object.exists(self.Configure_Apps_Window)):
            if(object.exists(":Log ")):
                self.Configure_Apps_Window = ":Log "
            else:
                self.Configure_Apps_Window_Num = self.Configure_Apps_Window_Num+1
                self.Configure_Apps_Window = ":CCEPMessageDlg" + str(self.Configure_Apps_Window_Num)

    #@summary: Selects Configure Apps from the IPC menu
    def selectIPC_Options(self):
        self.activateItem(ExtensionsConst.MENU_BAR, "Extensions")
        self.activateItem(ExtensionsConst.EXTENSIONS_MENU, ExtensionsConst.IPC)
        self.activateItem(IPCConst.IPC_MENU, IPCConst.OPTION)
        if (not object.exists(self.Configure_Apps_Window)):
            if(object.exists(":IPC Options")):
                self.Configure_Apps_Window = ":IPC Options"
            else:
                self.Configure_Apps_Window_Num = self.Configure_Apps_Window_Num+1
                self.Configure_Apps_Window = ":QWidget" + str(self.Configure_Apps_Window_Num)

        
    #@summary: launch a Apps from the list
    #@param p_AppsFile: Apps item as show under the ID column
    # i.e "net\\.netacad\\.cisco\\.ipctest"
    def launchApps(self, p_AppsItem):
        self.clickItem(self.Configure_Apps_Window + IPCConst.Configure_Apps.APPS_LIST, p_AppsItem)
        self.clickButton(self.Configure_Apps_Window + IPCConst.Configure_Apps.LAUNCH_BUTT)
        
    #@summary: add a Apps item into the list
    #@param p_AppsFile: .pna file
    def addApps(self, p_AppsFile):
        self.clickButton(self.Configure_Apps_Window + IPCConst.Configure_Apps.ADD_BUTT)
        self.setText(self.Configure_Apps_Window + IPCConst.Configure_Apps.Apps_List.ADD_APPS_FILENAME_EDIT, p_AppsFile)
        self.clickButton(self.Configure_Apps_Window + IPCConst.Configure_Apps.Apps_List.ADD_APPS_FILENAME_OPEN_BUTT)

        
    #@summary: Selects remove a Apps item from the list
    #@param p_AppsFile: Apps item as show under the ID column
    # i.e "net\\.netacad\\.cisco\\.ipctest"
    def removeApps(self, p_AppsItem):
        self.clickItem(self.Configure_Apps_Window + IPCConst.Configure_Apps.APPS_LIST, p_AppsItem)
        self.clickButton(self.Configure_Apps_Window + IPCConst.Configure_Apps.REMOVE_BUTT)

    
    #@summary: set startup and saving setting for Apps
    #@param p_setting: constant defined in IPCConst
    def setAppsSettings(self, p_setting):
        self.clickTab(self.Configure_Apps_Window + IPCConst.Configure_Apps.TAB_BAR, IPCConst.Configure_Apps.SETTING_TAB)
        self.clickButton(self.Configure_Apps_Window + p_setting)

        
    #@summary: check on security setting for Apps
    #@param p_item: list of constant defined in IPCConst
    def setAppsSecurity(self, p_securityList):
        self.clickTab(self.Configure_Apps_Window + IPCConst.Configure_Apps.TAB_BAR, IPCConst.Configure_Apps.SECURITY_TAB)
        for i in range (0, len(p_securityList)):
            self.clickButton(self.Configure_Apps_Window + p_securityList[i])
        
    #@summary: disconnect a Apps that PT connect to
    #@param p_path: i.e UPnP.29426200
    def disconnectApps(self, p_path):
        self.clickItem(IPCConst.Active_Apps.APPS_LIST, p_path)
        self.clickButton(self.Active_Apps_Window + IPCConst.Active_Apps.DISCONNECT_BUTT)
        self.clickButton(self.Active_Apps_Window + IPCConst.Active_Apps.CANCEL_BUTT)
    
    def setIPCOption(self, p_port):
        self.setText(self.Options_Window + IPCConst.Options.PORT_NUM_EDIT, p_port)
        self.clickButton(self.Options_Window + IPCConst.Options.OK_BUTT)
    
    def clearLogMessage(self):
        self.clickButton(self.Log_Window + IPCConst.Log.CLEAR_BUTT)
        self.clickButton(self.Log_Window + IPCConst.Log.CLOSE_BUTT)

    def closeConfigureApps(self):
        self.clickButton(self.Configure_Apps_Window + IPCConst.Configure_Apps.OK_BUTT)

    def closeActiveApps(self):
        self.clickButton(self.Active_Apps_Window + IPCConst.Active_Apps.CANCEL_BUTT)

    def closeOptions(self):
        self.clickButton(self.Options_Window + IPCConst.Options.OK_BUTT)

    def closeLog(self):
        self.clickButton(self.Log_Window + IPCConst.Log.CLOSE_BUTT)