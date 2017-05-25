##Chris Allen

from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Utility.Util import Util
from squish import *

class ConstantsHelper(SquishObjectName):
    def __init__(self):
        SquishObjectName.__init__(self)
    
    def replace_string_in_obj_name(self, string, string_to_replace, replacement_string):
        return string.replace(string_to_replace, replacement_string)
        
    def objName(self, obj):
        no_association_text = '.CPCBaseWirelessNoAssociation.frameNoAssociation.'
        association_text = '.CPCBaseWirelessAssociation.frameAssociation.'
        original_obj_name = ' '
        replacement_obj_name = ' '
        if no_association_text in obj:
            original_obj_name = no_association_text
            replacement_obj_name = association_text
        elif association_text in obj:
            original_obj_name = association_text
            replacement_obj_name = no_association_text
        
        object_name = SquishObjectName.objName(self, obj)
        try:
            foundObj = findObject(object_name)
            if foundObj.visible:
                return object_name
            else:
                return self.replace_string_in_obj_name(object_name, original_obj_name, replacement_obj_name)
        except LookupError, e:
            new_name = self.replace_string_in_obj_name(object_name, original_obj_name, replacement_obj_name)
            findObject(new_name)
            return new_name

class LinkInformationCheck(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def radioBand(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.RADIO_BAND), expected, **kwargs)
    
    def wirelessNetworkName(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.WIRELESS_NETWORK_NAME), expected, **kwargs)
    
    def wirelessMode(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.WIRELESS_MODE), expected, **kwargs)
    
    def wideChannel(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.WIDE_CHANNEL), expected, **kwargs)
    
    def standardChannel(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.STANDARD_CHANNEL), expected, **kwargs)
    
    def security(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.SECURITY), expected, **kwargs)
    
    def authentication(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.AUTHENTICATION), expected, **kwargs)
    
    def networkType(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.NETWORK_TYPE), expected, **kwargs)
    
    def ipAddress(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.IP_ADDRESS), expected, **kwargs)
    
    def subnetMask(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.SUBNET_MASK), expected, **kwargs)
    
    def defaultGateway(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.DEFAULT_GATEWAY), expected, **kwargs)
    
    def dns1(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.DNS1), expected, **kwargs)
    
    def macAddress(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.MAC_ADDRESS), expected, **kwargs)
        
    def transmitRate(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.TRANSMIT_RATE), expected, **kwargs)
    
    def receiveRate(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.linkInformationTab.networkStatus.RECEIVE_RATE), expected, **kwargs)

    
class LinkInformationTab(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
        self.check = LinkInformationCheck(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
        self.check.updateName(squishName)
    
    def moreInformationButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.linkInformationTab.MORE_INFO_BUTTON))
    
    def _clickButton(self, buttonList):
        for button in buttonList:
            try:
                if findObject(self.objName(button)).visible:
                    self.util.clickButton(self.objName(button))
                    return
            except LookupError, e:
                continue
        raise LookupError('Unable to find button')
    
    def backButton(self):
        buttons = [DesktopConst.pcwireless.linkInformationTab.BACK_BUTTON_STATS_PAGE,
                       DesktopConst.pcwireless.linkInformationTab.BACK_BUTTON_STATUS_PAGE]
        self._clickButton(buttons)

    def statisticsButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.linkInformationTab.STATISTICS_BUTTON))
    
    def statusButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.linkInformationTab.STATUS_BUTTON))
    
    def saveToProfileButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.linkInformationTab.SAVE_TO_PROFILE_BUTTON))
    
    def refreshButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.linkInformationTab.REFRESH_BUTTON))

class ConnectionSecurityWpa(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
        
    def security(self, security):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.connectTab.wpaPage.SECURITY_COMBO))
    
    def encryption(self, encryption):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.connectTab.wpaPage.ENCRYPTION_COMBO))
    
    def key(self, key):
        self.util.setText(self.objName(DesktopConst.pcwireless.connectTab.wpaPage.PRE_SHARED_KEY), key)
    
class ConnectionSecurityWpa2(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def security(self, security):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.connectTab.wpa2Page.SECURITY_COMBO))
    
    def key(self, key):
        self.util.setText(self.objName(DesktopConst.pcwireless.connectTab.wpa2Page.PRE_SHARED_KEY), key)

    def connectButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.connectTab.wpa2Page.CONNECT_BUTTON))
        
