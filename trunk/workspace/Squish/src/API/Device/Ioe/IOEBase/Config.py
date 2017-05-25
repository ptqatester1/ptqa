#**************************************************************#
#@Author: Chris Allen                                          #
#**************************************************************#

from API.Device.Ioe.IoeBaseConst import IoeBaseConst
from API.Device.DeviceBase import ConfigBase
from API.SquishSyntax import SquishSyntax
from API.Device.DeviceBase import DeviceBase
		
class AbstractPort:
	def __init__(self):
		self.squishName = ''
		self.DeviceBase = DeviceBase(self.squishName)
		self.click = self.DeviceBase.click
		self.clickItem = self.DeviceBase.clickItem
		self.setText = self.DeviceBase.setText
		self.clickButton = self.DeviceBase.clickButton
			
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		self.DeviceBase.updateName(self.squishName)
		
	def togglePortStatus(self):
		self.clickButton(IoeBaseConst.config.interface.PORT_STATUS_CHECKBOX)

	def setMacAddress(self, p_mac):
		self.setText(IoeBaseConst.config.interface.MAC_ADDRESS_EDIT, p_mac)

	def setDhcp(self):
		self.clickButton(IoeBaseConst.config.interface.DHCP_RADIO)
		
	def setStatic(self):
		self.clickButton(IoeBaseConst.config.interface.STATIC_RADIO)

	def setGateway(self, p_gateway):
		self.setText(IoeBaseConst.config.interface.GATEWAY_EDIT, p_gateway)

	def setIpAddress(self, p_ip):
		self.setText(IoeBaseConst.config.interface.IP_ADDRESS_EDIT, p_ip)

	def setSubnetMask(self, p_subnet):
		self.setText(IoeBaseConst.config.interface.SUBNET_MASK_EDIT, p_subnet)

	def setDnsServer(self, p_dns):
		self.setText(IoeBaseConst.config.interface.DNS_EDIT, p_dns)

	def configureIp(self, p_ip = '', p_subnet = '', p_gateway = '', p_dns = ''):
		self.setStatic()
		if p_ip:
			self.setIpAddress(p_ip)
		if p_subnet:
			self.setSubnetMask(p_subnet)
		if p_gateway:
			self.setGateway(p_gateway)
		if p_dns:
			self.setDnsServer(p_dns)

	def setDhcpv6(self):
		self.clickButton(IoeBaseConst.config.interface.IPv6_DHCP_RADIO)

	def setStaticv6(self):
		self.clickButton(IoeBaseConst.config.interface.IPv6_STATIC_RADIO)

	def setAutoConfig(self):
		self.clickButton(IoeBaseConst.config.interface.IPv6_AUTO_CONFIG_RADIO)

	def setIpv6Address(self, p_ipv6Address):
		self.setText(IoeBaseConst.config.interface.IPv6_ADDRESS_EDIT, p_ipv6Address)

	def setIpv6Subnet(self, p_subnet):
		self.setText(IoeBaseConst.config.interface.IPv6_SUBNET_MASK_EDIT, p_subnet)

	def setIpv6LinkLocal(self, p_linkLocal):
		self.setText(IoeBaseConst.config.interface.IPv6_LINK_LOCAL_ADDRESS_EDIT, p_linkLocal)

	def setIpv6Gateway(self, p_gateway):
		self.setText(IoeBaseConst.config.interface.IPv6_GATEWAY_EDIT, p_gateway)

	def setIpv6Dns(self, p_dns):
		self.setText(IoeBaseConst.config.interface.IPv6_DNS_EDIT, p_dns)
	
	def configureIpv6(self, p_ipv6 = '', p_subnet = '', p_gateway = '', p_dns = '', p_linkLocal = ''):
		self.setStaticv6()
		if p_ipv6:
			self.setIpv6Address(p_ipv6)
		if p_subnet:
			self.setIpv6Subnet(p_subnet)
		if p_gateway:
			self.setIpv6Gateway(p_gateway)
		if p_dns:
			self.setIpv6Dns(p_dns)
		if p_linkLocal:
			self.setIpv6LinkLocal(p_linkLocal)

