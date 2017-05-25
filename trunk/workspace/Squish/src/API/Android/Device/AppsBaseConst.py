##################################################################
#@summary: To be inherited from other devices for App constants  #
#          these are being shared across the desktop and server. #  
#          Also, includes App constants for Wireless Router and  #
#          Cloud devices.                                        #
##################################################################

from API.Android.Device.DeviceBase import DeviceBaseConst

class AppButtonsConst:
    IP_CONFIGURATION = ':ipv4applet_HTML_Object'
    IPV6_CONFIGURATION = ':ipv6applet_HTML_Object'
    PC_WIRELESS = ':wirelessApplet_HTML_Object'
    TEXTEDITOR = ':textEditorApplet_HTML_Object'
    WEB_BROWSER = ':browser_HTML_Object'
    TERMINAL = ':terminal_HTML_Object'
    COMMAND_PROMPT = ':cmdprompt_HTML_Object'
    IPV4_FIREWALL = ':firewallServiceApplet_HTML_Object'
    IPV6_FIREWALL = ':ipv6FirewallServiceApplet_HTML_Object'
    VPN = ':vpnServiceApplet_HTML_Object'
    EMAIL = ':mailClientApplet_HTML_Object'
    EMAIL_SERVICE = ':emailServiceApplet_HTML_Object'
    PPPOE_DIALER = ':pppoeDialerApplet_HTML_Object'
    TFTP = ':tftpApplet_HTML_Object'
    FTP = ':ftpApplet_HTML_Object'
    HTTP = ':httpServiceApplet_HTML_Object'
    DHCP = ':dhcpServiceApplet_HTML_Object'
    DHCPv6 = ':dhcpv6ServiceApplet_HTML_Object'
    DNS = ':dnsServiceApplet_HTML_Object'
    AAAACCOUNTING = ':aaaServiceApplet_HTML_Object'
    NTP = ':ntpServiceApplet_HTML_Object'
    SYSLOG = ':syslogServiceApplet_HTML_Object'
    
class AddressSharedConst:
    DHCP_RADIO = ':dhcp_HTML_Object'
    STATIC_RADIO = ':static_HTML_Object'
    IPV4_APPLET = ':IPv4Applet_HTML_Object'
    SUBMIT_BUTTON = ':saveButton_HTML_Object'
    INTERFACE_DROPDOWN = ':interfaceSelect_HTML_Object'
    
class IPconfigConst(AddressSharedConst):
    IP_EDIT = ':ipAddress_HTML_Object'
    SUBNET_EDIT = ':subnetMask_HTML_Object'
    GATEWAY_EDIT = ':defaultGateway_HTML_Object'
    DNS_EDIT = ':dnsServer_HTML_Object'
    
class IPv6ConfigConst(AddressSharedConst):
    IPV6_EDIT = ':ipv6Address_HTML_Object'
    IPV6_PREFIX_EDIT = ':prefix_HTML_Object'
    LINK_LOCAL_EDIT = ':linkLocalAddress_HTML_Object'
    GATEWAY_EDIT = ':ipv6Gateway_HTML_Object'
    DNS_EDIT = ':ipv6DnsServer_HTML_Object'
    AUTOCONFIG_RADIO = ':auto_config_HTML_Object'
    
class PcWirelessConst:
    class WirelessInterface:
        MAC_ADDRESS = ':macAddress_HTML_Object'
        SSID = ':ssid_HTML_Object'
        BANDWIDTH = ':bandwidth_HTML_Object'
        PORT_ON_OFF = ':portOn_select_HTML_Object'
    class Authentication:
        SECURITY_MODE = ':securityMode_HTML_Object'
        DISABLED = ':disabled_HTML_Object'
        WEP = ':WEP_HTML_Object'
        WPA_PSK = ':WPA_PSK_HTML_Object'
        WPA2_PSK = ':WPA2-PSK_HTML_Object'
        WPA = ':WPA_HTML_Object'
        WPA2 = ':WPA2_HTML_Object'
        ENCRYPTION_DROPDOWN = ':encryption_select_HTML_Object'
        AES = ':AES_HTML_Object'
        TKIP = 'TKIP_HTML_Object'
        KEY = ':key_HTML_Object'
        KEY_PHRASE = ':keyPhrase_text_HTML_Object'
        USER_ID = ':userID_text_HTML_Object'
        PASSWORD = ':password_text_HTML_Object'
        SUBMIT_BUTTON = ':submitBtn_HTML_Object'

