#############################################################
#@Author: Chris Allen                                       #
#@Summary: This holds the functions common among device apps#
#############################################################

from API.Android.Device.DeviceBase import DeviceBase, CliBase, DeviceBaseConst
from API.Android.Device.AppsBaseConst import (AAA_AccountingConst, AppButtonsConst, Basic_SetupConst, CommandPromptConst, CloudAppButtonsConst, DhcpConst, 
                                            Dhcpv6Const, DLCI_Const, DnsConst, EmailConst, EmailServerConst, FtpConst, HttpConst, IPconfigConst, IPFirewallConst, IPv6ConfigConst, 
                                            IPv6FirewallConst, MAC_Address_FilterConst, NtpConst, PcWirelessConst, PPPoEConst, TerminalConst, TftpConst, 
                                            VPNConst, WAN_ProviderConst, WebBrowserConst, Wireless_Admin_MgmtConst, WirelessAppButtonsConst, Wireless_SecurityConst, 
                                            Wireless_SettingConst, Wireless_StatusConst, Port_Forwarding, PortSetup, APAppButtonsConst, TextEditorConst,
                                            BackboneInterfaceConst, COServerAppButtonsConst, COServerDhcpConst, SyslogConst, SnifferAppButtonsConst, SnifferConst)
from API.Android.Utility.functions import functions
from API.Android.Utility.Util import Util
from API.Android.Utility import UtilConst
import object
from squish import *
from API.Android.Device.LinksysRouter.LinksysRouterConst import LinksysRouterConst

util = Util()
class AppButtons:
    def __init__(self):
        self.util = util
    
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
        
    def commandPromptButton(self):
        self.waitForVisibleObject(AppButtonsConst.COMMAND_PROMPT)
        self.util.tap(AppButtonsConst.COMMAND_PROMPT)
        snooze(5)
    
    def emailButton(self):
        self.waitForVisibleObject(AppButtonsConst.EMAIL)
        self.util.tap(AppButtonsConst.EMAIL)
        snooze(5)
    
    def emailServiceButton(self):
        self.waitForVisibleObject(AppButtonsConst.EMAIL_SERVICE)
        self.util.tap(AppButtonsConst.EMAIL_SERVICE)
        snooze(5)
    
    def ipConfigurationButton(self):
        self.waitForVisibleObject(AppButtonsConst.IP_CONFIGURATION)
        self.util.tap(AppButtonsConst.IP_CONFIGURATION)
        snooze(5)
    
    def ipFirewallButton(self):
        self.waitForVisibleObject(AppButtonsConst.IPV4_FIREWALL)
        self.util.tap(AppButtonsConst.IPV4_FIREWALL)
        snooze(5)
    
    def ipv6ConfigurationButton(self):
        self.waitForVisibleObject(AppButtonsConst.IPV6_CONFIGURATION)
        self.util.tap(AppButtonsConst.IPV6_CONFIGURATION)
        snooze(5)
    
    def ipv6FirewallButton(self):
        self.waitForVisibleObject(AppButtonsConst.IPV6_FIREWALL)
        self.util.tap(AppButtonsConst.IPV6_FIREWALL)
        snooze(5)
    
    def pcWirelessButton(self):
        self.waitForVisibleObject(AppButtonsConst.PC_WIRELESS)
        self.util.tap(AppButtonsConst.PC_WIRELESS)
        snooze(5)

    def textEditorButton(self):
        self.waitForVisibleObject(AppButtonsConst.TEXTEDITOR)
        self.util.tap(AppButtonsConst.TEXTEDITOR)
        snooze(5)

    def pppoeButton(self):
        self.waitForVisibleObject(AppButtonsConst.PPPOE_DIALER)
        self.util.tap(AppButtonsConst.PPPOE_DIALER)
        snooze(5)
    
    def terminalButton(self):
        self.waitForVisibleObject(AppButtonsConst.TERMINAL)
        self.util.tap(AppButtonsConst.TERMINAL)
        snooze(5)
    
    def vpnButton(self):
        self.waitForVisibleObject(AppButtonsConst.VPN)
        self.util.tap(AppButtonsConst.VPN)
        snooze(5)
    
    def webBrowserButton(self):
        self.waitForVisibleObject(AppButtonsConst.WEB_BROWSER)
        self.util.tap(AppButtonsConst.WEB_BROWSER)
        snooze(5)
    
    def tftpButton(self):
        self.waitForVisibleObject(AppButtonsConst.TFTP)
        self.util.tap(AppButtonsConst.TFTP)
        snooze(5)
    
    def ftpButton(self):
        self.waitForVisibleObject(AppButtonsConst.FTP)
        self.util.tap(AppButtonsConst.FTP)
        snooze(5)
    
    def httpButton(self):
        self.waitForVisibleObject(AppButtonsConst.HTTP)
        self.util.tap(AppButtonsConst.HTTP)
        snooze(5)
    
    def dhcpButton(self):
        self.waitForVisibleObject(AppButtonsConst.DHCP)
        self.util.tap(AppButtonsConst.DHCP)
        snooze(5)
        
    def dhcpv6Button(self):
        self.waitForVisibleObject(AppButtonsConst.DHCPv6)
        self.util.tap(AppButtonsConst.DHCPv6)
        snooze(5)
    
    def dnsButton(self):
        self.waitForVisibleObject(AppButtonsConst.DNS)
        self.util.tap(AppButtonsConst.DNS)
        snooze(5)
    
    def aaaAccountingButton(self):
        self.waitForVisibleObject(AppButtonsConst.AAAACCOUNTING)
        self.util.tap(AppButtonsConst.AAAACCOUNTING)
        snooze(5)
    
    def ntpButton(self):
        self.waitForVisibleObject(AppButtonsConst.NTP)
        self.util.tap(AppButtonsConst.NTP)
        snooze(5)
        
    def syslogButton(self):
        self.waitForVisibleObject(AppButtonsConst.SYSLOG)
        self.util.tap(AppButtonsConst.SYSLOG)
        snooze(5)
        
        
class PortForwarding:
    def __init__(self):
        self.util = util
    
    def selectApplication(self, p_row, p_application):
        obj = Port_Forwarding.APP_NAME1.replace('appName1', 'appName' + str(p_row))
        self.util.tap(obj)
        snooze(1)
        if p_application == 'HTTP':
            self.util.touchAndDrag(UtilConst.MainViewConst.PT_MOBILE_WEBVIEW, 346, 760, 24, -250)
            snooze(5)
        parentSibling = ':guidance_HTML_Object' #This is the closest object up the object tree that I could find with a named id
        parentSiblingObj = findObject(parentSibling)
        parentObj = object.parent(parentSiblingObj)
        parentName = ':' + parentObj.id + '_HTML_Object'
        childObj = self.util.findTag(parentName, 'SPAN', p_application)
        self.util.tap(childObj)
    
    def setIpAddress(self, p_row, p_ipLastOctet):
        obj = Port_Forwarding.IP_ADDRESS1.replace('toIpAddr1', 'toIpAddr' + str(p_row))
        self.util.tapTextArea(obj)
        self.util.setText(obj, p_ipLastOctet)
        #self.util.type(p_ipLastOctet)
    
    def enable(self, p_row):
        obj = Port_Forwarding.ENABLED1.replace('enabled1', 'enabled' + str(p_row))
        self.util.tap(obj)
    
    def setPortForwarding(self, p_row, p_application, p_ipLastOctet):
        if not p_row:
            raise Exception('A row must be specified')
        self.selectApplication(p_row, p_application)
        self.setIpAddress(p_row, p_ipLastOctet)
        self.enable(p_row)
        self.submit()
        
    def submit(self):
        self.util.tap(Port_Forwarding.SUBMIT_BUTTON)
        
class LinksysAppButtons:
    def __init__(self):
        self.util = util
    
    def basicSettingsButton(self):
        self.util.waitForVisibleObject(WirelessAppButtonsConst.BASIC_SETUP)
        self.util.tap(WirelessAppButtonsConst.BASIC_SETUP)
        snooze(5)
    
    def macAddressFilterButton(self):
        self.util.waitForVisibleObject(WirelessAppButtonsConst.MAC_ADDRESS_FILTER)
        self.util.tap(WirelessAppButtonsConst.MAC_ADDRESS_FILTER)
        snooze(5)

    def adminManagementButton(self):
        self.util.waitForVisibleObject(WirelessAppButtonsConst.WIRELESS_ADMIN_MGMT)
        self.util.tap(WirelessAppButtonsConst.WIRELESS_ADMIN_MGMT)
        snooze(5)
        
    def wirelessSecurityButton(self):
        self.util.waitForVisibleObject(WirelessAppButtonsConst.WIRELESS_SECURITY)
        self.util.tap(WirelessAppButtonsConst.WIRELESS_SECURITY)
        snooze(5)
        
    def wirelessSettingsButton(self):
        self.util.waitForVisibleObject(WirelessAppButtonsConst.WIRELESS_SETTING)
        self.util.tap(WirelessAppButtonsConst.WIRELESS_SETTING)
        snooze(5)
        
    def wirelessStatusButton(self):
        self.util.waitForVisibleObject(WirelessAppButtonsConst.WIRELESS_STATUS)
        self.util.tap(WirelessAppButtonsConst.WIRELESS_STATUS)
        snooze(5)
        
    def portForwardingButton(self):
        self.util.waitForVisibleObject(WirelessAppButtonsConst.PORT_FORWARDING)
        self.util.tap(WirelessAppButtonsConst.PORT_FORWARDING)
        snooze(5)
                
