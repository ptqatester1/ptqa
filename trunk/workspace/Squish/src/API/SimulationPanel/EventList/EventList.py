##Chris Allen

from API.Utility.Util import Util
from API.SimulationPanel.EventList.EventListConst import EventListConst
from API.SimulationPanel.PlayControls.PlayControls import PlayControls
from squish import *
import test
import object


class PDU:
    def __init__(self, lastDevice, atDevice, type, info, row):
        self.lastDevice = lastDevice
        self.atDevice = atDevice
        self.type = type
        self.info = info
        self.row = row

class EventList:
    '''Functions:
        resetSimulationButton(self)
        constantDelayCheckbox(self, checked = None)
        findEvent(self, lastDevice, atDevice, type)
        findEventReversed(self, lastDevice, atDevice, type)
        findEventAt(self, row)
        findAllEventType(self, type)
        findAllAtDevice(self, device)
        findAllLastDevice(self, lastDevice)
        eventFinder(self, lastDevice = None, atDevice = None, type = None, **kwargs)
        waitForEvent(self, lastDevice = None, atDevice = None, type = None, maxTries = 100)
        selectEvent(self, lastDevice = None, atDevice = None, type = None, **kwargs)
        EVENT_LIST_PDUS(self)
    '''
    def __init__(self):
        self.util = Util()
    
    def resetSimulationButton(self):
        self.util.clickButton(EventListConst.RESET_SIMULATION)
        
    def constantDelayCheckbox(self, checked = None):
        '''
        checked - None || Boolean (If None toggle otherwise check if True and uncheck if False)
        '''
        checkbox = findObject(EventListConst.CONSTANT_DELAY)
        if checked == None:
            self.util.click(checkbox)
        elif checked == True:
            if not checkbox.checked:
                self.util.click(checkbox)
        elif checked == False:
            if checkbox.checked:
                self.util.click(checkbox)
        else:
            raise ValueError('checked must be None, True, or False')
    
    def findEvent(self, lastDevice, atDevice, type):
        '''Finds the first event in the list matching the given parameters'''
        return self.eventFinder(lastDevice, atDevice, type)
    
    def findEventReversed(self, lastDevice, atDevice, type):
        '''Finds the last event in the list matching the given parameters'''
        return self.eventFinder(lastDevice, atDevice, type, reversed = True)
    
    def findEventAt(self, lastDevice = None, atDevice = None, type = None):
        return self.eventFinder(lastDevice, atDevice, type)
    
    def findAllEventType(self, type):
        events = []
        for event in self.EVENT_LIST_PDUS:
            if event.type.text == type:
                events.append(event)
        return events
    
    def findAllAtDevice(self, device):
        events = []
        for event in self.EVENT_LIST_PDUS:
            if event.atDevice.text == device:
                events.append(event)
        return events
    
    def findAllLastDevice(self, lastDevice):
        events = []
        for event in self.EVENT_LIST_PDUS:
            if event.lastDevice.text == lastDevice:
                events.append(event)
        return events
        
    def eventFinder(self, lastDevice = None, atDevice = None, type = None, **kwargs):
        '''
        lastDevice - String (Value of the Last Device Column)
        atDevice   - String (Value of the At Device Column)
        type       - String (Value of the Type Column)
        kwargs -
            reversed - Boolean (If true search the lis in reverse)
            row      - Integer (Find the event at a specific row)
            eventNum - Integer (Find the nth event that matches the given parameters if reversed = True search in reverse)
        '''
        if not lastDevice and not atDevice and not type:
            raise ValueError('Must include at least one parameter')
        events = self.EVENT_LIST_PDUS
        if 'row' in kwargs:
            return events[kwargs['row']]#Returns the event at the given value or row. 0 indexing
        if 'reversed' in kwargs:
            if kwargs['reversed']:
                events = reversed(events)
        eventNum = 0
        if 'eventNum' in kwargs:
            eventNum = kwargs['eventNum']
        count = 0
        for event in events:
            eventFound = True
            if lastDevice:
                if not event.lastDevice.text == lastDevice:
                    eventFound = False
            if atDevice:
                if not event.atDevice.text == atDevice:
                    eventFound = False
            if type:
                if not event.type.text == type:
                    eventFound = False
            if eventFound:
                count += 1
                if not eventNum or count == eventNum:
                    return event
        return False
    
    def waitForEvent(self, lastDevice = None, atDevice = None, type = None, maxTries = 100, **kwargs):
        '''Checks to see if the expected event is in the event list. If not clicks capture forward and checks again.
        Will continue for maxTries'''
        if not lastDevice and not atDevice and not type:
            raise ValueError('Must specify at least one parameter')
        for i in range(maxTries):
            event = self.eventFinder(lastDevice, atDevice, type, **kwargs)
            if event:
                return event
            PlayControls().captureForward()

    def selectEvent(self, lastDevice = None, atDevice = None, type = None, **kwargs):
        '''
        lastDevice - String (Value of the Last Device Column)
        atDevice   - String (Value of the At Device Column)
        type       - String (Value of the Type Column)
        kwargs -
            reversed - Boolean (If true search the lis in reverse)
            row      - Integer (Find the event at a specific row)
            eventNum - Integer (Find the nth event that matches the given parameters if reversed = True search in reverse)
        '''
        event = self.eventFinder(lastDevice, atDevice, type, **kwargs)
        try:
            scrollbar = findObject(EventListConst.SIMULATION_SCROLLBAR_HORIZONTAL)
        except LookupError, e:
            scrollbar = None
        if scrollbar:
            scrollbar.setValue(scrollbar.maximum)
        self.util.click(event.info)
        if scrollbar:
            scrollbar.setValue(scrollbar.minimum)
        
    @property
    def EVENT_LIST_PDUS(self):
        '''Returns a PDU object which holds the squish objects for the current PDU event
        PDU.lastDevice    //The squish object for the lastDevice column
        PDU.atDevice      //The squish object for the atDevice column
        PDU.type          //The squish object for the type column
        PDU.info          //The squish object for the info column
        These can be used to click on them or access any of the squish object properties
        for example PDU.type.text'''
        EVENTLIST = EventListConst.EVENT_LISTVIEW
        eventList = findObject(EVENTLIST)
        numberOfItemsInList = eventList.topLevelItemCount
        eventListItems = []
        for i in range(numberOfItemsInList):
            (lastDevice,
             atDevice,
             type,
             info) = (findObject(EVENTLIST + '.item_' + str(i) + '/2'),
                      findObject(EVENTLIST + '.item_' + str(i) + '/3'),
                      findObject(EVENTLIST + '.item_' + str(i) + '/4'),
                      findObject(EVENTLIST + '.item_' + str(i) + '/5'))
            eventListItems.append(PDU(lastDevice, atDevice, type, info, i))
        return eventListItems
