#############################################################
##Author: AbbasH
#@summary:DHCP handles DHCP configuration 
#############################################################
from API.Android.Device.EndDevice.Server import ServerConst

class Services(ServicesBase): 
    def __init__(self):
        self.squishName = ""

	def changeInterface(self, p_interfaceName):
        self.tapObject(ServerConst.DHCP.INTERFACE_SELECT, p_interfaceName)
	
	def changeServerPool(self, p_serverPoolName):
		self.tapObject(ServerConst.DHCP.POOL_SELECT, p_serverPoolName)
	
	def setDHCPServiceOn(self):
		self.tapObject(ServerConst.DHCP.SERVICE_ON)

	def setDHCPServiceOff(self):
		self.tapObject(ServerConst.DHCP.SERVICE_OFF)

    def setDhcpPoolName(self, p_name):
        self.setText(ServerConst.DHCP.POOL_NAME, p_name)  

    def setDhcpGateway(self, p_gateway):
        self.setText(ServerConst.DHCP.GATEWAY, p_gateway)  
		
    #@summary: set dhcp domain name
    #@param p_domain: domain name        
    def setDhcpDNS(self, p_domain):
        self.setText(ServerConst.DHCP.DNS_SERVER, p_domain)        

    #@summary: set dhcp IP
    #@param p_ip: ip octet         
    def setDhcpStartIp(self, p_ip):
        self.setText(ServerConst.DHCP.START_IP_ADDRESS, p_ip) 

    def setDhcpSubnet(self, p_subnet):
        self.setText(ServerConst.DHCP.SUBNET_MASK, p_subnet)  		
        
    #@summary: set dhcp maximum number of user
    #@param p_max: max number 
    def setDhcpMaxUser(self, p_max):
        self.setText(ServerConst.DHCP.MAX_USERS, p_max)

    def setDhcpTftpServer(self, p_tftp):
        self.setText(ServerConst.DHCP.TFTP_SERVER, p_tftp)
        
    #@summary: add dhcp pool
    def addDhcpPool(self, p_name, p_gateway, p_dns, p_startIP, p_subnet, p_maxUsers):
        self.setDHCPServiceOn()
        self.setDhcpPoolName(p_name)
        self.setDhcpGateway(p_gateway)
        self.setDhcpDNS(p_dns)
        self.setDhcpStartIp(p_startIP)
        self.setDhcpSubnet(p_subnet)
        self.setDhcpMaxUser(p_maxUsers)
        self.tapObject(ServerConst.DHCP.ADD_BUTTON)
        
    def editPool(self, p_pool, p_name, p_gateway, p_dns, p_startIP, p_subnet, p_maxUsers):
        self.tapObject(ServerConst.Services.DHCP_LIST_VIEW, p_pool)       
        self.setDHCPServiceOn()
        self.setDhcpPoolName(p_name)
        self.setDhcpGateway(p_gateway)
        self.setDhcpDNS(p_dns)
        self.setDhcpStartIp(p_startIP)
        self.setDhcpSubnet(p_subnet)
        self.setDhcpMaxUser(p_maxUsers)
        self.tapObject(ServerConst.DHCP.SAVE_BUTTON)

    #@summary: remove dhcp pool
    #@param p_pool: e.g. "serverPool|0.0.0.0|0.0.0.0|0.0.0.0|0.0.0.0|0"
    def removeDhcpPool(self, p_pool):
        self.clickItem(ServerConst.DHCP.DHCP_POOL_LIST, p_pool)
        self.clickButton(ServerConst.DHCP.REMOVE_BUTTON)		