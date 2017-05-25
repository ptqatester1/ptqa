################################################
#@author: Chris Allen                          #
#@summary: This holds the common device methods#
################################################
from API.Android.SquishSyntax import SquishSyntax
from API.Android.Workspace.WorkspaceConst import WorkspaceConst,\
    NavigationBarConst, LoginConst
from API.Android.ContextMenus.ContextMenusConst import EndDeviceContextMenu,\
    CliDeviceContextMenu, DeviceContextMenu
from API.Android.ContextMenus import ContextMenusConst
from API.Android.Utility.Util import Util
from API.Android.Utility import UtilConst
from API.Android.ActionBar.ActionBarConst import ActionBarConst
from API.Android.Utility.UtilConst import KeyboardCli

from squish import *
import test
import re

import object

util = Util()
contextMenu = DeviceContextMenu()
endDeviceMenu = EndDeviceContextMenu()
cliDeviceMenus = CliDeviceContextMenu()

class DeviceBaseConst:
    ContextMenu = contextMenu
    EndDeviceMenus = endDeviceMenu
    CliDeviceMenus = cliDeviceMenus   
    class Desktop:
        None
    
    class Services:
        None
    
    class Cli:
        CLI_CONSOLE = ":cliTextArea_HTML_Object"
        KEYBOARD_BUTTON = ':webview.specialKeys_btnKeyboard_HTML_Object'
        QUESTION_BUTTON = ':specialKeys_btnQuestion_HTML_Object'
        MORE_BUTTON = ':specialKeys_btnMore_HTML_Object'
        UP_BUTTON = ':specialKeys_btnUp_HTML_Object'
        DOWN_BUTTON = ':specialKeys_btnDown_HTML_Object'
        ABORT_BUTTON = ':specialKeys_btnAbort_HTML_Object'
        BREAK_BUTTON = ':specialKeys_btnBreak_HTML_Object'
        END_BUTTON = ':specialKeys_btnEnd_HTML_Object'
        PREV_BUTTON = ':specialKeys_btnPrevCmds_HTML_Object'
        SCRIPTEDIT_BUTTON = ':specialKeys_btnScriptEdit_HTML_Object'
        SCRIPTLIST_BUTTON = ':specialKeys_btnScriptEdit_HTML_Object'
        BACKSPACE = ':specialKeys_btnBackspace_HTML_Object'
        BACKWORD = ':specialKeys_btnBackword_HTML_Object'
        ENTER = ':specialKeys_btnEnter_HTML_Object'
        COMMAND_PANEL = ":cmdButtonPanel_HTML_Object"
        CMD_BUTTON_PANEL = ':cmdButtonPanel_HTML_Object'
        
        class CommandButtons:
            Yes = ':cliYesBtn_HTML_Object'
            No = ':cliNoBtn_HTML_Object'
        
        class ScriptEditor:
            NEW_BUTTON = ':id-clismui-new-btn_HTML_Object'
            PASTE_BUTTON = ':id-clismui-paste-btn_HTML_Object'
            OPEN_BUTTON = ':id-clismui-open-btn_HTML_Object'
            SAVE_BUTTON = ':id-clismui-save-btn_HTML_Object'
            DELETE_BUTTON = ':id-clismui-delete-btn_HTML_Object'
            PASTE_TO_CLI_BUTTON = ':id-clismui-paste-cli-btn_HTML_Object'
            CLOSE_BUTTON = ':id-clismui-close-btn_HTML_Object'
            NAME = ':id-clismui-script-name-text_HTML_Object'
            FIELD = ':id-clismui-script-textarea_HTML_Object'
        
        class ScriptList:
            CLOSE_BUTTON = ':id-clismui-close-btn_HTML_Object'
        
    class GUI:
        None
    
    class HTML:
        None
    
    class Physical:
        PHYSICAL_WORKSPACE = ':PhysicalView_HTML_Object'
        pass
        
