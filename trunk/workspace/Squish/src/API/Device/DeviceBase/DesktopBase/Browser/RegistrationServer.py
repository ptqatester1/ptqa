from API.Device_Old.DeviceBase import DeviceBase
from API.Utility.Util import Util
from API.SquishSyntax import SquishSyntax
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import WebBrowser
from API.functions import WebviewTagFind2 as TF
from squish import *
import object
import test

deviceBase = DeviceBase('')
squishname = ''

def customInteractions(func):
    def waitForPage(*args, **kwargs):
        for i in range(20):
            if waitForObject(squishname + WebBrowser.RegistrationServer.MAIN_WEB_VIEW).evalJS("document.readyState") == "complete":
                deviceBase.clearCache(squishname + WebBrowser.RegistrationServer.MAIN_WEB_VIEW)
                return func(*args, **kwargs)
            snooze(1)
            
    return waitForPage

class RegistrationServer:
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        self.setText = customInteractions(deviceBase.setText)
        self.click = customInteractions(deviceBase.click)
        self.clickButton = customInteractions(deviceBase.clickButton)
        self.clickLink = customInteractions(deviceBase.clickLink)
        self.selectOption = customInteractions(deviceBase.selectOption)
        self.loginPage = LoginPage(p_squishName)
        self.signUpPage = SignUpPage(p_squishName)
        self.homePage = HomePage(p_squishName)       
        self.conditionsPage = ConditionsPage(p_squishName)
        self.editorPage = EditorPage(p_squishName)
        self.addRule = AddRule(p_squishName)
#        self.configurePage = ConfigurePage(p_squishName)
#        self.configureActionPage = ConfigureActionPage(p_squishName)
        self.util = Util()
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName
        self.loginPage.updateName(p_squishName)
        self.signUpPage.updateName(p_squishName)
        self.homePage.updateName(p_squishName)
        self.conditionsPage.updateName(p_squishName)
        self.editorPage.updateName(p_squishName)
        self.addRule.updateName(p_squishName)        
#        self.configurePage.updateName(p_squishName)
#        self.configureActionPage.updateName(p_squishName)
        deviceBase.updateName(p_squishName)
        global squishname
        squishname = self.squishName
        #test.log(self.squishName + ' from update function')
        #test.log(self.loginPage.squishName + ' loging')
        #test.log(self.signUpPage.squishName + ' signup')
        #test.log(self.homePage.squishName + ' home')
        #test.log(self.configureActionPage.squishName + ' configureaction')
        #test.log(self.configurePage.squishName + ' configure')
        #test.log(deviceBase.squishName + ' deviceBase')
        
    def textCheckPoint(self, p_searchText, p_occurrenceNum = -1):
        self.util.textCheckPoint(self.squishName + WebBrowser.RegistrationServer.MAIN_HTML_BODY, p_searchText, p_occurrenceNum)

class LoginPage:
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        self.setText = customInteractions(deviceBase.setText)
        self.click = customInteractions(deviceBase.click)
        self.clickLink = customInteractions(deviceBase.clickLink)
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName

    def editUsername(self, p_username):
        self.setText(WebBrowser.RegistrationServer.USERNAME, p_username)
    
    def editPasswrod(self, p_password):
        self.setText(WebBrowser.RegistrationServer.PASSWORD, p_password)
    
    def signInButton(self):
        self.click(WebBrowser.RegistrationServer.SIGN_IN_BUTTON)
        
    @customInteractions
    def signIn(self, p_username, p_password):
        self.editUsername(p_username)
        self.editPasswrod(p_password)
        self.signInButton()
    
    def signUpLink(self):
        self.clickLink(WebBrowser.RegistrationServer.SIGN_UP_LINK)
        
class SignUpPage:
    '''Same as the login page but with different naming'''
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        login = LoginPage(p_squishName)
        self.setText = customInteractions(deviceBase.setText)
        self.click = customInteractions(deviceBase.click)
        self.clickLink = customInteractions(deviceBase.clickLink)
        self.signUp = login.signIn
        self.editUsername = login.editUsername
        self.editPassword = login.editPasswrod
        self.createButton = login.signInButton

    def updateName(self, p_squishName):
        self.squishName = p_squishName
    