class WebBrowserConst:
    BACK = ':btnBack_HTML_Object'
    FORWARD = ':btnForward_HTML_Object'
    URL_EDIT = ':urlField_HTML_Object'
    GO = ':btnGo_HTML_Object'
    AT_SYMBOL = ':btnCfg_HTML_Object'
    CONTENT_AREA = ':wbaPage_HTML_Object'
    DIALOG_CONTENT = ':desktopDialog_HTML_Object'
    WEB_PAGE = ':wbPageRootId-1_HTML_Object'
    
class SyslogConst:
    ON = ':id-syslog-radio-on_HTML_Object'
    OFF = ':id-syslog-radio-off_HTML_Object'
    CLOSE = ''
    CLEAR = ':id-syslog-clear-btn_HTML_Object'
    ENTRIES = ':id-syslog-entries-list_HTML_Object'

class TerminalConst(DeviceBaseConst.Cli):
    class Setup:
        TERMINAL_SETTINGS = ':terminalsettings_HTML_Object'
        BPS = ''
        DATA_BITS = ''
        PARITY = ''
        STOP_BITS = ''
        FLOW_CONTROL = ''
        SUBMIT = ':okbtn_HTML_Object'
        
    class Console(DeviceBaseConst.Cli):
        None
class CommandPromptConst(DeviceBaseConst.Cli):
    None

class FirewallConst:
    INTERFACE = ':interfaceSelect_HTML_Object'
    FIREWALL_RULE = ':ruleSelect_HTML_Object'
    ON_RADIO = ':firewallOn_HTML_Object'
    OFF_RADIO = ':firewallOff_HTML_Object'
    ACTION = ':actionSelect_HTML_Object'
    REMOTE_PORT = ':remotePort_HTML_Object'
    PROTOCOL = ':protocolSelect_HTML_Object'
    WILDCARD_MASK = ':remoteWildcardMask_HTML_Object'
    LOCAL_PORT = ':localPort_HTML_Object'
    ADD = ':addBtn_HTML_Object'
    SAVE = ':saveBtn_HTML_Object'
    REMOVE = ':removeBtn_HTML_Object'

class IPFirewallConst(FirewallConst):
    REMOTE_IP = ':remoteIp_HTML_Object'

class IPv6FirewallConst(FirewallConst):
    REMOTE_IPV6 = ':remoteIp_HTML_Object'
    
class VPNConst:
    GROUP_NAME = ':groupName_HTML_Object'
    GROUP_KEY = ':groupKey_HTML_Object'
    HOST_IP = ':serverIp_HTML_Object'
    USERNAME = ':username_HTML_Object'
    PASSWORD = ':password_HTML_Object'
    CONNECT_BUTTON = ':connectBtn_HTML_Object'
    
class EmailConst:
    class MailClient:
        COMPOSE_BUTTON = ':Compose_HTML_Object'
        REPLY_BUTTON = ':replyButton_HTML_Object'
        RECEIVE_BUTTON = ':receiveButton_HTML_Object'
        DELETE_BUTTON = ':deleteButton_HTML_Object'
        CONFIGURE_MAIL_BUTTON = ':Configure Mail_HTML_Object'
        SELECT_VIEW = ':activitySelect_HTML_Object'
        FROM_HEADER = ':ext-label-9_HTML_Object'
        SUBJECT_HEADER = ':ext-label-10_HTML_Object'
        RECEIVED_HEADER = ':ext-label-11_HTML_Object'
        STATUS = ':status_HTML_Object'
        CONTENT = ':contents_HTML_Object'
    class ConfigureMail:
        NAME = ':name_HTML_Object'
        EMAIL_ADDRESS = ':email_HTML_Object'
        INCOMING_MAIL_SERVER = ':incomingMailServer_HTML_Object'
        OUTGOING_MAIL_SERVER = ':outgoingMailServer_HTML_Object'
        USERNAME = ':username_HTML_Object'
        PASSWORD = ':password_HTML_Object'
        SAVE_BUTTON = ':saveButton_HTML_Object'
        CLEAR_BUTTON = ':clearButton_HTML_Object'
        RESET_BUTTON = ':resetButton_HTML_Object'
        CANCEL_BUTTON = ':cancelConfigureButton_HTML_Object'
    class ComposeAndReply:
        TO = ':to_HTML_Object'
        SUBJECT = ':subject_HTML_Object'
        CONTENT = ':composeContent_HTML_Object'
        SEND_BUTTON = ':Send_HTML_Object'
        CANCEL_BUTTON = ':ext-button-83_HTML_Object'

