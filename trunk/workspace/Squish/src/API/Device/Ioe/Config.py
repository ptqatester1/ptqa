#@author: Chris Allen


from API.Device.DeviceBase import ConfigBase
from API.Device.Ioe import IoeConst
from API.Device.DeviceBase import DeviceBase
from squish import *
import object
       
class Settings:
    def __init__(self):
        self.squishName = ''
        self.deviceBase = DeviceBase('')
        
    def updateName(self, p_squishName):
        self.squishName = p_squishName
        self.deviceBase.updateName(self.squishName)
        
    def setDisplayName(self , p_squishName):
        obj = IoeConst.Config.DISPLAY_NAME
        self.deviceBase.setText(obj, p_squishName)
    
    def getSerial(self):
        return findObject(self.squishName + IoeConst.Config.Settings.SERIAL_NUMBER).text
    
    def setRemoteServer(self, p_serverAdd, p_user, p_pass):
        self.deviceBase.clickButton(IoeConst.Config.Settings.REMOTE_SERVER)
        self.deviceBase.setText(IoeConst.Config.Settings.SERVER_ADDRESS, p_serverAdd)
        self.deviceBase.setText(IoeConst.Config.Settings.USER_NAME, p_user)
        self.deviceBase.setText(IoeConst.Config.Settings.PASSWORD, p_pass)