###############################################
#@author: Chris Allen                         #
#@summary: To be inherited from other devices #
###############################################
class DeviceBase(SquishSyntax):
    def __init__(self):
        self.util = util
        pass
    
    def updateName(self, p_squishName):
        self.squishName = p_displayName
        
    def tap(self, p_obj):
        super(DeviceBase, self).tap(p_obj)
    
    def typeText(self, p_obj, p_text):
        self.util.typeText(p_obj, p_text)
        #super(DeviceBase, self).type()
        #super(DeviceBase, self).typeText(p_text)
        
    def typeTextSE(self, p_obj, p_text):
        self.util.typeTextSE(p_obj, p_text)
        
    def doubleTap(self, p_obj):
        super(DeviceBase, self).doubleTap(p_obj)
    
    def switchToDevice(self, p_newDevice, p_x = None, p_y = None, p_x2 = None, p_y2 = None):
        if not isinstance(p_newDevice, str):
            newDevice = p_newDevice.displayName
        
        #test not if inside a device
        if not findObject(ActionBarConst.DEVICE_BUTTON).visible:
            self.doubleTapSelect()
            for i in range(10):
                if findObject(ActionBarConst.DEVICE_BUTTON).visible:
                    break
                snooze(1)
        self.util.tap(ActionBarConst.DEVICE_BUTTON)
        if p_x:
            self.util.touchAndDrag(UtilConst.MainViewConst.PT_MOBILE_WEBVIEW, p_x, p_y, p_x2, p_y2)
        childObj = self.util.findTag(':deviceSelectorListID_HTML_Object', 'DIV', newDevice) 
        self.util.tap(childObj)

        
    def returnToWorkspace(self):
        try:
            if findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                self.tap(DeviceBaseConst.Cli.ScriptEditor.PASTE_TO_CLI_BUTTON)
                for i in range(120):
                    try:
                        #test.log('Attempt #' + str(i) + ' at closing')
                        closeButton = waitForObject(DeviceBaseConst.Cli.ScriptEditor.CLOSE_BUTTON)
                        self.tap(closeButton)
                        #snooze(1)
                        break
                    except:
                        snooze(1)
                        continue
        except:
            pass
        for i in range(15):
            try:
                if findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                    snooze(1)
                    self.tap(closeButton)
                    break
                else:
                    continue
            except:
                None
        self.util.tap(NavigationBarConst.WORKSPACE_BUTTON)
        snooze(1)
        self.util.tap(NavigationBarConst.WORKSPACE_BUTTON)
        snooze(1)
        try:
            if not findObject(WorkspaceConst.WORKSPACE).visible:
                snooze(1)
                self.util.tap(NavigationBarConst.WORKSPACE_BUTTON)
        except:
            pass
        
    def returnToCluster(self):
        try:
            if findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                self.tap(DeviceBaseConst.Cli.ScriptEditor.PASTE_TO_CLI_BUTTON)
                for i in range(120):
                    try:
                        #test.log('Attempt #' + str(i) + ' at closing')
                        closeButton = waitForObject(DeviceBaseConst.Cli.ScriptEditor.CLOSE_BUTTON)
                        self.tap(closeButton)
                        #snooze(1)
                        break
                    except:
                        snooze(1)
                        continue
        except:
            pass
        for i in range(15):
            try:
                if findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                    snooze(1)
                    self.tap(closeButton)
                    break
                else:
                    continue
            except:
                None
        self.util.tap(NavigationBarConst.CLUSTER_BUTTON)
        snooze(1)
        self.util.tap(NavigationBarConst.CLUSTER_BUTTON)
        snooze(1)
        try:
            if not findObject(WorkspaceConst.WORKSPACE).visible:
                snooze(1)
                self.util.tap(NavigationBarConst.CLUSTER_BUTTON)
        except:
            pass
        
    def setText(self, p_obj, p_text):
        self.util.setText(p_obj, p_text)
        
    def setConsoleText(self, p_obj, p_text):
        pass
    #    self.util.setConsoleText(p_obj, p_text)

    def textCheckPoint(self, p_obj, p_searchText, p_occurrenceNum = -1):
        self.util.textCheckPoint(p_obj, p_searchText, p_occurrenceNum)
        
    def checkDeviceExists(self):
        None
     
    #@summary: Used to wait a specified time until the expected text is in the prompt
    #          This could be used for waiting for a ping or tracert to finish
    #@param p_waitTime: Time to wait in seconds
    #@param p_expectedText: Text that is being waited for
    #@param p_endsWith: If set to True will only check the end of the text if False will check the entire page
    def waitForText(self, p_waitTime, p_expectedText = None, p_endsWith = True, p_object = DeviceBaseConst.Cli.CLI_CONSOLE):
        for i in range(p_waitTime):
            #Try to find the object in case it does not exist yet. If it does the if statements will be
            #executed, but if not a snooze will be issued and findObject will be tried again.
            try:
                findObject(p_object)
            except:
                try:
                    util.fastForwardTime()
                    continue
                except:
                    snooze(1)
                    continue
            #if p_expectedText is not specified then it will look for the common PC prompt > and router prompt #
            if not p_expectedText:
                if not (str(findObject(p_object).simplifiedInnerText).endswith('>')
                        or str(findObject(p_object).simplifiedInnerText).endswith('#')):
                    try:
                        util.fastForwardTime()
                    except:
                        snooze(1)
                break
            #if p_expectedText is specified it will search for that text instead
            if p_endsWith:
                if not str(findObject(p_object).simplifiedInnerText).endswith(p_expectedText):
                    try:
                        util.fastForwardTime()
                    except:
                        snooze(1)
                    continue
            else:
                if not p_expectedText in str(findObject(p_object).simplifiedInnerText):
                    try:
                        util.fastForwardTime()
                    except:
                        snooze(1)
                    
            break
    
