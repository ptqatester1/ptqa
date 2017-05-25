####################################################
#@author: Chris Allen
#@summary: Util includes all commonly used functions
####################################################
from API.Android.SquishSyntax import SquishSyntax
from API.Android.Utility.UtilConst import *
from API.Android.Workspace.WorkspaceConst import LoginConst
from API.Android.Workspace.WorkspaceConst import NavigationBarConst
from API.Android.Workspace.WorkspaceConst import WorkspaceConst
from API.Android.ActionBar.File.LoadNetwork.LoadNetworkConst import LoadNetworkConst
from API.Android.ActionBar.ActionBarConst import ActionBarConst
from API.Android.ContextMenus.ContextMenusConst import DeviceContextMenu,\
    CableDevices, MainContextMenu, ShapeSubMenuConst
from API.Android.ActionBar.File.LoadNetwork.LoadNetwork import LoadNetwork
from API.Android.ActionBar.File.NewNetwork.NewNetwork import NewNetwork
from API.Android.Simulation.PDU.PduConst import PduConst
from API.Android.CableDevices.cableDeviceConst import CableTypeMenu
import test
import os
import object
from squish import *
import re
from API.Android.InstructionWindow.InstructionsConst import Instruction
from API.Android.Simulation.PDU import PduConst
from API.Android.CableDevices.cableDevice import cableDevices
from API.Android.Utility import UtilConst

deviceMenuBase = DeviceContextMenu()
actionBar = ActionBarConst()
loadNetwork = LoadNetwork()
newNetwork = NewNetwork()