class EmailServerConst:
    DOMAIN_NAME = ":emailDomainName_HTML_Object"
    SMTP_SERVICE_ON_RADIO = ":enableSmtp_HTML_Object"
    SMTP_SERVICE_OFF_RADIO = ":disableSmtp_HTML_Object"
    POP3_SERVICE_ON_RADIO = ":enablePop3_HTML_Object"
    POP3_SERVICE_OFF_RADIO = ":disablePop3_HTML_Object"
    EMAIL_USERNAME = ":emailuserTxt_HTML_Object"
    EMAIL_PASSWORD = ":emailPasswdTxt_HTML_Object"
    ADD_USER_BUTTON = ":addEmailAccountBtn_HTML_Object"
    REMOVE_USER_BUTTON = ":removeEmailAccountBtn_HTML_Object"
    CHANGE_PASSWORD_BUTTON = ":changeEmailAcctPasswdBtn_HTML_Object"
    SUBMT_BUTTON = ":submitEmailServerChanges_HTML_Object"
    USER_LIST = ""

class PPPoEConst:
    USERNAME = ':username_HTML_Object'
    PASSWORD = ':password_HTML_Object'
    CONNECT_BUTTON = ':connectBtn_HTML_Object'

class TextEditorConst:
    TEXT_CONTENT = ':textArea_HTML_Object'
    TEXT_OPEN = ':openButton_HTML_Object'
    TEXT_SAVE = ':saveButton_HTML_Object'
    FILE_OPEN = ':btnOpen_HTML_Object'
    FILE_CANCEL = ':btnCancel_HTML_Object'
    FILE_LIST = ':lstFiles_HTML_Object'
    FILE_OPEN = ':btnOpen_HTML_Object'
    FILE_CANCEL = ':btnCancel_HTML_Object'
    
#######################
#Server Specific Apps #
#######################

class TftpConst:
    ON = ':tftpOn_HTML_Object'
    OFF = ':tftpOff_HTML_Object'
    REMOVE_BUTTON = ':removeBtn_HTML_Object'
    FILE_LIST = ':lstFiles_HTML_Object'

class FtpConst:
    USERNAME = ':username_HTML_Object'
    PASSWORD = ':password_HTML_Object'
    ON = ':ftpOn_HTML_Object'
    OFF = ':ftpOff_HTML_Object'
    WRITE = ':write_HTML_Object'
    READ = ':read_HTML_Object'
    DELETE = ':delete_HTML_Object'
    RENAME = ':rename_HTML_Object'
    LIST = ':list_HTML_Object'
    ADD_BUTTON = ':addButton_HTML_Object'
    DELETE_BUTTON = ':deleteButton_HTML_Object'
    SAVE_BUTTON = ':saveButton_HTML_Object'
    USER_LIST = ':usernamePasswordList_HTML_Object'
    FILE_LIST = ':lstFiles_HTML_Object'
    REMOVE_FILE_BUTTON = ':removeBtn_HTML_Object'

class HttpConst:
    HTTP_ON = ':httpOn_HTML_Object'
    HTTP_OFF = ':httpOff_HTML_Object'
    HTTPS_ON = ':httpsOn_HTML_Object'
    HTTPS_OFF = ':httpsOff_HTML_Object'
    FILE_NAME = ':filenameEdit_HTML_Object'
    FILE_CONTENT = ':htmlEdit_HTML_Object'
    BACK_PAGE = ':prevBtn_HTML_Object'
    FORWARD_PAGE = ':nextBtn_HTML_Object'
    ADD_PAGE = ':addBtn_HTML_Object'
    REMOVE_PAGE = ':removeBtn_HTML_Object'
    SUBMIT_BUTTON = ':submitBtn_HTML_Object'
    PAGE_NUMBER = ':pageNumber_HTML_Object'
    EDIT_PAGE = ':editBtn_HTML_Object'
    
class DhcpConst:
    INTERFACE_SELECT = ':interfaceSelect_HTML_Object'
    POOL_SELECT = ':poolSelect_HTML_Object'
    ON = ':dhcpOn_HTML_Object'
    OFF = ':dhcpOff_HTML_Object'
    POOL_NAME = ':poolName_HTML_Object'
    GATEWAY = ':defaultGateway_HTML_Object'
    DNS_SERVER = ':dnsServer_HTML_Object'
    START_IP = ':startIpAddress_HTML_Object'
    SUBNET = ':subnetMask_HTML_Object'
    MAX_USERS = ':maxUsers_HTML_Object'
    TFTP_SERVER = ':tftpServer_HTML_Object'
    ADD_BUTTON = ':addBtn_HTML_Object'
    SAVE_BUTTON = ':saveBtn_HTML_Object'
    REMOVE_BUTTON = ':removeBtn_HTML_Object'
    
