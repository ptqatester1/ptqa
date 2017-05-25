#***********************************************************
#@author: Pam Vinco
#@summary: UserCreatedPDUList handles all PDU List functions
#***********************************************************
from API.SquishSyntax import SquishSyntax
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.UserCreatedPacketWindow.UserCreatedPDUListConst import UserCreatedPDUListConst
from API.Utility.Util import Util

class UserCreatedPDUList(SquishSyntax, SquishObjectName):
    #@summary: Clicks on fire PDU
    #@param p_obj: Text on line of PDU being fired (ex. "|Failed|1B|Eagle_Server|ICMP||0.000|N|0|(edit)|(delete)")
    def firePDU(self, p_obj, p_x, p_y):
        self.doubleClickItem_x_y(UserCreatedPDUListConst.PDU_LIST, p_obj, p_x, p_y)
        
    def firePDU_toggled_view(self, p_obj, p_x, p_y):
        self.doubleClickItem_x_y(UserCreatedPDUListConst.PDU_LIST_TOGGLED_VIEW, p_obj, p_x, p_y)
        
    #@summary: Clicks on edit PDU
    #@param p_obj: Text on line of PDU being edited (ex. "(edit)" or "(edit)_2"
    def editPDU(self, p_obj, p_x, p_y):
        self.doubleClickItem_x_y(UserCreatedPDUListConst.PDU_LIST, p_obj, p_x, p_y)
        
    def editPDU_toggled_view(self, p_obj, p_x, p_y):
        self.doubleClickItem_x_y(UserCreatedPDUListConst.PDU_LIST_TOGGLED_VIEW, p_obj, p_x, p_y)
        
    #@summary: Clicks on edit PDU
    #@param p_obj: Text on line of PDU being edited (ex. "|Failed|1B|Eagle_Server|ICMP||0.000|N|0|(edit)|(delete)")
    def deletetPDU(self, p_obj, p_x, p_y):
        self.doubleClickItem_x_y(UserCreatedPDUListConst.PDU_LIST, p_obj, p_x, p_y)
        
    def deletePDU_toggled_view(self, p_obj, p_x, p_y):
        self.doubleClickItem_x_y(UserCreatedPDUListConst.PDU_LIST_TOGGLED_VIEW, p_obj, p_x, p_y)
        
    #@summary: choose an item in the PDU list window
    #@param p_fieldText: The text in the field of the PDU you want to click example: To click an item that has a source of Router0 enter "Router0"
    #@param p_listLocation: The vertical location of the item you want clicked example: 1, 2, 3 where the number
    ##corresponds to the items location in the list
    #@param p_pduItem: The tuple for the item in the PDU list to be clicked
    #@note: Does not work for IP add and time yet.
    def selectPDUItem(self, p_fieldText, p_listLocation, p_pduItem=(14, 10)):
        import object
        from squish import *
        
        if(p_fieldText == "fire"):
            p_fieldText = ""
        if(p_fieldText == "Num" or p_fieldText == "Number"):
            p_fieldText = ""
        if(p_fieldText == "edit"):
            p_fieldText = "(edit)"
        if(p_fieldText == "delete"):
            p_fieldText = "(delete)"
        if(p_fieldText == "color"):
            p_fieldText = ""
            p_listLocation = p_listLocation + findObject(UserCreatedPDUListConst.PDU_LIST).topLevelItemCount
        self.doubleClickItem_x_y(UserCreatedPDUListConst.PDU_LIST, p_fieldText + "_" + str(p_listLocation), p_pduItem[0], p_pduItem[1])
        
    def expand(self):
        self.click(UserCreatedPDUListConst.EXPAND_LIST_BUTTON)

    def lastStatus(self, p_item, p_status):
        Util().textCheckPoint(self.objName(UserCreatedPDUListConst.PDU_LIST + ".item_" + p_item + "/1"), p_status, -1)
