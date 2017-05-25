#********************************************************************************
#@author: Pam Vinco
#@summary: CustomDeviceWindow handles functions found in the Custom Device Window
#********************************************************************************
from CustomDeviceWindowConst import CustomDeviceWindowConst
from API.SquishSyntax import SquishSyntax
from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Utility import UtilConst
from API.functions import getType
from API.Utility.Util import Util
from API import functions
from squish import *
import object
import test

import squish
squish

class PopupWarnings:
    def __init__(self):
        self.util = Util()
    
    @property
    def chooseASubGroupDialog(self):
        ''':QMessageBox1'''
        try:
            return findObject(CustomDeviceWindowConst.CHOOSE_A_SUB_GROUP_DIALOG)
        except LookupError, e:
            return False
        
    def chooseASubGroupOkButton(self):
        self.util.clickButton(CustomDeviceWindowConst.CHOOSE_A_SUB_GROUP_OK_BUTTON)
    
    @property
    def saveReplaceExistingDialog(self):
        ''':CAppWindowBase.CBaseDeviceTemplateManager.QFileDialog.Save File in Templates Folder'''
        try:
            return findObject(CustomDeviceWindowConst.SAVE_REPLACE_EXISTING_DIALOG)
        except LookupError, e:
            return False

    def saveReplaceExistingYesButton(self):
        self.util.clickButton(CustomDeviceWindowConst.SAVE_REPLACE_EXISTING_YES)
    
    def saveReplaceExistingNoButton(self):
        self.util.clickButton(CustomDeviceWindowConst.SAVE_REPLACE_EXISTING_NO)
    
    @property
    def changeDeviceNameDialog(self):
        ''':Do you want to change the Device Name?'''
        try:
            return findObject(CustomDeviceWindowConst.CHANGE_DEVICE_NAME_DIALOG)
        except LookupError, e:
            return False
    
    def changeDeviceNameYesButton(self):
        self.util.clickButton(CustomDeviceWindowConst.CHANGE_DEVICE_NAME_DIALOG_YES)
    
    def changeDeviceNameNoButton(self):
        self.util.clickButton(CustomDeviceWindowConst.CHANGE_DEVICE_NAME_DIALOG_NO)

    @property
    def overwriteFileDialog(self):
        ''':Overwrite File?'''
        try:
            return findObject(CustomDeviceWindowConst.OVERWRITE_FILE_DIALOG)
        except LookupError, e:
            return False

    def overwriteFileYesButton(self):
        self.util.clickButton(CustomDeviceWindowConst.OVERWRITE_FILE_DIALOG_YES)
    
    def overwriteFileNoButton(self):
        self.util.clickButton(CustomDeviceWindowConst.OVERWRITE_FILE_DIALOG_NO)
        
class FileDialog:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
    
    @property
    def fileDialog(self):
        try:
            return findObject(CustomDeviceWindowConst.SAVE_DIALOG)
        except LookupError, e:
            return False
    
    def filename(self, filename):
        self.util.setText(CustomDeviceWindowConst.SAVE_TEMPLATE_DIALOG_FILENAME, filename)
    
    def saveButton(self):
        self.util.clickButton(CustomDeviceWindowConst.SAVE_TEMPLATE_DIALOG_OK)
    
    def cancelButton(self):
        self.util.clickButton(CustomDeviceWindowConst.SAVE_TEMPLATE_DIALOG_CANCEL)
    
    def save(self, filename = None, newFilename = None):    
        '''
        filename - String (If None default filename will be used
        newFileName - String (If not None then it is assuming that the first filename existed already and was not meant to
                              be overwritten. When prompted to overwrite it will press no and then enter the new filename
        '''
        if filename:
            self.filename(filename)
        self.saveButton()
        if self.popups.saveReplaceExistingDialog:
            if newFilename:
                self.popups.saveReplaceExistingNoButton()
                self.save(newFilename)
            else:
                self.popups.saveReplaceExistingYesButton()

