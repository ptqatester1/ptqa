from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
 
from API.Utility.Util import Util
from API.Utility import UtilConst

util = Util()

pc0 = PC(ComponentBoxConst.DeviceModel.CUSTOM_WIRELESS_PC, 100, 200, "PC0")
linksys = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 300, 200, "Wireless Router0")

def main():
    util.init()
    createTopology()
    checkpoint1()
    newProfile()
    configureLinksys()
    editProfile()

def createTopology():
    pc0.create()
    linksys.create()

def checkpoint1():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.pcWireless()
    pc0.desktop.pcWireless.tabs.profiles()
    snooze(5)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.NETWORK_TABLE).rowCount, 1)
    
def newProfile():
    pc0.desktop.pcWireless.profiles.newButton()
    snooze(1)
    test.compare(findObject(DesktopConst.pcwireless.profilesTab.ProfilesEdit.NAME_EDIT_WINDOW).visible, True)
    pc0.desktop.pcWireless.profiles.createProfile.newProfileDialog.profileName("Test")
    snooze(5)
    pc0.desktop.pcWireless.profiles.createProfile.advancedSetupButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.WirelessMode.INFRASTRUCTURE_RADIO_BUTT).checked, True)
    pc0.desktop.pcWireless.profiles.createProfile.wirelessModePage.networkName("Test")
    pc0.desktop.pcWireless.profiles.createProfile.wirelessModePage.nextButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Settings.DHCP_RADIO_BUTT).checked, True)
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.specifyNetworkSettings()
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.nextButton()
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Please enter an IP address and subnet mask into the fields with format")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.ip('123')
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.nextButton()
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Please enter an IP address and subnet mask into the fields with format")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.subnet('123')
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.nextButton()
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Please enter an IP address and subnet mask into the fields with format")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.gateway('123')
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.nextButton()
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Please enter an IP address and subnet mask into the fields with format")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.dns1('123')
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.nextButton()
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "Please enter an IP address and subnet mask into the fields with format")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.ip("1.1.1.2")
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.subnet("255.0.0.0")
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.gateway("1.1.1.1")
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.dns1("2.1.1.1")
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.nextButton()
    snooze(2)
    pc0.desktop.pcWireless.profiles.createProfile.wirelessSecurityPage.backButton()
    snooze(2)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Settings.IP_EDIT).text, "1.1.1.2")
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Settings.SUBNET_MASK_EDIT).text, "255.0.0.0")
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Settings.GATEWAY_EDIT).text, "1.1.1.1")
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Settings.DNS1_EDIT).text, "2.1.1.1")
    
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.obtainNetworkSettingsAutomatically()
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.specifyNetworkSettings()
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Settings.IP_EDIT).text, "1.1.1.2")
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Settings.SUBNET_MASK_EDIT).text, "255.0.0.0")
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Settings.GATEWAY_EDIT).text, "1.1.1.1")
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Settings.DNS1_EDIT).text, "2.1.1.1")
    
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.obtainNetworkSettingsAutomatically()
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.nextButton()
    snooze(2)
    
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Security.SECURITY_PAGE).visible, True)
    pc0.desktop.pcWireless.profiles.createProfile.wirelessSecurityPage.security("WEP")
    pc0.desktop.pcWireless.profiles.createProfile.wirelessSecurityPage.nextButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Security.WEP_PAGE).visible, True)
    pc0.desktop.pcWireless.profiles.createProfile.wepPage.key("1234")
    pc0.desktop.pcWireless.profiles.createProfile.wepPage.nextButton()
    util.textCheckPoint(UtilConst.ERROR_MESSAGE_POPUP, "WEP Key must be 10 characters for 64-bit WEP or 26 characters for 128-bit WEP")
    util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    
    pc0.desktop.pcWireless.profiles.createProfile.wepPage.key("1234567891")
    pc0.desktop.pcWireless.profiles.createProfile.wepPage.nextButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Confirm.CONFIRM_PAGE).visible, True)
    pc0.desktop.pcWireless.profiles.createProfile.confirmPage.saveButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Confirm.PROFILE_SAVED_PAGE).visible, True)
    pc0.desktop.pcWireless.profiles.createProfile.successPage.connectToNetworkButton()
    
def configureLinksys():
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.NO_ASSOCIATION_FRAME).visible, True)
    pc0.close()
    
    linksys.select()
    linksys.clickConfigTab()
    linksys.config.selectInterface("Wireless")
    linksys.config.interface.wireless.wep()
    linksys.config.interface.wireless.wepkey("1234567891")
    linksys.config.interface.wireless.ssid("Test") 
    linksys.close()
    
    util.fastForwardTime()
    
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.pcWireless()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.ASSOCIATION_FRAME).visible, True)
    
def editProfile():
    pc0.desktop.pcWireless.tabs.profiles()
    pc0.desktop.pcWireless.profiles.selectNetwork("Test")
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.SITE_INFORMATION_SECURITY).text, "WEP")
    pc0.desktop.pcWireless.profiles.editButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.NEW_PROFILE_PAGE).visible, True)
    pc0.desktop.pcWireless.profiles.createProfile.advancedSetupButton()
    pc0.desktop.pcWireless.profiles.createProfile.wirelessModePage.nextButton()
    pc0.desktop.pcWireless.profiles.createProfile.networkSettingsPage.nextButton()
    pc0.desktop.pcWireless.profiles.createProfile.wirelessSecurityPage.security("Disable")
    pc0.desktop.pcWireless.profiles.createProfile.wirelessSecurityPage.nextButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Confirm.CONFIRM_PAGE).visible, True)
    pc0.desktop.pcWireless.profiles.createProfile.confirmPage.saveButton()
    snooze(1)
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.ProfilesEdit.Advance.Confirm.PROFILE_SAVED_PAGE).visible, True)
    pc0.desktop.pcWireless.profiles.createProfile.successPage.returnToProfilesScreenButton()
    pc0.desktop.pcWireless.profiles.selectNetwork("Test")
    test.compare(findObject(pc0.squishName + DesktopConst.pcwireless.profilesTab.SITE_INFORMATION_SECURITY).text, "Disable")