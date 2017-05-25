#*********************************************************************************************************
#@author: Pam Vinco
#@summary: CommonToolsBar handles tools found in Common Tools Bar (on the right hand side of PT interface)
#*********************************************************************************************************
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.Toolbar.CommonToolsBar.ComplexPDUWindow import ComplexPDUWindow
from API.Utility.Util import Util
from API.Utility import UtilConst
from squish import *
import object

util = Util()
complexPDUWindow = ComplexPDUWindow()

class Inspect:
    def __init__(self):
        self.util = Util()
    
    @property
    def inspectMenuObjectName(self):
        workspace = self.util.currentWorkspace
        menuName = workspace + '.' +  CommonToolsBarConst.TABLE_TYPE_MENU.split('.')[-1]
        return menuName

    @property
    def inspectMenuObject(self):
        return findObject(self.inspectMenuObjectName)
    
    def selectMenuItem(self, menuItem):   
        for item in object.children(self.inspectMenuObject):
            if item.text == menuItem:
                self.util.click(item)
                return
        raise ValueError('Unable to find menu item: ' + menuItem)

class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def confirmDeleteDialog(self):
        '''
        This will return the visible dialog for confirming deletion or False if none exist.
        Dialog:
        Confirm Delete
        Do you want to delete the selected items?'''
        workspace = self.util.currentWorkspace
        dialogs = [workspace + '.' +  CommonToolsBarConst.DELETE_CONFIRM_DIALOG.split('.')[-1],
                   workspace + '.' +  CommonToolsBarConst.DELETE_CONFIRM_DIALOG.split('.')[-1] + ' -- Packet Tracer']
        for dialog in dialogs:
            try:
                return findObject(dialog)
            except LookupError, e:
                continue
        return False
    
    def _dialogButton(self, buttonName, dialog):
        if not dialog:
            raise LookupError('The confirm delete dialog does not exist or was not found')
        children = object.children(dialog)
        for item in children:
            try:
                if item.objectName == 'qt_msgbox_buttonbox':
                    buttonbox = item
                    break
            except AttributeError, e:
                continue
        for button in object.children(buttonbox):
            try:
                if buttonName in str(button.text):
                    return button
            except AttributeError, e:
                print(e)
        raise LookupError('Unable to find the "%s" button.'%(buttonName))
    
    def confirmDeleteYesButton(self):
        yesButton = self._dialogButton('Yes', self.confirmDeleteDialog)
        self.util.clickButton(yesButton)
    
    def confirmDeleteNoButton(self):
        noButton = self._dialogButton('No', self.confirmDeleteDialog)
        self.util.clickButton(noButton)
    
    def confirmDeleteCancelButton(self):
        cancelButton = self._dialogButton('Cancel', self.confirmDeleteDialog)
        self.util.clickButton(cancelButton)
    
    def confirmDeleteUnclusterButton(self):
        unclusterButton = self._dialogButton('Uncluster', self.confirmDeleteDialog)
        self.util.clickButton(unclusterButton)
    
    def confirmDeleteDeleteClusterButton(self):
        deleteClusterButton = self._dialogButton('Delete Cluster', self.confirmDeleteDialog)
        self.util.clickButton(deleteClusterButton)
        
