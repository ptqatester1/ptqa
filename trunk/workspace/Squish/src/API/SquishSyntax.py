#*************************************************************
#@author: Thi Nguyen
#@summary: SquishSyntax includes syntax that is only understandable to Squish
#*************************************************************
import squish
from squish import *
import test
import inspect
import re
from API.functions import isType

class SquishSyntax(object):
    #@summary: click on button
    #@param p_obj: obj name
    def clickButton(self, p_obj):
        waitForObject(p_obj)
        self.clearCache(p_obj)
        clickButton(p_obj)

    #@summary: mouseClick on an object
    #@param p_obj: obj name    
    def click(self, p_obj):
        self.clearCache(p_obj)
        waitForObject(p_obj)
        mouseClick(p_obj, 10, 10, Qt.NoModifier, Qt.LeftButton)
    
    def clickLink(self, p_obj):
        snooze(1)
        self.clearCache(p_obj)
        waitForObject(p_obj)
        clickLink(p_obj)
        snooze(1)
        
    #@summary: mouseClick on an object from a list
    #@param p_obj: obj name    
    def clickList(self, p_obj, p_item):
        self.clearCache(p_obj)
        mouseClick(waitForObjectItem(p_obj, p_item), 22, 4, 0, Qt.LeftButton)

    #@summary: mouseClick on an object
    #@param p_obj: obj name    
    def click_right(self, p_obj):
        self.clearCache(p_obj)
        waitForObject(p_obj)
        mouseClick(p_obj, 10, 11, 1, Qt.RightButton)

    #@summary: mouseClick at a specific xy coordination on object
    #@param p_obj: obj name
    #@param p_x: x coordination
    #@param p_y: y coordination
    def click_x_y(self, p_obj, p_x, p_y):
        self.clearCache(p_obj)
        waitForObject(p_obj)
        mouseClick(p_obj, p_x, p_y, 1, Qt.LeftButton)

    #@summary: click on Item from a combo box dropdown
    #@param p_obj: obj name
    #@param p_item: item(string appear on PT) to be clicked
    def clickItem(self, p_obj, p_item):
        self.clearCache(p_obj)
        waitForObjectItem(p_obj, p_item)
        clickItem(p_obj, p_item, 3, 9, 1, Qt.LeftButton)

    #@summary: click on Item from a combo box dropdown
    #@param p_obj: obj name
    #@param p_item: item(string appear on PT) to be clicked
    #@param p_x: x coordination
    #@param p_y: y coordination
    def clickItem_x_y(self, p_obj, p_item, p_x, p_y):
        self.clearCache(p_obj)
        waitForObject(p_obj)
        clickItem(p_obj, p_item, p_x, p_y, 0, Qt.LeftButton)

    #@summary: click on a tab
    #@param p_obj: obj name  
    #@param p_tabName: tab name     
    def clickTab(self, p_obj, p_tabName):
        self.clearCache(p_obj)
        clickTab(waitForObject(p_obj), p_tabName)

    #@summary: type text
    #@param p_obj: obj name    
    #@param p_text: text to be typed
    def typeText(self, p_obj, p_text):
        waitForObject(p_obj)
        type(p_obj, p_text)

    #@summary: double click on an object
    #@param p_obj: obj name    
    def doubleClick(self, p_obj):
        self.clearCache(p_obj)
        waitForObject(p_obj)
        doubleClick(p_obj, 10, 10, 0, Qt.LeftButton)

    #@summary: double click on an item on a tree
    #@param p_obj: obj name  
    #@param p_item: item to be clicked
    def doubleClickItem(self, p_obj, p_item):  
        self.clearCache(p_obj)
        waitForObject(p_obj)
        doubleClickItem(p_obj, p_item, 100, 5, 0, Qt.LeftButton)
        
    #@summary: double click on an item on a tree
    #@param p_obj: obj name  
    #@param p_item: item to be clicked
    def doubleClickItem_x_y(self, p_obj, p_item, p_x, p_y):  
        self.clearCache(p_obj)
        waitForObject(p_obj)
        doubleClickItem(p_obj, p_item, p_x, p_y, 0, Qt.LeftButton)


    def doubleClick_x_y(self, p_obj, p_x, p_y):  
        self.clearCache(p_obj)
        waitForObject(p_obj)
        doubleClick(p_obj, p_x, p_y, 0, Qt.LeftButton)
        
    #@summary: activate an item from a menu listview
    #@param p_obj: obj name  
    #@param p_item: item name
    def activateItem(self, p_obj, p_item):
        waitForObjectItem(p_obj, p_item)
        squish.activateItem(p_obj, p_item)
            
    #@summary: close an object
    #@param p_obj: obj name               
    def close(self, p_objName):
        waitForObject(p_objName)
        sendEvent("QCloseEvent", p_objName)

    #@summary: close an object
    #@param p_obj: obj name               
    def move(self, p_objName, p_x1, p_y1, p_x2, p_y2):
        waitForObject(p_objName)
        sendEvent("QMoveEvent", p_objName, p_x1, p_y1, p_x2, p_y2)
        
    #@summary: hide an object
    #@param p_obj: obj name               
    def hide(self, p_objName):
        waitForObject(p_objName)
        sendEvent("QHideEvent", p_objName)
        
    def nativeType(self, p_text):
        nativeType( p_text)
        
    def nativeMouseClick(self, p_obj, p_x, p_y):
        nativeMouseClick(p_obj, p_x, p_y, 0, Qt.LeftButton)
        
    def scrollTo(self, p_obj, p_value):
        waitForObject(p_obj)
        scrollTo(p_obj, p_value)

    #@summary: Shift selects an object at (x,y) on p_obj
    #@note: Use Util.deselectObjectsOnWorkspace() first to make sure not to include unintended objects
    #@param p_obj: obj name
    #@param p_x: x coordinate
    #@param p_y: y coordinate
    def selectObject(self, p_obj, p_x, p_y):
        waitForObject(p_obj)
        type(p_obj, "<Shift>")
        waitForObject(p_obj)
        mouseClick(p_obj, p_x, p_y, 33554433, Qt.LeftButton)
    
    def attachPT(self, AttachedPT):
        if(AttachedPT):
            attachToApplication("PacketTracer")
    
    def dragAndDrop(self, from_obj, from_x, from_y, to_obj, to_x = 0, to_y = 0):
        self.mousePress(from_obj, from_x, from_y)
        waitForObject(from_obj)
        dragAndDrop(from_obj, from_x, from_y, to_obj, to_x, to_y, Qt.MoveAction)

    def mouseDrag(self, p_obj, from_x, from_y, to_x, to_y):
        try:
            waitForObject(p_obj)
        except TypeError, e:
            pass
        mouseDrag(p_obj, from_x, from_y, to_x, to_y, 1, Qt.LeftButton)
    
    def mouseDragAltButton(self, from_obj, from_x, from_y, to_x, to_y, p_time = 0.5):
        '''Example: util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x - 10, pot.y - 10, pot.x + 10, pot.y + 10, 5)'''
        self.mousePressAltButton(from_obj, from_x, from_y)
        snooze(p_time)
        self.mouseMove(from_obj, to_x, to_y)
        snooze(p_time)
        self.mouseReleaseAltButton(from_obj, to_x, to_y)
        
    def mouseDragCtrlButton(self, from_obj, from_x, from_y, to_x, to_y, p_time = 0.5):
        '''Example: util.mouseDragAltButton(UtilConst.WORKSPACE, pot.x - 10, pot.y - 10, pot.x + 10, pot.y + 10, 5)'''
        self.mousePressCtrlButton(from_obj, from_x, from_y)
        snooze(p_time)
        self.mouseMove(from_obj, to_x, to_y)
        snooze(p_time)
        self.mouseReleaseCtrlButton(from_obj, to_x, to_y)
        
    def dragItemBy(self, p_obj, from_x, from_y, to_x, to_y):
        self.clearCache(p_obj)
        waitForObject(p_obj)
        dragItemBy(p_obj, from_x, from_y, to_x, to_y, 1, Qt.LeftButton)

    def press_releaseMouseEvent(self, p_obj, p_x, p_y):
        waitForObject(p_obj)
        sendEvent("QMouseEvent", p_obj, QEvent.MouseButtonPress, p_x, p_y, Qt.LeftButton, 0)
        waitForObject(p_obj)
        sendEvent("QMouseEvent", p_obj, QEvent.MouseButtonRelease, p_x, p_y, Qt.LeftButton, 1)
        
    def mousePress(self, p_obj, p_x, p_y):
        waitForObject(p_obj)
        sendEvent("QMouseEvent", p_obj, QEvent.MouseButtonPress, p_x, p_y, Qt.LeftButton, 0)
        
    def mousePressAltButton(self, p_obj, p_x, p_y):
        obj = findObject(p_obj)
        mousePress(obj, p_x, p_y, MouseButton.LeftButton, Modifier.Alt)

    def mousePressCtrlButton(self, p_obj, p_x, p_y):
        obj = findObject(p_obj)
        mousePress(obj, p_x, p_y, MouseButton.LeftButton, Modifier.Control)
    
    def mouseReleaseCtrlButton(self, p_obj, p_x, p_y):
        obj = findObject(p_obj)
        mouseRelease(obj, p_x, p_y, MouseButton.LeftButton, Modifier.Control)
            
    def mouseReleaseAltButton(self, p_obj, p_x, p_y):
        obj = findObject(p_obj)
        mouseRelease(obj, p_x, p_y, MouseButton.LeftButton, Modifier.Alt)

    def mouseRelease(self, p_obj, p_x, p_y):
        waitForObject(p_obj)
        sendEvent("QMouseEvent", p_obj, QEvent.MouseButtonRelease, p_x, p_y, Qt.LeftButton, 1)
        
    def mouseMove(self, p_obj, p_x, p_y):
        waitForObject(p_obj)
        mouseMove(p_obj, p_x, p_y)
        
    def openContextMenu(self, p_obj, p_x, p_y):
        waitForObject(p_obj)
        openContextMenu(p_obj, p_x, p_y, 0)
        
    def keyPress(self, p_obj, p_key):
        waitForObject(p_obj)
        sendEvent("QKeyEvent", p_obj, QEvent.KeyPress, 16777220, 13, 0, p_key, False, 1)

    def sendEvent(self, p_obj, p_event):
        sendEvent(p_event, p_obj)
        
    def comparePlainText(self, p_obj, p_text):
        test.compare(findObject(p_obj).plainText, p_text)
        
    def compareText(self, p_obj, p_text):
        self.clearCache(p_obj)
        test.compare(findObject(p_obj).text, p_text)
        
    def resizeWindow(self, p_obj, p_x1, p_y1, p_x2, p_y2):
        waitForObject(p_obj)
        sendEvent("QResizeEvent", p_obj, p_x1, p_y1, p_x2, p_y2)
        
    def minimizeWindow(self, p_obj):
        waitForObject(p_obj)
        setWindowState(waitForObject(p_obj), WindowState.Minimize)

    def maximizeWindow(self, p_obj):
        waitForObject(p_obj)
        setWindowState(waitForObject(p_obj), WindowState.Maximize)
        
    def restoreWindow(self, p_obj):
        waitForObject(p_obj)
        setWindowState(waitForObject(p_obj), WindowState.Normal)
        
    def selectOption(self, p_obj, p_item):
        selectOption(p_obj, p_item)
        
    def snooze(self, p_time):
        snooze(p_time)
        
    #@summary: delete the existing content and pass in the new text for the textField
    #@param p_obj: name of the textfield
    #@param p_text: text to be typed in to textfield 
    def setText(self , p_obj, p_text):
        self.clearCache(p_obj)
        self.click(p_obj)
        self.typeText(p_obj, "<Ctrl+a>")
        self.nativeType("<Ctrl+a>")
        self.typeText(p_obj, p_text)
        
    def clearCache(self, p_obj = None):
        webview = p_obj
        if not isType(webview, 'Object'):
            if '.DOCUMENT' in webview:
                l = webview.split('.')
                webview = '.'.join(l[:l.index('DOCUMENT')])
            try:
                findObject(webview).clearObjectCache()
            except AttributeError, e:
                pass
        else:
            try:
                webview.clearObjectCache()
            except AttributeError, e:
                pass