class Dhcpv6Const:
    POOL_LIST_OPTIONS = ':poolListOptions_HTML_Object'
    POOL_CREATE = ':Create_HTML_Object'
    POOL_REMOVE = ':Remove_HTML_Object'
    POOL_NAME = ':poolName_HTML_Object'
    DNS_NAME = ':dnsName_HTML_Object'
    DOMAIN_NAME = ':domain_HTML_Object'
    IP_ADDRESS = ':ipv6Addr_HTML_Object'
    PREFIX = ':prefix_HTML_Object'
    DUID = ':duid_HTML_Object'
    PREFIX_VALID_LIFE = ':delValidLifetime_HTML_Object'
    PREFIX_PREFERRED_LIFE = ':delPreferredLifetime_HTML_Object'
    LOCAL_POOL = ':localPool_HTML_Object'
    LOCAL_VALID_LIFE = ":poolValidLifetime_HTML_Object"
    LOCAL_PREFFERED_LIFE = ':poolPreferredLifetime_HTML_Object'
    SAVE_BUTTON = ':saveBtn_HTML_Object'
    CANCEL_BUTTON = 'cancelBtn_HTML_Object'
    
class DnsConst:
    TYPE = ':typeSelect_HTML_Object'
    RESOURCE_RECORD = ':resourceRecordSelect_HTML_Object'
    ON = ':dnsOn_HTML_Object'
    OFF = ':dnsOff_HTML_Object'
    RESOURCE_RECORD_NAME = ':resourceRecordName_HTML_Object'
    A_RECORD_ADDRESS = ':ARECORD_address_HTML_Object'
    CNAME_HOSTNAME = ':CNAME_hostName_HTML_Object'
    SOA_PRIMARY_SERVER_NAME = ':SOA_primaryServerName_HTML_Object'
    SOA_MAILBOX = ':SOA_mailbox_HTML_Object'
    SOA_MINIMUM_TTL = ':SOA_minimumTtl_HTML_Object'
    SOA_REFRESH_TIME = ':SOA_refreshTime_HTML_Object'
    SOA_RETRY_TIME = ':SOA_retryTime_HTML_Object'
    SOA_EXPIRY_TIME = ':SOA_expiryTime_HTML_Object'
    NSRECORD_NAME_SERVER = ':NSRECORD_serverName_HTML_Object'
    ADD_BUTTON = ':addBtn_HTML_Object'
    SAVE_BUTTON = ':saveBtn_HTML_Object'
    REMOVE_BUTTON = ':removeBtn_HTML_Object'
    
    A_RECORD = ":A Record_HTML_Object"
    CNAME = ":CNAME_HTML_Object"
    SOA = ":SOA_HTML_Object"
    NS_RECORD = ":NS Record_HTML_Object"
    
class AAA_AccountingConst:
    AAA_ON_RADIO = ":aaaRadioOn_HTML_Object"
    AAA_OFF_RADIO = ":aaaRadioOff_HTML_Object"
    AAA_RADIUS_PORT = ":aaaPort_HTML_Object"
    AAA_CLIENT_NAME = ":aaaClientName_HTML_Object"
    AAA_CLIENT_IP = ":aaaClientIp_HTML_Object"
    AAA_CLIENT_SECRET = ":aaaClientSecret_HTML_Object"
    AAA_RADIUS = ":aaaRadius_HTML_Object"
    AAA_TACACS = ":aaaTacacs_HTML_Object"
    ADD_CLIENT_BUTTON = ":aaaClientAddBtn_HTML_Object"
    REMOVE_CLIENT_BUTTON = ":aaaClientRemoveBtn_HTML_Object"
    SAVE_CLIENT_BUTTON = ":aaaClientSaveBtn_HTML_Object"
    AAA_USER_NAME = ":aaaUsernameField_HTML_Object"
    AAA_USER_PASSWORD = ":aaaPasswordField_HTML_Object"
    ADD_USER_BUTTON = ":aaaUserAddBtn_HTML_Object"
    REMOVE_USER_BUTTON = ":aaaUserRemoveBtn_HTML_Object"
    SAVE_USER_BUTTON = ":aaaUserSaveBtn_HTML_Object"
    SUBMIT_BUTTON = ":submitAAABtn_HTML_Object"
    CLIENT_LIST = ":aaaClientTable_HTML_Object"
    USER_LIST = ":aaaUserListTable_HTML_Object"
    
class NtpConst:
    ON = ':on_HTML_Object'
    OFF = ':off_HTML_Object'
    ENABLE = ':enable_HTML_Object'
    DISABLE = ':disable_HTML_Object'
    KEY = ':key_HTML_Object'
    PASSWORD = ':password_HTML_Object'
    DATE = ':date_HTML_Object'
    HOUR = ':hour_HTML_Object'
    HOUR_MINUS = ''
    HOUR_PLUS = ''
    MIN = ':min_HTML_Object'
    MIN_MINUS = ''
    MIN_PLUS = ''
    SEC = ':sec_HTML_Object'
    SEC_MINUS = ''
    SEC_PLUS = ''
    APPLY_CHANGES_BUTTON = ':submitButton_HTML_Object'
    