class CommonToolsBar:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
        self.inspectMenu = Inspect()
    
    def selectToolButton(self):
        self.util.clickButton(CommonToolsBarConst.SELECT_TOOL)
    
    def noteButton(self):
        self.util.clickButton(CommonToolsBarConst.PLACENOTE_TOOL)
    
    def deleteButton(self):
        self.util.clickButton(CommonToolsBarConst.DELETE_TOOL)
    
    def inspectButton(self):
        self.util.clickButton(CommonToolsBarConst.INSPECT_TOOL)
    
    def resizeButton(self):
        self.util.clickButton(CommonToolsBarConst.RESIZE_TOOL)
    
    def shapesButton(self):
        self.util.clickButton(CommonToolsBarConst.DRAW_TOOL)
    
    def simplePduButton(self):
        self.util.clickButton(CommonToolsBarConst.ADD_SIMPLE_PDU)
    
    def complexPduButton(self):
        self.util.clickButton(CommonToolsBarConst.ADD_COMPLEX_PDU)
    
    def deleteItem(self, p_x, p_y, **kwargs):
        '''
        p_x, p_y: x,y coordinates on the workspace
        kwargs:
            snoozeFactor: Int (number in seconds to snooze)
        '''
        snoozeFactor = 1
        if 'snoozeFactor' in kwargs:
            snoozeFactor = kwargs['snoozeFactor']
        self.deleteButton()
        snooze(snoozeFactor)
        if self.popups.confirmDeleteDialog:
            snooze(snoozeFactor)
            self.popups.confirmDeleteNoButton()
        self.util.clickOnWorkspace(p_x, p_y)
        if self.popups.confirmDeleteDialog:
            self.popups.confirmDeleteYesButton() 
        self.selectToolButton()
    
    def setNoteText(self, text):
        cworkspace = [item for item in self.util.currentWorkspace.split('.') if 'CWorkspace' in item][0]
        placenoteEdit = CommonToolsBarConst.PLACENOTE_TEXT_EDIT.replace('CWorkspace1', cworkspace)
        self.util.typeText(placenoteEdit, text)
    
    def addPlaceNote(self, p_note, p_x, p_y):
        self.noteButton()
        self.util.clickOnWorkspace(p_x, p_y)
        self.setNoteText(p_note)
        self.selectToolButton()
        
    def addSimplePDU(self, p_x1, p_y1, p_x2, p_y2):
        self.simplePduButton()
        self.util.clickOnWorkspace(p_x1, p_y1)
        self.util.clickOnWorkspace(p_x2, p_y2)
        self.selectToolButton()
        
    def inspectDevice(self, p_x, p_y, inpsectMenuItem):
        self.inspectButton()
        self.util.clickOnWorkspace(p_x, p_y)
        self.inspectMenu.selectMenuItem(inpsectMenuItem)
        self.selectToolButton()
        
    def addComplexPDU(self, p_x, p_y, application, destinationIp, sourceIp, ttl, tos, sequence, sourcePort, destinationPort, size, oneShotOrPeriodic, timeOrInterval, outgoingPort = None):
        self.complexPduButton()
        self.util.clickOnWorkspace(p_x, p_y)
        complexPDUWindow.complexPDU(application, destinationIp, sourceIp, ttl, tos, sequence, sourcePort, destinationPort, size, oneShotOrPeriodic, timeOrInterval, outgoingPort)
        self.selectToolButton()
        
    def addComplexPing(self, p_x, p_y, p_destIP, p_srcIP, p_ttl, p_TOS, p_seq, p_size, p_simSetting, p_timeOrInterval, p_outgoingPort = ""):
        self.complexPduButton()
        self.util.clickOnWorkspace(p_x, p_y)
        complexPDUWindow.ping(p_destIP, p_srcIP, ttl=p_ttl, tos=p_TOS, sequenceNumber=p_seq,
                              size=p_size, oneShotOrPeriodic=p_simSetting, timeOrInterval=p_timeOrInterval, outgoingPort=p_outgoingPort)
        #complexPDUWindow.complexPing(p_destIP, p_srcIP, p_ttl, p_TOS, p_seq, p_size, p_simSetting, p_timeOrInterval)
        self.selectToolButton()
        
    def resizePhysical(self, p_obj, from_x, from_y, to_x, to_y):
        self.resizeButton()
        self.util.dragItemBy(p_obj, from_x, from_y, to_x, to_y)
        self.selectToolButton()
        
    def uncluster(self, p_x, p_y):
        self.deleteButton()
        if self.popups.confirmDeleteDialog:
            self.popups.confirmDeleteNoButton()
        self.util.clickOnWorkspace(p_x, p_y)
        self.popups.confirmDeleteUnclusterButton()
        self.selectToolButton()

    def deletecluster(self, p_x, p_y):
        self.deleteButton()
        if self.popups.confirmDeleteDialog:
            self.popups.confirmDeleteNoButton()
        self.util.clickOnWorkspace(p_x, p_y)
        self.popups.confirmDeleteDeleteClusterButton()
        self.selectToolButton()