class CliBase(DeviceBase):
    def __init__(self):
        self.util = util
    
    def showKeyboard(self):
        super(DeviceBase, self).tap_x_y(DeviceBaseConst.Cli.KEYBOARD_BUTTON, 1, 1)
        
    def hideCLIKeyboard(self):
        keyboard = KeyboardCli()
        self.util.tap_x_y(keyboard.CHARS['[hideKeyboard]'][0], keyboard.CHARS['[hideKeyboard]'][1], keyboard.CHARS['[hideKeyboard]'][2])
            
    def startConsole(self):
        #import time
        #start = time.time()
        for i in range(15):
            #test.log('Trying. Attempt: ' + str(i))
            try:
                if waitForObject(DeviceBaseConst.Cli.SCRIPTEDIT_BUTTON).visible:
            #        snooze(1)
                    self.tap(DeviceBaseConst.Cli.SCRIPTEDIT_BUTTON)
                    if waitForObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                        #continue trying to find and press the script editor button until the script edit field is visible then break out of the loop
            #            snooze(5)
                        break
                    continue
            except:
            #    snooze(1)
                continue
            #snooze(1)
        #stop = time.time()
        #test.log('It took ' + str(stop - start) + ' seconds to go from workspace to device')
        self.tap(DeviceBaseConst.Cli.ScriptEditor.FIELD)
        self.typeTextSE(DeviceBaseConst.Cli.ScriptEditor.FIELD, "no")
        self.typeTextSE(DeviceBaseConst.Cli.ScriptEditor.FIELD, "\r")
        self.tap(DeviceBaseConst.Cli.ScriptEditor.PASTE_TO_CLI_BUTTON)
        self.tap(DeviceBaseConst.Cli.ScriptEditor.NEW_BUTTON)
        self.tap(DeviceBaseConst.Cli.ScriptEditor.FIELD)
        #self.setCliText('no')
        #self.setCliText('\r')

    def setCliText(self, p_text):
        for i in range(5):
            try:
                #Try to find the object
                #If it is not visible execute if block
                if not findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                    self.tap(DeviceBaseConst.Cli.SCRIPTEDIT_BUTTON)
                    self.tap(DeviceBaseConst.Cli.ScriptEditor.FIELD)
            except:
                #if an exception is raised then, under the assumption it is raised because the object 
                #doesn't currently exist (not visible) execute the same code as above
                try:
                    self.tap(DeviceBaseConst.Cli.SCRIPTEDIT_BUTTON)
                    self.tap(DeviceBaseConst.Cli.ScriptEditor.FIELD)
                except:
                    snooze(1)
        obj = self.util.findTag(DeviceBaseConst.Cli.ScriptEditor.FIELD, 'TEXTAREA')
        initialText = obj.value
        setText(obj, str(initialText) + '\r' + p_text)
        self.util.typeTextSE(obj, "\r")
        self.util.hideAndroidKeyboard()
        
    def setCliTextByKeyboard(self, p_text):
    #Try to find the keyboard. If this fails it will cause an exception
        for i in range(5):
            try:
                keyboard = findObject(UtilConst.KeyboardConst.PT_KEYBOARD)
            except:
                #Catch the exception with the class e
                #if this class isn't used then the if statement below will throw an exception
                class e:
                    def __init__(self):
                        self.visible = False
                keyboard = e()
                pass
            if not keyboard.visible: 
                self.util.tap(DeviceBaseConst.Cli.KEYBOARD_BUTTON)
                snooze(1)
            else:
                break
        self.util.typeWithKeyboard(p_text)
    
    def setCliTextByKeyboardNoReturn(self, p_text):
    #Try to find the keybaord. If this fails it will cause an exception
        for i in range(5):
            try:
                keyboard = findObject(UtilConst.KeyboardConst.PT_KEYBOARD)
            except:
                #Catch the exception with the class e
                #if this class isn't used then the if statement below will throw an exception
                class e:
                    def __init__(self):
                        self.visible = False
                keyboard = e()
                pass
            if not keyboard.visible: 
                self.util.tap(DeviceBaseConst.Cli.KEYBOARD_BUTTON)
            else:
                break
        self.util.typeWithKeyboard(p_text, 'cli', False)

    def tapCommandKey(self, p_command, p_x = None, p_y = None, p_x2 = None, p_y2 = None):
        if p_x:
            self.util.touchAndDrag(UtilConst.MainViewConst.PT_MOBILE_WEBVIEW, p_x, p_y, p_x2, p_y2)
        childObj = self.util.findTag(':cmdButtonPanel_HTML_Object', 'DIV', p_command)
        self.util.tap(childObj)            
        
    def pasteToCli(self):
        try:
            if findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                self.tap(DeviceBaseConst.Cli.ScriptEditor.PASTE_TO_CLI_BUTTON)
                for i in range(10):
                    try:
                        closeButton = waitForObject(DeviceBaseConst.Cli.ScriptEditor.CLOSE_BUTTON)
                        snooze(1)
                        self.tap(closeButton)
                        break
                    except:
                        snooze(1)
                        continue
        except:
            pass
        for i in range(10):
            try:
                if findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                    snooze(1)
                    self.tap(closeButton)
                    break
                else:
                    continue
            except:
                pass
        try:
            for i in range(20):
                closeButton = findObject(DeviceBaseConst.Cli.ScriptEditor.CLOSE_BUTTON)
                if closeButton.visible:
                    self.tap(closeButton)
                    snooze(1)
        except:
            pass
        
    def textCheckPoint(self, p_searchText, p_occurrenceNum = -1):
        try:
            if findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                self.tap(DeviceBaseConst.Cli.ScriptEditor.PASTE_TO_CLI_BUTTON)
                for i in range(30):
                    try:
                        closeButton = waitForObject(DeviceBaseConst.Cli.ScriptEditor.CLOSE_BUTTON)
                        self.tap(closeButton)
                        #snooze(1)
                        break
                    except:
                        snooze(1)
                        continue
        except:
            pass
        
        for i in range(10):
            try:
                if findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                    snooze(1)
                    self.tap(closeButton)
                    break
                else:
                    continue
            except:
                pass
        self.util.fastForwardTime()
        self.util.textCheckPoint(DeviceBaseConst.Cli.CLI_CONSOLE, p_searchText, p_occurrenceNum)
        
    def tapMore(self):
        try:
            if findObject(DeviceBaseConst.Cli.ScriptEditor.FIELD).visible:
                self.tap(DeviceBaseConst.Cli.ScriptEditor.PASTE_TO_CLI_BUTTON)
                for i in range(30):
                    try:
                        snooze(1)
                        closeButton = waitForObject(DeviceBaseConst.Cli.ScriptEditor.CLOSE_BUTTON)
                        snooze(1)
                        self.tap(closeButton)
                        
                        break
                    except:
                        snooze(1)
                        continue
        except:
            pass
        self.util.tap(DeviceBaseConst.Cli.MORE_BUTTON)
        
    def tapEnter(self):
        self.util.tap(DeviceBaseConst.Cli.ENTER)
    