################################
#Wireless Router Specific Apps #
################################

class WirelessAppButtonsConst:
    BASIC_SETUP = ':linksysBasicSetupApplet_HTML_Object'
    WIRELESS_SETTING = ':linksysBasicWirelessSettingApplet_HTML_Object'
    WIRELESS_SECURITY = ':linksysWirelessSecurityApplet_HTML_Object'
    WIRELESS_STATUS = ':linksysStatusApplet_HTML_Object'
    MAC_ADDRESS_FILTER = ':wirelessMacFilterApplet_HTML_Object'
    WIRELESS_ADMIN_MGMT = ':wirelessRouterAdminMgntApplet_HTML_Object'
    PORT_FORWARDING = ':wirelessRouterPortForwardingApplet_HTML_Object'

class Basic_SetupConst:
    INTERNET_CONNECTION_TYPE = ':internetConnectionSelect_HTML_Object'
    INTERNET_CONNECTION_DHCP = ':Automatic Configuration - DHCP_HTML_Object'
    INTERNET_CONNECTION_STATIC = ':Static IP_HTML_Object'
    INTERNET_CONNECTION_PPPOE = ':PPPoE_HTML_Object'
    
    #When Connection Type is Static IP
    STATIC_INTERNET_IP = ':internetIpAddress_HTML_Object'
    STATIC_SUBNET_MASK = ':subnetMask_HTML_Object'
    STATIC_DEFAULT_GATEWAY = ':defaultGateway_HTML_Object'
    STATIC_DNS1 = ':dns1_HTML_Object'
    STATIC_DNS2 = ':dns2_HTML_Object'
    STATIC_DNS3 = ':dns3_HTML_Object'
    
    #When Connection Type is PPPoE
    PPPOE_USERNAME = ':username_HTML_Object'
    PPPOE_PASSWORD = ':password_HTML_Object'
    PPPOE_SERVICE_NAME = ':serviceName_HTML_Object'
    PPPOE_IDLE_TIME = ':maxIdleTime_HTML_Object'
    PPPOE_MINUTE = ':minute_HTML_Object'
    PPPOE_REDIAL_PERIOD = ':keepAlive_HTML_Object'
    PPPOE_SECOND = ':second_HTML_Object'
    
    HOST_NAME = 'hostname_HTML_Object'
    DOMAIN_NAME = 'domainName_HTML_Object'
    MTU = 'mtu_HTML_Object'
    MTU_SIZE = 'size_HTML_Object'
    
    NETWORK_SETUP_IP = ':ipAddress_HTML_Object'
    NETWORK_SUBNET_MASK = ':subnetMask2_HTML_Object'
    
    DHCP_ON = ':dhcpEnabled_HTML_Object'
    DHCP_OFF = ':dhcpDisabled_HTML_Object'
    DHCP_SERVER_ACTION = ':dhcpReservation_HTML_Object'
    CONFIG_DHCP_RESERVATION = ':Configure DHCP Reservation_HTML_Object'
    ADD_CLIENT_BUTTON = ':addClientBtn_HTML_Object'
    REMOVE_CLIENT_BUTTON = ':removeBtn_HTML_Object'
    CLIENT_MAC_ADDRESS = ':clientMac_HTML_Object'
    DHCP_START_IP = ':startIpAddress_HTML_Object'
    DHCP_MAX_NUMBER = ':maxNum_HTML_Object'
    DHCP_IP_RANGE = ':ipAddressRange_HTML_Object'
    DHCP_LEASE_TIME = ':clientLeaseTime_HTML_Object'
    DHCP_STATIC_DNS1 = ':staticDns1_HTML_Object'
    DHCP_STATIC_DNS2 = ':staticDns2_HTML_Object'
    DHCP_STATIC_DNS3 = ':staticDns3_HTML_Object'
    DHCP_WINS = ':wins_HTML_Object'
    SUBMIT_BUTTON = ':submitBtn_HTML_Object'
    
    #DHCP Reservation
    FINISH = ':closeBtn_HTML_Object'
    
