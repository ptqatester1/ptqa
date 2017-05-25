#*************************************************************
#@author: Thi Nguyen
#@summary: Util includes all commonly used function in tests
#*************************************************************
from API.ComponentBox.ComponentBox import ComponentBox
from API.ComponentBox.ComponentBoxConst import DeviceGroup
from API.ComponentBox.ComponentBoxConst import Connection
from API.ComponentBox.ComponentBoxConst import DeviceType
from API.SquishSyntax import SquishSyntax
from API.Toolbar.MainToolBar.MainToolbar import MainToolbar
from API.Utility import UtilConst
from API.MenuBar.File.Open.OpenConst import OpenConst
from API.MenuBar.Options.UserProfile.UserProfile import UserProfile
from API.MenuBar.File.Exit.ExitConst import ExitConst
from API.ComponentBox.ComponentBoxConst import DeviceModel
from API.Toolbar.GoldenRealtimeToolbar.GoldenRealtimeToolbarConst import GoldenRealtimeToolbarConst
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst
from API.ActivityWizard.TestActivity.TestActivityConst import TestActivityConst
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.NetspaceLogin.NetspaceLogin import NetspaceLogin
from API.NetspaceLogin.NetspaceLoginConst import NetspaceLoginConst
from API.Toolbar.GoldenPhysicalToolbar.GoldenPhysicalToolbarConst import GoldenPhysicalToolbarConst

import os
import object
import sys
import test
import inspect
import re
from API.functions import isType
from API.functions import escapeRegex
from API.functions import trace
from API.functions import getType
from API.functions import check
import operator
from squish import *