class HomePage:
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        self.setText = customInteractions(deviceBase.setText)
        self.clickLink = customInteractions(deviceBase.clickLink)
        self.click = customInteractions(deviceBase.click)
        self.clickButton = customInteractions(deviceBase.clickButton)
        self.textCheckPoint = customInteractions(deviceBase.textCheckPoint)
        self.util = Util()

    def updateName(self, p_squishName):
        self.squishName = p_squishName
    
    def conditionsLink(self):
        self.clickLink(WebBrowser.RegistrationServer.CONDITIONS_LINK)
    
    def editorLink(self):
        self.clickLink(WebBrowser.RegistrationServer.EDITOR_LINK)
        
    def logoutLink(self):
        self.clickLink(WebBrowser.RegistrationServer.LOGOUT_LINK)
#from API.Device_Old.EndDevice.PC.Desktop.Browser.RegistrationServer import *
    @customInteractions
    def getListObject(self):
        snooze(1)
        deviceList = TF().findTagWithID(self.squishName + WebBrowser.RegistrationServer.MAIN_HTML_BODY, 'devicesDiv')
        return deviceList
    
    @customInteractions
    def getListItemObject(self, p_itemName):
        deviceList = self.getListObject()
        for item in object.children(deviceList):
            if p_itemName == str(item.innerText).split()[0]:
                return item
        raise ValueError('Unable to find ' + p_itemName)
    
    
    @customInteractions
    def getListItemHeaderObject(self, p_itemName):
        listItem = self.getListItemObject(p_itemName)
        header = object.children(listItem)[0]
        return header
    
    def getButtonOrValueObject(self, p_itemName, objectLineNumber = 1, buttonNumber = 1):
        #objectLineNumber is used if there is more than one thing listed
        #in the device. An example would be the CO detector. It has alarm and level
        #so in order to check the level use 2 instead of default 1
        listItem = self.getListItemObject(p_itemName)
        item = object.children(listItem)
        header, div = item[0], item[1]
        subDiv = object.children(div)[objectLineNumber - 1]
        subDivChildren = object.children(subDiv)
        statusSpan, buttonSpan = subDivChildren[0], subDivChildren[1]
        button = object.children(buttonSpan)[buttonNumber - 1]
        return button
    
    def toggleButton(self, p_itemName):
        button = self.getButtonOrValueObject(p_itemName)
        snooze(1)
        self.util.click(button)
        snooze(1)
    
    @customInteractions
    def expandItem(self, p_itemName):
        item = self.getListItemHeaderObject(p_itemName)
        self.util.click(item)        
    
