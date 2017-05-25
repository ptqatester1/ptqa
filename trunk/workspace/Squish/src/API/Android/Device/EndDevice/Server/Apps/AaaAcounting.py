#############################################################
##Author: AbbasH
#@summary:AaaAccounting handles AAA Acounting configuration 
#############################################################
from API.Android.Device.EndDevice.Server import ServerConst

class Services(ServicesBase): 
    def __init__(self):
        self.squishName = ""
        
    def addAAAClient(self, p_client_host, p_client_ip, p_secret, p_server_type):
		self.tapObject(ServerConst.AAA_Accounting.AAA_ON_RADIO)
		self.setText(ServerConst.AAA_Accounting.AAA_CLIENT_NAME, p_client_host)
		self.setText(waitForObject(ServerConst.AAA_Accounting.AAA_CLIENT_IP), p_client_ip)
		self.setText(waitForObject(ServerConst.AAA_Accounting.AAA_CLIENT_SECRET), p_secret)
		if p_server_type == "Tacacs":
			self.tapObject(ServerConst.AAA_Accounting.AAA_TACACS)
		else:	
			self.tapObject(ServerConst.AAA_Accounting.AAA_RADIUS)
		self.tapObject(ServerConst.AAA_Accounting.ADD_CLIENT_BUTTON)
		self.tapObject(ServerConst.AAA_Accounting.SUBMIT_BUTTON)
        
    def addUser(self, p_username, p_password):
		self.setText(ServerConst.AAA_Accounting.AAA_USER_NAME, p_username)
		self.setText(ServerConst.AAA_Accounting.AAA_USER_PASSWORD, p_password)
		self.tapObject(ServerConst.AAA_Accounting.ADD_USER_BUTTON)
		self.tapObject(ServerConst.AAA_Accounting.SUBMIT_BUTTON)