class COServerAppButtons:
    def __init__(self):
        self.util = util
        pass
        
    def backboneInterfaceButton(self):
        self.util.waitForVisibleObject(COServerAppButtonsConst.BACKBONE_INTERFACE)
        self.util.tap(COServerAppButtonsConst.BACKBONE_INTERFACE)
        snooze(5)
                
    def cellTowerInterfaceButton(self):
        self.util.waitForVisibleObject(COServerAppButtonsConst.CELL_TOWER_INTERFACE)
        self.util.tap(COServerAppButtonsConst.CELL_TOWER_INTERFACE)
        snooze(5)
        
    def dhcpButton(self):
        self.util.waitForVisibleObject(COServerAppButtonsConst.DHCP)
        self.util.tap(COServerAppButtonsConst.DHCP)
        snooze(5)
        
    def dhcpv6Button(self):
        self.util.waitForVisibleObject(COServerAppButtonsConst.DHCP6)
        self.util.tap(COServerAppButtonsConst.DHCP6)
        snooze(5)
        
    def cellTowerServiceButton(self):
        self.util.waitForVisibleObject(COServerAppButtonsConst.CELL_TOWER_SERVICE)
        self.util.tap(COServerAppButtonsConst.CELL_TOWER_SERVICE)
        snooze(5)
        
    def papChapServiceButton(self):
        self.util.waitForVisibleObject(COServerAppButtonsConst.PAP_CHAP_SERVICE)
        self.util.tap(COServerAppButtonsConst.PAP_CHAP_SERVICE)
        snooze(5)
        
class SnifferAppButtons:
    def __init__(self):
        self.util = util
        pass
    
    def snifferButton(self):
        self.util.waitForVisibleObject(SnifferAppButtonsConst.SNIFFER)
        self.util.tap(SnifferAppButtonsConst.SNIFFER)
        snooze(5)
        
class AaaAccounting: 
    def __init__(self):
        self.util = util
        pass
    
    def submit(self):
        self.util.tap(AAA_AccountingConst.SUBMIT_BUTTON)
    
    def addAAAClient(self, p_client_host, p_client_ip, p_secret, p_server_type = 'Radius'):
        self.util.tap(AAA_AccountingConst.AAA_ON_RADIO)
        self.util.setText(AAA_AccountingConst.AAA_CLIENT_NAME, p_client_host)
        self.util.setText(AAA_AccountingConst.AAA_CLIENT_IP, p_client_ip)
        self.util.setText(AAA_AccountingConst.AAA_CLIENT_SECRET, p_secret)
        if p_server_type == "Tacacs":
            self.util.tap(AAA_AccountingConst.AAA_TACACS)
        else:   
            self.util.tap(AAA_AccountingConst.AAA_RADIUS)
        self.util.swipe(500, 500, 0, -500)
        self.util.tap(AAA_AccountingConst.ADD_CLIENT_BUTTON)
        self.submit()
        
    def addUser(self, p_username, p_password):
        self.util.setText(AAA_AccountingConst.AAA_USER_NAME, p_username)
        self.util.setText(AAA_AccountingConst.AAA_USER_PASSWORD, p_password)
        self.util.tap(AAA_AccountingConst.ADD_USER_BUTTON)
        self.submit()
    
    def updateUser(self, p_currentUsername, p_newUsername, p_newPassword):
        functions().findTagWithProperties(AAA_AccountingConst.USER_LIST, 'TD', {'innerText':p_currentUsername})
        self.util.setText(AAA_AccountingConst.AAA_USER_NAME, p_newUsername)
        self.util.setText(AAA_AccountingConst.AAA_USER_PASSWORD, p_newPassword)
        self.util.tap(AAA_AccountingConst.SAVE_USER_BUTTON)
        self.submit()

class BasicSetup:
    def __init__(self):
        self.util = util
        pass
    
    def changeConnectionType(self, p_connectionType):
        if p_connectionType == 'DHCP':
            p_connectionType = Basic_SetupConst.INTERNET_CONNECTION_DHCP
        elif p_connectionType == 'Static':
            p_connectionType = Basic_SetupConst.INTERNET_CONNECTION_STATIC
        else:
            p_connectionType = Basic_SetupConst.INTERNET_CONNECTION_PPPOE
             
        self.util.tap(Basic_SetupConst.INTERNET_CONNECTION_TYPE)
        snooze(1)
        self.util.tap(p_connectionType)

    def setStaticIP(self, p_staticIP):
        self.util.setText(Basic_SetupConst.STATIC_INTERNET_IP, p_staticIP)
    
    def setStaticMask(self, p_staticMask):
        self.util.setText(Basic_SetupConst.STATIC_SUBNET_MASK, p_staticMask)
    
    def setStaticGate(self, p_staticGate):
        self.util.setText(Basic_SetupConst.STATIC_DEFAULT_GATEWAY, p_staticGate)
        
    def setStaticDNS(self, p_staticDNS):
        self.util.setText(Basic_SetupConst.STATIC_DNS1, p_staticDNS)
    
    def configureStaticIP(self, p_connectionType, p_staticIP, p_staticMask, p_staticGate, p_staticDNS = ''):
        if p_connectionType:
            self.changeConnectionType(p_connectionType)
        if p_staticIP:
            self.setStaticIP(p_staticIP)
        if p_staticMask:
            self.setStaticMask(p_staticMask)
        if p_staticGate:
            self.setStaticGate(p_staticGate)
        if p_staticDNS:
            self.setStaticDNS(p_staticDNS)
        self.submit()
            
    def enableDHCP(self):
        self.util.tap(Basic_SetupConst.DHCP_ON)
        
    def disableDHCP(self):
        self.util.tap(Basic_SetupConst.DHCP_OFF)
        
    def setDHCP_StartIP(self, p_startIP):
        startIp = p_startIP.split('.')[-1]
        for i in range(3):
            self.util.setText(Basic_SetupConst.DHCP_START_IP, '<Backspace>')
        self.util.setText(Basic_SetupConst.DHCP_START_IP, startIp)
    
    def setDHCP_Max(self, p_dhcpMax):
        for i in range(3):
            self.util.setText(Basic_SetupConst.DHCP_MAX_NUMBER, '<Backspace>')
        self.util.setText(Basic_SetupConst.DHCP_MAX_NUMBER, p_dhcpMax)
    
    def setDHCP_DNS1(self, p_dhcpDNS):
        self.util.setText(Basic_SetupConst.DHCP_STATIC_DNS1, p_dhcpDNS)
    
    def configureDHCP(self, p_startIP, p_dhcpMax, p_dhcpDNS):
        self.enableDHCP()
        if p_startIP:
            self.setDHCP_StartIP(p_startIP)
        if p_dhcpMax:
            self.setDHCP_Max(p_dhcpMax)
        if p_dhcpDNS:
            self.setDHCP_DNS1(p_dhcpDNS)
        self.submit()
        
    def setPPPOEusername(self, p_username):
        self.util.setText(Basic_SetupConst.PPPOE_USERNAME, p_username)
    
    def setPPPOEpassword(self, p_password):
        self.util.setText(Basic_SetupConst.PPPOE_USERNAME, p_password)
    
    def setNetworkAddress(self, p_networkAddress):
        self.util.setText(Basic_SetupConst.NETWORK_SETUP_IP, p_networkAddress)
        
    def setNetworkSubnetMask(self, p_networkMask):
        self.util.tap(Basic_SetupConst.NETWORK_SUBNET_MASK)
        parentSibling = ':guidance_HTML_Object' #This is the closest object up the object tree that I could find with a named id
        parentSiblingObj = findObject(parentSibling)
        parentObj = object.parent(parentSiblingObj)
        parentName = ':' + parentObj.id + '_HTML_Object'
        childObj = self.util.findTag(parentName, 'SPAN', p_networkMask) 
        self.util.tap(childObj)
        
    def goToReserveDHCP(self):
        self.util.swipe(961, 585, -1, -224)
        snooze(5)
        self.util.tap(Basic_SetupConst.DHCP_SERVER_ACTION)
        self.util.tap(Basic_SetupConst.CONFIG_DHCP_RESERVATION)

    def submit(self):
        self.util.tap(Basic_SetupConst.SUBMIT_BUTTON)
        
class CommandPrompt: 
    def __init__(self):
        self.util = util
        self.setCliText = CliBase().setCliTextByKeyboard

    def textCheckPoint(self, p_text, p_occurrenceNum = -1):
        self.util.textCheckPoint(CommandPromptConst.CLI_CONSOLE, p_text, p_occurrenceNum)
        