class Util(SquishSyntax):
    def __init__(self):
        self.connectDevices = cableDevices()
    #@param p_login: Can pass the values for the new or load buttons
    def init(self, p_login = None):        #Below is used to wait for the main login/new/open window
        import time
        startTime = time.time()
        
        '''objectShowed = False
        for i in range(120):
            None
            try:
                if waitForObject(LoginConst.OK_BUTTON).visible:
                    self.tap(LoginConst.OK_BUTTON)
                    objectShowed = True
                    break
            except:
                continue
        if not objectShowed:
            test.log('Internet connection is detected'.upper())'''
            
        objectShowed = False
        for i in range(360):
            None
            try:
                if waitForObject(LoginConst.PT_MOBILE_TITLE).visible:
                    objectShowed = True
                    break
            except:
                continue
        if not objectShowed:
            test.log('PT_MOBILE_TITLE never showed. Name may have changed if this \
            is the case then it needs fixed or this function will be slowing down testing'.upper())
            
        if p_login:
            self.tap(p_login)
        stopTime = time.time()
        test.log('Starting PT took ' + str(stopTime - startTime) + ' seconds')
        snooze(5)
                        
    def open(self, p_fileName, p_location = ''):
        loadNetwork.openFile(p_fileName, p_location)
        waitForObject(WorkspaceConst.WORKSPACE)

    def PKAcompatibilityCheck(self):
        self.waitForObject(LoadNetworkConst.PKA_ALERT_OK)
        self.tap(LoadNetworkConst.PKA_ALERT_OK)
    
    def waitForObject(self, p_obj):
        for i in range(15):
            try:
                if not waitForObject(p_obj).visible:
                    continue
                break
            except:
                continue
            
    def saveNew(self, p_fileName, p_location = ''):
        loadNetwork.saveNewFile(p_fileName, p_location)
        
    def saveAs(self, p_fileName, p_location = ''):
        loadNetwork.saveAsFile(p_fileName, p_location)
        if object.exists(LoadNetworkConst.SAVE_OVERWRITE_YES):
            self.tap(LoadNetworkConst.SAVE_OVERWRITE_YES)
        else:
            pass
        self.tap(':ext-button-3_HTML_Object')
    
    def exit(self):
        loadNetwork.exitPT()
        
    def tapSimulationPDU(self):
        self.tap(ActionBarConst.OVERFLOW_BUTTON)
        snooze(1)
        self.tap(ActionBarConst.Options.PDU_BUTTON)
        
    def createDevice(self, p_deviceType, p_deviceModel, p_x, p_y):
        p_obj = waitForObject(WorkspaceConst.WORKSPACE)
        self.tap_x_y(p_obj, p_x, p_y)
        snooze(5)
        self.tap(p_deviceType)
        snooze(2)
        self.tap(p_deviceModel)
    
    def drawShape(self, p_shape, p_x1, p_y1, p_x2, p_y2):
        self.tap_x_y(WorkspaceConst.WORKSPACE, 1, 1)
        snooze(2)
        self.tap(MainContextMenu.SHAPES)
        self.tap(p_shape)
        self.touchAndDrag(WorkspaceConst.WORKSPACE, p_x1, p_y1, p_x2, p_y2)
        self.tap_x_y(WorkspaceConst.WORKSPACE, 1, 1)
        self.tap(MainContextMenu.EXIT)
    
    def ShapesOptions(self):
        self.tap_x_y(WorkspaceConst.WORKSPACE, 1, 1)
        snooze(2)
        self.tap(ShapeSubMenuConst.OPTIONS)
        
    
    def tapOnWorkspace(self, p_x, p_y):
        p_obj = waitForObject(WorkspaceConst.WORKSPACE)
        self.tap_x_y(p_obj, p_x, p_y)
        
    def simulationForward(self):
        self.tap(ActionBarConst.SIMULATION_FORWARD_BUTTON)
        
    def simulationBackward(self):
        self.tap(ActionBarConst.SIMULATION_BACK_BUTTON)
        
    def doubleTapOnWorkspace(self, p_x, p_y):
        p_obj = waitForObject(WorkspaceConst.WORKSPACE)
        self.doubleTap_x_y(p_obj, p_x, p_y)
    
    def tapOnDevice(self, p_dev):
        p_obj = waitForObject(WorkspaceConst.WORKSPACE)
        self.tap_x_y(p_obj, p_dev.x, p_dev.y)
        
    def swipe(self, p_x, p_y, p_x2, p_y2):
        self.touchAndDrag(WorkspaceConst.MAIN_APPLICATION, p_x, p_y, p_x2, p_y2)
        
    def newWorkspace(self):
        newNetwork.selectNewNetwork()
    
    def setText(self, p_obj, p_text):
        waitForObject(p_obj)
        if not 'cli' in p_obj:
            obj = self.findTag(p_obj, 'INPUT', '')
            try:
                obj.value = ''
            except:
                pass
            snooze(1)
            self.tap(obj)
            snooze(1)
            self.setTextValue(obj, p_text)
            snooze(1)
            self.tap(obj)
        else:
            p_obj = waitForObject(p_obj)
            self.tap(p_obj)
            
    def setSearchText(self, p_obj, p_text):
        waitForObject(p_obj)
        if not 'cli' in p_obj:
            obj = self.findTag(p_obj, 'INPUT', '')
            try:
                obj.value = ''
            except:
                pass
            snooze(1)
            self.tap(obj)
            snooze(1)
            from squish import *
            type(obj, p_text)
            snooze(1)
        else:
            p_obj = waitForObject(p_obj)
            self.tap(p_obj)
        
    def tapTextArea(self, p_obj):
        waitForObject(p_obj)
        if not 'cli' in p_obj:
            obj = self.findTag(p_obj, 'INPUT', '')
            try:
                obj.value = ''
            except:
                pass
            self.tap(obj)
            snooze(2)
            self.tap(self.findTag(p_obj, 'INPUT', ''))
        else:
            p_obj = waitForObject(p_obj)
            self.tap(p_obj)
        
    def getTextInputValue(self, p_obj):
        waitForObject(p_obj)
        p_obj = self.findTag(p_obj, 'INPUT', '')
        try:
            return p_obj.value
        except:
            return test.fail('Could not get value')
    
    def hideAndroidKeyboard(self):
        hideKeyboard(waitForObject(UtilConst.KeyboardConst.ANDROID_KEYBOARD));
        
    def hideCLIKeyboard(self):
        self.typeWithKeyboard('[hideKeyboard]')
        
    def setConsoleText(self, p_obj, p_text):
        self.typeText(waitForObject(p_obj), p_text)
        self.typeText(waitForObject(p_obj), "\r")
    
    def speedUpConvergence(self):
        self.tap(ActionBarConst.REALTIME_FORWARD_BUTTON)
        snooze(1)
        self.tap(ActionBarConst.REALTIME_FORWARD_BUTTON)
        snooze(1)
        self.tap(ActionBarConst.REALTIME_FORWARD_BUTTON)
        snooze(1)
        self.tap(ActionBarConst.REALTIME_FORWARD_BUTTON)
        snooze(1)
        self.tap(ActionBarConst.REALTIME_FORWARD_BUTTON)
        snooze(5)

    def connect(self, p_dev1, p_dev2, p_cableType, p_int1, p_int2):
        cableDevs = cableDevices()
        cableDevs.connect(p_dev1, p_dev2, p_cableType, p_int1, p_int2)

    def disconnect(self, p_dev1, p_dev2, p_port1):
        from API.Android.CableDevices.cableDeviceConst import PortInterface
        port1 = PortInterface.PORT_BASE + str(p_port1) + PortInterface.PORT_END
        self.tapOnDevice(p_dev1)
        self.tap(DeviceContextMenu.CONNECT)
        self.tapOnDevice(p_dev2)
        self.tap(port1)
        snooze(1)
        self.tap(ActionBarConst.WORKSPACE_BUTTON)

    def addPDU(self, p_dev1, p_dev2):
        self.tapOnDevice(p_dev1)
        snooze(2)
        self.tap(DeviceContextMenu.ADD_PDU)
        self.tapOnDevice(p_dev2)

    def addComplexPDU(self, p_dev, p_app, p_destIP, p_tos, p_ttl, p_seq, p_size, p_simSetting, p_timeOrInterval, p_port = ''):
        self.tapOnDevice(p_dev)
        deviceMenuBase.selectAddComplexPdu()

        if (p_app != ""):
            self.setText(PduConst.ComplexPDU.APPLICATION, p_app)
            #neeeded to be rewritten since the applications doesn't have object name        
            #self.tap(waitForObject(PduConst.ComplexPDU.APPLICATION + p_app))
        snooze(5)
        if (p_port != ""):
            self.tap(PduConst.ComplexPDU.AUTO_SELECT_PORT)
            self.tap(PduConst.ComplexPDU.OUTGOING_PORT)
            #neeeded to be rewritten since the ports doesn't have object name
            #self.tap(waitForObject(PduConst.ComplexPDU.OUTGOING_PORT + p_port))
        snooze(5)
        if (p_destIP != ""):
            self.setText(PduConst.ComplexPDU.DESTINATION_IP, p_destIP)
        if (p_srcIP != ""):
            self.setText(PduConst.ComplexPDU.SOURCE_IP, p_srcIP)
        if (p_tos != ""):
            self.setText(PduConst.ComplexPDU.TOS, p_tos)
        if (p_ttl != ""):
            self.setText(PduConst.ComplexPDU.TTL, p_ttl)
        if (p_seq != ""):
            self.setText(PduConst.ComplexPDU.SEQ_NUM, p_seq)
        if (p_size != ""):
            self.setText(ComplexPDUWindowConst.SIZE, p_size)
        if (p_simSetting != ""):
            if (p_simSetting == 'oneshot'):
                self.tap(PduConst.ComplexPDU.ONE_SHOT_RADIO)
                self.setText(PduConst.ComplexPDU.ONE_SHOT_TIME, p_timeOrInterval)
            elif (p_simSetting == 'periodic'):
                self.tap(PduConst.ComplexPDU.PERIODIC_RADIO)
                self.setText(PduConst.ComplexPDU.PERIODIC_TIME, p_timeOrInterval)
            
        if (p_sPort != ""):
            self.setText(PduConst.ComplexPDU.s, p_app)
        if (p_dPort != ""):
            self.setText(ComplexPDUWindowConst.DESTINATION_PORT, p_dPort)

        self.clickButton(ComplexPDUWindowConst.CREATE_PDU)
    
    #@summary: This is for checking if text exists in a string
    #@param p_textType: This is to specify a specific type of text to be used for checking
    #                   Ex. p_textType = 'innnerHTML' would check innerHTML 
    def textCheckPoint(self, p_obj, p_searchText, p_occurrenceNum = -1, p_textType = ''):
        consoleText = None
        waitFor("object.exists('" + p_obj + "')", 2000)
        widget = findObject(p_obj)
        properties = object.properties(widget)
        if not p_textType:
            if 'text' in properties:
                consoleText = str(findObject(p_obj).text)
            if 'plainText' in properties:
                consoleText = str(findObject(p_obj).plainText)
            if 'innerText' in properties:
                consoleText = str(findObject(p_obj).innerText)
            if 'value' in properties:
                consoleText = str(findObject(p_obj).value)
        else:
            if p_textType in properties:
                consoleText = str(properties[p_textType])
            else:
                test.log('Unable to find the specified text type')
        super(Util, self).textCheckPoint(consoleText, p_searchText, p_occurrenceNum)
    
    def fastForwardTime(self):
        self.tap(ActionBarConst.REALTIME_FORWARD_BUTTON)
        snooze(1)
    
    def tapSimulation(self):
        self.tap(ActionBarConst.SIMULATION_BUTTON)

    def tapRealtime(self):
        self.tap(ActionBarConst.REALTIME_BUTTON) 
        
    def toggleRealtimeSimulation(self): 
        if findObject(ActionBarConst.SIMULATION_BUTTON).visible:
            self.tap(ActionBarConst.SIMULATION_BUTTON)
        else:
            self.tap(ActionBarConst.REALTIME_BUTTON)              
    
    def checkActivityCompletion(self, p_progress = "Complete: 100/100"):
        self.tap(Instruction.COMPLETE_BUTTON)
        snooze(5)
        self.textCheckPoint(Instruction.COMPLETE_BUTTON, p_progress, -1, 'simplifiedInnerText')
        
    def typeWithKeyboard(self, p_text, p_keyboard = 'cli', p_implicitReturn = True):
        keyboards = {'cli':KeyboardCli, 'cmd':KeyboardCmd}
        keyboard = keyboards[p_keyboard]()
        if p_text.startswith('[') and p_text.endswith(']'):
            self.tap_x_y(keyboard.CHARS[p_text][0], keyboard.CHARS[p_text][1], keyboard.CHARS[p_text][2])
        else:
            for char in p_text:
                if char in keyboard.SPECIAL_CHARS:
                    self.tap_x_y(keyboard.CHARS['[shift]'][0], keyboard.CHARS['[shift]'][1], keyboard.CHARS['[shift]'][2])
                    self.tap_x_y(keyboard.SPECIAL_CHARS[char][0], keyboard.SPECIAL_CHARS[char][1], keyboard.SPECIAL_CHARS[char][2])
                elif char in keyboard.UPPER_CHARS:
                    self.tap_x_y(keyboard.CHARS['[shift]'][0], keyboard.CHARS['[shift]'][1], keyboard.CHARS['[shift]'][2])
                    self.tap_x_y(keyboard.UPPER_CHARS[char][0], keyboard.UPPER_CHARS[char][1], keyboard.UPPER_CHARS[char][2])
                else:
                    self.tap_x_y(keyboard.CHARS[char][0], keyboard.CHARS[char][1], keyboard.CHARS[char][2])
                if char == ' ':
                    None
                #test.log(char)
        if not p_text == '[hideKeyboard]' and p_implicitReturn:#implicit return is just used to do an automatic return at the end set to false for no return at the end
            self.tap_x_y(keyboard.CHARS['\r'][0], keyboard.CHARS['\r'][1], keyboard.CHARS['\r'][2])
            
    def toggleInstructions(self):
        self.tap(Instruction.INSTRUCTIONS_BUTTON)
               
    #@summary: This function is used to find a specific tag with a specific value
    #          For instance if you want to find the ip edit <input> with a value of '0.0.0.0',
    #          You would call findTag(ServerConst.IPConfig.IP_EDIT, 'INPUT', '0.0.0.0')
    #@param startTag: This is the base where it will start searching from
    #@param searchTag: This is the tag you are searching for
    #@param searchValue: This is the value of the tag you a searching for. It can be any string that would uniquely(or at least almost uniquely) identify that item.
    def findTag(self, startTag, searchTag, searchTagValue = ''):
        childValue = []
        startTag = findObject(startTag)
        def getTag(startTag, searchTag, searchTagValue):
            children = object.children(startTag)
            for child in children:
                properties = object.properties(child)
                if 'tagName' in properties:
                    if properties['tagName'] == searchTag:
                        if searchTagValue:
                            for key in properties:
                                match = re.match(searchTagValue, str(properties[key]))
                                if match:
                                    if str(match.group()) == str(properties[key]): 
                                        childValue.append(child)
                                        raise Exception('Breaking out of recursion')
                                        #return child
                        else:
                            childValue.append(child)
                            raise Exception('Breaking out of recursion')
                            #return child
                if child.numChildren > 0:
                    getTag(child, searchTag, searchTagValue)
        try:
            getTag(startTag, searchTag, searchTagValue)
        except:
            pass
        if not childValue:
            raise Exception('Unable to find the value searched for')
        return childValue[0]
        
    def waitForVisibleObject(self, p_obj, p_times = 15):
        for i in range(p_times):
            try:
                if waitForObject(p_obj).visible:
                    snooze(1)
                    break
            except:
                snooze(1)
                continue
            continue
            
    def setNote(self, p_x, p_y, p_text):
        self.tapOnWorkspace(p_x, p_y)
        snooze(2)
        self.tap(MainContextMenu.PLACE_NOTE)
        snooze(2)
        self.typeText(WorkspaceConst.NOTE_TEXT_AREA, p_text)
        self.tapOnWorkspace(100, 100)
        
    def renameDevice(self, p_dev1, p_text):
        self.tapOnDevice(p_dev1)
        snooze(2)
        self.tap(DeviceContextMenu.RENAME)        
        
        for i in range (10): 
            self.tap(WorkspaceConst.DEVICE_NAME_TEXT)
            self.typeText(WorkspaceConst.DEVICE_NAME_TEXT, "<Backspace>")
            self.typeText(WorkspaceConst.DEVICE_NAME_TEXT, "<Backspace>")

        self.typeText(WorkspaceConst.DEVICE_NAME_TEXT, p_text)
        self.tap(WorkspaceConst.ACTION_BAR_APPLY)
    
    def checkObjectExist(self, p_squishName):
        if object.exists(p_squishName):
            return True
        else:
            return False
    
    
    def getPositions(self, devicesInScript, deviceNamesThatSpanMultipleLines = [], addSpace = True):
        '''First argument is a list of the device objects that are used in the script. Second argument is used if the names span multiple lines.
        Third argument is if there is a device name such as cisco.pka.se ver where the ver is on a second line. In this case use False as the third
        argument and add ['cisco.pka.se ver'] to the second argument.'''
        modelNameList = [
                         'PC-PT', 'Laptop-PT', 'TabletPC-PT', 'SMARTPHONE-PT', 'TV-PT', 'Server-PT', 'Analog-Phone-PT', 'Home-VoIP-PT',
                         '7960', 'Printer-PT', 'WiredEndDevice-PT', 'WirelessEndDevice-PT', 'Sniffer', 'Router-PT-Empty', '1841', '1941',
                         '2620XM', '2621XM', '2811', '2901', '2911', '819', 'Router-PT', 'Bridge-PT', 'Switch-PT', '2960-24TT', '2950T-24',
                         '2950-24', '3560-24PS', 'Switch-PT-Empty', 'Linksys-WRT300N', 'AccessPoint-PT', 'AccessPoint-PT-A', 'AccessPoint-PT-N',
                         'Cell-Tower', 'Central-Office-Server', 'DSL-Modem-PT', 'Cable-Modem-PT', 'Cloud-PT', 'Cloud-PT-Empty',
                         '5505', 'Repeater-PT', 'CoAxialSplitter-PT', 'Hub-PT'
                         ]
        workspace = findObject(WorkspaceConst.WORKSPACE)
        c = object.children
        mainObject = c(c(c(c(c(c(workspace)[0])[1])[0])[2])[0])[7]
        deviceString = str(mainObject.innerText)
        for name in deviceNamesThatSpanMultipleLines:
            if addSpace:
                deviceString = deviceString.replace('\n'.join(name.split()), name)
            else:
                deviceString = deviceString.replace('\n'.join(name.split()), ''.join(name.split()))
        devList = deviceString.splitlines()
        
        for device in devList:
            if device in modelNameList:
                removeItem = True
                for dev in devicesInScript:
                    if dev.displayName in modelNameList:
                        removeItem = False
                if removeItem:
                    test.log('Removing '  + device)
                    devList.remove(device)
                    
        imageList = c(c(c(c(mainObject)[0])[0])[0])
        devDict = {}
        i = 0
        for dev in devList:
            test.log(dev)
            while i < len(imageList) and imageList[i].screenRect.x == -1 or imageList[i].screenRect.y == -1:
                i += 1
                if i >= len(imageList):
                    None
                    break
            if i >= len(imageList):
                None
                break
            devDict[dev] = (imageList[i].screenRect.x+5, imageList[i].screenRect.y-2)
            i += 1
        for dev in devicesInScript:
            try:
                dictEntry = devDict[dev.displayName]
            except KeyError, e:
                raise Exception('If there is a key error then the most likely cause is that there is a device who\'s \
                name is multiple lines. Add that device to the list of deviceNamesThatSpanMultipleLines')
            except Exception, e:
                raise Exception(e)
            dev.x = dictEntry[0]
            dev.y = dictEntry[1]
            
    def JScheck(self):
        snooze(10)
        if (object.exists(WorkspaceConst.DIAGNOSTICS_REPORT_DIALOG)):
            test.fail("Javascript error!")
        else:
            test.passes("No Javascript error.")