class CustomDeviceWindow:
    def __init__(self):
        self.util = Util()
        self.popups = PopupWarnings()
        self.fileDialog = FileDialog()
        None
    
    def selectButton(self):
        self.util.clickButton(CustomDeviceWindowConst.SELECT_CUSTOM_DEVICE)
    
    def selectTemplate(self, templateDevName):
        self.util.clickItem(CustomDeviceWindowConst.CUSTOM_DEVICE_NAME_LIST, templateDevName)
    
    def templateName(self, templateName):
        self.util.setText(CustomDeviceWindowConst.CUSTOM_DEVICE_NAME, templateName)
    
    def description(self, description):
        self.util.setText(CustomDeviceWindowConst.CUSTOM_DEVICE_DESCRIPTION, description)
    
    def categoryCheckbox(self, category, checked = None):
        '''
        category - String (Name of the category to check as written in PT)
        checked - None || Boolean (If None then it acts as a toggle otherwise
                                   it will check based off True or False
        '''
        checkbox = None
        editGroupbox = findObject(CustomDeviceWindowConst.EDIT_GROUPBOX)
        for item in object.children(editGroupbox):
            if 'checkable' in object.properties(item):
                if item.checkable:
                    if category in str(item.text):
                        checkbox = item
                        break
        if not checkbox:
            raise ValueError('Could not find checkbox: ' + category)
        if checked == None:
            self.util.click(checkbox)
        elif checked == True:
            if not checkbox.checked:
                self.util.click(checkbox)
        elif checked == False:
            if checkbox.checked:
                self.util.click(checkbox)
        
    def updateButton(self):
        self.util.clickButton(CustomDeviceWindowConst.UPDATE_BUTTON)
    
    def removeButton(self):
        self.util.clickButton(CustomDeviceWindowConst.REMOVE_CUSTOM_DEVICE)
    
    def addButton(self):
        self.util.clickButton(CustomDeviceWindowConst.ADD_CUSTOM_DEVICE)
    
    def cancelButton(self):
        self.util.clickButton(CustomDeviceWindowConst.CANCEL_ADD_CUSTOM_DEVICE)

    def removeDeviceTemplate(self, device, *moreDevices):
        devices = (device,) + moreDevices
        self.goToTemplateManager()
        for device in devices:
            self.selectTemplate(device)
            self.removeButton()
    
    @property
    def templateManagerWindow(self):
        '''If the template manager window is found and visible return the object otherwise return false'''
        try:
            window = findObject(CustomDeviceWindowConst.CUSTOM_DEVICE_WINDOW)
            if window.visible:
                return window
            else:
                return False
        except LookupError, e:
            return False
    
    def add(self, changeName = False, overwrite = True, filename = None, **kwargs):
        '''
        changeName - Boolean (If true the change name popup yes button will be clicked a newFilename will need to be provided via kwargs
        overwrite - Boolean (If true the overwrite popup yes button will be clicked
                             If False the overwrite popup no button will be clicked a newFilename will need to be provided via kwargs)
        filename - String (Filename to be entered)
        kwargs -
            newTemplateName - String(Template name if changeName is True)
            newFilename - String (Filename to be entered overwrite is False)
        '''
        if not 'newFileName' in kwargs:
            newFileName = None
        else:
            newFileName = kwargs['newFileName']
        if not 'newTemplateName' in kwargs:
            newTemplateName = None
        else:
            newTemplateName = kwargs['newTemplateName']
            
        self.addButton()
        if self.fileDialog.fileDialog:
            self.fileDialog.save(filename, newFileName)
        if self.popups.changeDeviceNameDialog:
            if changeName:
                if not newTemplateName:
                    raise ValueError('In order to change the template name the newTemplateName parameter must be passed')
                self.popups.changeDeviceNameYesButton()
                self.templateName(newTemplateName)
                self.add(changeName, overwrite, filename)
            else:
                self.popups.changeDeviceNameNoButton()
                if self.popups.overwriteFileDialog:
                    if overwrite:
                        self.popups.overwriteFileYesButton()
                        self.fileDialog.save(filename, newFileName)
                    else:
                        self.popups.overwriteFileNoButton()
        
                    
            
    def addTemplate(self, workspaceDevice, templateName, description, location, *morelocations, **kwargs):
        '''
        workspaceDevice - Object (Device object of the device on the workspace)
        templateName    - String (Name of the new template)
        description     - String (Description of the new template)
        location        - String (Location checkbox to be checked)
        moreLocations   - String (Optional parameters for more locations)
        kwargs:
            workspace   - String (Optional parameter to define which workspace the template device is on
            filename    - String (filename to attempt to save as)
            newFileName - String (Optional parameter to be passed to the add function if the file should not be overwritten)
            newTemplateName - String (Optional parameter to be passed to the add function if the template name should be changed)
        '''
        #Setup code for the add function
        if 'filename' in kwargs:
            filename = kwargs['filename']
        else:
            filename = None
        if 'newFileName' in kwargs:
            overwrite = False
            newFileName = kwargs['newFileName']
        else:
            overwrite = True
            newFileName = None
        if 'newTemplateName' in kwargs:
            changeName = True
            newTemplateName = kwargs['newTemplateName']
        else:
            changeName = False
            newTemplateName = None
        
        #Create a tuple containing all locations to be selected
        locations = (location,) +  morelocations
        
        #Go to device manager if not already there
        #Select the device to create a template from
        #Enter a template name and description
        #Check locations
        #Add according to the parameters passed to kwargs
        self.goToTemplateManager()
        self.selectButton()
        try:
            workspaceDevice.select()
        except AttributeError, e:
            self.util.clickOnWorkspace(workspaceDevice.x, workspaceDevice.y)
        self.templateName(templateName)
        self.description(description)
        self.checkLocations(*locations)
        self.add(changeName, overwrite, filename, newTemplateName=newTemplateName, newFileName=newFileName)
    
    def checkLocations(self, *p_locations):
        for location in p_locations:
            self.categoryCheckbox(location, True)
    
    def goToTemplateManager(self):
        if not self.templateManagerWindow:
            self.util.clickButton(MainToolbarConst.CUSTOM_DEVICES)
    
    @property
    def deviceListObjects(self):
        comboBox = findObject(CustomDeviceWindowConst.CUSTOM_DEVICE_NAME_LIST)
        itemCount = comboBox.count
        devList = []
        for i in range(itemCount):
            devList.append(findObject(CustomDeviceWindowConst.CUSTOM_DEVICE_NAME_LIST + '.item_' + str(i) + '/0'))
        return devList
    
    @property
    def deviceList(self):
        return [str(obj.text) for obj in self.deviceListObjects]
        
    def close(self):
        self.util.close(CustomDeviceWindowConst.CUSTOM_DEVICE_WINDOW)
        
    @property
    def MISC_CHECKBOX(self):
        return 'Miscellaneous'
    
    def cleanup(self, p_deviceName, *moreDevices):
        '''Remove a device after creating a template. To be called in the cleanup functions.
        Check if there are popups and close if there are.
        Call util.init() for new workspace.
        Remove the item from the templates.'''
        functions.Aut().killAut()
        functions.Aut().startAut()
        Util().init()
        templateDevices = self.deviceList
        for devName in (p_deviceName,) + moreDevices:
            if devName in templateDevices:
                self.removeDeviceTemplate(devName)
            else:
                test.log('%s was not found in the template list'%(devName,))