class Dhcp: 
    def __init__(self):
        self.util = util
        pass

    def changeInterface(self, p_interfaceName):
        self.util.tap(DhcpConst.INTERFACE_SELECT, p_interfaceName)
    
    def changeServerPool(self, p_serverPoolName):
        self.util.tap(DhcpConst.POOL_SELECT, p_serverPoolName)
    
    def setDHCPServiceOn(self):
        self.util.tap(DhcpConst.SERVICE_ON)

    def setDHCPServiceOff(self):
        self.util.tap(DhcpConst.SERVICE_OFF)

    def setDhcpPoolName(self, p_name):
        self.util.setText(DhcpConst.POOL_NAME, p_name)  

    def setDhcpGateway(self, p_gateway):
        self.util.setText(DhcpConst.GATEWAY, p_gateway)  
        
    def setDhcpDNS(self, p_domain):
        self.util.setText(DhcpConst.DNS_SERVER, p_domain)        

         
    def setDhcpStartIp(self, p_ip):
        self.util.setText(DhcpConst.START_IP_ADDRESS, p_ip) 

    def setDhcpSubnet(self, p_subnet):
        self.util.setText(DhcpConst.SUBNET_MASK, p_subnet)       
        

    def setDhcpMaxUser(self, p_max):
        self.util.setText(DhcpConst.MAX_USERS, p_max)

    def setDhcpTftpServer(self, p_tftp):
        self.util.setText(DhcpConst.TFTP_SERVER, p_tftp)
        
    def addDhcpPool(self, p_name, p_gateway, p_dns, p_startIP, p_subnet, p_maxUsers):
        self.setDHCPServiceOn()
        self.setDhcpPoolName(p_name)
        self.setDhcpGateway(p_gateway)
        self.setDhcpDNS(p_dns)
        self.setDhcpStartIp(p_startIP)
        self.setDhcpSubnet(p_subnet)
        self.setDhcpMaxUser(p_maxUsers)
        self.util.tap(DHCP.ADD_BUTTON)
        
    def editPool(self, p_pool, p_name, p_gateway, p_dns, p_startIP, p_subnet, p_maxUsers):
        self.util.tap(ServerConst.Services.DHCP_LIST_VIEW, p_pool)       
        self.setDHCPServiceOn()
        self.setDhcpPoolName(p_name)
        self.setDhcpGateway(p_gateway)
        self.setDhcpDNS(p_dns)
        self.setDhcpStartIp(p_startIP)
        self.setDhcpSubnet(p_subnet)
        self.setDhcpMaxUser(p_maxUsers)
        self.util.tap(DHCP.SAVE_BUTTON)

    def removeDhcpPool(self, p_pool):
        self.util.tap(ServerConst.DHCP.DHCP_POOL_LIST, p_pool)
        '''Need to finish implementation'''
        self.util.tap(ServerConst.DHCP.REMOVE_BUTTON)
        
class Dhcpv6:
    def __init__(self):
        self.util = util
        pass
    
    def createPool(self):
        self.util.tap(Dhcpv6Const.POOL_LIST_OPTIONS)
        self.util.tap(Dhcpv6Const.POOL_CREATE)
    
    def setPoolName(self, p_pname):
        self.util.setText(Dhcpv6Const.POOL_NAME, p_pname)
        
    def setDNS(self, p_dns):
        self.util.setText(Dhcpv6Const.DNS_NAME, p_dns)
    
    def setDomain(self, p_domain):
        self.util.setText(Dhcpv6Const.DOMAIN_NAME, p_domain)
        
    def setIPv6add(self, p_add, p_prefix):
        self.util.setText(Dhcpv6Const.IP_ADDRESS, p_add)
        self.util.setText(Dhcpv6Const.PREFIX, p_prefix)
        
    def setDuid(self, p_duid):
        self.util.setText(Dhcpv6Const.DUID, p_duid)
    
    def setValidLife(self, p_valid):
        self.util.setText(Dhcpv6Const.PREFIX_VALID_LIFE, p_valid)
        
    def setPrefLife(self, p_prefer):
        self.util.setText(Dhcpv6Const.PREFIX_PREFERRED_LIFE, p_prefer)
        
    def setLocalName(self, p_lname):
        self.util.setText(Dhcpv6Const.LOCAL_POOL, p_lname)
    
    def setLocalValid(self, p_valid_local):
        self.util.setText(Dhcpv6Const.LOCAL_VALID_LIFE, p_valid_local)
    
    def setLocalPrefer(self, p_prefer_local):
        self.util.setText(Dhcpv6Const.LOCAL_PREFFERED_LIFE, p_prefer_local)
    
    def editPool(self, p_name, p_dns, p_domain):
        self.setPoolName(p_pname)
        self.setDNSName(p_dns)
        self.setDomain(p_domain)
    
    def editPrefixDel(self):
        pass
    
    def editPrefixPool(self):
        pass
        
class Dns:
    def __init__(self):
        self.util = util
        pass
    
    def serviceOn(self):
        self.util.tap(DnsConst.ON)
    
    def serviceOff(self):
        self.util.tap(DnsConst.OFF)
        
    def selectType(self, p_type):
        self.util.tap(DnsConst.TYPE)
        if p_type.lower() == 'a record':
            self.util.tap(waitForObject(DnsConst.A_RECORD))
        elif p_type.lower() == 'cname':
            self.util.tap(waitForObject(DnsConst.CNAME))
        elif p_type.lower() == 'soa':
            self.util.tap(waitForObject(DnsConst.SOA))
        elif p_type.lower() == 'ns record':
            self.util.tap(waitForObject(DnsConst.NS_RECORD))
        else:
            self.util.tap(waitForObject(p_location))
        pass
    
    def selectRecord(self, p_record):
        self.util.tap(DnsConst.RESOURCE_RECORD)
        '''Need to finish implementation'''
    
    def editResourceRecordName(self, p_name):
        self.util.setText(DnsConst.RESOURCE_RECORD_NAME, p_name)
    
    def editARecordAddress(self, p_address):
        self.util.setText(DnsConst.A_RECORD_ADDRESS, p_address)
    
    def editCNameHostName(self, p_hostName):
        self.util.setText(DnsConst.CNAME_HOSTNAME, p_hostname)
    
    def editSoaPrimaryServerName(self, p_serverName):
        self.util.setText(DnsConst.SOA_PRIMARY_SERVER_NAME, p_serverName)
    
    def editSoaMailBox(self, p_mailBox):
        self.util.setText(DnsConst.SOA_MAILBOX, p_mailBox)
    
    def editSoaMinTTL(self, p_ttl):
        self.util.setText(DnsConst.SOA_MINIMUM_TTL, p_ttl)
    
    def editSoaRefreshTime(self, p_refreshTime):
        self.util.setText(DnsConst.SOA_REFRESH_TIME, p_refreshTime)
        
    def editSoaRetryTime(self, p_retryTime):
        self.util.setText(DnsConst.SOA_RETRY_TIME, p_retryTime)
        
    def editSoaExpiryTime(self, p_expiryTime):
        self.util.setText(DnsConst.SOA_EXPIRY_TIME, p_expiryTime)
        
    def editNsServerName(self, p_serverName):
        self.util.setText(DnsConst.NSRECORD_NAME_SERVER, p_serverName)
    
    def addRecord(self):
        self.util.tap(DnsConst.ADD_BUTTON)
        
    def createARecord(self, p_name, p_address, p_onOff, p_saveYesNo = 'y'):
        if str(p_onOff).lower().startswith('o'):
            self.serviceOn()
        self.editResourceRecordName(p_name)
        self.editARecordAddress(p_address)
        self.addRecord()
        if str(p_saveYesNo).lower().startswith('y'):
            self.util.tap(DnsConst.SAVE_BUTTON)
    
    def createCName(self, p_name, p_hostName, p_onOff, p_saveYesNo = 'y'):
        if str(p_onOff).lower().startswith('o'):
            self.serviceOn()
        self.editResourceRecordName(p_name)
        self.editCNameHostName(p_hostName)
        self.addRecord()
        if str(p_saveYesNo).lower().startswith('y'):
            self.util.tap(DnsConst.SAVE_BUTTON)
        
    def createSoa(self, p_name, p_primaryServer, p_mailBox, p_ttl, p_refreshTime, p_retryTime, p_expiryTime, p_onOff, p_saveYesNo = 'y'):
        if str(p_onOff).lower().startswith('o'):
            self.serviceOn()
        self.editResourceRecordName(p_name)
        self.editSoaPrimaryServerName(p_serverName)
        self.editSoaMailBox(p_mailBox)
        self.editSoaMinTTL(p_ttl)
        self.editSoaRefreshTime(p_refreshTime)
        self.editSoaRetryTime(p_retryTime)
        self.editSoaExpiryTime(p_expiryTime)
        self.addRecord()
        if str(p_saveYesNo).lower().startswith('y'):
            self.util.tap(DnsConst.SAVE_BUTTON)
    
    def createNsRecord(self, p_name, p_serverName, p_onOff, p_saveYesNo = 'y'):
        if str(p_onOff).lower().startswith('o'):
            self.serviceOn()
        self.editResourceRecordName(p_name)
        self.editNsServerName(p_serverName)
        self.addRecord()
        if str(p_saveYesNo).lower().startswith('y'):
            self.util.tap(DnsConst.SAVE_BUTTON)
        
