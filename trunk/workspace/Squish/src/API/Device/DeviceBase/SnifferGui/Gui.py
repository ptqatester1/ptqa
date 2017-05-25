##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.EndDevice.Sniffer.SnifferConst import SnifferConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from squish import *
import object
from API import functions

def err(msg = ''):
    raise NotImplementedError(msg)

class Filters(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def editFiltersButton(self):
        Util().clickButton(self.objName(SnifferConst.gui.EDIT_FILTERS_BUTTON))
        
    def showAllNoneButton(self):
        Util().clickButton(self.objName(SnifferConst.gui.SHOW_ALL_NONE_BUTTON))
        
    @property
    def currentFiltersObject(self):
        return findObject(self.objName(SnifferConst.gui.CURRENT_FILTERS_TEXT))
    
    @property
    def currentFiltersText(self):
        return str(self.currentFiltersObject.text)
    
    @property
    def currentFiltersList(self):
        '''Return a list of the current filters'''
        return self.currentFiltersText.split(', ')
    
    def clearFilters(self):
        '''Clear all filters'''
        if not 'None.' in self.currentFiltersList:
            self.showAllNoneButton()
        
    @property
    def ipv4Filters(self):
        return findObject(self.objName(SnifferConst.editFilters.EDIT_FILTERS_MENU_IPV4))
    
    @property
    def ipv6Filters(self):
        return findObject(self.objName(SnifferConst.editFilters.EDIT_FILTERS_MENU_IPV6))
    
    @property
    def miscFilters(self):
        return findObject(self.objName(SnifferConst.editFilters.EDIT_FILTERS_MENU_MISC))
    
    def clickTab(self, tabName):
        '''Tabs: ipv4, ipv6, misc'''
        if tabName.lower() == 'ip' or tabName.lower() == 'ipv4':
            tab = SnifferConst.editFilters.IP_FILTERS_TAB
        elif tabName.lower() == 'ipv6':
            tab = SnifferConst.editFilters.IPV6_FILTERS_TAB
        elif tabName.lower() == 'misc':
            tab = SnifferConst.editFilters.MISC_FILTERS_TAB
        Util().clickTab(self.objName(SnifferConst.editFilters.EDIT_FILTERS_TABBAR), tab)

    def checkItem(self, filter):
        '''Go through each tab of the filter list searching for the matching filter. Once found check the filter then return and exit the function'''
        for tab in ['ipv4', 'ipv6', 'misc']:
            self.clickTab(tab)
            for filterItem in object.children(getattr(self, tab + 'Filters')):#getattr calls the self.(tab) + Filters property
                try:                                                          #Example if tab is ipv4 then it will call self.ipv4Filters  
                    if filterItem.text == filter:
                        if filterItem.checkState == 'unchecked':
                            Util().click(filterItem)
                        return
                except AttributeError, e:
                    pass
        raise ValueError('Filter: ' + filter + ' not found. Check the spelling.')

    def checkFilters(self, filter, *otherFilters, **kwargs):
        '''Args: Name of the filter such as 'Arp'
           Kwargs: clearFilters - Bool
        '''
        if 'clearFilters' in kwargs:
            if kwargs['clearFilters']:
                self.clearFilters()
        filters = (filter,) + otherFilters
        self.editFiltersButton()
        for item in filters:
            self.checkItem(item)
        Util().click(self.currentFiltersObject)

class GuiCheck(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName        
        
    def updateName(self, squishName):
        self.squishName = squishName

    def on(self, checked=True):
        Util().isChecked(self.objName(SnifferConst.gui.SERVICE_ON_RADIO), checked)
    
    def off(self, checked=True):
        Util().isChecked(self.objName(SnifferConst.gui.SERVICE_OFF_RADIO), checked)
    
    def port0(self, checked=True):
        Util().isChecked(self.objName(SnifferConst.gui.PORT_0_RADIO), checked)
    
    def port1(self, checked=True):
        Util().isChecked(self.objName(SnifferConst.gui.PORT_1_RADIO), checked)
    
    def bufferSize(self, bufferSize):
        buffer = findObject(self.objName(SnifferConst.gui.BUFFER_SIZE_SLIDER))
        functions.check(buffer.value == int(bufferSize))
    
    def portLabel(self, labelText):
        Util().textCheckPoint(self.objName(SnifferConst.gui.PORT_LABEL), labelText)

class Gui(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName        
        self.filters = Filters(self)
        self.check = GuiCheck(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
        self.filters.updateName(squishName)
        self.check.updateName(squishName)

    def on(self):
        Util().clickButton(self.objName(SnifferConst.gui.SERVICE_ON_RADIO))
    
    def off(self):
        Util().clickButton(self.objName(SnifferConst.gui.SERVICE_OFF_RADIO))
    
    def port0(self):
        Util().clickButton(self.objName(SnifferConst.gui.PORT_0_RADIO))
    
    def port1(self):
        Util().clickButton(self.objName(SnifferConst.gui.PORT_1_RADIO))
    
    def bufferSize(self, bufferSize):
        buffer = findObject(self.objName(SnifferConst.gui.BUFFER_SIZE_SLIDER))
        buffer.value = int(bufferSize)
    
    @property
    def eventTableName(self):
        return self.objName(SnifferConst.gui.PACKET_LIST)
    
    @property
    def eventTable(self):
        return findObject(self.eventTableName)
    
    @property
    def pduInfo(self):
        return findObject(self.objName(SnifferConst.gui.PACKET_INFORMATION_WINDOW))
    
    def eventAt(self, row):
        return findObject(self.eventTableName + '.item_%s/0'%(row,))
    
    def selectEventInTable(self):
        err('Need to determine implementation for this. Do we want to select the first matching packet, last matching packet, select match by row, or nth matching packet?')
    
    def selectEventAt(self, row):
        Util().click(self.eventTableName + '.item_%/0'%(row,))
    
    def selectEventType(self, type):
        Util().clickItem(self.objName(SnifferConst.gui.PACKET_LIST), type)
    
    def editFiltersButton(self):
        Util().clickButton(self.objName(SnifferConst.gui.EDIT_FILTERS_BUTTON))
    
    def clearButton(self):
        Util().clickButton(self.objName(SnifferConst.gui.CLEAR_BUTTON))
        