class ConnectionSecurityWep(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def security(self, security):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.connectTab.wepPage.SECURITY_COMBO))
    
    def key(self, key):
        self.util.setText(self.objName(DesktopConst.pcwireless.connectTab.wepPage.PRE_SHARED_KEY), key)
    
    def connectButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.connectTab.wepPage.CONNECT_BUTTON))
    
    def cancelButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.connectTab.wepPage.CANCEL_BUTTON))
    

class ConnectionSecurity(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
        self.wep = ConnectionSecurityWep(self)
        self.wpa = ConnectionSecurityWpa(self)
        self.wpa2 = ConnectionSecurityWpa2(self)
    
    def updateName(self, squishName):
        self.squishName = squishName
        self.wep.updateName(squishName)
        self.wpa.updateName(squishName)
        self.wpa2.updateName(squishName)
    
class ConnectTab(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
        self.security = ConnectionSecurity(self)
        self.check = ConnectTabCheck(self)
    
    def updateName(self, squishName):
        self.squishName = squishName
        self.security.updateName(squishName)
        self.check.updateName(squishName)
    
    @property
    def networkTableName(self):
        return self.objName(DesktopConst.pcwireless.connectTab.NETWORK_TABLE)
    
    @property
    def networkTable(self):
        return findObject(self.networkTableName)
    
    def refreshButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.connectTab.REFRESH_BUTTON))
    
    def connectButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.connectTab.CONNECT_BUTTON))
    
    def selectNetwork(self, ssid):
        for i in range(self.networkTable.rowCount):
            currentNet = findObject(self.networkTableName + '.item_%s/0'%(i,))
            if currentNet.text == ssid:
                self.util.click(currentNet)
                return
            
class ConnectTabCheck(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def wirelessMode(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.connectTab.siteInformation.WIRELESS_MODE), expected, **kwargs)
    
    def siteNetworkType(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.connectTab.siteInformation.NETWORK_TYPE), expected, **kwargs)
        
    def siteRadioBand(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.connectTab.siteInformation.RADIO_BAND), expected, **kwargs)
        
    def security(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.connectTab.siteInformation.SECURITY), expected, **kwargs)
        
    def macAddress(self, expected, **kwargs):
        self.util.textCheckPoint(self.objName(DesktopConst.pcwireless.connectTab.siteInformation.MAC_ADDRESS), expected, **kwargs)
        
class ProfileNewDailog(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def profileName(self, name):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.newDialog.PROFILE_NAME_EDIT), name)
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.newDialog.OK_BUTTON))
    
    def setName(self, name):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.newDialog.PROFILE_NAME_EDIT), name)
    
    def okButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.newDialog.OK_BUTTON))
    
    def cancelButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.newDialog.CANCEL_BUTTON))

class ProfileSetupWirelessMode(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def infrastructureMode(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wirelessModePage.INFRASTRUCTURE_RADIO))

    def adhocMode(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wirelessModePage.ADHOC_MODE_RADIO))
    
    def networkName(self, ssid):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.wirelessModePage.WIRELESS_NETWORK_NAME_EDIT), ssid)
    
    def backButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wirelessModePage.BACK_BUTTON))
    
    def nextButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wirelessModePage.NEXT_BUTTON))

class ProfileSetupNetworkSettings(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def obtainNetworkSettingsAutomatically(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.networkSettingsPage.OBTAIN_NETWORK_SETTINGS_AUTOMATICALLY_RADIO))
    
    def specifyNetworkSettings(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.networkSettingsPage.SPECIFY_NETWORK_SETTINGS_RADIO))
    
    def ip(self, ip):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.networkSettingsPage.IP_ADDRESS), ip)
    
    def subnet(self, subnet):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.networkSettingsPage.SUBNET_MASK), subnet)
    
    def gateway(self, gateway):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.networkSettingsPage.GATEWAY), gateway)
    
    def dns1(self, dns1):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.networkSettingsPage.DNS1), dns1)
    
    def dns2(self, dns2):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.networkSettingsPage.DNS2), dns2)
    
    def backButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.networkSettingsPage.BACK_BUTTON))
        
    def nextButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.networkSettingsPage.NEXT_BUTTON))