class Interface:
    def __init__(self):
        self.squishName = ''
        self.deviceBase = DeviceBase(self.squishName)
    
    def updateName(self, p_squishName):
        self.squishName = p_squishName
        self.deviceBase.updateName(self.squishName)
        
    def togglePortStatus(self):
        self.deviceBase.click(IoeConst.Config.Interface.PORT_STATUS_CHECKBOX)
    
    def setBandwidth(self, p_bandwidth):
        checkBox = findObject(self.squishName + IoeConst.Config.Interface.BANDWIDTH_AUTO_CHECKBOX)
        if p_bandwidth.lower() == 'auto':
            if not checkBox.checked:
                self.deviceBase.click(checkBox)
        else:
            if checkBox.checked:
                self.clickButton(checkBox)
            if p_bandwidth == '1000':
                self.deviceBase.clickButton(IoeConst.Config.Interface.BANDWIDTH_1000_MBPS_RADIO)
            elif p_bandwidth == '100':
                self.deviceBase.clickButton(IoeConst.Config.Interface.BANDWIDTH_100_MBPS_RADIO)
            elif p_bandwidth == '10':
                self.deviceBase.clickButton(IoeConst.Config.Interface.BANDWIDTH_10_MBPS_RADIO)
    
    def setDuplex(self, p_duplex):
        checkBox = findObject(self.squishName + IoeConst.Config.Interface.DUPLEX_AUTO_CHECKBOX)
        if p_duplex.lower() == 'auto':
            if not checkBox.checked:
                self.deviceBase.click(checkBox)
        else:
            if checkBox.checked:
                self.deviceBase.click(checkBox)
            if 'full' in p_duplex.lower():
                self.deviceBase.clickButton(IoeConst.Config.Interface.DUPLEX_FULL_RADIO)
            elif 'half' in p_duplex.lower():
                self.deviceBase.clickButton(IoeConst.Config.Interface.DUPLEX_HALF_RADIO)
    
    def setMac(self, p_mac):
        self.deviceBase.setText(IoeConst.Config.Interface.MAC_ADDRESS_EDIT, p_mac)
    
    def setDhcp(self):
        self.deviceBase.clickButton(IoeConst.Config.Interface.DHCP_RADIO)
    
    def setIpConfig(self, p_ip = None, p_sub = None, p_gate = None, p_dns = None):
        self.deviceBase.clickButton(IoeConst.Config.Interface.STATIC_RADIO)
        if p_ip:
            self.deviceBase.setText(IoeConst.Config.Interface.IP_ADDRESS_EDIT, p_ip)
        if p_sub:
            self.deviceBase.setText(IoeConst.Config.Interface.SUBNET_MASK_EDIT, p_sub)
        if p_gate:
            self.deviceBase.setText(IoeConst.Config.Interface.GATEWAY_EDIT, p_gate)
        if p_dns:
            self.deviceBase.setText(IoeConst.Config.Interface.DNS_EDIT, p_dns)
    
    def setIpv6Dhcp(self):
        self.deviceBase.clickButton(IoeConst.Config.Interface.IPv6_DHCP_RADIO)
    
    def setIpv6Autoconfig(self):
        self.deviceBase.clickButton(IoeConst.Config.Interface.IPv6_AUTO_CONFIG_RADIO)
    
    def setIpv6Config(self, p_ipv6 = None, p_mask = None, p_linklocal = None, p_gateway = None, p_dns = None):
        self.deviceBase.clickButton(IoeConst.Config.Interface.IPv6_STATIC_RADIO)
        if p_ipv6:
            self.deviceBase.setText(IoeConst.Config.Interface.IPv6_ADDRESS_EDIT, p_ipv6)
        if p_mask:
            self.deviceBase.setText(IoeConst.Config.Interface.IPv6_SUBNET_MASK_EDIT, p_mask)
        if p_linklocal:
            self.deviceBase.setText(IoeConst.Config.Interface.IPv6_LINK_LOCAL_ADDRESS_EDIT, p_linklocal)
        if p_gateway:
            self.deviceBase.setText(IoeConst.Config.Interface.IPv6_GATEWAY_EDIT, p_gateway)
        if p_dns:
            self.deviceBase.setText(IoeConst.Config.Interface.IPv6_DNS_EDIT, p_dns)

    def setSSID(self, p_ssid):
        self.deviceBase.setText(IoeConst.Config.Interface.SSID_EDIT, p_ssid)
    
    def setAuthentication(self, p_authentication):
        try:
            authType = findObject(self.squishName + p_authentication)
        except:
            auth = p_authentication.lower()
            if auth == 'disabled':
                authType = findObject(self.squishName + IoeConst.Config.Interface.DISABLED_RADIO)
            elif auth == 'wep':
                authType = findObject(self.squishName + IoeConst.Config.Interface.WEP_RADIO)
            elif auth == 'wpa-psk':
                authType = findObject(self.squishName + IoeConst.Config.Interface.WPA_PSK_RADIO)
            elif auth == 'wpa2-psk':
                authType = findObject(self.squishName + IoeConst.Config.Interface.WPA2_PSK_RADIO)
            elif auth == 'wpa':
                authType = findObject(self.squishName + IoeConst.Config.Interface.WPA_RADIO)
            elif auth == 'wpa2':
                authType = findObject(self.squishName + IoeConst.Config.Interface.WPA2_RADIO)
            else:
                raise Exception('Incorrect value passed to p_authentication parameter of setAuthentication function')
        self.deviceBase.clickButton(authType)
            
    def setWepKey(self, p_key):
        self.deviceBase.setText(IoeConst.Config.Interface.WEP_KEY_EDIT, p_key)
    
    def setPassPhrase(self, p_passphrase):
        self.deviceBase.setText(IoeConst.Config.Interface.PSK_PASS_PHRASE_EDIT, p_passphrase)
    
    def setUserId(self, p_userid):
        self.deviceBase.setText(IoeConst.Config.Interface.USER_ID_EDIT, p_userid)
    
    def setPassword(self, p_password):
        self.deviceBase.setText(IoeConst.Config.Interface.PASSWORD_EDIT, p_password)
    
    def setEncryptionType(self, p_encryption):
        None
    
    def configureWireless(self, p_ssid, p_authentication, p_keyPhraseOrPassword = None, p_userid = None):
        self.setSSID(p_ssid)
        self.setAuthentication(p_authentication)
        if findObject(self.squishName + IoeConst.Config.Interface.DISABLED_RADIO).checked:
            pass
        elif findObject(self.squishName + IoeConst.Config.Interface.WEP_RADIO).checked:
            self.setWepKey(p_keyPhraseOrPassword)
        elif findObject(self.squishName + IoeConst.Config.Interface.WPA_PSK_RADIO).checked or findObject(self.squishName + IoeConst.Config.Interface.WPA2_PSK_RADIO).checked:
            self.setPassPhrase(p_keyPhraseOrPassword) 
        else:
            self.setUserId(p_userid)
            self.setPassword(p_password)

class Config(ConfigBase):
    def __init__(self):
        self.squishName = ""
        self.settings = Settings()
        self.interface = Interface()
    
    #@summary: update the actual name of object that squish uses to reference
    #@param p_squishName: display name of the device    
    def updateName(self, p_squishName):
        self.squishName = p_squishName
        super(Config, self).updateName(self.squishName)
        self.settings.updateName(self.squishName)
        self.interface.updateName(self.squishName)
        
        