class Wireless_SettingConst:
    NETWORK_MODE = ':networkMode_HTML_Object'
    MIXED = ':Mixed_HTML_Object'
    BG_MIXED = ':BG-Mixed_HTML_Object'
    WIRELESS_G = ':Wireless_G_HTML_Object'
    WIRELESS_B = ':Wireless_B_HTML_Object'
    WIRELESS_N = ':Wireless-N Only_HTML_Object'
    DISABLED = ':Disabled_HTML_Object'
    
    NETWORK_SSID = ':ssid_HTML_Object'
    
    RADIO_BAND = ':radioBand_HTML_Object'
    AUTO = ':'
    STANDARD = ':'
    WIDE = ':'
    
    STANDARD_CHANNEL = ':standardChannel_HTML_Object'
    SSID_BROADCAST_ON = ':enabled_HTML_Object'
    SSID_BROADCAST_OFF = ':disabled_HTML_Object'
    SUBMIT_BUTTON = ':submitBtn_HTML_Object'
    
class Wireless_SecurityConst:
    SECURITY_MODE = ':securityMode_HTML_Object'
    DISABLED = ':Disabled_HTML_Object'
    WEP = ':WEP_HTML_Object'
    WPA_PERSONAL = ':WPA Personal_HTML_Object'
    WPA_ENTERPRISE = ':WPA Enterprise_HTML_Object'
    WPA2_PERSONAL = ':WPA2 Personal_HTML_Object'
    WPA2_ENTERPRISE = ':WPA2 Enterprise_HTML_Object'
    SUBMIT_BUTTON = ':submitBtn_HTML_Object'
    
    WEP_ENCRYPTION = ':encryption_HTML_Object'
    WEP_KEY1 = ':key1_HTML_Object'
    WPA_PERSONAL_ENCRYPTION = ':wpaPersonalEncryption_HTML_Object'
    WPA_PERSONAL_PASSPHRASE = ':wpaPersonalPassphrase_HTML_Object'
    WPA_ENTERPRISE_ENCRYPTION = ':wpaEnterpriseEncryption_HTML_Object'
    WPA_ENTERPRISE_RADIUS = 'wpaEnterpriseRadiusServer_HTML_Object'
    WPA_ENTERPRISE_SECRET = 'wpaEnterpriseSharedSecret_HTML_Object'
    WPA2_PERSONAL_ENCRYPTION = ':wpa2PersonalEncryption_HTML_Object'
    WPA2_PERSONAL_PASSPHRASE = ':wpa2PersonalPassphrase_HTML_Object'
    WPA2_ENTERPRISE_ENCRYPTION = ':wpa2EnterpriseEncryption_HTML_Object'
    WPA2_ENTERPRISE_RADIUS = ':wpa2EnterpriseRadiusServer_HTML_Object'
    WPA2_ENTERPRISE_SECRET = ':wpa2EnterpriseShareSecret_HTML_Object'
        
    AES = ':AES_HTML_Object'
    TKIP = ':TKIP_HTML_Object'

class Wireless_StatusConst:
    IP_ADD_RELEASE = ':ipAddressReleaseBtn_HTML_Object'
    IP_ADD_RENEW = ':ipAddressRenewBtn_HTML_Object'
    IP_REFRESH = ':linksysStatusRefreshBtn_HTML_Object'
    CONNECT_BUTTON = ':connectButton_HTML_Object'