class ProfileSetupWirelessSecurityWep(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
        
    def wep(self, bitNumber):
        self.util.clickItem(self.objName(DesktopConst.pcwireless.profilesTab.wepPage.WEP_COMBO), bitNumber)
    
    def key(self, key):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.wepPage.KEY_EDIT), key)
    
    def backButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wepPage.BACK_BUTTON))
        
    def nextButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wepPage.NEXT_BUTTON))

class ProfileSetupWirelessSecurityWpaPersonal(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def encryption(self, encryption):
        self.util.clickItem(self.objName(DesktopConst.pcwireless.profilesTab.wpaPersonalPage.ENCRYPTION_COMBO), encryption)
    
    def key(self, key):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.wpaPersonalPage.KEY_EDIT), key)
    
    def backButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wpaPersonalPage.BACK_BUTTON))
    
    def nextButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wpaPersonalPage.NEXT_BUTTON))

class ProfileSetupWirelessSecurityWpaEnterprise(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName

    def loginName(self, loginName):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.wpaEnterprisePage.LOGIN_NAME), loginName)
    
    def password(self, password):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.wpaEnterprisePage.PASSWORD))
    
    def encryption(self, encryption):
        self.util.clickItem(self.objName(DesktopConst.pcwireless.profilesTab.wpaEnterprisePage.ENCRYPTION), encryption)

    def backButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wpaEnterprisePage.BACK_BUTTON))
    
    def nextButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wpaEnterprisePage.NEXT_BUTTON))

class ProfileSetupWirelessSecurityWpa2Personal(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def key(self, key):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.wpa2PersonalPage.KEY_EDIT), key)
    
    def backButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wpa2PersonalPage.BACK_BUTTON))
    
    def nextButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wpa2PersonalPage.NEXT_BUTTON))

class ProfileSetupWirelessSecurityWpa2Enterprise(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def loginName(self, loginName):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.wpa2EnterprisePage.LOGIN_NAME), loginName)
    
    def password(self, password):
        self.util.setText(self.objName(DesktopConst.pcwireless.profilesTab.wpa2EnterprisePage.PASSWORD), password)

    def backButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wpa2EnterprisePage.BACK_BUTTON))
    
    def nextButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wpa2EnterprisePage.NEXT_BUTTON))

class ProfileSetupWirelessSecurity(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def security(self, securityMode):
        self.util.clickItem(self.objName(DesktopConst.pcwireless.profilesTab.wirelessSecurityPage.SECURITY_COMBO), securityMode)
    
    def backButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wirelessSecurityPage.BACK_BUTTON))
    
    def nextButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.wirelessSecurityPage.NEXT_BUTTON))
        
class ProfileSetupConfirm(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName

    def exitButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.confirmSettingsPage.EXIT_BUTTON))
    
    def backButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.confirmSettingsPage.BACK_BUTTON))
    
    def saveButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.confirmSettingsPage.SAVE_BUTTON))
    
class ProfileSetupSuccess(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def returnToProfilesScreenButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.successPage.RETURN_TO_PROFILES_SCREEN_BUTTON))
    
    def connectToNetworkButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.successPage.CONNECT_TO_NETWORK_BUTTON))

