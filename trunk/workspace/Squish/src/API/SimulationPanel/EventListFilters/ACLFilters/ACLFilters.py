#**************************************************************************
#@author: Tuan Hoang
#@summary: ACLFilter handles the ACL Filter Window
#**************************************************************************
from API.SimulationPanel.EventListFilters.ACLFilters.ACLFiltersConst import ACLFiltersConst
from API.SquishSyntax import SquishSyntax
from squish import *

class ACLFilters(SquishSyntax):
    #@summary: Creates a new named extended ACL called p_aclName
    #@param p_aclName: Name of the extended ACL
    def createACLFilter(self, p_aclName):
        self.clickButton(ACLFiltersConst.NEW)
        self.setText(ACLFiltersConst.ACL_FILTER, p_aclName)
        self.click(ACLFiltersConst.ACL_COMMAND_LINE_ENTRY)

    #@summary: Deletes the named extended ACL called p_aclName
    #@param p_aclName: Name of the extended ACL
    def deleteACLFilter(self, p_aclName):
        self.clickItem(ACLFiltersConst.ACL_FILTER_DROP_DOWN, p_aclName)
        self.clickButton(ACLFiltersConst.DELETE)

    #@summary: Selects the named extended ACL p_aclName
    #@param p_aclName: Name of the extended ACL
    def selectACLFilter(self, p_aclName):
        self.clickItem(ACLFiltersConst.ACL_FILTER_DROP_DOWN, p_aclName)

    #@summary: Enters the extended ACL statement p_aclStatement
    #@param p_aclName: Extended ACL statement
    def enterACLStatement(self, p_aclStatement):
        self.setText(ACLFiltersConst.ACL_COMMAND_LINE_ENTRY, p_aclStatement)
        self.clickButton(ACLFiltersConst.SUBMIT)