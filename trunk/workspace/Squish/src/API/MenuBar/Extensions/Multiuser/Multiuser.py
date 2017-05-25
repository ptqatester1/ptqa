#**************************************************************************
#@author: Tuan Hoang, Thi Nguyen
#@summary: MultiUser features
#**************************************************************************
from API.MenuBar.Extensions.Multiuser.MultiuserConst import MultiuserConst
from API.SquishSyntax import SquishSyntax
from API.MenuBar.Extensions.ExtensionsConst import ExtensionsConst
class MultiUser(SquishSyntax):
    #@summary: Selects p_item from the MultiUser Menu
    #@param p_item: Listen, Port Visibility, Options...
    def selectMultiUserItem(self, p_item):
        self.activateItem(ExtensionsConst.MENU_BAR, "Extensions")
        self.activateItem(ExtensionsConst.EXTENSIONS_MENU, "Multiuser")
        self.activateItem(MultiuserConst.MULTI_USER_MENU, p_item)
        
    def startListen(self, p_port, p_password, p_acceptMode):
        self.selectMultiUserItem(MultiuserConst.LISTEN)
        if (not p_port == ""):
            self.setText(MultiuserConst.Listen.PORT_NUM_EDIT, p_port)
        if (not p_password == ""):
            self.setText(MultiuserConst.Listen.PASSWORD_EDIT, p_password)
        self.clickButton(p_acceptMode)
        self.clickButton(MultiuserConst.Listen.START_LISTEN_BUTT)
    
    def setPortVisibility(self, p_portList):
        self.selectMultiUserItem(MultiuserConst.PORT_VISIBILITY)
        self.clickButton(MultiuserConst.Port_Visilbility.NETWORK_TREE_VIEW)
        self.clickButton(MultiuserConst.Port_Visilbility.OK_BUTT)
        
    def setOption(self, p_option):
        self.selectMultiUserItem(MultiuserConst.OPTION)
        self.clickButton(p_option)
        self.clickButton(MultiuserConst.Options.OK_BUTT)
    
    def saveCopyOfflineAs(self):
        self.selectMultiUserItem(MultiuserConst.SAVE_OFFLINE)
        