class ProfilesCreateAProfile(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
        self.newProfileDialog = ProfileNewDailog(self)
        self.confirmPage = ProfileSetupConfirm(self)
        self.networkSettingsPage = ProfileSetupNetworkSettings(self)
        self.successPage = ProfileSetupSuccess(self)
        self.wirelessModePage = ProfileSetupWirelessMode(self)
        self.wirelessSecurityPage = ProfileSetupWirelessSecurity(self)
        self.wepPage = ProfileSetupWirelessSecurityWep(self)
        self.wpa2EnterprisePage = ProfileSetupWirelessSecurityWpa2Enterprise(self)
        self.wpa2PersonalPage = ProfileSetupWirelessSecurityWpa2Personal(self)
        self.wpaEnterprisePage = ProfileSetupWirelessSecurityWpaEnterprise(self)
        self.wpaPersonalPage = ProfileSetupWirelessSecurityWpaPersonal(self)
        
    def updateName(self, squishName):
        self.squishName = squishName
        self.newProfileDialog.updateName(squishName)
        self.confirmPage.updateName(squishName)
        self.networkSettingsPage.updateName(squishName)
        self.successPage.updateName(squishName)
        self.wirelessModePage.updateName(squishName)
        self.wirelessSecurityPage.updateName(squishName)
        self.wepPage.updateName(squishName)
        self.wpa2EnterprisePage.updateName(squishName)
        self.wpa2PersonalPage.updateName(squishName)
        self.wpaEnterprisePage.updateName(squishName)
        self.wpaPersonalPage.updateName(squishName)
    
    @property
    def networkTableName(self):
        return self.objName(DesktopConst.pcwireless.profilesTab.availableNetworksPage.NETWORK_TABLE)
    
    @property
    def networkTable(self):
        return findObject(self.networkTableName)
    
    def refreshButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.availableNetworksPage.REFRESH_BUTTON))
    
    def connectButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.availableNetworksPage.CONNECT_BUTTON))
    
    def selectNetwork(self, ssid):
        for i in range(self.networkTable.rowCount):
            currentNet = findObject(self.networkTableName + '.item_%s/0'%(i,))
            if currentNet.text == ssid:
                self.util.click(currentNet)
                return
    
    def exitButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.availableNetworksPage.EXIT_BUTTON))
    
    def advancedSetupButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.availableNetworksPage.ADVANCED_SETUP_BUTTON))
    
class ProfilesTab(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.createProfile = ProfilesCreateAProfile(self)
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
        self.createProfile.updateName(squishName)
    
    @property
    def networkTableName(self):
        return self.objName(DesktopConst.pcwireless.profilesTab.NETWORK_TABLE)
    
    @property
    def networkTable(self):
        return findObject(self.networkTableName)
    
    def connectButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.CONNECT_BUTTON))
    
    def selectNetwork(self, ssid):
        for i in range(self.networkTable.rowCount):
            currentNet = findObject(self.networkTableName + '.item_%s/0'%(i,))
            if currentNet.text == ssid:
                self.util.click(currentNet)
                return
                
    def newButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.NEW_BUTTON))
    
    def editButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.EDIT_BUTTON))
    
    def importButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.IMPORT_BUTTON))
    
    def exportButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.EXPORT_BUTTON))
    
    def deleteButton(self):
        self.util.clickButton(self.objName(DesktopConst.pcwireless.profilesTab.DELETE_BUTTON))
    
class Tabs(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.util = Util()
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def _clickTab(self, tabList):
        for tab in tabList:
            try:
                if findObject(self.objName(tab)).visible:
                    self.util.clickButton(self.objName(tab))
                    return
            except LookupError, e:
                continue
        raise LookupError('Unable to find tab in pcwireless')
    
    def linkInformation(self):
        tab_buttons = [DesktopConst.pcwireless.connectTab.TAB_LINK_INFORMATION,
                       DesktopConst.pcwireless.profilesTab.TAB_LINK_INFORMATION]
        self._clickTab(tab_buttons)
    
    def connect(self):
        tab_buttons = [DesktopConst.pcwireless.linkInformationTab.TAB_CONNECT,
                       DesktopConst.pcwireless.profilesTab.TAB_CONNECT]
        self._clickTab(tab_buttons)
    
    def profiles(self):
        tab_buttons = [DesktopConst.pcwireless.linkInformationTab.TAB_PROFILES,
                       DesktopConst.pcwireless.connectTab.TAB_PROFILES]
        self._clickTab(tab_buttons)
    
class PCWireless(ConstantsHelper):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.linkInformation = LinkInformationTab(self)
        self.connect = ConnectTab(self)
        self.profiles = ProfilesTab(self)
        self.successPage = ProfileSetupSuccess(self)
        self.tabs = Tabs(self)

    def updateName(self, squishName):
        self.squishName = squishName
        self.linkInformation.updateName(squishName)
        self.connect.updateName(squishName)
        self.profiles.updateName(squishName)
        self.successPage.updateName(squishName)
        self.tabs.updateName(squishName)
    
    def closeButton(self):
        close_buttons = [DesktopConst.pcwireless.connectTab.CLOSE_BUTTON,
                         DesktopConst.pcwireless.linkInformationTab.CLOSE_BUTTON,
                         DesktopConst.pcwireless.profilesTab.CLOSE_BUTTON]
        for button in close_buttons:
            try:
                Util().clickButton(self.objName(button))
                return
            except LookupError, e:
                continue
        raise LookupError('Unable to find close button in wireless dialog')