class DeviceMenuBase:
    def __init__(self):
        self.deviceBase = DeviceBase()
        self.contextMenu = DeviceBaseConst.ContextMenu

    def select(self):
        self.util.tapOnWorkspace(self.x, self.y)        
 
    def selectConnect(self):
        self.deviceBase.tap(self.contextMenu.CONNECT)
        
    def selectDelete(self):
        self.deviceBase.tap(self.contextMenu.DELETE)
        
    def selectCopy(self):
        self.deviceBase.tap(self.contextMenu.COPY)
        
    def selectInspect(self):
        self.deviceBase.tap(self.contextMenu.INSPECT)
        
    def selectPhysical(self):
        self.deviceBase.tap(self.contextMenu.PHYSICAL)
        
    def selectAddComplexPdu(self):
        self.deviceBase.tap(self.contextMenu.ADD_COMPLEX_PDU)

    def selectAddPdu(self):
        self.deviceBase.tap(self.contextMenu.ADD_PDU)
    
    def selectAutoConnect(self):
        self.deviceBase.tap(self.contextMenu.AUTO_CONNECT)

    def selectRename(self):
        self.deviceBase.tap(self.contextMenu.RENAME)
    
    def selectMultiSelect(self):
        self.deviceBase.tap(self.contextMenu.MULTI_SELECT)
    
    def rename(self, p_newName):
        DEVICE_NAME = ':deviceName_text_HTML_Object'
        APPLY_BUTTON = ':actionbar_apply_button_HTML_Object'
        self.select()
        self.selectRename()
        util.setText(DEVICE_NAME, p_newName)
        util.tap(APPLY_BUTTON)
        