class ConditionsPage:
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        self.setText = customInteractions(deviceBase.setText)
        self.click = customInteractions(deviceBase.click)
        self.clickLink = customInteractions(deviceBase.clickLink)
        self.textCheckPoint = customInteractions(deviceBase.textCheckPoint)
        self.selectOption = customInteractions(deviceBase.selectOption)
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName
                
    def homeLink(self):
        self.clickLink(WebBrowser.RegistrationServer.ConditionsPage.HOME_LINK)
        
    def editorLink(self):
        self.clickLink(WebBrowser.RegistrationServer.ConditionsPage.EDITOR_LINK)
        
    def logoutLink(self):
        self.clickLink(WebBrowser.RegistrationServer.ConditionsPage.LOGOUT_LINK)
        
    def addRule(self, p_name, p_disable, p_ifName, p_ifState, p_ifValue, p_thenName, p_thenState, p_thenValue):
        self.addButton()
        self.editRule(p_name, p_disable, p_ifName, p_ifState, p_ifValue, p_thenName, p_thenState, p_thenValue)
        
    def addButton(self):
        self.click(WebBrowser.RegistrationServer.ConditionsPage.ADD_BUTTON)
        
    def editRule(self, p_name, p_disable, p_ifName, p_ifState, p_ifValue, p_thenName, p_thenState, p_thenValue):
        self.setText(WebBrowser.RegistrationServer.ConditionsPage.EditRule.NAME, p_name)
        if (p_disable != ""):
            self.click(WebBrowser.RegistrationServer.ConditionsPage.EditRule.ENABLED_CHECKBOX)
        self.selectOption(WebBrowser.RegistrationServer.ConditionsPage.EditRule.IF_NAME_DROPDOWN, p_ifName)
        snooze(1)
        self.selectOption(WebBrowser.RegistrationServer.ConditionsPage.EditRule.IF_STATE_DROPDOWN, p_ifState)
        snooze(1)
        self.selectOption(WebBrowser.RegistrationServer.ConditionsPage.EditRule.IF_VALUE_DROPDOWN, p_ifValue)
        snooze(2)
        self.selectOption(WebBrowser.RegistrationServer.ConditionsPage.EditRule.THEN_NAME_DROPDOWN, p_thenName)
        snooze(1)
        self.selectOption(WebBrowser.RegistrationServer.ConditionsPage.EditRule.THEN_STATE_DROPDOWN, p_thenState)
        snooze(1)
        self.selectOption(WebBrowser.RegistrationServer.ConditionsPage.EditRule.THEN_VALUE_DROPDOWN, p_thenValue)
        snooze(1)        
        self.click(WebBrowser.RegistrationServer.ConditionsPage.EditRule.OK_BUTTON)
        
    #@summary: Get table item returns the actual name of the cell being looked for
    #          This is used since the number of cells is dynamic and the names are
    #          dependent on the row/column numbers
    def getTableItem(self, p_row, p_column):
        rows = WebBrowser.RegistrationServer.ConfigurationPage.TABLE_ROW
        cols = WebBrowser.RegistrationServer.ConfigurationPage.TABLE_COLUMN
        cell = rows + str(p_row) + cols + str(p_column)
        return cell
    
    #@summary: This selects any amount of the delete check boxes
    #@param *p_row: Enter the number of the row of each check box to be selected
    #               Example: callingObject.selectDeleteCheckBox(1,3,4,6)
    #               In the example the checkboxes in rows 1, 3, 4, and 6 would be selected
    def selectDeleteCheckBox(self, *p_row):
        for row in p_row:
            self.click(self.getTableItem(row, 4))
    
    #@summary: This calls the selectDeleteCheckBox function and then presses the remove button.
    #@param *p_row: Same as *p_row for selectDeleteCheckBox
    def removeItems(self, *p_row):
        self.selectDeleteCheckBox(*p_row)
        self.removeButton()
    
    def checkTableRowText(self, p_row, p_description = None, p_condition = None, p_action = None, p_delete = None):
        '''iterate over all provided parameters and check the corresponding cell for the parameter text'''
        vals = dict(locals())
        if p_row == 1:
            tableColumnTag = WebBrowser.RegistrationServer.HomePage.TABLE_HEADER_COLUMN
        else:
            tableColumnTag = WebBrowser.RegistrationServer.HomePage.TABLE_COLUMN
        cells = {'p_description':1, 'p_condition':2, 'p_action':3, 'p_delete':4}
        None
        for key, val in vals.iteritems():
            if key == 'self' or val == None or key == 'p_row':
                continue
            snooze(1)
            self.textCheckPoint(self.squishName + WebBrowser.RegistrationServer.HomePage.TABLE_ROW + str(p_row) + tableColumnTag + str(cells[key]), val)
    
class EditorPage:
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        self.setText = customInteractions(deviceBase.setText)
        self.click = customInteractions(deviceBase.click)
        self.clickLink = customInteractions(deviceBase.clickLink)
        self.textCheckPoint = customInteractions(deviceBase.textCheckPoint)
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName
                
    def homeLink(self):
        self.clickLink(WebBrowser.RegistrationServer.EditorPage.HOME_LINK)
    
    def conditionsLink(self):
        self.clickLink(WebBrowser.RegistrationServer.EditorPage.CONDITIONS_LINK)
        
    def logoutLink(self):
        self.clickLink(WebBrowser.RegistrationServer.EditorPage.LOGOUT_LINK)
        