class DLCI_Config:
    def __init__(self):
        self.util = util
        pass
        
    def selectInterface(self, p_interface):
        self.util.tap(DLCI_Const.INTERFACE, p_interface)
    
    def selectLMI(self, p_LMI):
        self.util.tap(DLCI_Const.LMI_TYPE, p_LMI)
        
    def editDLCInumber(self, p_DLCInum):
        self.util.setText(DLCI_Const.DLCI, p_DLCI)
    
    def editDLCIname(self, p_DLCIname):
        self.util.setText(DLCI_Const.DLCI_NAME, p_DLCIname)
        
    def addDLCIconfig(self, p_interface, p_portStatus, p_LMI, p_DLCInum, p_DLCIname):
        self.selectInterface(p_interface)
        self.togglePortStatus()
        self.selectLMI(p_LMI)
        self.editDLCInumber(p_DLCInum)
        self.DLCInname(p_DLCIname)
        self.util.tap(DLCI_Const.ADD_BUTTON)
    
    def removeDLCIconfig(self, p_entry):
        self.util.tap(DLCI_Const.DLCI_TABLE, p_entry)
        self.util.tap(DLCI_Const.REMOVE_BUTTON)
            
class EmailClient:
    def __init__(self):
        self.util = util
        pass
    
    def editName(self, p_name):
        self.util.setText(EmailConst.ConfigureMail.NAME, p_name)
    
    def editEmailAddress(self, p_emailAddress):
        self.util.setText(EmailConst.ConfigureMail.EMAIL_ADDRESS, p_emailAddress)
        
    def editIncomingMailServer(self, p_incomingServer):
        self.util.setText(EmailConst.ConfigureMail.INCOMING_MAIL_SERVER, p_incomingServer)
    
    def editOutgoingMailServer(self, p_outgoingServer):
        self.util.setText(EmailConst.ConfigureMail.OUTGOING_MAIL_SERVER, p_outgoingServer)
    
    def editUsername(self, p_username):
        self.util.setText(EmailConst.ConfigureMail.USERNAME, p_username)
    
    def editPassword(self, p_password):
        self.util.setText(EmailConst.ConfigureMail.PASSWORD, p_password)
    
    def configureEmail(self, p_name, p_emailAddress, p_incomingServer, p_outgoingServer, p_username, p_password, p_saveYesNo = 'y'):
        self.util.tap(EmailConst.MailClient.SELECT_VIEW)
        snooze(1)
        self.util.tap(EmailConst.MailClient.CONFIGURE_MAIL_BUTTON)
        snooze(1)
        self.editName(p_name)
        self.editEmailAddress(p_emailAddress)
        self.editIncomingMailServer(p_incomingServer)
        self.editOutgoingMailServer(p_outgoingServer)
        self.editUsername(p_username)
        self.editPassword(p_password)
        if str(p_saveYesNo).lower().startswith('y'):
            self.util.tap(EmailConst.ConfigureMail.SAVE_BUTTON)
        elif str(p_saveYesNo).lower().startswith('n'):
            self.util.tap(EmailConst.ConfigureMail.CANCEL_BUTTON)
            
    def editTo(self, p_to):
        self.util.setText(EmailConst.ComposeAndReply.TO, p_to)
    
    def editSubject(self, p_subject):
        self.util.setText(EmailConst.ComposeAndReply.SUBJECT, p_subject)
    
    def editContent(self, p_content):
        self.util.typeText(EmailConst.ComposeAndReply.CONTENT, p_content)
        
    def composeEmail(self, p_to, p_subject, p_content, p_sendCancel = 's'):
        self.util.tap(EmailConst.MailClient.SELECT_VIEW)
        self.util.tap(EmailConst.MailClient.COMPOSE_BUTTON)
        self.editTo(p_to)
        self.editSubject(p_subject)
        self.editContent(p_content)
        if str(p_sendCancel).lower().startswith('s'):
            self.util.tap(self.util.findTag(':composeMailBtnContainer_HTML_Object', 'SPAN', 'Send'))
            #self.util.tap(EmailConst.ComposeAndReply.SEND_BUTTON)
        elif str(p_sendCancel).lower().startswith('c'):
            self.util.tap(self.util.findTag(':composeMailBtnContainer_HTML_Object', 'SPAN', 'Cancel'))
            #self.util.tap(EmailConst.ComposeAndReply.CANCEL_BUTTON)
        
    def replyEmail(self, p_to, p_subject, p_content, p_sendCance = 's'):
        self.util.tap(EmailConst.MailClient.REPLY_BUTTON)
        self.editTo(p_to)
        self.editSubject(p_subject)
        self.editContent(p_content)
        if str(p_sendCancel).lower().startswith('s'):
            self.util.tap(EmailConst.ComposeAndReply.SEND_BUTTON)
        elif str(p_sendCancel).lower().startswith('c'):
            self.util.tap(EmailConst.ComposeAndReply.CANCEL_BUTTON)
        
    def receiveMail(self):
        self.util.tap(EmailConst.MailClient.RECEIVE_BUTTON)
        
    def deleteEmail(self, p_emailToDelete):
        '''Need to implement this'''
        pass

class EmailServer:
    def __init__(self):
        self.util = util
        pass
    
    def submit(self):
        self.util.tap(EmailServerConst.SUBMT_BUTTON)  
        
    def addUser(self, p_user, p_password):
        self.util.setText(EmailServerConst.EMAIL_USERNAME, p_user)
        self.util.setText(EmailServerConst.EMAIL_PASSWORD, p_password)
        self.util.tap(EmailServerConst.ADD_USER_BUTTON)
        
    def smtpON(self):
        self.util.tap(EmailServerConst.SMTP_SERVICE_ON_RADIO)
        
    def pop3ON(self):
        self.util.tap(EmailServerConst.POP3_SERVICE_ON_RADIO)
        
    def setDomainName(self, p_domain):
        self.util.setText(EmailServerConst.DOMAIN_NAME, p_domain)
    
class FrameRelayMapping:
    def __init__(self):
        self.util = util
    pass
    
    def selectFromPort(self, p_fromPort):
        self.util.tap(FrameRelayConst.FROM_PORT, p_fromPort)
    
    def selectToPort (self, p_toPort):
        self.util.tap(FrameRelayConst.TO_PORT, p_toPort)
    
    def selectFromSublink(self, p_fromSublink):
        self.util.tap(FrameRelayConst.FROM_SUBLINK, p_fromSublink)
        
    def selectToSublink(self, p_toSublink):
        self.util.tap(FrameRelayConst.TO_SUBLINK, p_toSublink)
        
    def addMapping(self, p_fromPort, p_toPort, p_fromSublink, p_toSublink):
        self.selectFromPort(p_fromPort)
        self.selectFromSublink(p_fromSublink)
        self.selectToPort(p_toPort)
        self.selectToSublink(p_toSublink)
        self.util.tap(FrameRelayConst.ADD_BUTTON)
        
    def removeMapping(self, p_entry):
        self.util.tap(FrameRelayConst.FRAME_RELAY_TABLE, p_entry)
        self.util.tap(FrameRelayConst.REMOVE_BUTTON)

class IpFirewall:
    def __init__(self):
        self.util = util
        pass
    
    def selectInterface(self):
        self.util.tap(IPFirewallConst.INTERFACE)
        '''This needs to be finished later'''
    
    def serviceOn(self):
        self.util.tap(IPFirewallConst.ON_RADIO)
        
    def serviceOff(self):
        self.util.tap(IPFirewallConst.OFF_RADIO)
        
    def selectAction(self, p_action):
        self.util.tap(IPFirewallConst.ACTION)
        '''This needs to be finished later'''
    
    def editRemoteIp(self, p_remoteIp):
        self.util.setText(IPFirewallConst.REMOTE_IP, p_remoteIp)
        
    def editProtocol(self, p_protocol):
        self.util.tap(IPFirewallConst.PROTOCOL)
        '''This needs to be finished later'''
        
    def editRemoteWildcardMask(self, p_mask):
        self.util.setText(IPFirewallConst.WILDCARD_MASK, p_mask)
    
    def editRemotePort(self, p_remotePort):
        self.util.setText(IPFirewallConst.REMOTE_PORT, p_remotePort)
        
    def editLocalPort(self, p_localPort):
        self.util.setConsoleText(IPFirewallConst.LOCAL_PORT, p_localPort)
        
    def selectFirewallRule(self, p_rule):
        self.util.tap(IPFirewallConst.FIREWALL_RULE)
        '''This needs to be finished later'''
        
    def createRule(self, p_action, p_remoteIP, p_protocol, p_mask, p_remotePort, p_localPort, p_saveYesNo):
        self.serviceOn()
        if p_action:
            self.selectAction(p_action)
        if p_remoteIp:
            self.editRemoteIp(p_remoteIp)
        if p_protocol:
            self.editProtocol(p_protocol)
        if p_mask:
            self.editRemoteWildcardMask(p_mask)
        if p_remotePort:
            self.editRemotePort(p_remotePort)
        if p_localPort:
            self.editLocalPort(p_localPort)
        self.util.tap(IPFirewallConst.ADD)
        if str(p_saveYesNo).lower().startswith('y'):
            self.saveRule()
        
    def addRule(self):
        self.util.tap(IPFirewallConst.ADD)
        
    def saveRule(self):
        self.util.tap(IPFirewallConst.SAVE)
    
    def removeRule(self, p_rule):
        self.util.tap(IPFirewallConst.FIREWALL_RULE)
        '''Need to figure out how to select a specific rule and then add
        a line to select p_rule'''
        self.util.tap(IPFirewallConst.REMOVE)
        