class Wired(AbstractPort):
	def setBandWidth(self, p_bandWidth = ''):
		if p_bandWidth and not str(p_bandWidth).lower() == 'auto':
			if findObject(self.squishName + IoeBaseConst.config.interface.BANDWIDTH_AUTO_CHECKBOX).checked:
				self.clickButton(IoeBaseConst.config.interface.BANDWIDTH_AUTO_CHECKBOX)
			p_bandWidth = str(p_bandWidth)
			if p_bandwidth == '10':
				self.clickButton(IoeBaseConst.config.interface.BANDWIDTH_10_MBPS_RADIO)
			elif p_bandWidth == '100':
				self.clickButton(IoeBaseConst.config.interface.BANDWIDTH_100_MBPS_RADIO)
			elif p_bandWidth == '1000':
				self.clickButton(IoeBaseConst.config.interface.BANDWIDTH_1000_MBPS_RADIO)
			else:
				raise('Invalid parameters')
		else:
			if not findObject(self.squishName + IoeBaseConst.config.interface.BANDWIDTH_AUTO_CHECKBOX).checked:
				self.clickButton(IoeBaseConst.config.interface.BANDWIDTH_AUTO_CHECKBOX)
		None

	def setDuplex(self, p_duplex):
		if p_duplex and not str(p_duplex).lower() == 'auto':
			if findObject(self.squishName + IoeBaseConst.config.interface.DUPLEX_AUTO_CHECKBOX):
				self.clickButton(IoeBaseConst.config.interface.DUPLEX_AUTO_CHECKBOX)
			p_duplex = p_duplex.lower()
			if p_duplex == 'half':
				self.clickButton(IoeBaseConst.config.interface.DUPLEX_HALF_RADIO)
			elif p_duplex == 'full':
				self.clickButton(IoeBaseConst.config.interface.DUPLEX_FULL_RADIO)
			else:
				raise('Invalid parameters')
		else:
			if not findObject(self.squishName + IoeBaseConst.config.interface.DUPLEX_AUTO_CHECKBOX):
				self.clickButton(IoeBaseConst.config.interface.DUPLEX_AUTO_CHECKBOX)

class Wireless(AbstractPort):
	def setSSID(self, p_ssid):
		self.setText(IoeBaseConst.config.interface.SSID_EDIT, p_ssid)
		None

	def configureAuthentication(self, p_authenticationType = 'disabled', p_keyOrPass = '', p_user = '', p_encryption = ''):
		if p_authenticationType.lower() == 'disabled':
			self.disabled(IoeBaseConst.config.interface.DISABLED_RADIO)
		elif p_authenticationType.lower() == 'wep':
			self.setWep(p_keyOrPass)
		elif p_authenticationType.lower() == 'wpa-psk':
			self.setWpaPsk(p_keyOrPass)
		elif p_authenticationType.lower() == 'wpa2-psk':
			self.setWpa2Psk(p_keyOrPass)
		elif p_authenticationType.lower() == 'wpa':
			self.setWpa(p_keyOrPass, p_user)
		elif p_authenticationType.lower() == 'wpa2':
			self.setWpa2(p_keyOrPass, p_user)
		if p_encryption:
			self.setEncryptionType(p_encryption)

	def setEncryptionType(self, p_encryption):
		self.click(IoeBaseConst.config.interface.ENCRYPTION_TYPE_DROPDOWN)
		self.clickItem(IoeBaseConst.config.interface.ENCRYPTION_TYPE_DROPDOWN, p_encryption)

	def setWep(self, p_key = ''):
		self.clickButton(IoeBaseConst.config.interface.WEP_RADIO)
		if p_key:
			self.setText(IoeBaseConst.config.interface.WEP_KEY_EDIT, p_key)

	def setWpaPsk(self, p_passphrase = ''):
		self.clickButton(IoeBaseConst.config.interface.WPA_PSK_RADIO)
		if p_passphrase:
			self.setText(IoeBaseConst.config.interface.PSK_PASS_PHRASE_EDIT, p_passphrase)

	def setWpa2Psk(self, p_passphrase = ''):
		self.clickButton(IoeBaseConst.config.interface.WPA2_PSK_RADIO)
		if p_passphrase:
			self.setText(IoeBaseConst.config.interface.PSK_PASS_PHRASE_EDIT, p_passphrase)

	def setWpa(self, p_password, user):
		self.clickButton(IoeBaseConst)

class Port:
	wired = Wired()
	wireless = Wireless()
	def __init__(self):
		self.squishName = ''
		
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		self.wired.updateName(p_squishName)
		self.wireless.updateName(p_squishName)