class AddRule:
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        self.setText = customInteractions(deviceBase.setText)
        self.click = customInteractions(deviceBase.click)
        self.clickLink = customInteractions(deviceBase.clickLink)
        self.textCheckPoint = customInteractions(deviceBase.textCheckPoint)
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName
        
    def nameEdit(self, p_name):
        nameEdit = TF().findTagWithID(self.squishName + WebBrowser.RegistrationServer.MAIN_WEB_VIEW, 'newName')
        self.setText(nameEdit, p_name)
        None
    
    def enabledCheckboxToggle(self):
        enabledCheckbox = TF().findTagWithID(self.squishName + WebBrowser.RegistrationServer.MAIN_WEB_VIEW, 'enabled')
        self.click(enabled)
        None
    
    @customInteractions
    def matchCombo(self, p_option):
        matchComboParent = TF().findTagWithID(self.squishName + WebBrowser.RegistrationServer.MAIN_WEB_VIEW, 'rootLogicalGroup')
        matchCombo = object.children(matchComboParent)[0]
        for i in range(matchCombo.numChildren):
            if matchCombo.optionAt(i).text == p_option:
                matchCombo.setSelectedIndex(i)
                break
        raise ValueError('Unable to find a device with the name of %s'%(p_option,))
        None
    
    def addConditionButton(self):
        raise NotImplementedError('Future')
    
    def addGroupButton(self):
        raise NotImplementedError('Future')
    
    @property
    def conditions(self):
        firstCondition = TF().findTagWithID(self.squishName + WebBrowser.RegistrationServer.MAIN_WEB_VIEW, '_condition')
        parent = object.parent(firstCondition)
        conditions = object.children(parent)
        return conditions
    
    @customInteractions
    def deviceSelectionCondition(self, row, deviceName):
        '''row number 0 indexed. Multiple groups not supported by this function.'''
        condition = self.conditions[row]
        deviceSelectionCombo = object.children(condition)[0]
        for i in range(deviceSelectionCombo.numChildren):
            if deviceSelectionCombo.optionAt(i).text == deviceName:
                deviceSelectionCombo.setSelectedIndex(i)
                return
        raise ValueError('Unable to find a device with the name of %s'%(deviceName,))
    
    @customInteractions
    def firstDeviceCondition(self, row, p_condition):
        '''row number 0 indexed. Multiple groups not supported by this function.'''
        condition = self.conditions[row]
        firstConditionCombo = object.children(condition)[1]
        for i in range(firstConditionCombo.numChildren):
            if firstConditionCombo.optionAt(i).text == p_condition:
                firstConditionCombo.setSelectedIndex(i)
                return
        raise ValueError('Unable to find a device with the name of %s'%(p_condition,))

    @customInteractions
    def secondDeviceCondition(self, row, p_condition):
        '''row number 0 indexed. Multiple groups not supported by this function.'''
        condition = self.conditions[row]
        span = object.children(condition)[2]
        childSpan = object.children(span)[0]
        secondConditionCombo = object.children(childSpan)[0]
        for i in range(secondConditionCombo.numChildren):
            if secondConditionCombo.optionAt(i).text == p_condition:
                secondConditionCombo.setSelectedIndex(i)
                return
        raise ValueError('Unable to find a device with the name of %s'%(p_condition,))
    
    @customInteractions
    def removeCondition(self, row):
        condition = self.conditions[row]
        removeButton = object.children(condition)[3]
        self.click(removeButton)
    
    @property
    @customInteractions
    def actions(self):
        firstAction = TF().findTagWithID(self.squishName + WebBrowser.RegistrationServer.MAIN_WEB_VIEW, 'actions')
        parent = object.parent(firstAction)
        actions = object.children(parent)
        return actions
    
    @customInteractions
    def deviceSelectionAction(self, row, deviceName):
        action = self.actions[row]
        deviceSelectionCombo = object.children(action)[0]
        for i in range(deviceSelectionCombo.numChildren):
            if deviceSelectionCombo.optionAt(i).text == deviceName:
                deviceSelectionCombo.setSelectedIndex(i)
                return
        raise ValueError('Unable to find a device with the name of %s'%(deviceName,))
    
    @customInteractions
    def firstDeviceAction(self, row, p_action):
        '''row number 0 indexed. Multiple groups not supported by this function.'''
        action = self.actions[row]
        firstActionCombo = object.children(action)[1]
        for i in range(firstActionCombo.numChildren):
            if firstActionCombo.optionAt(i).text == p_action:
                firstActionCombo.setSelectedIndex(i)
                return
        raise ValueError('Unable to find a device with the name of %s'%(p_action,))
    
    @customInteractions
    def secondDeviceCondition(self, row, p_action):
        '''row number 0 indexed. Multiple groups not supported by this function.'''
        action = self.actions[row]
        span = object.children(action)[2]
        childSpan = object.children(span)[0]
        secondActionCombo = object.children(childSpan)[0]
        for i in range(secondActionCombo.numChildren):
            if secondActionCombo.optionAt(i).text == p_action:
                secondActionCombo.setSelectedIndex(i)
                return
        raise ValueError('Unable to find a device with the name of %s'%(p_action,))
    
    @customInteractions
    def removeCondition(self, row):
        action = self.actions[row]
        removeButton = object.children(action)[3]
        self.click(removeButton)
    
    def okButton(self):
        raise NotImplementedError('Issue finding OK button')