class Ipv6Firewall:
    def __init__(self):
        self.util = util
        pass
    
    def selectInterface(self):
        self.util.tap(IPv6FirewallConst.INTERFACE)
        '''This needs to be finished later'''
    
    def serviceOn(self):
        self.util.tap(IPv6FirewallConst.ON_RADIO)
        
    def serviceOff(self):
        self.util.tap(IPv6FirewallConst.OFF_RADIO)
        
    def selectAction(self, p_action):
        self.util.tap(IPv6FirewallConst.ACTION)
        if p_action.lower() == 'allow':
            self.util.tap(waitForObject(IPv6FirewallConst.ALLOW))
        elif p_action.lower() == 'deny':
            self.util.tap(waitForObject(IPv6FirewallConst.DENY))

    
    def editRemoteIpv6(self, p_remoteIpv6):
        self.util.setText(IPv6FirewallConst.REMOTE_IPV6, p_remoteIpv6)
        
    def editProtocol(self, p_protocol):
        self.util.tap(IPv6FirewallConst.PROTOCOL)
        if p_protocol.lower() == 'ipv6':
            self.util.tap(waitForObject(IPv6FirewallConst.IPV6))
        elif p_protocol.lower() == 'icmpv6':
            self.util.tap(waitForObject(IPv6FirewallConst.ICMPV6))
        elif p_protocol.lower() == 'tcp':
            self.util.tap(waitForObject(IPv6FirewallConst.TCP))            
        elif p_protocol.lower() == 'udp':
            self.util.tap(waitForObject(IPv6FirewallConst.UDP))            
        
        
    def editPrefix(self, p_prefix):
        self.util.setText(IPv6FirewallConst.WILDCARD_MASK, p_prefix)
    
    def editRemotePort(self, p_remotePort):
        self.util.setText(IPv6FirewallConst.REMOTE_PORT, p_remotePort)
        
    def editLocalPort(self, p_localPort):
        self.util.setConsoleText(IPv6FirewallConst.LOCAL_PORT, p_localPort)
        
    def selectFirewallRule(self, p_rule):
        self.util.tap(IPv6FirewallConst.FIREWALL_RULE)
        '''This needs to be finished later'''
        
    def createRule(self, p_action, p_remoteIP, p_protocol, p_prefix, p_remotePort, p_localPort, p_saveYesNo):
        if p_action:
            self.selectAction(p_action)
        if p_remoteIP:
            self.editRemoteIpv6(p_remoteIP)
        if p_protocol:
            self.editProtocol(p_protocol)
        if p_prefix:
            self.editPrefix(p_prefix)
        if p_remotePort:
            self.editRemotePort(p_remotePort)
        if p_localPort:
            self.editLocalPort(p_localPort)
        self.util.tap(IPv6FirewallConst.ADD)
        if str(p_saveYesNo).lower().startswith('y'):
            self.util.tap(IPv6FirewallConst.SAVE)
    
    def removeRule(self, p_rule):
        self.util.tap(IPv6FirewallConst.FIREWALL_RULE)
        '''Need to figure out how to select a specific rule and then add
        a line to select p_rule'''
        self.util.tap(IPv6FirewallConst.REMOVE)
            
class Ftp:
    def __init__(self):
        self.util = util
        pass
    
    def editUsername(self, p_username):
        self.util.setText(FtpConst.USERNAME, p_username)
        
    def editPassword(self, p_password):
        self.util.setText(FtpConst.PASSWORD, p_password)
    
    def serviceOn(self):
        self.util.tap(FtpConst.ON)
    
    def serviceOff(self):
        self.util.tap(FtpConst.OFF)
        
    #@summary: This sets the permissions
    #@param p_write, p_read, p_delete, p_rename, p_list: These all take a boolean value. An empty string can also be used to represent
    #                                                    False while a string with any text can represent true. 0 and 1 will work also.
    def setPermissions(self, p_write, p_read, p_delete, p_rename, p_list):
        if p_write == True:
            self.util.tap(FtpConst.WRITE)
        if p_read == True:
            self.util.tap(FtpConst.READ)
        if p_delete == True:
            self.util.tap(FtpConst.DELETE)
        if p_rename == True:
            self.util.tap(FtpConst.RENAME)
        if p_list == True:
            self.util.tap(FtpConst.LIST)
    
    def addUser(self):
        self.util.tap(FtpConst.ADD_BUTTON)
    
    def deleteUser(self, p_username):
        #this function needs to be edite 7/15/14 -Abbas
        user = self.util.findTag(FtpConst.USER_LIST, 'DIV', p_username)
        self.util.tap(user)
        self.util.tap(FtpConst.DELETE_BUTTON)
        pass
    
    def saveUserInfo(self):
        self.util.tap(FtpConst.SAVE_BUTTON)
    
    def removeFile(self, p_filename):
        '''This will be implemented later'''
        pass
    
    def createUser(self, p_username, p_password, p_write, p_read, p_delete, p_rename, p_list):
        self.editUsername(p_username)
        self.editPassword(p_password)
        self.setPermissions(p_write, p_read, p_delete, p_rename, p_list)
        self.addUser()
        
class Http:
    def __init__(self):
        self.util = util
        pass
    
    def serviceHttpOn(self):
        self.util.tap(HttpConst.HTTP_ON)
    
    def serviceHttpOff(self):
        self.util.tap(HttpConst.HTTP_OFF)
    
    def serviceHttpsOn(self):
        self.util.tap(HttpConst.HTTPS_ON)
    
    def serviceHttpsOff(self):
        self.util.tap(HttpConst.HTTPS_OFF)
        
    def editFileName(self, p_filename):
        self.util.setText(HttpConst.FILE_NAME, p_filename)
    
    def editPageContent(self, p_content):
        self.util.setText(HttpConst.FILE_CONTENT, p_content)
    
    def pageForward(self):
        self.util.tap(HttpConst.FORWARD_PAGE)
    
    def pageBack(self):
        self.util.tap(HttpConst.BACK_PAGE)
    
    def pageAdd(self):
        self.util.tap(HttpConst.ADD_PAGE)
        
    def pageEdit(self):
        self.util.tap(HttpConst.EDIT_PAGE)
    
    def pageDel(self):
        self.util.tap(HttpConst.REMOVE_PAGE)
        
    def submit(self):
        self.util.tap(HttpConst.SUBMIT_BUTTON)  
    
class IPConfiguration:
    def __init__(self):
        self.util = util
        pass
    
    def setDhcp(self):
        self.util.tap(IPconfigConst.DHCP_RADIO)
        snooze(1)
        self.submit()
    
    def setStatic(self):
        self.util.tap(IPconfigConst.STATIC_RADIO)
        snooze(1)
            
    def changeInterface(self, p_int = None):
        util.tap(IPconfigConst.INTERFACE_DROPDOWN)
        self.util.tap(":" + p_int + "_HTML_Object")    
        
    def editIp(self, p_ip):
        self.util.setText(IPconfigConst.IP_EDIT, p_ip)
    
    def editSubnet(self, p_sub):
        self.util.setText(IPconfigConst.SUBNET_EDIT, p_sub)
    
    def editGateway(self, p_gate):
        self.util.setText(IPconfigConst.GATEWAY_EDIT, p_gate)
    
    def editDns(self, p_dns):
        self.util.setText(IPconfigConst.DNS_EDIT, p_dns)
        
    def submit(self):
        self.util.tap(IPconfigConst.SUBMIT_BUTTON)
        
    def setIpConfig(self, p_ip = None, p_sub = None, p_gate = None, p_dns = None):
        self.setStatic()
        if p_ip:
            self.editIp(p_ip)
        if p_sub:
            self.editSubnet(p_sub)
        if p_gate:
            self.editGateway(p_gate)
        if p_dns:
            self.editDns(p_dns)
        if waitForObject(UtilConst.KeyboardConst.ANDROID_KEYBOARD).visible:
            util.hideAndroidKeyboard()
        self.submit()
    
    def checkIp(self, p_ip):
        from API.Android.SquishSyntax import SquishSyntax
        squish = SquishSyntax()
        currentIpAddress = self.util.getTextInputValue(IPconfigConst.IP_EDIT)
        squish.textCheckPoint(currentIpAddress, p_ip)
        
    def checkSubnet(self, p_subnet):
        from API.Android.SquishSyntax import SquishSyntax
        squish = SquishSyntax()
        currentSubnet = self.util.getTextInputValue(IPconfigConst.SUBNET_EDIT)
        squish.textCheckPoint(currentSubnet, p_subnet)
        
    def checkGateway(self, p_gateway):
        from API.Android.SquishSyntax import SquishSyntax
        squish = SquishSyntax()
        currentIpAddress = self.util.getTextInputValue(IPconfigConst.GATEWAY_EDIT)
        squish.textCheckPoint(currentIpAddress, p_gateway)
        
    def checkDns(self, p_dns):
        from API.Android.SquishSyntax import SquishSyntax
        squish = SquishSyntax()
        currentIpAddress = self.util.getTextInputValue(IPconfigConst.DNS_EDIT)
        squish.textCheckPoint(currentIpAddress, p_dns)
        
