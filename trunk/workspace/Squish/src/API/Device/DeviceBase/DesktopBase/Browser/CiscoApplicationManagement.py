from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Utility.Util import Util
from squish import *

class CiscoApplicationManagement(DeviceBase): 
    def __init__(self, p_squishName):
        self.squishName = p_squishName
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName
        
    def login(self, p_user, p_pass):
        Util().setText(self.objName(DesktopConst.webbrowser.CiscoApplicationManagementPage.USERNAME), p_user)
        Util().setText(self.objName(DesktopConst.webbrowser.CiscoApplicationManagementPage.PASSWORD), p_pass)
        Util().click(self.objName(DesktopConst.webbrowser.CiscoApplicationManagementPage.LOGIN_BUTTON))
        
    def addDeploy(self, p_appID, p_projectName):
        snooze(5)
        Util().click(self.objName(DesktopConst.webbrowser.CiscoApplicationManagementPage.Applications.ADD_DEPLOY_BUTTON))
        snooze(1)
        Util().setText(self.objName(DesktopConst.webbrowser.CiscoApplicationManagementPage.Applications.DeployApplication.APPLICATION_ID), p_appID)
        #Click Choose File Button
        Util().click_x_y(self.objName(DesktopConst.webbrowser.CiscoApplicationManagementPage.MAIN_WEB_VIEW), 325, 205)
        snooze(1)
        Util().clickItem(self.objName(DesktopConst.webbrowser.CiscoApplicationManagementPage.Applications.DeployApplication.ProjectName.PROJECT_LIST), p_projectName)
        
        Util().clickButton(self.objName(DesktopConst.webbrowser.CiscoApplicationManagementPage.Applications.DeployApplication.ProjectName.OPEN_BUTTON))
        Util().click(self.objName(DesktopConst.webbrowser.CiscoApplicationManagementPage.Applications.DeployApplication.OK_BUTTON))
        snooze(5)#Wait for the instance to be added before moving forward
        
    def clearBrowserCache(self):
        obj = self.squishName + DesktopConst.webbrowser.MAIN_WEB_VIEW
        Util().clearCache(obj)