class ConfigurePage:
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        self.setText = customInteractions(deviceBase.setText)
        self.click = customInteractions(deviceBase.click)
        self.clickLink = customInteractions(deviceBase.clickLink)
        self.textCheckPoint = customInteractions(deviceBase.textCheckPoint)
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName

    def homeLink(self):
        self.clickLink(WebBrowser.RegistrationServer.ConfigurationPage.HOME_LINK)
    
    def configureLink(self):
        self.clickLink(WebBrowser.RegistrationServer.ConfigurationPage.CONFIGURE_LINK)
    
    def logoutLink(self):
        self.clickLink(WebBrowser.RegistrationServer.ConfigurationPage.LOGOUT_LINK)
    
    def AddButton(self):
        self.click(WebBrowser.RegistrationServer.ConfigurationPage.ADD_BUTTON)
    
    def removeButton(self):
        self.click(WebBrowser.RegistrationServer.ConfigurationPage.REMOVE_BUTTON)
    
    def editLink(self):
        self.click(WebBrowser.RegistrationServer.ConfigurationPage.EDIT_LINK)
    
    #@summary: Get table item returns the actual name of the cell being looked for
    #          This is used since the number of cells is dynamic and the names are
    #          dependent on the row/column numbers
    def getTableItem(self, p_row, p_column):
        rows = WebBrowser.RegistrationServer.ConfigurationPage.TABLE_ROW
        cols = WebBrowser.RegistrationServer.ConfigurationPage.TABLE_COLUMN
        cell = rows + str(p_row) + cols + str(p_column)
        return cell
    
    #@summary: This selects any amount of the delete check boxes
    #@param *p_row: Enter the number of the row of each check box to be selected
    #               Example: callingObject.selectDeleteCheckBox(1,3,4,6)
    #               In the example the checkboxes in rows 1, 3, 4, and 6 would be selected
    def selectDeleteCheckBox(self, *p_row):
        for row in p_row:
            self.click(self.getTableItem(row, 4))
    
    #@summary: This calls the selectDeleteCheckBox function and then presses the remove button.
    #@param *p_row: Same as *p_row for selectDeleteCheckBox
    def removeItems(self, *p_row):
        self.selectDeleteCheckBox(*p_row)
        self.removeButton()
    
    def checkTableRowText(self, p_row, p_description = None, p_condition = None, p_action = None, p_delete = None):
        #iterate over all provided parameters and check the corresponding cell for the parameter text
        vals = dict(locals())
        if p_row == 1:
            tableColumnTag = WebBrowser.RegistrationServer.HomePage.TABLE_HEADER_COLUMN
        else:
            tableColumnTag = WebBrowser.RegistrationServer.HomePage.TABLE_COLUMN
        cells = {'p_description':1, 'p_condition':2, 'p_action':3, 'p_delete':4}
        None
        for key, val in vals.iteritems():
            if key == 'self' or val == None or key == 'p_row':
                continue
            snooze(1)
            self.textCheckPoint(self.squishName + WebBrowser.RegistrationServer.HomePage.TABLE_ROW + str(p_row) + tableColumnTag + str(cells[key]), val)
        
    
    
    
class ConfigureActionPage:
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        self.setText = customInteractions(deviceBase.setText)
        self.click = customInteractions(deviceBase.click)
        self.clickLink = customInteractions(deviceBase.clickLink)
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName
    
    def homeLink(self):
        self.clickLink(WebBrowser.RegistrationServer.ConfigureActionPage.HOME_LINK)
    
    def configureLink(self):
        self.clickLink(WebBrowser.RegistrationServer.ConfigureActionPage.CONFIGURE_LINK)
    
    def logoutLink(self):
        self.clickLink(WebBrowser.RegistrationServer.ConfigureActionPage.LOGOUT_LINK)
    
    def editDescription(self, p_description):
        self.setText(WebBrowser.RegistrationServer.ConfigureActionPage.DESCRIPTION_INPUT, p_description)
    
    @customInteractions
    def editCondition(self, p_condition):
        self.setText(WebBrowser.RegistrationServer.ConfigureActionPage.CONDITION_INPUT, p_condition)
    
    def editAction(self, p_action):
        self.setText(WebBrowser.RegistrationServer.ConfigureActionPage.ACTION_INPUT, p_action)
    
    def submitButton(self):
        self.click(WebBrowser.RegistrationServer.ConfigureActionPage.SUBMIT_BUTTON)
    
    def cancelButton(self):
        self.click(WebBrowser.RegistrationServer.ConfigureActionPage.CANCEL_BUTTON)
    
    @customInteractions
    def addCondition(self, p_description, p_condition, p_action, p_submit=True):
        self.editDescription(p_description)
        self.editCondition(p_condition)
        self.editAction(p_action)
        if p_submit:
            self.submitButton()
        else:
            self.cancelButton()