class IPv6Configuration:
    def __init__(self):
        self.util = util
        pass
       
    def setDhcp(self):
        self.util.tap(IPv6ConfigConst.DHCP_RADIO)
        snooze(1)
        self.submit()
    
    def setAutoConfig(self):
        self.util.tap(IPv6ConfigConst.AUTOCONFIG_RADIO)
        snooze(1)
        self.submit()
    
    def setStatic(self):
        self.util.tap(IPv6ConfigConst.STATIC_RADIO)
    
    def editIpv6(self, p_ipv6Add):
        self.util.setText(IPv6ConfigConst.IPV6_EDIT, p_ipv6Add)
    
    def editSubnet(self, p_sub):
        self.util.setText(IPv6ConfigConst.IPV6_PREFIX_EDIT, p_sub)
        
    def editLinkLocal(self, p_linkLocal):
        self.util.setText(IPv6ConfigConst.LINK_LOCAL_EDIT, p_linkLocal)
    
    def editGateway(self, p_gate):
        self.util.setText(IPv6ConfigConst.GATEWAY_EDIT, p_gate)
    
    def editDns(self, p_dns):
        self.util.setText(IPv6ConfigConst.DNS_EDIT, p_dns)
    
    def submit(self):
        self.util.tap(IPv6ConfigConst.SUBMIT_BUTTON)
        
    def setIpv6Config(self, p_ipv6Add, p_sub, p_gate, p_dns = None, p_linkLocal = None):
        self.setStatic()
        self.editIpv6(p_ipv6Add)
        snooze(1)
        self.editSubnet(p_sub)
        snooze(1)
        if p_linkLocal:
            self.editLinkLocal(p_linkLocal)
            snooze(1)
        self.editGateway(p_gate)
        snooze(1)
        if p_dns:
            self.editDns(p_dns)
            snooze(1)
        self.submit()

    def checkIpv6(self, p_ip):
        from API.Android.SquishSyntax import SquishSyntax
        squish = SquishSyntax()
        currentIpAddress = self.util.getTextInputValue(IPv6ConfigConst.IPV6_EDIT)
        squish.textCheckPoint(currentIpAddress, p_ip)

    def checkSubnet(self, p_subnet):
        from API.Android.SquishSyntax import SquishSyntax
        squish = SquishSyntax()
        currentSubnet = self.util.getTextInputValue(IPv6ConfigConst.IPV6_PREFIX_EDIT)
        squish.textCheckPoint(currentSubnet, p_subnet)
                
    def checkGateway(self, p_gateway):
        from API.Android.SquishSyntax import SquishSyntax
        squish = SquishSyntax()
        currentGateway = self.util.getTextInputValue(IPv6ConfigConst.GATEWAY_EDIT)
        squish.textCheckPoint(currentGateway, p_gateway)
                
    def checkDns(self, p_dns):
        from API.Android.SquishSyntax import SquishSyntax
        squish = SquishSyntax()
        currentDNS = self.util.getTextInputValue(IPv6ConfigConst.DNS_EDIT)
        squish.textCheckPoint(currentDNS, p_dns)
                
    def checkLinkLocal(self, p_linkLocal):
        from API.Android.SquishSyntax import SquishSyntax
        squish = SquishSyntax()
        currentLinkLocal = self.util.getTextInputValue(IPv6ConfigConst.LINK_LOCAL_EDIT)
        squish.textCheckPoint(currentLinkLocal, p_linkLocal)
                
class MacFilter:
    def __init__(self):
        self.util = util
        pass
    
    def MacFilter_On(self):
        self.util.tap(MAC_Address_FilterConst.MAC_FILTER_ENABLED)
    
    def MacFilter_Off(self):
        self.util.tap(MAC_Address_FilterConst.MAC_FILTER_DISABLED)
        
    def preventAccess(self):
        self.util.tap(MAC_Address_FilterConst.PREVENT_ACCESS)
    
    def allowAccess(self):
        self.util.tap(MAC_Address_FilterConst.ALLOW_ACCESS)
    
    #there are 50 fields to enter a mac address. what is most efficient way to do this?
    def setMacAddress(self):
        pass 
        
    def submit(self):
        self.util.tap(MAC_Address_FilterConst.SUBMIT_BUTTON)
    
class Netflow:
    def __init__(self):
        pass
     
class Syslog:
    def __init__(self):
        self.util = util
        pass
    
    def serviceOn(self):
        self.util.tap(SyslogConst.ON)
       
class Ntp:
    def __init__(self):
        self.util = util
        pass
    
    def serviceOn(self):
        self.util.tap(NtpConst.ON)
    
    def serviceOf(self):
        self.util.tap(NtpConst.OFF)
    
    def authenticationEnable(self):
        self.util.tap(NtpConst.ENABLE)
    
    def authenticationDisable(self):
        self.util.tap(NtpConst.DISABLE)
        
    def editKey(self, p_key):
        self.util.setText(NtpConst.KEY, p_key)
    
    def editPassword(self, p_password):
        self.util.setText(NtpConst.PASSWORD, p_password)
        
    def setDate(self, p_month, p_date, p_year):
        self.util.tap(NtpConst.DATE)
        snooze(2)
        if p_month:
            self.util.tap(':' + p_month + "_HTML_Object")
        if p_date:
            self.util.tap(':' + p_date + "_HTML_Object")
        if p_year:
            self.util.tap(":" + p_year + "_HTML_Object")
        
        doneObj = self.util.findTag(":ext-datepicker-1_HTML_Object", 'DIV', 'Done')
        self.util.tap(doneObj)
    
    def addHour(self, p_hour):
        plusObj = self.util.findTag(NtpConst.HOUR, 'DIV', '\+')
        
        for i in range (p_hour):
            self.util.tap(plusObj)
        
    def minusHour(self, p_hour):
        minusObj = self.util.findTag(NtpConst.HOUR, 'DIV', '\-')
        
        for i in range (p_hour):
            self.util.tap(minusObj)
    
    def addMin(self, p_minute):  
        plusObj = self.util.findTag(NtpConst.MIN, 'DIV', '\+')
        
        for i in range (p_minute):
            self.util.tap(plusObj)
    
    def minusMin(self, p_minute):
        minusObj = self.util.findTag(NtpConst.MIN, 'DIV', '\-')
        
        for i in range (p_minute):
            self.util.tap(minusObj)
    
    def addSec(self, p_second):
        addObj = self.util.findTag(NtpConst.SEC, 'DIV', '\+')
        
        for i in range (p_second):
            self.util.tap(addObj)
            
    def minusSec(self, p_second):
        minusObj = self.util.findTag(NtpConst.SEC, 'DIV', '\-')
        
        for i in range (p_second):
            self.util.tap(minusObj)
    
    def applyChanges(self):
        self.util.tap(NtpConst.APPLY_CHANGES_BUTTON)
    
    def configureNtp(self, p_date, p_hour, p_minute, p_second, p_key, p_password):
        self.serviceOn()
        self.setTime(p_date, p_hour, p_minute, p_second)
        if p_key:
            self.authenticationEnable()
            self.editKey(p_key)
        if p_password:
            self.editPassword(p_password)
            
