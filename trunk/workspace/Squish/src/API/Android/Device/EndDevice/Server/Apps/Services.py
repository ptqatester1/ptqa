#**************************************************************************
#@author: Thi Nguyen
#@summary: Config handles activities on the Config tab of Server
#**************************************************************************
from API.Device.EndDevice.Server import ServerConst
from API.Device.DeviceBase import ConfigBase
from API.Device.DeviceBase import ServicesBase
class Services(ServicesBase): 
    def __init__(self):
        self.squishName = ""
    
    #@summary: update the actual name of object that squish uses to reference
    #@param p_squishName: display name of the device        
    def updateName(self, p_squishName):
        self.squishName = p_squishName
        super(Services, self).updateName(self.squishName)
        
    #@summary: set dhcp domain name
    #@param p_domain: domain name        
    def setDhcpDNS(self, p_domain):
        obj = ServerConst.Services.DHCP_DNS
        self.setText(obj, p_domain)        

    #@summary: set dhcp 1st octet of IP
    #@param p_ip: ip octet         
    def setDhcpStartIp1(self, p_ip):
        obj = ServerConst.Services.DHCP_EDIT_START_IP_1
        self.setText(obj, p_ip)          

    #@summary: set dhcp 2nd octet of IP
    #@param p_ip: ip octet 
    def setDhcpStartIp2(self, p_ip):
        obj = ServerConst.Services.DHCP_EDIT_START_IP_2
        self.setText(obj, p_ip)  

    #@summary: set dhcp 3rd octet of IP
    #@param p_ip: ip octet 
    def setDhcpStartIp3(self, p_ip):
        obj = ServerConst.Services.DHCP_EDIT_START_IP_3
        self.setText(obj, p_ip)  

    #@summary: set dhcp 4th octet of IP
    #@param p_ip: ip octet 
    def setDhcpStartIp4(self, p_ip):
        obj = ServerConst.Services.DHCP_EDIT_START_IP_4
        self.setText(obj, p_ip)  
        
    #@summary: set dhcp maximum number of user
    #@param p_max: max number 
    def setDhcpMaxUser(self, p_max):
        obj = ServerConst.Services.DHCP_EDIT_MAX_USER
        self.setText(obj, p_max)
        
    #@summary: set DHCPv6 On/Off
    #@param p_enable: True or False
    def setDhcpv6Enable(self, p_enable):
        if(p_enable):
            self.clickButton(ServerConst.Services.DHCP_V6_ON)
        else:
            self.clickButton(ServerConst.Services.DHCP_V6_OFF)
            
    #@summary: create a new dhcpv6 pool
    #@param p_name: pool name
    #@param p_dnsName: DNS Server
    #@param p_domainName: Domain Name
    #@param p_ipv6Add: Ipv6 address
    #@param p_ipv6Subnet: Ipv6 subnet
    #@param p_DUID: DHCPv6 Unique Identifier
    #@param p_localPoolName: Name of local pool 
    #@param p_validLifeTime: Valid lifetime for the ipv6 prefix
    #@param p_preferredLifeTime: Preferred lifetime for the ipv6 prefix
    #@param p_localValidLifeTime: Valid lifetime for the local pool
    #@param p_localPreferredLifeTime: Preferred lifetime for the local pool
    def addNewDhcpv6Pool(self, p_name, p_dnsName, p_domainName, p_ipv6Add, p_ipv6Subnet, p_DUID, p_localPoolName, p_validLifeTime = "2592000", p_preferredLifeTime = "640800", p_localValidLifeTime = "2592000", p_localPreferredLifeTime = "604800"):
        self.clickButton(ServerConst.Services.DHCP_V6_CREATE_POOL)
        self.setText(ServerConst.Services.DHCP_Pool_Config.POOL_NAME, p_name)
        self.setText(ServerConst.Services.DHCP_Pool_Config.DNS_NAME, p_dnsName)
        self.setText(ServerConst.Services.DHCP_Pool_Config.DOMAIN_NAME, p_domainName)
        self.setText(ServerConst.Services.DHCP_Pool_Config.IPV6_LINE1, p_ipv6Add)
        self.setText(ServerConst.Services.DHCP_Pool_Config.IPV6_LINE2, p_ipv6Subnet)
        self.setText(ServerConst.Services.DHCP_Pool_Config.DUID, p_DUID)
        self.setText(ServerConst.Services.DHCP_Pool_Config.LOCAL_POOL_NAME, p_localPoolName)
        self.setText(ServerConst.Services.DHCP_Pool_Config.VALID_LIFETIME, p_validLifeTime)
        self.setText(ServerConst.Services.DHCP_Pool_Config.PREFERRED_LIFETIME, p_preferredLifeTime)
        self.setText(ServerConst.Services.DHCP_Pool_Config.VALID_POOL_LIFETIME, p_localValidLifeTime)
        self.setText(ServerConst.Services.DHCP_Pool_Config.PREFERRED_POOL_LIFETIME, p_localPreferredLifeTime)
        self.clickButton(ServerConst.Services.DHCP_Pool_Config.SAVE_BUTTON)
        
    #@summary: Add a new local pool
    def addNewLocalPool(self, p_poolName, p_prefix, p_subnet, p_prefixLength):
        self.clickButton(ServerConst.Services.DHCP_V6_LOCAL_CREATE_BUTTON)
        self.setText(ServerConst.Services.DHCP_Local_Config.LOCAL_POOL, p_poolName)
        self.setText(ServerConst.Services.DHCP_Local_Config.POOL_PREFIX_LINE1, p_prefix)
        self.setText(ServerConst.Services.DHCP_Local_Config.POOL_PREFIX_LINE2, p_subnet)
        self.setText(ServerConst.Services.DHCP_Local_Config.PREFIX_LENGTH, p_prefixLength)
        self.clickButton(ServerConst.Services.DHCP_Local_Config.SAVE_BUTTON)
        
    #@summary: add dhcp pool
    def addDhcpPool(self, p_name, p_gateway, p_dns, p_startIP1, p_startIP2, p_startIP3, p_startIP4, p_subnet1, p_subnet2, p_subnet3, p_subnet4, p_maxUsers):
        obj = ServerConst.Services.DHCP_POOL_NAME_EDIT
        self.setText(obj, p_name)
        obj = ServerConst.Services.DHCP_GATEWAY
        self.setText(obj, p_gateway)
        obj = ServerConst.Services.DHCP_DNS
        self.setText(obj, p_dns)
        obj = ServerConst.Services.DHCP_EDIT_START_IP_1
        self.setText(obj, p_startIP1)
        obj = ServerConst.Services.DHCP_EDIT_START_IP_2
        self.setText(obj, p_startIP2)
        obj = ServerConst.Services.DHCP_EDIT_START_IP_3
        self.setText(obj, p_startIP3)
        obj = ServerConst.Services.DHCP_EDIT_START_IP_4
        self.setText(obj, p_startIP4)
        obj = ServerConst.Services.DHCP_EDIT_SUBNET_MASK_1
        self.setText(obj, p_subnet1)
        obj = ServerConst.Services.DHCP_EDIT_SUBNET_MASK_2
        self.setText(obj, p_subnet2)
        obj = ServerConst.Services.DHCP_EDIT_SUBNET_MASK_3
        self.setText(obj, p_subnet3)
        obj = ServerConst.Services.DHCP_EDIT_SUBNET_MASK_4
        self.setText(obj, p_subnet4)
        obj = ServerConst.Services.DHCP_EDIT_MAX_USER
        self.setText(obj, p_maxUsers)
        obj = ServerConst.Services.DHCP_ADD_NEW_BUTT
        self.clickButton(obj)

    #@summary: remove dhcp pool
    #@param p_pool: e.g. "serverPool|0.0.0.0|0.0.0.0|0.0.0.0|0.0.0.0|0"
    def removeDhcpPool(self, p_pool):
        obj = ServerConst.Services.DHCP_LIST_VIEW
        self.clickItem(obj, p_pool)
        obj = ServerConst.Services.DHCP_ADD_REMOVE_BUTT
        self.clickButton(obj)

    #@summary: set tftp file to be used
    #@param p_fileName: file name 
    def setTftpfile(self, p_fileName):
        obj = ServerConst.Services.TFTP_FILE_PATH_LIST
        self.clickItem(obj, p_fileName)

    #@summary: add domain name for DNS sever
    #@param p_domain: domain name
    #@param p_ip: ip address associate with domain name
    def addDNSDomain(self, p_domain, p_ip):
        obj = ServerConst.Services.DNS_DOMAIN_NAME
        self.setText(obj, p_domain)  
        obj = ServerConst.Services.DNS_IP_ADD
        self.setText(obj, p_ip)  
        obj = ServerConst.Services.DNS_ADD_BUTT
        self.clickButton(obj)

 
    #@summary: removeDNSDomain removes an existing domain in the Config dialog
    #@postcondition: domain is removed
    #@precondition: domain exists
    #@param: p_domain_ip: "www.cs.com|10.1.1.1"
    def removeDNSDomain(self, p_domain, p_ip):
        domain_ip_item = p_domain + "|" + p_ip
        obj = ServerConst.Services.DNS_LIST_VIEW
        self.clickItem(obj, domain_ip_item)
        obj = ServerConst.Services.DNS_REMOVE_BUTT
        self.clickButton(obj)

    def addNewPool(self, p_poolName, p_gateway, p_dns, p_ip1, p_ip2, p_ip3, p_ip4, p_mask1, p_mask2,p_mask3,p_mask4, p_max):
        self.clickButton(ServerConst.Services.DHCP_ON)
        self.setText(ServerConst.Services.DHCP_POOL_NAME_EDIT, p_poolName)
        self.setText(ServerConst.Services.DHCP_GATEWAY, p_gateway)
        self.setText(ServerConst.Services.DHCP_DNS, p_dns)
        self.setText(ServerConst.Services.DHCP_EDIT_START_IP_1, p_ip1)
        self.setText(ServerConst.Services.DHCP_EDIT_START_IP_2, p_ip2)
        self.setText(ServerConst.Services.DHCP_EDIT_START_IP_3, p_ip3)
        self.setText(ServerConst.Services.DHCP_EDIT_START_IP_4, p_ip4)        
        self.setText(ServerConst.Services.DHCP_EDIT_SUBNET_MASK_1, p_mask1)
        self.setText(ServerConst.Services.DHCP_EDIT_SUBNET_MASK_2, p_mask2)
        self.setText(ServerConst.Services.DHCP_EDIT_SUBNET_MASK_3, p_mask3)
        self.setText(ServerConst.Services.DHCP_EDIT_SUBNET_MASK_4, p_mask4)     
        self.setText(ServerConst.Services.DHCP_EDIT_MAX_USER, p_max)  
        self.clickButton(ServerConst.Services.DHCP_ADD_NEW_BUTT) 
        
    def editPool(self, p_pool, p_poolName, p_gateway, p_dns, p_ip1, p_ip2, p_ip3, p_ip4, p_mask1, p_mask2,p_mask3,p_mask4, p_max):
        obj = ServerConst.Services.DHCP_LIST_VIEW
        self.clickItem(obj, p_pool)       
        self.setText(ServerConst.Services.DHCP_POOL_NAME_EDIT, p_poolName)
        self.setText(ServerConst.Services.DHCP_GATEWAY, p_gateway)
        self.setText(ServerConst.Services.DHCP_DNS, p_dns)
        self.setText(ServerConst.Services.DHCP_EDIT_START_IP_1, p_ip1)
        self.setText(ServerConst.Services.DHCP_EDIT_START_IP_2, p_ip2)
        self.setText(ServerConst.Services.DHCP_EDIT_START_IP_3, p_ip3)
        self.setText(ServerConst.Services.DHCP_EDIT_START_IP_4, p_ip4)        
        self.setText(ServerConst.Services.DHCP_EDIT_SUBNET_MASK_1, p_mask1)
        self.setText(ServerConst.Services.DHCP_EDIT_SUBNET_MASK_2, p_mask2)
        self.setText(ServerConst.Services.DHCP_EDIT_SUBNET_MASK_3, p_mask3)
        self.setText(ServerConst.Services.DHCP_EDIT_SUBNET_MASK_4, p_mask4)     
        self.setText(ServerConst.Services.DHCP_EDIT_MAX_USER, p_max)  
        self.clickButton(ServerConst.Services.DHCP_ADD_SAVE_BUTT)
    
    def changeInterface(self, p_interfaceName):
        self.clickItem(ServerConst.Services.DHCP_INTERFACE_COMBO, p_interfaceName)
        
    def addAAAClient(self, p_client_host, p_client_ip, p_secret, p_server_type):
        self.clickButton(ServerConst.Services.AAA_ON)
        self.setText(ServerConst.Services.AAA_HOST_EDIT, p_client_host)
        self.setText(ServerConst.Services.AAA_HOST_IP_EDIT, p_client_ip)
        self.setText(ServerConst.Services.AAA_SHARED_SECRET, p_secret)
        self.clickItem(ServerConst.Services.AAA_TYPE_VALUE, p_server_type)
        self.clickButton(ServerConst.Services.AAA_ADD_CLIENT_BUTT)
        
    def addUser(self, p_username, p_password):
        self.setText(ServerConst.Services.AAA_USERNAME_EDIT, p_username)
        self.setText(ServerConst.Services.AAA_PASSWORD_EDIT, p_password)
        self.clickButton(ServerConst.Services.AAA_USER_ADD_BUTT)
        
    def add_Record(self, p_name, p_ip):
        self.clickItem(ServerConst.Services.DNS_TYPE_COMBO, "A Record")
        self.setText(ServerConst.Services.DNS_DOMAIN_NAME, p_name)
        self.setText(ServerConst.Services.DNS_IP_ADD, p_ip)
        self.clickButton(ServerConst.Services.DNS_ADD_BUTT)
        
    def add_CNAME(self, p_name, p_hostname):
        self.clickItem(ServerConst.Services.DNS_TYPE_COMBO, "CNAME")
        self.setText(ServerConst.Services.DNS_DOMAIN_NAME, p_name)  
        self.setText(ServerConst.Services.CNAME_HOSTNAME_EDIT, p_hostname)  
        self.clickButton(ServerConst.Services.DNS_ADD_BUTT)
    
    def add_SOA(self, p_name, p_server, p_mailbox, p_min_ttl, p_refresh_time, p_retry_time, p_expiry_time):
        self.clickItem(ServerConst.Services.DNS_TYPE_COMBO, "SOA")
        self.setText(ServerConst.Services.DNS_DOMAIN_NAME, p_name)  
        self.setText(ServerConst.Services.SOA_SERVER, p_server)
        self.setText(ServerConst.Services.SOA_MAILBOX, p_mailbox)  
        self.setText(ServerConst.Services.SOA_MIN_TTL, p_min_ttl)
        self.setText(ServerConst.Services.SOA_REFRESH_TIME, p_refresh_time)  
        self.setText(ServerConst.Services.SOA_RETRY_TIME, p_retry_time)
        self.setText(ServerConst.Services.SOA_EXPIRE_TIME, p_expiry_time)    
        self.clickButton(ServerConst.Services.DNS_ADD_BUTT)   
        
    def add_NS_Record(self, p_name, p_serverName):
        self.clickItem(ServerConst.Services.DNS_TYPE_COMBO, "NS Record")
        self.setText(ServerConst.Services.DNS_DOMAIN_NAME, p_name)  
        self.setText(ServerConst.Services.NS_SERVER_NAME, p_serverName)
        self.clickButton(ServerConst.Services.DNS_ADD_BUTT)
        
    def set_NTP_Date(self, p_month, p_year, p_day):
        self.clickButton(ServerConst.Services.NTP_ON)
        self.clickButton(ServerConst.Services.NTP_CALENDAR_MONTH_BUTTON)
        self.activateItem(ServerConst.Services.NTP_CALENDAR_MONTH_DROPDOWN, p_month)
        self.clickButton(ServerConst.Services.NTP_CALENDAR_YEAR_BUTTON)
        self.typeText(ServerConst.Services.NTP_CALENDAR_YEAR_EDIT, p_year)
        self.typeText(ServerConst.Services.NTP_CALENDAR_DAY, "<Return>")
        self.clickItem(ServerConst.Services.NTP_CALENDAR_DAY, p_day)
        self.typeText(ServerConst.Services.NTP_CALENDAR_DAY, "<Return>")
        
    def set_NTP_Time(self, p_hour, p_min, p_sec, p_ampm):
        self.click(ServerConst.Services.NTP_TIME)
        self.typeText(ServerConst.Services.NTP_TIME, "<Del>")
        self.typeText(ServerConst.Services.NTP_TIME, "<Backspace>")
        self.typeText(ServerConst.Services.NTP_TIME, p_hour)
        self.typeText(ServerConst.Services.NTP_TIME, "<Right>")
        self.typeText(ServerConst.Services.NTP_TIME, "<Del>")
        self.typeText(ServerConst.Services.NTP_TIME, "<Del>")
        self.typeText(ServerConst.Services.NTP_TIME, p_min)
        self.typeText(ServerConst.Services.NTP_TIME, "<Right>")
        self.typeText(ServerConst.Services.NTP_TIME, "<Del>")
        self.typeText(ServerConst.Services.NTP_TIME, "<Del>")
        self.typeText(ServerConst.Services.NTP_TIME, p_sec)
        self.typeText(ServerConst.Services.NTP_TIME, "<Right>")
        self.typeText(ServerConst.Services.NTP_TIME, "<Del>")
        self.typeText(ServerConst.Services.NTP_TIME, "<Del>")
        self.typeText(ServerConst.Services.NTP_TIME, p_ampm)
        self.typeText(ServerConst.Services.NTP_CALENDAR_DAY, "<Return>")
        
    def set_NTP_Authentication(self, p_key, p_pass):
        self.clickButton(ServerConst.Services.NTP_AUTHENTICATION_ENABLE)
        self.setText(ServerConst.Services.NTP_AUTHENTICATION_KEY, p_key)
        self.setText(ServerConst.Services.NTP_AUTHENTICATION_PASSWORD, p_pass)

    def set_Email_Domain_Name(self, p_domainName):
        self.setText(ServerConst.Services.EMAIL_DOMAIN_NAME_EDIT, p_domainName)
        self.clickButton(ServerConst.Services.EMAIL_DOMAIN_NAME_SET_BUTT)

    def add_Email_User(self, p_user, p_pass):
        self.setText(ServerConst.Services.EMAIL_USERNAME_EDIT, p_user)
        self.setText(ServerConst.Services.EMAIL_PASSWORD_EDIT, p_pass)
        self.clickButton(ServerConst.Services.EMAIL_USER_ADD_BUTT)

    def remove_Email_User(self, p_user):
        self.clickItem(ServerConst.Services.EMAIL_USER_LIST, p_user)
        self.clickButton(ServerConst.Services.EMAIL_USER_REMOVE_BUTT)

    def change_Email_Password(self, p_user, p_newPass):
        self.clickItem(ServerConst.Services.EMAIL_USER_LIST, p_user)
        self.clickButton(ServerConst.Services.EMAIL_USER_CHANGE_PASSWORD_BUTT)
        self.setText(ServerConst.Services.EMAIL_NEW_PASSWORD_EDIT, p_newPass)
        self.clickButton(ServerConst.Services.EMAIL_NEW_PASSWORD_OK_BUTT)
        self.clickButton(ServerConst.Services.EMAIL_CHANGE_PASSWORD_CONFIRM_BUTT)

    def add_FTP_User(self, p_user, p_password, p_write, p_read, p_delete, p_rename, p_list):
        self.setText(ServerConst.Services.FTP_USERNAME_EDIT, p_user)
        self.setText(ServerConst.Services.FTP_PASSWORD_EDIT, p_password)
        if p_write == True:
            self.clickButton(ServerConst.Services.FTP_WRITE_CHKBOX)
        if p_read == True:
            self.clickButton(ServerConst.Services.FTP_READ_CHKBOX)
        if p_delete == True:
            self.clickButton(ServerConst.Services.FTP_DELETE_CHKBOX)
        if p_rename == True:
            self.clickButton(ServerConst.Services.FTP_RENAME_CHKBOX)
        if p_list == True:
            self.clickButton(ServerConst.Services.FTP_LIST_CHKBOX)
        self.clickButton(ServerConst.Services.FTP_USER_ADD_BUTT)

    def remove_FTP_User(self, p_table_entry):
        self.clickItem(ServerConst.Services.FTP_USER_LIST, p_table_entry)
        self.clickButton(ServerConst.Services.FTP_USER_REMOVE_BUTT)

    def remove_FTP_File(self, p_table_entry):
        self.clickItem(ServerConst.Services.FTP_FILE_LIST, p_table_entry)
        self.clickButton(ServerConst.Services.FTP_FILE_REMOVE_BUTT)
        
    #@summary: set the content for http page
    #@param p_text: text         
    def setHttpPageContent(self, p_text):
        obj = ServerConst.Services.HTTP_PAGE_CONTENT
        self.setText(obj, p_text)   