class Util(SquishSyntax):    
    
    def __init__(self):
        self.componentBox = ComponentBox()
        self.mainToolbar = MainToolbar()
        self.userProfile = UserProfile()
        
    def init(self, AttachedPT = False):
        self.attachPT(AttachedPT)
        while (object.exists(":CAppWindowBase.Cisco Packet Tracer - Add New Script Module.qt_msgbox_buttonbox.Always from Same Publisher") or
               object.exists(":CAppWindowBase.Cisco Packet Tracer - Add New Script Module.qt_msgbox_buttonbox.Yes") or
               object.exists(":CAppWindowBase.Cisco Packet Tracer - Add New ExApp.qt_msgbox_buttonbox.Yes") or
               object.exists(":Packet Tracer.qt_msgbox_buttonbox.OK") or
               object.exists(":CAppWindowBase.Cisco Packet Tracer - Add New ExApp.qt_msgbox_buttonbox.Always from Same Publisher")):
            if (object.exists(":Packet Tracer.qt_msgbox_buttonbox.OK")):
                self.clickButton(":Packet Tracer.qt_msgbox_buttonbox.OK")
            if (object.exists(":CAppWindowBase.Cisco Packet Tracer - Add New Script Module.qt_msgbox_buttonbox.Always from Same Publisher")):        
                self.clickButton(":CAppWindowBase.Cisco Packet Tracer - Add New Script Module.qt_msgbox_buttonbox.Always from Same Publisher")
            if (object.exists(":CAppWindowBase.Cisco Packet Tracer - Add New ExApp.qt_msgbox_buttonbox.Always from Same Publisher")):
                self.clickButton(":CAppWindowBase.Cisco Packet Tracer - Add New ExApp.qt_msgbox_buttonbox.Always from Same Publisher")
            if (object.exists(":CAppWindowBase.Cisco Packet Tracer - Add New Script Module.qt_msgbox_buttonbox.Yes")):
                self.clickButton(":CAppWindowBase.Cisco Packet Tracer - Add New Script Module.qt_msgbox_buttonbox.Yes")
            if (object.exists(":CAppWindowBase.Cisco Packet Tracer - Add New ExApp.qt_msgbox_buttonbox.Yes")):
                self.clickButton(":CAppWindowBase.Cisco Packet Tracer - Add New ExApp.qt_msgbox_buttonbox.Yes")
        if object.exists(NetspaceLoginConst.NETSPACE_BASE):
            NetspaceLogin().login()
        self.newWorkspace()

    def findWorkspace(self):
        import object
        workspaces = [UtilConst.WORKSPACE, UtilConst.WORKSPACE_2, UtilConst.WORKSPACE_3,
                      UtilConst.PKA_WORKSPACE, UtilConst.PKT_PKA_WORKSPACE,
                      UtilConst.ANSWER_NETWORK_WORKSPACE, UtilConst.INITIAL_NETWORK_WORKSPACE,
                      UtilConst.PHYSICAL_WORKSPACE, UtilConst.CLOSET_WORKSPACE]
        currentWorkspace = None
        for workspace in workspaces:
            if not object.exists(workspace):
                continue#If the object doesn't exist just skip it and move on
            workspaceObject = findObject(workspace)
            properties = object.properties(workspaceObject)
            if 'visible' in properties:
                if workspaceObject.visible:
                    currentWorkspace = workspace
                    #break
        if not currentWorkspace:
            raise ValueError('Could not find a visible workspace')
        return currentWorkspace
    
    @property
    def currentWorkspace(self):
        return self.findWorkspace()
    
    #@summary:
    #@param p_x: x coordinate
    #@param p_y: y coordinate
    def clickOnWorkspace(self, p_x, p_y):
        currentWorkspace = self.findWorkspace()
        self.click_x_y(currentWorkspace, p_x, p_y)

    #@summary: Double click on workspace
    #@param p_x: x coordinate
    #@param p_y: y coordinate
    def doubleclickOnWorkspace(self, p_x, p_y):
        currentWorkspace = self.findWorkspace()
        self.doubleClick_x_y(currentWorkspace, p_x, p_y)

    def closePT(self):
        waitForObject(":CAppWindowBase")
        self.sendEvent(":CAppWindowBase", "QCloseEvent")
        if (object.exists(ExitConst.SAVE_NETWORK_PROMPT_NO)):
            self.clickButton(ExitConst.SAVE_NETWORK_PROMPT_NO)
            
    def newWorkspace(self):
        self.mainToolbar.newNoSave()

    #@summary: get the right filePath depending on the system it's running on and open it
    #@param p_fileName: name of the file
    #@param p_testType: type of the test
    def open(self, p_fileName, p_testType = UtilConst.CCIE_TEST):
        self.mainToolbar.openFile(self.getFilePath(p_fileName, p_testType))
        if (object.exists(OpenConst.UPDATE_IOE_DEVICES)):
            self.clickButton(OpenConst.UPDATE_IOE_DEVICES_YES)
        
    def openOverwriteExisitng(self, p_fileName, p_testType = UtilConst.CCIE_TEST):
        self.mainToolbar.openFileSaveOverwrite(self.getFilePath(p_fileName, p_testType))

    #@summary: get the right filePath depending on the system it's running on
    #@param p_fileName: name of the file
    #@param p_testType: type of the test
    def getFilePath(self, p_fileName, p_testType = UtilConst.CCIE_TEST):
        if(os.name =='posix'):
            return "/home/drevil/Desktop/P/ptqa/trunk/workspace/Squish/Pkt_Pka_ForTesting/" + p_testType + "/" + p_fileName
        else:
            #return "P:\\ptqa\\trunk\\workspace\\Squish\\Pkt_Pka_ForTesting\\" + p_testType + "\\" + p_fileName
            return "C:\\Users\\Abbas Hakimzadeh\\Desktop\\ptqa\\trunk\\workspace\\Squish\\Pkt_Pka_ForTesting\\" + p_testType + "\\" + p_fileName
            #return "C:\\Users\\pvinco\\Desktop\\ptqa\\trunk\\workspace\\Squish\\Pkt_Pka_ForTesting\\" + p_testType + "\\" + p_fileName
        
    #@summary: Create a device on workspace
    #@param p_device: type of device to be created
    #@param p_x: x coordinate of the device
    #@param p_y: y coordinate of the device
    def createDevice (self, p_deviceType, p_deviceModel , p_x, p_y):
        if p_deviceType == DeviceType.ROUTER or p_deviceType == DeviceType.SWITCH or p_deviceType == DeviceType.HUB or p_deviceType == DeviceType.WIRELESS_DEVICE or p_deviceType == DeviceType.SECURITY or p_deviceType == DeviceType.WAN:
            self.componentBox.clickButton(DeviceGroup.NETWORK_DEVICES)
        elif p_deviceType == DeviceType.END_DEVICE or p_deviceType == DeviceType.HOME or p_deviceType == DeviceType.SMART_CITY or p_deviceType == DeviceType.INDUSTRIAL or p_deviceType == DeviceType.POWER_GRID:
            self.componentBox.clickButton(DeviceGroup.END_DEVICES)
        elif p_deviceType == DeviceType.BOARDS or p_deviceType == DeviceType.ACTUATORS or p_deviceType == DeviceType.SENSORS:
            self.componentBox.clickButton(DeviceGroup.COMPONENTS)
        elif p_deviceType == DeviceType.MISCELLANEOUS:
            self.componentBox.clickButton(DeviceGroup.MISCELLANEOUS)
        elif p_deviceType == DeviceType.MULTIUSER:
            self.componentBox.clickButton(DeviceGroup.MULTIUSER)
        else:
            None
        self.componentBox.clickButton(p_deviceType)
        self.componentBox.clickButton(p_deviceModel)
        self.clickOnWorkspace(p_x, p_y)
        
    def createExtension(self, p_x, p_y):
        self.componentBox.clickButton(DeviceType.MULTIUSER)
        self.dragAndDrop(DeviceModel.MULTIUSER, 23, 21, p_x, p_y)
        self.clickOnWorkspace(p_x, p_y)

    #@summary: Connect two devices together on workspace
    #@param p_x1: x coordinate of the first device
    #@param p_y1: y coordinate of the first device
    #@param p_x2: x coordinate of the second device
    #@param p_y2: y coordinate of the second device
    #@param p_connection: type of cable
    #@param p_port: port name
    def connect(self, p_x1, p_y1, p_x2, p_y2, p_connection, p_port1, p_port2):
        self.componentBox.clickButton(DeviceGroup.CONNECTIONS)
        self.componentBox.clickButton(DeviceType.CONNECTION)
        self.componentBox.clickButton(p_connection)
        self.clickOnWorkspace(p_x1, p_y1)
        if p_connection != Connection.CONN_AUTO:
            snooze(1)
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN), p_port1)
        self.clickOnWorkspace(p_x2, p_y2)
        if p_connection != Connection.CONN_AUTO:
            snooze(1)
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN), p_port2)

    def connectOnCloset(self, devObj0, devObj1, p_connection, p_port1, p_port2):
        self.componentBox.clickButton(DeviceGroup.CONNECTIONS)
        self.componentBox.clickButton(DeviceType.CONNECTION)
        self.componentBox.clickButton(p_connection)
        waitForObject(UtilConst.CLOSET_WORKSPACE)
        self.click(devObj0)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN), p_port1)
        waitForObject(UtilConst.CLOSET_WORKSPACE)
        self.click(devObj1)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN), p_port2)

    #@summary: Connect two devices together on physical workspace
    #@param p_x1: x coordinate of the first device/location
    #@param p_y1: y coordinate of the first device/location
    #@param p_x2: x coordinate of the second device/location
    #@param p_y2: y coordinate of the second device/location
    #@param p_connection: type of cable
    #@param p_port1 & 2: ports name    
    #@param p_obj1: in case the first device is in GeoView the object name of the GeoView should be passed
    #@param p_obj2: in case the second device is in GeoView the object name of the GeoView should be passed
    #@param p_location1: Location of the first device (Ex: "Intercity_1/Home City/Corporate Office")
    #@param p_location1: Location of the second device (Ex: "Intercity_1/Home City/Corporate Office")
    def connectOnPhysical(self, p_x1, p_y1, p_x2, p_y2, p_connection, p_port1, p_port2, p_location1 = "", p_location2 = ""):
        self.componentBox.clickButton(DeviceGroup.CONNECTIONS)
        self.componentBox.clickButton(DeviceType.CONNECTION)
        self.componentBox.clickButton(p_connection)
        if not "/" in p_location1 and p_location1 == "":
            waitForObject(UtilConst.PHYSICAL_WORKSPACE)
            self.clickOnWorkspace(p_x1, p_y1)
            if p_connection != Connection.CONN_AUTO:
                self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN), p_port1) 
        
        elif p_connection == Connection.CONN_AUTO:
            print "Auto-Connection Can Not Be Used When 2 Devices Are Not In The Same Location."
            return
        else:
            locationList = p_location1.split("/")
            print locationList

            self.clickOnWorkspace(p_x1, p_y1)
            dropdownObj = GoldenPhysicalToolbarConst.CONNECTION_DROPDOWN

            #For each location activate the menu item and then append the location to the menu object name
            for location in locationList:
                self.activateItem(dropdownObj, location)
                dropdownObj += '.' + location
                self.snooze(1)
                #If at the end of the list select to move to that location
                if location == locationList[len(locationList)-1]:
                    self.activateItem(dropdownObj, p_port1)        

        if not "/" in p_location2 and p_location2 == "":
            waitForObject(UtilConst.PHYSICAL_WORKSPACE)
            self.clickOnWorkspace(p_x2, p_y2)
            if p_connection != Connection.CONN_AUTO:
                self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN), p_port2)

        elif p_connection == Connection.CONN_AUTO:
            print "Auto-Connection Can Not Be Used When 2 Devices Are Not In The Same Location."
            return
            
        else:                       
            locationList = p_location2.split("/")
            print locationList

            self.clickOnWorkspace(p_x2, p_y2)
            dropdownObj = GoldenPhysicalToolbarConst.CONNECTION_DROPDOWN
            #For each location activate the menu item and then append the location to the menu object name
            for location in locationList:
                self.activateItem(dropdownObj, location)
                dropdownObj += '.' + location
                self.snooze(1)
                #If at the end of the list select to move to that location
                if location == locationList[len(locationList)-1]:
                    self.activateItem(dropdownObj, p_port2)  
    
    #@summary: ungroup cables in physical workspace 
    #@param p_x: x coordinate of the group point
    #@param p_y: y coordinate of the group point
    #@param p_firstEnd: first end of the cable, like: PC1/FastEthernet0
    #@param p_firstEnd: first end of the cable, like: Switch1/FastEthernet0/1
    #@param p_i: it is bc menu object name changes everytime and it's added by 1 #bug17017
    def ungroupCables(self, p_x, p_y, p_firstEnd, p_secondEnd, p_i):
        ungroupMenu = GoldenPhysicalToolbarConst.UNGROUPING_MENU
        self.clickButton(CommonToolsBarConst.DELETE_TOOL)
        self.clickOnPhysicalWorkspace(p_x, p_y)
        self.activateItem(ungroupMenu + p_i, "UnGroup Cable from " + p_firstEnd + " to " + p_secondEnd)
        self.clickButton(CommonToolsBarConst.SELECT_TOOL)
       
    #@summary: Connect two devices together on pka workspace
    #@param p_x1: x coordinate of the first device
    #@param p_y1: y coordinate of the first device
    #@param p_x2: x coordinate of the second device
    #@param p_y2: y coordinate of the second device
    #@param p_connection: type of cable
    #@param p_port: port name
    def connectOnPka(self, p_x1, p_y1, p_x2, p_y2, p_connection, p_port1, p_port2):
        self.componentBox.clickButton(DeviceGroup.CONNECTIONS)
        self.componentBox.clickButton(DeviceType.CONNECTION) 
        self.componentBox.clickButton(p_connection)
        self.clickOnWorkspace(p_x1, p_y1)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN_PKA), p_port1)
        self.clickOnWorkspace(p_x2, p_y2)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN_PKA), p_port2)

    #@summary: Connect two devices together on answer network workspace
    #@param p_x1: x coordinate of the first device
    #@param p_y1: y coordinate of the first device
    #@param p_x2: x coordinate of the second device
    #@param p_y2: y coordinate of the second device
    #@param p_connection: type of cable
    #@param p_port: port name
    def connectOnAnswerNetwork(self, p_x1, p_y1, p_x2, p_y2, p_connection, p_port1, p_port2):
        self.componentBox.clickButton(DeviceGroup.CONNECTIONS)
        self.componentBox.clickButton(DeviceType.CONNECTION)
        self.componentBox.clickButton(p_connection)
        self.clickOnWorkspace(p_x1, p_y1)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN_PKA), p_port1)
        self.clickOnWorkspace(p_x2, p_y2)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN_PKA), p_port2)
        
    #@summary: Connect two devices together on initial network workspace
    #@param p_x1: x coordinate of the first device
    #@param p_y1: y coordinate of the first device
    #@param p_x2: x coordinate of the second device
    #@param p_y2: y coordinate of the second device
    #@param p_connection: type of cable
    #@param p_port: port name
    def connectOnInitialNetwork(self, p_x1, p_y1, p_x2, p_y2, p_connection, p_port1, p_port2):
        self.componentBox.clickButton(DeviceGroup.CONNECTIONS)
        self.componentBox.clickButton(DeviceType.CONNECTION)
        self.componentBox.clickButton(p_connection)
        self.clickOnWorkspace(p_x1, p_y1)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN_PKA), p_port1)
        self.clickOnWorkspace(p_x2, p_y2)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(waitForObject(UtilConst.CONNECTION_DROPDOWN_PKA), p_port2)
            
    #@summary: Connect two devices together on initial network workspace
    #@param p_x1: x coordinate of the first device
    #@param p_y1: y coordinate of the first device
    #@param p_x2: x coordinate of the second device
    #@param p_y2: y coordinate of the second device
    #@param p_connection: type of cable
    #@param p_port: port name
    def connectOnPktPka(self, p_x1, p_y1, p_x2, p_y2, p_connection, p_port1, p_port2):
        self.componentBox.clickButton(DeviceGroup.CONNECTIONS)
        self.componentBox.clickButton(DeviceType.CONNECTION)     
        self.componentBox.clickButton(p_connection)
        self.clickOnWorkspace(p_x1, p_y1)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(UtilConst.CONNECTION_DROPDOWN_PKT_PKA, p_port1)
        self.clickOnWorkspace(p_x2, p_y2)
        if p_connection != Connection.CONN_AUTO:
            self.activateItem(UtilConst.CONNECTION_DROPDOWN_PKT_PKA, p_port2)
            
    #@summary: get the current name of the object that squish uses
    #p_squishName: display name of object
    def getCurrentDeviceName(self, p_displayName):
        self.snooze(.2)
        print "p_displayName- :" + p_displayName
        if not self.checkObjectExist(":" + p_displayName):
            print "getCurrentDeviceName- :CBaseDeviceWidget"
            return ":CBaseDeviceWidgetClass"
        else:
            print "getCurrentDeviceName- :" + p_displayName
            return ":" + p_displayName
        
    #@summary: pass in the text for the console window
    #@param p_obj: name of the console
    #@param p_text: text to be typed in to console
    def setConsoleText(self , p_obj, p_text):
        self.typeText(p_obj, p_text)
        self.typeText(p_obj, "\r")

    #@summary: click on simulation tab and realtime tab to speed up convergence
    def speedUpConvergence(self):
        self.fastForwardTime()
        self.fastForwardTime()
        self.fastForwardTime()
        self.fastForwardTime()
        self.fastForwardTime()
        
    #@summary: check to see if an object exist
    #@param p_squishName: the name of the object that squish references
    def checkObjectExist(self, p_squishName):
        if object.exists(p_squishName):
            return True
        else:
            return False
        
    #@summary: check to see if an object doesnt exist
    #@param p_squishName: the name of the object that squish references
    def checkObjectNotExist(self, p_squishName):
        if object.exists(p_squishName):
            return False
        else:
            return True
        
    #@summary: Deselects all objects on the workspace
    def deselectObjectsOnWorkspace(self):
        self.clickOnWorkspace(8, 45)

    #@summary: Shift selects the device at (x,y) on the workspace
    #@note: Use Util.deselectObjectsOnWorkspace() first to make sure not to include unintended objects
    #@param p_obj: obj name
    #@param p_x: x1 coordinate
    #@param p_y: y1 coordinate
    def selectObjectsOnWorkspace(self, p_x, p_y):
        currentWorkspace = self.findWorkspace()
        self.selectObject(currentWorkspace, p_x, p_y)
    
    def getObjectText(self, obj, **kwargs):
        if getType(obj) == getType('str'):
            waitFor("object.exists('" + obj + "')", 2000)
            self.clearCache(obj)
            widget = findObject(obj)
        else:
            widget = obj
        properties = object.properties(widget)
        
        if 'textProperty' in kwargs:
            return str(getattr(widget, kwargs['textProperty']))#Allow the calling function to specify which text it wants
        if 'text' in properties:
            consoleText = str(widget.text)
        elif 'plainText' in properties:
            consoleText = str(widget.plainText)
        elif 'innerText' in properties:
            consoleText = str(widget.innerText)
        elif 'currentText' in properties:
            consoleText = str(widget.currentText)
        elif 'simplifiedInnerText' in properties:
            consoleText = str(widget.simplifiedInnerText)
        elif 'currentText' in properties:
            consoleText = str(widget.currentText)
        return consoleText

    #@summary: check text
    #@param p_obj: obj name  
    #@param p_searchText: text to be checked
    #@param p_occurrenceNum: number of times text is expected to appear 
    # if not set, textCheckPoint will only check if the text is found
    #@param args: See sliceConsoleText function for examples and explanation
    #@param args: escape argument is used to call re.escape on the string to remove all regex patters
    def textCheckPoint(self, p_obj, p_searchText, p_occurrenceNum = -1, **args):
        consoleText = self.getObjectText(p_obj, **args)
        return self.checkText(consoleText, p_searchText, p_occurrenceNum, **args)
        
    def checkText(self, text, searchText, occurrence = -1, **args):
        if len(args.keys()) > 0:
            if 'escape' in args:
                if args['escape']:
                    searchText = escapeRegex(searchText)
                
        consoleText = self.sliceConsoleText(text, **args)
    
        if len(searchText) == 0 and not len(consoleText) == 0:
            test.fail('Failed ', 'Empty text was not found')
            self.getLineNumForTextCheckPoint()
            return False
        if (occurrence == -1):
            if (re.search(searchText, consoleText)):
                test.passes("Passed", searchText + " found" + '\n' + trace('test.py'))   
                return True            
            else:
                test.fail("Failed", searchText + " was not found")
                self.getLineNumForTextCheckPoint()
                return False
        else:      
            print re.findall(searchText, consoleText)      
            if len(re.findall(searchText, consoleText)) == occurrence:
                test.passes("Passed", searchText + " found " + str(occurrence) + " times")
                return True                 
            else:
                test.fail("Failed", searchText + " was not found")
                self.getLineNumForTextCheckPoint()
                return False

    def maximizePT(self):
        self.maximizeWindow(":CAppWindowBase")
    
    def restorePT(self):
        self.restoreWindow(":CAppWindowBase")
        
    def minimizePT(self):
        self.minimizeWindow(":CAppWindowBase")
        
    def fastForwardTime(self):
        self.clickButton(GoldenRealtimeToolbarConst.FAST_FORWARD_TIME)

    #@summary: Click on physical workspace
    #@param p_x: x coordinate
    #@param p_y: y coordinate
    #@param p_obj: from intercity clicking on home city or for devices in racks and on tables
    def clickOnPhysicalWorkspace(self, p_x, p_y, p_obj = ""):
        if p_obj == "":
            self.click_x_y(UtilConst.PHYSICAL_WORKSPACE, p_x, p_y)
        else:
            self.click(p_obj)   
            
    def plainTextCompare(self, p_obj, p_text):
        self.comparePlainText(p_obj, p_text)
        
    #@summary: click on workspace
    #@param p_x: x coordinate
    #@param p_y: y coordinate
    def clickOnPhysicalWorkspaceIcon2(self, p_x, p_y):
        self.click_x_y(UtilConst.ICON2_PHYSICAL_WORKSPACE, p_x, p_y)
        
    #@summary: click on simulation tab
    def clickOnSimulation(self):
        self.clickButton(UtilConst.SIMULATION_SWITCH)

    #@summary: click on realtime tab
    def clickOnRealtime(self):
        self.clickButton(UtilConst.REALTIME_SWITCH)

    #@summary: click on physical tab
    def clickOnPhysical(self):
        self.clickButton(UtilConst.PHYSICAL_SWITCH)

    #@summary: click on logical tab
    def clickOnLogical(self):
        self.clickButton(UtilConst.LOGICAL_SWITCH)
    
    def checkActivityCompletion(self, p_progress):    
        self.textCheckPoint(TestActivityConst.INSTRUCTION_BOX_PROGRESS_LABEL, p_progress)
    
    #@summary: Check for completion if the progress text is using alternate object name
    #@param p_percent: The percent completed expected either as a string or integer    
    def checkComplete(self, p_percent):
        for i in range(0, 32):
            if(i < 10):
                if(object.exists(":PT Activity: 00:00:0" + str(i) + ".progressLbl")):
                    self.textCheckPoint(":PT Activity: 00:00:0" + str(i) + ".progressLbl", "Completion: " + str(p_percent) + "%")
                    break
            elif(i < 30):
                if(object.exists(":PT Activity: 00:00:" + str(i) + ".progressLbl")):
                    self.textCheckPoint(":PT Activity: 00:00:" + str(i) + ".progressLbl", "Completion: " + str(p_percent) + "%")
                    break
            else:
                if(object.exists(TestActivityConst.INSTRUCTION_BOX_PROGRESS_LABEL)):
                    self.textCheckPoint(TestActivityConst.INSTRUCTION_BOX_PROGRESS_LABEL, "Completion: " + str(p_percent) + "%")
        
    #@summary: docks window (temporary fix since doubleClicking on window title bar does not work to dock windwos)
    def dockWindow(self, p_obj):
        obj = waitForObject(p_obj)
        self.nativeMouseClick(obj, 10, -15)
        self.nativeMouseClick(obj, 10, -15)

    def zoomOut(self):
        self.clickButton(MainToolbarConst.ZOOM_OUT)
        
    def userProfileClose(self):
        self.userProfile.closeAndConfirm()

    #@Summary: Used to be able to search only a specific area in consoletext
    #@params:
    #    lines: integer
    #        Number of lines to include starting at the end and going backwards.
    #        Example: lines = 10 would include the last 10 lines in p_consoleText
    #    chars: integer
    #        Number of previous characters to include in the search
    #        Example: chars = 100 would include the last 100 characters in p_consoleText
    #    string: string
    #        string to start at where it would include text from the last found instance of the string to the end
    #        Example: string = 'ping' would include from the last time ping appears in p_consoleText to the end of p_consoleText
    #    start: integer || string
    #        This can be an integer or string.
    #            If it is an integer it does the same as chars but the number is the starting index
    #            If it is a string it does the same as string but it will start from the first found instance of the string
    #    Stop: integer || string
    #        This is the same as start except telling the function where to stop. It finds the first occurrence after start
    #    Start/Stop
    #        Example:
    #            start = 0, stop = 100 would search the first 100 chars in the string
    #            start = 'ping', stop = 'Received = [1234]' would search from ping (inclusive) to the end of Received = [1234] (inclusive)
    def sliceConsoleText(self, p_consoleText, **args):
        if len(args.keys()) > 0:
            if 'lines' in args:
                temp = p_consoleText.splitlines()
                p_consoleText = '\n'.join(temp[-args['lines']:])
            elif 'chars' in args:
                p_consoleText = p_consoleText[-args['chars']:]
            elif 'string' in args:
                it = re.finditer(args['string'], p_consoleText)
                index = 0
                for match in it:
                    index = match.start()
                p_consoleText = p_consoleText[index:]
            elif 'start' in args:
                startIndex = 0
                stopIndex = len(p_consoleText)
                if isType(args['start'], 'int'):
                    startIndex = args['start']
                elif isType(args['start'], 'str'):
                    startIndex = re.search(args['start'], p_consoleText).start()
                else:
                    raise ValueError('Must be either an integer or string')
                if 'stop' in args:
                    if isType(args['stop'], 'int'):
                        stopIndex = args['stop']
                    elif isType(args['stop'], 'str'):
                        stopIndex = re.search(args['stop'], p_consoleText[startIndex:]).end()
                    else:
                        raise ValueError('Must be either an integer or string')
                p_consoleText = p_consoleText[startIndex:startIndex + stopIndex]
        return p_consoleText
               
    def getLineNumForTextCheckPoint(self):
        test.log(trace('test.py'))
        return trace('test.py')
        
    def getLineNum(self):
        callframe = inspect.stack()
        for stackItem in callframe:
            frame = stackItem[0]
            info = inspect.getframeinfo(frame)
            if("test.py" in str(info[0])):
                return "line " +  str(info[1]) + " of " + str(info[0])
            
    def containText(self, p_obj, p_searchText):
        self.clearCache(p_obj)
        consoleText = str(findObject(p_obj).text)
        if (re.search(p_searchText, consoleText)):    
            return True            
        else:
            return False
        
    def hasText(self, p_consoleText, p_searchText, p_occurrenceNum = -1):
        if len(p_searchText) == 0 and not len(p_consoleText) == 0:
            return False
        if (p_occurrenceNum == -1):
            if (re.search(p_searchText, p_consoleText)):
                return True            
            else:
                return False
        else:            
            if len(re.findall(p_searchText, p_consoleText)) == p_occurrenceNum:
                return True                 
            else:
                return False
            
    #@summary: delete the existing content and pass in the new text for the textField
    #@param p_obj: name of the textfield
    #@param p_text: text to be typed in to textfield 
    def setText(self , p_obj, p_text):
        self.clearCache(p_obj)
        self.click(p_obj)
        self.typeText(p_obj, "<Ctrl+a>")
        self.nativeType("<Ctrl+a>")
        self.typeText(p_obj, p_text)
    
    
    def checkboxState(self, checkbox):
        '''Return the checkstate of the checkbox in checked, unchecked, partiallyChecked format'''
        if getType(checkbox) == getType(''):
            checkbox = findObject(checkbox)#Get the object if a string was passed
        props = object.properties(checkbox)
        if 'checked' in props:
            if checkbox.checked:
                return 'checked'
            else:
                return 'unchecked' 
        elif 'checkState' in props:
            return checkbox.checkState
        else:
            raise AttributeError('Checkbox does not have a "checked" or "checkState" attribute.')
        
    def checkbox(self, checkbox, checked):
        '''Toggle a checkbox or set the state of a checkbox
        checkbox: String || Object (Object or object name of the checkbox)
        checked: None || Bool (None for toggle, True to check, false to uncheck)
        '''
        if getType(checkbox) == getType(''):
            checkbox = findObject(checkbox)#Get the object if a string was passed
        if checked == None:
            self.click(checkbox)
        elif checked == True:
            for i in range(3):
                if not self.checkboxState(checkbox) == 'checked':
                    self.click(checkbox)
        elif checked == False:
            for i in range(3):
                if not self.checkboxState(checkbox) == 'unchecked':
                    self.click(checkbox)
        else:
            raise ValueError('checked must be None, True, or False')
    
    def isChecked(self, checkbox, checked):
        if getType(checkbox) == getType(''):
            checkbox = findObject(checkbox)#Get the object if a string was passed
        check(checkbox.checked == checked, 'Check state is: %s and expected %s'%(checkbox.checked, checked))
        #if checkbox.checked == checked:
        #    test.passes('checked: %s'%(checked))
        #else:
        #    test.fail('checked: %s'%(checked))
    
    def checkProperty(self, obj, property, value=None, comparison='=='):
        if value==None:
            raise ValueError('The value keyword argument must be provided and must not be None')
        ops = {'>': operator.gt,
               '<': operator.lt,
               '>=': operator.ge,
               '<=': operator.le,
               '=': operator.eq,
               '==': operator.eq}
        if getType(obj) == getType(''):
            obj = findObject(obj)
        objValue = obj
        for prop in property.split('.'):#for multiple properties
            objValue = getattr(objValue, prop)
        check(ops[comparison](objValue, value), 'Property: %s, expected: %s, actual: %s, comparison:%s'%(property, value, objValue, comparison))
        
    def checkNoCrash(self):
        snooze(5)
        test.passes("PT did not crash")