class PCWireless:
    def __init__(self):
        self.util = util
    
    def editMac(self, p_mac):
        self.util.setText(PcWirelessConst.WirelessInterface.MAC_ADDRESS, p_mac)
    
    def editSSID(self, p_ssid):
        self.util.setText(PcWirelessConst.WirelessInterface.SSID, p_ssid)
    
    def portOn(self):
        self.util.tap(PcWirelessConst.WirelessInterface.PORT_ON_OFF)
        #Need to add tapping of on button
    
    def portOff(self):
        self.util.tap(PcWirelessConst.WirelessInterface.PORT_ON_OFF)
        #Need to add tapping of off button
    
    def setDisabled(self):
        self.util.tap(PcWirelessConst.Authentication.SECURITY_MODE)
        snooze(1)
        self.util.tap(PcWirelessConst.Authentication.DISABLED_RADIO)
    
    def setWep(self):
        self.util.tap(PcWirelessConst.Authentication.SECURITY_MODE)
        snooze(1)
        self.util.tap(PcWirelessConst.Authentication.WEP)
    
    def setWpaPsk(self):
        self.util.tap(PcWirelessConst.Authentication.SECURITY_MODE)
        snooze(1)
        self.util.tap(PcWirelessConst.Authentication.WPA_PSK)
    
    def setWpa2Psk(self):
        self.util.tap(PcWirelessConst.Authentication.SECURITY_MODE)
        snooze(1)
        self.util.tap(PcWirelessConst.Authentication.WPA2_PSK)
    
    def setWpa(self):
        self.util.tap(PcWirelessConst.Authentication.SECURITY_MODE)
        snooze(1)
        self.util.tap(PcWirelessConst.Authentication.WPA)
    
    def setWpa2(self):
        self.util.tap(PcWirelessConst.Authentication.SECURITY_MODE)
        snooze(1)
        self.util.tap(PcWirelessConst.Authentication.WPA2)
    
    def editKey(self, p_key):
        self.util.setText(PcWirelessConst.Authentication.KEY, p_key)
    
    def editKeyPhrase(self, p_keyPhrase):
        self.util.setText(PcWirelessConst.Authentication.KEY_PHRASE, p_keyPhrase)
        
    def editUserId(self, p_userId):
        self.util.setText(PcWirelessConst.Authentication.USER_ID, p_userId)
    
    def editPassword(self, p_password):
        self.util.setText(PcWirelessConst.Authentication.PASSWORD, p_password)
        
    def configureWepAuthentication(self, p_key):
        self.setWep()
        self.editKey(p_key)
        
    def configureWpaAuthentication(self, p_userId, p_password):
        self.setWpa()
        self.editUserId(p_userId)
        self.editPassword(p_password)
        
    def configureWpa2Authentication(self, p_keyPhrase):
        self.setWpa2()
        self.editUserId(p_userId)
        self.editPassword(p_password)
        
    def configureWpaPskAuthentication(self, p_keyPhrase):
        self.setWpaPsk()
        self.editKeyPhrase(p_keyPhrase)
    
    def submit(self):
        self.util.tap(PcWirelessConst.Authentication.SUBMIT_BUTTON)
    
    def configureWpa2PskAuthentication(self, p_keyPhrase):
        self.setWpa2Psk()
        self.editKeyPhrase(p_keyPhrase)
        
    def setEncryptionAES(self):
        self.util.tap(PcWirelessConst.Authentication.ENCRYPTION_DROPDOWN)
        snooze(1)
        self.util.tap(PcWirelessConst.Authentication.AES)
        
    def setEncryptionTKIP(self):
        self.util.tap(PcWirelessConst.Authentication.ENCRYPTION_DROPDOWN)
        snooze(1)
        self.util.tap(PcWirelessConst.Authentication.TKIP)

class PPPoE_Dialer:
    def __init__(self):
        self.util = util
        pass
    
    def editUsername(self, p_username):
        self.util.setText(PPPoEConst.USERNAME, p_username)
    
    def editPassword(self, p_password):
        self.util.setText(PPPoEConst.PASSWORD, p_password)
    
    def connect(self, p_username, p_password):
        self.editUsername(p_username)
        self.editPassword(p_password)
        self.util.tap(PPPoEConst.CONNECT_BUTTON)
        
class Terminal:
    def __init__(self):
        self.util = util
        self.setTerminalText = CliBase().setCliTextByKeyboard
        self.setTerminalTextNoReturn = CliBase().setCliTextByKeyboardNoReturn

    def textCheckPoint(self, p_text, p_occurrenceNum = -1):
        self.util.textCheckPoint(TerminalConst.CLI_CONSOLE, p_text, p_occurrenceNum)    
    
    def setBps(self, p_bps):
        self.util.tap(TerminalConst.Setup.BPS)
        '''This needs completed later once object names are assigned to terminal items'''
    
    def setDataBits(self, p_dataBits):
        self.util.tap(TerminalConst.Setup.DATA_BITS)
        '''This needs completed later once object names are assigned to terminal items'''
    
    def setParity(self, p_parity):
        self.util.tap(TerminalConst.Setup.PARITY)
        '''This needs completed later once object names are assigned to terminal items'''
    
    def setStopBits(self, p_stopBits):
        self.util.tap(TerminalConst.Setup.STOP_BITS)
        '''This needs completed later once object names are assigned to terminal items'''
    
    def setFlowControl(self, p_flowControl):
        self.util.tap(TerminalConst.Setup.FLOW_CONTROL)
        '''This needs completed later once object names are assigned to terminal items'''
    
    def pressOk(self):
        self.util.tap(TerminalConst.Setup.SUBMIT)
        
    def setupTerminal(self, p_bps, p_dataBits, p_parity, p_stopBits, p_flowControl):
        if p_bps:
            self.setBps(p_bps)
        if p_dataBits:
            self.setDataBits(p_dataBits)
        if p_parity:
            self.setParity(p_parity)
        if p_stopBits:
            self.setStopBits(p_stopBits)
        if p_flowControl:
            self.setFlowControl(p_flowControl)
        self.util.tap(TerminalConst.Setup.SUBMIT)
        
class TextEditor:
    def __init__(self):
        self.util = util
        pass
    
    def tapOpen():
        self.util.tap()
        
    def saveText():
        pass
        
class Tftp:
    def __init__(self):
        self.util = util
        pass
    
    def serviceOn(self):
        self.util.tap(TftpConst.ON)
    
    def serviceOff(self):
        self.util.tap(TftpConst.OFF)
    
    def removeFile(self, p_filename):
        '''This wont work as is. The self.util.tap(p_filename) is just a place holder until
        I figure out how to select items in a list'''
        self.util.tap(p_filename)
        self.util.tap(TftpConst.REMOVE_BUTTON)    
            
class VPN:
    def __init__(self):
        self.util = util
        pass

    def editGroupName(self, p_groupName):
        self.util.setText(VPNConst.GROUP_NAME, p_groupName)
    
    def editGroupKey(self, p_groupKey):
        self.util.setText(VPNConst.GROUP_KEY, p_groupKey)
    
    def editHostIp(self, p_ip):
        self.util.setText(VPNConst.HOST_IP, p_ip)
        
    def editUsername(self, p_username):
        self.util.setText(VPNConst.USERNAME, p_username)
    
    def editPassword(self, p_pass):
        self.util.setText(VPNConst.PASSWORD, p_pass)
        
    def pressConnect(self):
        self.util.tap(VPNConst.CONNECT_BUTTON)
        
    def connect(self, p_groupName, p_groupKey, p_ip, p_username, p_pass):
        if p_groupName:
            self.editGroupName(p_groupName)
        if p_groupKey:
            self.editGroupKey(p_groupKey)
        if p_ip:
            self.editHostIp(p_ip)
        if p_username:
            self.editUsername(p_username)
        if p_pass:
            self.editPassword(p_pass)
        self.pressConnect()

class WAN_Provider:
    def __init__(self):
        self.util = util
        pass
    
    def selectInterface(self, p_interface):
        self.util.tap(WAN_ProviderConst.INTERFACE, p_interface)
    
    def selectDSL(self):
        self.util.tap(WAN_ProviderConst.DSL)
        
    def selectCable(self):
        self.util.tap(WAN_ProviderConst.Cable)
    
    def selectProvider(self, p_provider):
        self.util.tap(WAN_ProviderConst.PROVIDER, p_provider)
        
    def selectFromPort(self, p_fromPort):
        self.util.tap(WAN_ProviderConst.FROM_PORT, p_fromPort)
    
    def selectToPort(self, p_toPort):
        self.util.tap(WAN_ProviderConst.TO_PORT, p_toPort)
        
    def addProvider(self):
        self.util.tap(WAN_ProviderConst.ADD_BUTTON)
    
    def removeProvider(self, p_entry):
        self.util.tap(WAN_ProviderConst.PROVIDER_TABLE, p_entry)
        self.util.tap(WAN_ProviderConst.REMOVE_BUTTON)
        
class WebBrowser:
    def __init__(self):
        self.util = util
        pass
    
    def back(self):
        self.util.tap(WebBrowserConst.BACK)
    
    def forward(self):
        self.util.tap(WebBrowserConst.FORWARD)
    
    def editUrl(self, p_url):
        self.util.setText(WebBrowserConst.URL_EDIT, p_url)
    
    def go(self):
        self.util.tap(WebBrowserConst.GO)
    
    def goToUrl(self, p_url):
        self.editUrl(p_url)
        snooze(1)
        self.go()
        
    #@summary: Used to clear the URL if it already has an address in it
    #@param p_currentUrlText: 
    def clearUrl(self, p_currentUrlText = 50):
        self.util.tap(WebBrowserConst.URL_EDIT)
        try:
            urlLength = len(p_currentUrlText) + 1
        except:
            urlLength = p_currentUrlText
        for i in range(urlLength):
            self.util.typeTextSE(WebBrowserConst.URL_EDIT, '<Backspace>')
            
    def textCheckPoint(self, p_text, p_occurrenceNum = -1):
        try:
            self.util.textCheckPoint(WebBrowserConst.CONTENT_AREA, p_text, p_occurrenceNum)
        except:
            self.util.textCheckPoint(WebBrowserConst.DIALOG_CONTENT, p_text, p_occurrenceNum)


class WirelessManagement:
    def __init__(self):
        self.util = util
        pass
    
    def setRouterPass(self, p_password):
        self.util.setText(Wireless_Admin_MgmtConst.ROUTER_PASSWORD, p_password)
    
    def confirmRouterPass(self, p_password):
        self.util.setText(Wireless_Admin_MgmtConst.REENTER_PASSWORD, p_password)
    
    def enableRemote(self):
        self.util.tap(Wireless_Admin_MgmtConst.REMOTE_MANAGEMENT_ENABLED)
        
    def disableRemote(self):
        self.util.tap(Wireless_Admin_MgmtConst.REMOTE_MANAGEMENT_DISABLED)
        
    def submit(self):
        self.util.tap(Wireless_Admin_MgmtConst.SUBMIT_BUTTON)
    

