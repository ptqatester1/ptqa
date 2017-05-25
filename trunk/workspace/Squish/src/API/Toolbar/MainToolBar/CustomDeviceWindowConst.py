#************************************************************************************************
#@author: Pam Vinco
#@summary: CustomDeviceWindowConst contains the common constants used in the Custom Device Window
#************************************************************************************************

class CheckBox:
    ROUTERS = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupRouters'
    SWITCHES = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupSwitches'
    HUBS = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupHubs'
    WIRELESS_DEVICES = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupWirelessDevices'
    BOARDS = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupBoards'
    END_DEVICES = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupEndDevices'
    SECURITY = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupSecurity'
    WAN_EMULATION = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupWANEmulation'
    HOME = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupHome'
    SMART_CITY = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupSmartCity'
    INDUSTRIAL = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupIndustrial'
    POWER_GRID = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupPowerGrid'
    ACTUATORS = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupActuators'
    SENSORS = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupSensors'
    MISCELLANEOUS = ':CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupMiscellaneous'

class CustomDeviceWindowConst:
    checkboxes = CheckBox
    CANCEL_ADD_CUSTOM_DEVICE = ":CAppWindowBase.CBaseDeviceTemplateManager.m_CancelButton"
    CLOSE_CUSTOM_DEVICE = ".CBaseDeviceTemplateManager.m_CancelButton"
    ADD_CUSTOM_DEVICE = ":CAppWindowBase.CBaseDeviceTemplateManager.m_AddButton"
    CUSTOM_DEVICE_DESCRIPTION = ":CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_DescriptionEdit"
    REMOVE_CUSTOM_DEVICE = ":CAppWindowBase.CBaseDeviceTemplateManager.m_RemoveButton"
    UPDATE_BUTTON = ":CAppWindowBase.CBaseDeviceTemplateManager.m_MoveToButton"
    SELECT_CUSTOM_DEVICE = ":CAppWindowBase.CBaseDeviceTemplateManager.SelectBox.m_SelectButton"
    CUSTOM_DEVICE_WINDOW = ":CAppWindowBase.CBaseDeviceTemplateManager"
    CUSTOM_DEVICE_NAME = ":CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_DeviceCombo.QLineEdit1"
    CUSTOM_DEVICE_NAME_LIST = ":CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_DeviceCombo"
                              
    
    CHOOSE_A_SUB_GROUP_DIALOG = 'QMessageBox1'
    CHOOSE_A_SUB_GROUP_OK_BUTTON = ':QMessageBox1.qt_msgbox_buttonbox.OK'
    
    CHANGE_DEVICE_NAME_DIALOG = ":Do you want to change the Device Name?"
    CHANGE_DEVICE_NAME_DIALOG_LABEL = ":Do you want to change the Device Name?.qt_msgbox_label"
    CHANGE_DEVICE_NAME_DIALOG_NO = ":Do you want to change the Device Name?.qt_msgbox_buttonbox.No"
    CHANGE_DEVICE_NAME_DIALOG_YES = ":Do you want to change the Device Name?.qt_msgbox_buttonbox.Yes"
    
    OVERWRITE_FILE_DIALOG = ":Overwrite File?"
    OVERWRITE_FILE_DIALOG_LABEL = ":Overwrite File?.qt_msgbox_label"
    OVERWRITE_FILE_DIALOG_NO = ":Overwrite File?.qt_msgbox_buttonbox.No"
    OVERWRITE_FILE_DIALOG_YES = ":Overwrite File?.qt_msgbox_buttonbox.Yes"
    
    SAVE_REPLACE_EXISTING_NO = ":CAppWindowBase.CBaseDeviceTemplateManager.QFileDialog.Save File in Templates Folder.qt_msgbox_buttonbox.No"
    SAVE_REPLACE_EXISTING_YES = ":CAppWindowBase.CBaseDeviceTemplateManager.QFileDialog.Save File in Templates Folder.qt_msgbox_buttonbox.Yes"
    SAVE_REPLACE_EXISTING_DIALOG = ":CAppWindowBase.CBaseDeviceTemplateManager.QFileDialog.Save File in Templates Folder"
    
    SAVE_TEMPLATE_DIALOG_FILENAME = ":CAppWindowBase.CBaseDeviceTemplateManager.QFileDialog.fileNameEdit"
    SAVE_TEMPLATE_DIALOG_CANCEL = ":CAppWindowBase.CBaseDeviceTemplateManager.QFileDialog.buttonBox.Cancel"
                                  
    SAVE_TEMPLATE_DIALOG_OK =     ":CAppWindowBase.CBaseDeviceTemplateManager.QFileDialog.buttonBox.Save"
    SAVE_DIALOG = ':CAppWindowBase.CBaseDeviceTemplateManager.QFileDialog'
    
    SELECT_GROUPBOX = ":CAppWindowBase.CBaseDeviceTemplateManager.SelectBox"
    EDIT_GROUPBOX = ":CAppWindowBase.CBaseDeviceTemplateManager.Edit"
    MAIN_DIALOG = ":CAppWindowBase.CBaseDeviceTemplateManager"
    
    MISC_CHECKBOX = ":CAppWindowBase.CBaseDeviceTemplateManager.Edit.m_subGroupMiscellaneous"