class Files:
	def __init__(self):
		self.squishName = ''
		self.DeviceBase = DeviceBase(self.squishName)
	
	def err(self):
		raise NotImplementedError
	
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		self.DeviceBase = DeviceBase(p_squishName)
	
	def selectFile(self, p_fileName):
		self.DeviceBase.clickItem(IoeBaseConst.config.files.TABLE, p_fileName)
		
	def selectRow(self, p_row):
		self.DeviceBase.click(IoeBaseConst.config.files.TABLE + '.item_' + str(p_row) + '/0')

	def upButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.UP_BUTTON)
	
	def newDirectoryButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.NEW_DIRECTORY_BUTTON)
	
	def newFileButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.NEW_FILE_BUTTON)
	
	def importButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.IMPORT_BUTTON)
	
	def getCurrentPath(self):
		return str(findObect(self.squishName + IoeBaseConst.config.files.FILE_PATH).text)
	
	def newDirectoryPath(self, p_path):
		self.DeviceBase.setText(IoeBaseConst.config.files.NEW_DIRECTORY_LINE_EDIT, p_path)
		
	def newDirectoryOkButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.NEW_DIRECTORY_OK_BUTTON)
	
	def newDirectoryCancelButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.NEW_DIRECTORY_CANCEL_BUTTON)
	
	def newDirectory(self, p_path, p_ok = True):
		self.newDirectoryButton()
		self.newDirectoryPath(p_path)
		if p_ok:
			self.newDirectoryOkButton()
		else:
			self.newDirectoryCancelButton()
	
	def newFilePath(self, p_path):
		self.DeviceBase.setText(IoeBaseConst.config.files.NEW_FILE_LINE_EDIT, p_path)
	
	def newFileOkButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.NEW_FILE_OK_BUTTON)
	
	def newFileCancelButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.NEW_FILE_CANCEL_BUTTON)
	
	def newFile(self, p_path, p_ok = True):
		self.newFileButton()
		self.newFilePath(p_path)
		if p_ok:
			self.newFileOkButton()
		else:
			self.newFileCancelButton()
	
	def importFile(self, p_path):
		self.err()
	
	def saveButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.SAVE_BUTTON)
	
	def fileManagerButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.FILE_MANAGER_BUTTON)
	
	def getRowOfFile(self, p_filename):
		for i in range(findObject(self.squishName + IoeBaseConst.config.files.TABLE).rowCount):
			if p_filename in findObject(self.squishName + IoeBaseConst.config.files.TABLE + '.item_' + str(i+1) + '/0').text:
				return i + 0
		raise ValueError(p_filename + ' not found')
	
	def edit(self, p_filename):
		row = self.getRowOfFile(p_filename)
		self.DeviceBase.click(IoeBaseConst.config.files.TABLE + '.item_' + str(row) + '/1')
		
	def rename(self, p_filename):
		row = self.getRowOfFile(p_filename)
		self.DeviceBase.click(IoeBaseConst.config.files.TABLE + '.item_' + str(row) + '/2')
		
	def delete(self, p_filename, p_yes = True):
		row = self.getRowOfFile(p_filename)
		self.DeviceBase.click(IoeBaseConst.config.files.TABLE + '.item_' + str(row) + '/3')
		if p_yes:
			self.deleteYesButton()
		else:
			self.deleteNoButton()
			
	def deleteYesButton(self):
		self.DeviceBase.click(IoeBaseConst.config.files.DELETE_YES_BUTTON)
	
	def deleteNoButton(self):
		self.DeviceBase.click(IoeBaseConst.config.files.DELETE_NO_BUTTON)
	
	def newFileErrorOkButton(self):
		self.DeviceBase.clickButton(IoeBaseConst.config.files.ERROR_CREATING_FILE_OK_BUTTON)
		
class Config(ConfigBase):
	port = Port()
	files = Files()
	def __init__(self):
		self.squishName = ""

	def updateName(self, p_squishName):
		self.squishName = p_squishName
		super(Config, self).updateName(p_squishName)
		self.port.updateName(p_squishName)
		self.files.updateName(p_squishName)

	def setDisplayName(self, p_displayName):
		self.setText(IoeBaseConst.config.settings.DISPLAY_NAME_EDIT, p_displayName)

	def getSerialNumber(self):
		return findObject(self.squishName + IoeBaseConst.config.settings.SERIAL_NUMBER)
	
	def setupIoeServer(self, p_remoteOrLan, p_serverIp = None, p_userName = None, p_password = None):
		'''First parameter is which radio to press (Remote, Lan, None).
		Second parameter is the server ip.
		Third parameter is the user name.
		Fourth parameter is the password.
		If first is None then the rest can be omitted.'''
		if p_remoteOrLan.lower()[0] == 'r':
			self.clickButton(IoeBaseConst.config.settings.REMOTE_SERVER_RADIO)
		elif p_remoteOrLan.lower[0] == 'l':
			self.clickButton(IoeBaseConst.config.settings.LAN_SERVER_RADIO)
		elif p_remoteOrLan.lower[0] == 'n':
			self.clickButton(IoeBaseConst.config.settings.NONE_RADIO)
			return
		else:
			raise('setupIoeServer takes arguments "Remote", "Lan", or "None" as the first parameter')
		self.setText(IoeBaseConst.config.settings.SERVER_ADDRESS_EDIT, p_serverIp)
		self.setText(IoeBaseConst.config.settings.USER_NAME_EDIT, p_userName)
		self.setText(IoeBaseConst.config.settings.PASSWORD_EDIT, p_password)
		self.connectToIoeServer()
	
	def connectToIoeServer(self):
		self.clickButton(IoeBaseConst.config.settings.CONNECT_BUTTON)