class WirelessSecurity:
    def __init__(self):
        self.util = util
        pass
    
    def setSecurityMode(self, p_securityMode):
        if p_securityMode == 'Disabled':
            p_securityMode = Wireless_SecurityConst.DISABLED
        elif p_securityMode == 'WEP':
            p_securityMode = Wireless_SecurityConst.WEP
        elif p_securityMode == 'WPA Personal':
            p_securityMode = Wireless_SecurityConst.WPA_PERSONAL
        elif p_securityMode == 'WPA Enterprise':
            p_securityMode = Wireless_SecurityConst.WPA_ENTERPRISE
        elif p_securityMode == 'WPA2 Personal':
            p_securityMode = Wireless_SecurityConst.WPA2_PERSONAL
        else:
            p_securityMode = Wireless_SecurityConst.WPA2_ENTERPRISE
             
        self.util.tap(Wireless_SecurityConst.SECURITY_MODE)
        snooze(1)
        self.util.tap(p_securityMode)
            
    def setWpa2PersonalEncryptionAES(self):
        self.util.tap(Wireless_SecurityConst.WPA2_PERSONAL_ENCRYPTION)
        snooze(1)
        self.util.tap(Wireless_SecurityConst.AES)
        
    def setWpa2PersonalEncryptionTKIP(self):
        self.util.tap(Wireless_SecurityConst.WPA2_PERSONAL_ENCRYPTION)
        snooze(1)
        self.util.tap(Wireless_SecurityConst.AES)
    
    def setKey(self, p_key):
        self.util.setText(Wireless_SecurityConst.WPA_PERSONAL_PASSPHRASE, p_key)
    
    def configureWEP(self, p_securityMode, p_encryption, p_key):
        self.setSecurityMode(p_securityMode)
        self.util.tap(Wireless_SecurityConst.WEP_ENCRYPTION, p_encryption)
        self.util.setText(Wireless_SecurityConst.WEP_KEY1, p_key)
        self.submit()
        
    def configureWPA_Personal(self, p_securityMode, p_encryption, p_passphrase):
        self.setSecurityMode(p_securityMode)
        self.util.tap(Wireless_SecurityConst.WPA_PERSONAL_ENCRYPTION, p_encryption)
        self.util.setText(Wireless_SecurityConst.WPA_PERSONAL_PASSPHRASE, p_passphrase)
        self.submit()
        
    def configureWPA_Enterprise(self, p_securityMode, p_encryption, p_radius, p_secret):
        self.setSecurityMode(p_securityMode)
        self.util.tap(Wireless_SecurityConst.WPA_ENTERPRISE_ENCRYPTION, p_encryption)
        self.util.tap(Wireless_SecurityConst.WPA_ENTERPRISE_RADIUS, p_radius)
        self.util.setText(Wireless_SecurityConst.WPA_ENTERPRISE_SECRET, p_secret)
        self.submit()
    
    def configureWPA2_Personal(self, p_securityMode, p_encryption, p_passphrase):
        self.setSecurityMode(p_securityMode)
        self.util.tap(Wireless_SecurityConst.WPA2_PERSONAL_ENCRYPTION, p_encryption)
        self.util.setText(Wireless_SecurityConst.WPA2_PERSONAL_PASSPHRASE, p_passphrase)
        self.submit()
    
    def configureWPA2_Enterprise(self, p_securityMode, p_encryption, p_radius, p_secret):
        self.setSecurityMode(p_securityMode)
        self.util.tap(Wireless_SecurityConst.WPA2_ENTERPRISE_ENCRYPTION, p_encryption)
        self.util.tap(Wireless_SecurityConst.WPA2_ENTERPRISE_RADIUS, p_radius)
        self.util.setText(Wireless_SecurityConst.WPA2_ENTERPRISE_SECRET, p_secret)
        self.submit()
        
    def submit(self):
        self.util.tap(Wireless_SecurityConst.SUBMIT_BUTTON) 
    
    
class WirelessSetting:
    def __init__(self):
        self.util = util
        pass
        
    def setNetworkMode(self, p_NetworkMode):
        if p_NetworkMode == 'Mixed':
            p_NetworkMode = Wireless_SettingConst.MIXED
        elif p_NetworkMode == 'BG-Mixed':
            p_NetworkMode = Wireless_SettingConst.BG_MIXED
        elif p_NetworkMode == 'Wireless-G Only':
            p_NetworkMode = Wireless_SettingConst.WIRELESS_G
        elif p_NetworkMode == 'Wireless-B Only':
            p_NetworkMode = Wireless_SettingConst.WIRELESS_B
        elif p_NetworkMode == 'Wireless-N Only':
            p_NetworkMode = Wireless_SettingConst.WIRELESS_N
        else:
            p_NetworkMode = Wireless_SettingConst.DISABLED
             
        self.util.tap(Wireless_SettingConst.NETWORK_MODE)
        snooze(1)
        self.util.tap(p_NetworkMode)
        
    def setSSID(self, p_SSID):
        self.util.setText(Wireless_SettingConst.NETWORK_SSID, p_SSID)
        
    def setRadioBand(self, p_radioBand):
        if p_radioBand == 'Auto':
            p_radioBand = Wireless_SettingConst.AUTO
        elif p_radioBand == 'Standard - 20Mhz Channel':
            p_radioBand = Wireless_SettingConst.STANDARD
        else:
            p_radioBand = Wireless_SettingConst.WIDE
            
        self.util.tap(Wireless_SettingConst.RADIO_BAND)
        snooze(1)
        self.util.tap(p_radioBand)
    
    def setChannel(self, p_channel):
        self.util.tap(Wireless_SettingConst.STANDARD_CHANNEL, p_channel)
        
    def enableSSID(self):
        self.util.tap(Wireless_SettingConst.SSID_BROADCAST_ON)
    
    def disableSSID(self):
        self.util.tap(Wireless_SettingConst.SSID_BROADCAST_OFF)
        
    def submit(self):
        self.util.tap(Wireless_SettingConst.SUBMIT_BUTTON)
        
class WirelessStatus:
    def __init__(self):
        self.util = util
        pass
    #the wireless status constants still need object ids
    def IP_Release(self):
        self.util.tap(Wireless_StatusConst.IP_ADD_RELEASE)
    
    def IP_Renew(self):
        self.util.tap(Wireless_StatusConst.IP_ADD_RENEW)
        
    def IP_Refresh(self):
        self.util.tap(Wireless_StatusConst.IP_REFRESH)
        
class APPortSetup:
    def __init__(self):
        self.util = util
        pass
    
    def submit(self):
        self.util.tap(PortSetup.SUBMIT_BUTTON)
    
    def setSSID(self, p_SSID):
        self.util.setText(PortSetup.SSID, p_SSID)
    
    def setWEP(self, p_key):
        self.util.tap(PortSetup.WEP)
        self.util.setText(PortSetup.WEP_KEY, p_key)
        self.submit()
        
    def setWPA_PSK(self, p_key):
        self.util.tap(PortSetup.WPA_PSK)
        self.util.setText(PortSetup.PSK_PASSPHRASE, p_key)
        self.submit()
        
    def setWPA2_PSK(self, p_key):
        self.util.tap(PortSetup.WPA2_PSK)
        self.util.setText(PortSetup.PSK_PASSPHRASE, p_key)
        self.submit()
        
class BackboneSetup:
    def __init__(self):
        self.util = util
        pass
    
    def submit(self):
        self.util.tap(BackboneInterfaceConst.SUBMIT_BUTTON)
        
    def setIPaddress(self, p_address):
        self.util.setText(BackboneInterfaceConst.IP_ADDRESS, p_address)
        
    def setSubnet(self, p_subnet):
        self.util.setText(BackboneInterfaceConst.SUBNET_MASK, p_subnet)
        
    def setGateway(self, p_gateway):
        self.util.setText(BackboneInterfaceConst.DEFAULT_GATEWAY, p_gateway)
        
    def setDNS(self, p_dns):
        self.util.setText(BackboneInterfaceConst.DNS_SERVER, p_dns)
        
    def BackboneConfig(self, p_address, p_subnet, p_gateway, p_dns):
        self.util.tap(BackboneInterfaceConst.STATIC_BUTTON)
        self.setIPaddress(p_address)
        self.setSubnet(p_subnet)
        self.setGateway(p_gateway)
        self.setDNS(p_dns)
        self.submit()
        
class COServerDHCP:
    def __init__(self):
        self.util = util
        pass
    
    def setStartIp(self):
        pass
    
    def setMaxUsers(self):
        pass
    
    def setDNS(self):
        pass
    
    def submit(self):
        self.util.tap(COServerDhcpConst.SUBMIT_BUTTON)
		
class SnifferList:
    def __init__(self):
        self.util = util
        pass
    
    def editFilter(self):
        self.util.tap(SnifferConst.EDIT_FILTER)

