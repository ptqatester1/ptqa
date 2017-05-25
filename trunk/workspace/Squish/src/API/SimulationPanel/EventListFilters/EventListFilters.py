##Chris Allen

from API.Utility.Util import Util
from API.SimulationPanel.EventListFilters.EventListFiltersConst import EventListFiltersConst
from squish import *
import object

def err(msg = ''): raise NotImplementedError(msg)

class AclFiltersCheck:
    def __init__(self):
        self.util = Util()
    
    def statementTextAtRow(self, row, statement):
        row_item = EventListFiltersConst.aclFilters.EDIT_FILTERS_STATEMENT_EDIT + '.item_%s/0'%(row,)
        self.util.textCheckPoint(row_item, statement)
    
class AclFilters:
    def __init__(self):
        self.util = Util()
        self.check = AclFiltersCheck()
        
    def selectAclFilter(self, filter):
        err()
    
    def newButton(self):
        self.util.clickButton(EventListFiltersConst.aclFilters.EDIT_FILTERS_NEW_BUTT)

    def nameOkButton(self):
        self.util.clickButton(EventListFiltersConst.aclFilters.EDIT_FILTERS_RENAME_OK)
                              
    def name(self, name):
        self.util.setText(EventListFiltersConst.aclFilters.EDIT_FILTERS_NAME_FIELD, name)
    
    def renameButton(self):
        self.util.clickButton(EventListFiltersConst.aclFilters.EDIT_FILTERS_RENAME_BUTT)
                              
    def deleteButton(self):
        self.util.clickButton(EventListFiltersConst.aclFilters.EDIT_FILTERS_DEL_BUTT)
    
    def extendedAclStatements(self, statements):
        self.util.setText(EventListFiltersConst.aclFilters.EDIT_FILTERS_COMMAND_EDIT, statements)
    
    def submitButton(self):
        self.util.clickButton(EventListFiltersConst.aclFilters.EDIT_FILTERS_SUBMIT_BUTT)
    
    def contextHelp(self, text):
        err()
    
    def deleteStatementButton(self):
        err()
    
    def close(self):
        self.util.close(EventListFiltersConst.aclFilters.DIALOG_WINDOW)
        

class EventListFilters:
    def __init__(self):
        self.util = Util()
        self.aclFilters = AclFilters()
    
    def editFiltersButton(self):
        self.util.clickButton(EventListFiltersConst.EDIT_FILTERS)

    def editAclFiltersButton(self):
        self.util.clickButton(EventListFiltersConst.EDIT_ACL_FILTERS)
    
    def showAllNoneButton(self):
        self.util.clickButton(EventListFiltersConst.SHOW_ALL_NONE)
    
    @property
    def currentFiltersObject(self):
        '''Returns the current filters Object'''
        return findObject(EventListFiltersConst.EDIT_FILTERS_LABEL)
    
    @property
    def currentFilters(self):
        '''Returns a string of the current filters'''
        return str(self.currentFiltersObject.text)

    @property
    def currentFiltersList(self):
        '''Returns a list of the current filters'''
        return self.currentFilters.split(', ')
        
    def clearFilters(self):
        '''Clear all filters'''
        if not 'None.' in self.currentFiltersList:
            self.showAllNoneButton()
            
    @property
    def ipv4Filters(self):
        return findObject(EventListFiltersConst.EVENT_LIST_FILTERS_MENU_IP)
    
    @property
    def ipv6Filters(self):
        return findObject(EventListFiltersConst.EVENT_LIST_FILTERS_MENU_IPV6)
    
    @property
    def miscFilters(self):
        return findObject(EventListFiltersConst.EVENT_LIST_FILTERS_MENU_MISC)
    
    def clickTab(self, tabName):
        '''Tabs: ipv4, ipv6, misc'''
        if tabName.lower() == 'ip' or tabName.lower() == 'ipv4':
            tab = EventListFiltersConst.IP_FILTERS_TAB
        elif tabName.lower() == 'ipv6':
            tab = EventListFiltersConst.IPV6_FILTERS_TAB
        elif tabName.lower() == 'misc':
            tab = EventListFiltersConst.MISC_FILTERS_TAB
        Util().clickTab(EventListFiltersConst.EDIT_FILTERS_TABBAR, tab)

    def checkItem(self, filter, checked = None):
        '''Go through each tab of the filter list searching for the matching filter. Once found check the filter then return and exit the function'''
        for tab in ['ipv4', 'ipv6', 'misc']:
            self.clickTab(tab)
            for filterItem in object.children(getattr(self, tab + 'Filters')):#getattr calls the self.(tab) + Filters property. Example if tab is ipv4 then it will call self.ipv4Filters
                try:
                    if filterItem.text == filter:
                        if checked == None:
                            Util().click(filterItem)
                        elif checked == True:
                            if filterItem.checkState == 'unchecked':
                                Util().click(filterItem)
                        elif checked == False:
                            if filterItem.checkState == 'checked':
                                Util().click(filterItem)
                        else:
                            raise ValueError('checked must be None, True, or False')
                        return
                except AttributeError, e:
                    pass
        raise ValueError('Filter: ' + filter + ' not found. Check the spelling.')

    @property
    def currentFilterMenu(self):
        for tab in ['ipv4', 'ipv6', 'misc']:
            try:
                filterMenu = getattr(self, tab + 'Filters')
                if filterMenu.visible:
                    return filterMenu
            except LookupError, e:
                continue
        return False

    def checkFilters(self, filter, *otherFilters, **kwargs):
        '''
            filter - String (Name of the filter to be checked)
            otherFilters - string (Optional names of more filters to be checked)
            kwargs -
                clearFilters - Bool (Clears filters if True)
                checked - None || Bool (If None filters will be toggled. If True filters will be checked. If False filters will be unchecked. If not provided default is toggle)
        '''
        checked = None
        if 'checked' in kwargs:
            checked = kwargs['checked']
        if 'clearFilters' in kwargs:
            if kwargs['clearFilters']:
                self.clearFilters()
        
        if not self.currentFilterMenu:
            self.editFiltersButton()
        filters = (filter,) + otherFilters
        for item in filters:
            self.checkItem(item, checked)
        self.util.click(EventListFiltersConst.EDIT_FILTERS_LABEL)#To close the filters menu when done