class EndDeviceMenuBase:
    def __init__(self):
        self.deviceMenuBase = DeviceMenuBase()
        self.endDeviceMenu = DeviceBaseConst.EndDeviceMenus
        self.selectConnect = self.deviceMenuBase.selectConnect
        self.selectDelete =  self.deviceMenuBase.selectDelete
        self.selectCopy = self.deviceMenuBase.selectCopy
        self.selectInspect = self.deviceMenuBase.selectInspect
        self.selectPhysical = self.deviceMenuBase.selectPhysical
        self.selectAddComplexPdu = self.deviceMenuBase.selectAddComplexPdu
        self.selectAddPdu = self.deviceMenuBase.selectAddPdu
        self.selectAutoConnect = self.deviceMenuBase.selectAutoConnect
        
    def selectDesktop(self):
        for i in range(10):
            if not object.exists(self.endDeviceMenu.DESKTOP):
                snooze(1)
        self.deviceMenuBase.deviceBase.tap(self.endDeviceMenu.DESKTOP)
        None
        
class CliDeviceMenuBase:
    def __init__(self):
        self.deviceMenuBase = DeviceMenuBase()
        self.cliDeviceMenu = DeviceBaseConst.CliDeviceMenus
        self.selectConnect = self.deviceMenuBase.selectConnect
        self.selectDelete =  self.deviceMenuBase.selectDelete
        self.selectCopy = self.deviceMenuBase.selectCopy
        self.selectInspect = self.deviceMenuBase.selectInspect
        self.selectPhysical = self.deviceMenuBase.selectPhysical
        self.selectAddComplexPdu = self.deviceMenuBase.selectAddComplexPdu
        self.selectAddPdu = self.deviceMenuBase.selectAddPdu
        self.selectAutoConnect = self.deviceMenuBase.selectAutoConnect
        self.selectRename = self.deviceMenuBase.selectRename
        self.selectMultiSelect = self.deviceMenuBase.selectMultiSelect
        self.rename = self.deviceMenuBase.rename
        
    def selectCli(self):
        for i in range(10):
            if not object.exists(self.cliDeviceMenu.CONSOLE):
                snooze(1)
                continue
            break
        self.deviceMenuBase.deviceBase.tap(self.cliDeviceMenu.CONSOLE)