class MAC_Address_FilterConst:
    MAC_FILTER_ENABLED = ':enableFilter_HTML_Object'
    MAC_FILTER_DISABLED = ':disableFilter_HTML_Object'
    PREVENT_ACCESS = ':preventMacs_HTML_Object'
    ALLOW_ACCESS = ':allowMacs_HTML_Object'
    MAC_ADDRESS_01 = ':mac01_HTML_Object'
    MAC_ADDRESS_02 = ':mac02_HTML_Object'
    MAC_ADDRESS_03 = ':mac03_HTML_Object'
    MAC_ADDRESS_04 = ':mac04_HTML_Object'
    MAC_ADDRESS_05 = ':mac05_HTML_Object'
    MAC_ADDRESS_06 = ':mac06_HTML_Object'
    MAC_ADDRESS_07 = ':mac07_HTML_Object'
    MAC_ADDRESS_08 = ':mac08_HTML_Object'
    MAC_ADDRESS_09 = ':mac09_HTML_Object'
    MAC_ADDRESS_10 = ':mac10_HTML_Object'
    MAC_ADDRESS_11 = ':mac11_HTML_Object'
    MAC_ADDRESS_12 = ':mac12_HTML_Object'
    MAC_ADDRESS_13 = ':mac13_HTML_Object'
    MAC_ADDRESS_14 = ':mac14_HTML_Object'
    MAC_ADDRESS_15 = ':mac15_HTML_Object'
    MAC_ADDRESS_16 = ':mac16_HTML_Object'
    MAC_ADDRESS_17 = ':mac17_HTML_Object'
    MAC_ADDRESS_18 = ':mac18_HTML_Object'
    MAC_ADDRESS_19 = ':mac19_HTML_Object'
    MAC_ADDRESS_20 = ':mac20_HTML_Object'
    MAC_ADDRESS_21 = ':mac21_HTML_Object'
    MAC_ADDRESS_22 = ':mac22_HTML_Object'
    MAC_ADDRESS_23 = ':mac23_HTML_Object'
    MAC_ADDRESS_24 = ':mac24_HTML_Object'
    MAC_ADDRESS_25 = ':mac25_HTML_Object'
    MAC_ADDRESS_26 = ':mac26_HTML_Object'
    MAC_ADDRESS_27 = ':mac27_HTML_Object'
    MAC_ADDRESS_28 = ':mac28_HTML_Object'
    MAC_ADDRESS_29 = ':mac29_HTML_Object'
    MAC_ADDRESS_30 = ':mac30_HTML_Object'
    MAC_ADDRESS_31 = ':mac31_HTML_Object'
    MAC_ADDRESS_32 = ':mac32_HTML_Object'
    MAC_ADDRESS_33 = ':mac33_HTML_Object'
    MAC_ADDRESS_34 = ':mac34_HTML_Object'
    MAC_ADDRESS_35 = ':mac35_HTML_Object'
    MAC_ADDRESS_36 = ':mac36_HTML_Object'
    MAC_ADDRESS_37 = ':mac37_HTML_Object'
    MAC_ADDRESS_38 = ':mac38_HTML_Object'
    MAC_ADDRESS_39 = ':mac39_HTML_Object'
    MAC_ADDRESS_40 = ':mac40_HTML_Object'
    MAC_ADDRESS_41 = ':mac41_HTML_Object'
    MAC_ADDRESS_42 = ':mac42_HTML_Object'
    MAC_ADDRESS_43 = ':mac43_HTML_Object'
    MAC_ADDRESS_44 = ':mac44_HTML_Object'
    MAC_ADDRESS_45 = ':mac45_HTML_Object'
    MAC_ADDRESS_46 = ':mac46_HTML_Object'
    MAC_ADDRESS_47 = ':mac47_HTML_Object'
    MAC_ADDRESS_48 = ':mac48_HTML_Object'
    MAC_ADDRESS_49 = ':mac49_HTML_Object'
    MAC_ADDRESS_50 = ':mac50_HTML_Object'
    SUBMIT_BUTTON = ':'

class Wireless_Admin_MgmtConst:
#lots of settings are not configurable. may change in future? 
    ROUTER_PASSWORD = ':password_HTML_Object'
    REENTER_PASSWORD = ':confirmPassword_HTML_Object'
    REMOTE_MANAGEMENT_ENABLED = ':enableRemoteManagement_HTML_Object'
    REMOTE_MANAGEMENT_DISABLED = ':disableRemoteManagement_HTML_Object'
    SUBMIT_BUTTON = ':submitBtn_HTML_Object'
    
class Port_Forwarding:
    APP_NAME1 = ':appName1_HTML_Object'
    IP_ADDRESS1 = ':toIpAddr1_HTML_Object'
    ENABLED1 = ':enabled1_HTML_Object'
    APP_NAME6 = ':appName6_HTML_Object'
    INTERNAL_PORT6 = ':internalPort6_HTML_Object'
    EXTERNAL_PORT6 = ':externalPort6_HTML_Object'
    PROTOCOL6 = ':protocol6_HTML_Object'
    IP_ADDRESS6 = ':toIpAddr6_HTML_Object'
    ENABLED6 = ':enabled6_HTML_Object'
    SUBMIT_BUTTON = ':submitButt_HTML_Object'
    
    HTTP = ":HTTP_HTML_Object"
    
################################
#Access Point Specific Apps #
################################  
class APAppButtonsConst:
    PORT_SETUP = ':accessPointWirelessPortApplet_HTML_Object'

class PortSetup:
    SSID = ':ssidTextField_HTML_Object'
    CHANNEL = ':channelSelect_HTML_Object'
    PORT_STATUS = ':portStatusChkbox_HTML_Object'
    DISABLED = ':disabledRadioButt_HTML_Object'
    WEP = ':wepRadioButt_HTML_Object'
    WEP_KEY = ':wepKeyTextField_HTML_Object'
    WPA_PSK = ':wpaRadioButt_HTML_Object'
    WPA2_PSK = ':wpa2RadioButt_HTML_Object'
    PSK_PASSPHRASE = ':passPhraseTextField_HTML_Object'
    
    SUBMIT_BUTTON = ':submitButt_HTML_Object'
    
################################
#Cloud Specific Apps #
################################