class Physical:
    def __init__(self):
        self.deviceBase = DeviceBase()
        self.contextMenu = DeviceBaseConst.ContextMenu

    #@summary: add module to device
    #@param p_power: power button object
    #@param p_slot_module: module that should be removed from slot and replaced by new module. if it '' it means the slot is empty
    #@param p_more_module: it is boolean and if it is 0 means there is no more module to be added or removed
    def addModule(self, p_powr, p_slot_module, p_modul, p_slot, p_more_modul):

        #check if device physical is open
        if not self.util.compare(waitForObject(DevicBaseConst.physicalview).visible, True):

            #check if focus is on workspace 
            if not self.util.compare(waitForObject(workspace).visible, True):
                self.util.tap(workspace)

            self.deviceBase.tap(self.contextMenu.PHYSICAL)

        #check power button is on/off
        if self.util.compare(waitForObject(DevicBaseConst.p_powr).status, 'ON'):
            self.deviceBase.tap(self.DeviceBaseConst.Physical.p_power)

        #check slot is empty
        if not p_powr_slot == '':
            self.deviceBase.tap(self.DeviceBaseConst.Physical.p_slot_module)
            
        self.deviceBase.tap(self.DeviceBaseConst.Physical.p_modul)
        self.deviceBase.tap(self.DeviceBaseConst.Physical.p_slot)

        #check if there is still module to be added or removed. If not turn power on and go back to workspace
        if not p_more_modul_number:
            self.deviceBase.tap(self.DeviceBaseConst.Physical.p_power)
            self.util.tap(workspace)

    #@summary: remove module
    #@param p_power: power button object
    #@param p_slot_module: module that should be removed from slot
    #@param p_more_module: it is boolean and if it is 0 means there is no more module to be added or removed
    def removeModule(self, p_powr, p_slot_module, p_more_modul):

        #check if device physical is open        
        if not self.util.compare(waitForObject(DevicBaseConst.physicalview).visible, True):

            if not self.util.compare(waitForObject(workspace).visible, True):
                self.util.tap(workspace)

            self.deviceBase.tap(self.contextMenu.PHYSICAL)

        #check power button is on/off
        if self.util.compare(waitForObject(DevicBaseConst.p_powr).status, 'ON'):
            self.deviceBase.tap(self.DeviceBaseConst.Physical.p_power)


        self.deviceBase.tap(self.DeviceBaseConst.Physical.p_slot_module)

        #check if there is still module to be added or removed. If not turn power on and go back to workspace
        if not p_more_modul_number:
            self.deviceBase.tap(self.DeviceBaseConst.Physical.p_power)
            self.util.tap(workspace)