class CloudAppButtonsConst:
    FRAME_RELAY_MAPPING = ''
    DLCI_CONFIGURATION = ''
    WAN_PROVIDER =  ''
    
class FrameRelayConst:
    FROM_PORT = ':fromPortSelect_HTML_Object'
    FROM_SUBLINK = ':fromSublinkSelect_HTML_Object'
    TO_PORT = ':toPortSelect_HTML_Object'
    TO_SUBLINK = ':toSublinkSelect_HTML_Object'
    FRAME_RELAY_TABLE = 'frameRelayMappingTable_HTML_Object'
    ADD_BUTTON = ''
    REMOVE_BUTTON = ''
    
class DLCI_Const:
    INTERFACE = ':interface_HTML_Object'
    PORT_STATUS = ':portStatus_HTML_Object'
    LMI_TYPE = ':lmi_HTML_Object'
    DLCI = ':dlci_HTML_Object'
    DLCI_NAME = ':name_HTML_Object'
    DLCI_TABLE = ':dlciTable_HTML_Object'
    ADD_BUTTON = ''
    REMOVE_BUTTON = ''
    
class WAN_ProviderConst:
    INTERFACE = ':interface_HTML_Object'
    DSL = ':dsl_HTML_Object'
    CABLE = ':cable_HTML_Object'
    PROVIDER = ':providerSelect_HTML_Object'
    FROM_PORT = ':fromPortSelect_HTML_Object'
    TO_PORT = ':toPortSelect_HTML_Object'
    PROVIDER_TABLE = ':wanProviderTable_HTML_Object'
    ADD_BUTTON = ''
    REMOVE_BUTTON = ''


################################
#CO Server Specific Apps 	   #
################################

class COServerAppButtonsConst:
    BACKBONE_INTERFACE = ':backboneIntfApplet_HTML_Object'
    CELL_TOWER_INTERFACE = ':cellTowerIntfApplet_HTML_Object'
    DHCP = ':coDhcpServiceApplet_HTML_Object'
    DHCP6 = ':coDhcpv6ServiceApplet_HTML_Object'
    CELL_TOWER_SERVICE = ':cellTowerServiceApplet_HTML_Object'
    PAP_CHAP_SERVICE = ':papChapServiceApplet_HTML_Object'
    
class BackboneInterfaceConst:
    DHCP_BUTTON = ':dhcp_HTML_Object'
    STATIC_BUTTON = ':static_HTML_Object'
    IP_ADDRESS = ':ipAddress_HTML_Object'
    SUBNET_MASK = ':subnetMask_HTML_Object'
    DEFAULT_GATEWAY = ':defaultGateway_HTML_Object'
    DNS_SERVER = ':dnsServer_HTML_Object'
    SUBMIT_BUTTON = ':saveBtn_HTML_Object'

class CellTowerInterfaceConst:
    pass

class COServerDhcpConst:
    LAST_OCTET = ':fourthOctet_HTML_Object'
    MAX_USERS = ':maxUser_HTML_Object'
    SUBMIT_BUTTON = ':saveBtn_HTML_Object'
    DNS_SERVER = ':dnsServer_HTML_Object'

class COServerDhcpv6Const:
    pass

class CellTowerServiceConst:
    pass

class PAP_CHAPServiceConst:
    pass
	
################################
#Sniffer Specific Apps #
################################

class SnifferAppButtonsConst:
	SNIFFER = ':snifferApplet_HTML_Object'

class SnifferConst:
    SERVICE_ON = ':onBtn_HTML_Object'
    SERVICE_OFF = ':offBtn_HTML_Object'
    INCOMING_PORT0 = ':port0Btn_HTML_Object'
    INCOMING_PORT1 = ':port1Btn_HTML_Object'
    BUFFER_SLIDER = ':bufferSlider_HTML_Object'
    PACKET_LIST = ':packetList_HTML_Object'
    EDIT_FILTER = ':editFilterBtn_HTML_Object'
    CLEAR = ':clearBtn_HTML_Object'
    
################################
#Menus for Devices #
################################

class Menu:
    LINK = ':link_HTML_Object_2'
    CLI = ':console_HTML_Object_2'
    DESKTOP = ':desktop_HTML_Object'
    SIMPLEPDU = ':addSimplePDU_HTML_Object'
    COMPLEXPDU = ':addComplexPDU_HTML_Object'
    PHYSICAL = ':physical_HTML_Object'
    INSPECT = ':inspect_HTML_Object'
    COPY = ':copy_HTML_Object'
    DELETE = ':delete_HTML_Object_2'
    MULTISELECT = ':multiSelect_HTML_Object'

class Cli(DeviceBaseConst.Cli):
    None