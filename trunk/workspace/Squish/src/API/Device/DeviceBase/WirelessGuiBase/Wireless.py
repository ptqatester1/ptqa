##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.WirelessGuiBase.WirelessGuiBaseConst import WirelessGuiConst
from API.Device.DeviceBase.WirelessGuiBase.ConstantsHelper import ConstantsHelper
from squish import *
import object


class BasicWirelessSettingsCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	def networkMode(self, mode):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.MODE_COMBO), mode, textProperty='currentText')
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.PC_MODE_COMBO), mode, textProperty='currentText')
	
	def networkName(self, ssid):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.SSID_EDIT), ssid)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.PC_SSID_EDIT), ssid)
	
	def radioBand(self, band):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.RADIO_BAND), band, textProperty='currentText')
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.PC_RADIO_BAND), band, textProperty='currentText')
	
	def wideChannel(self, wideChannel):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.WIDE_CHANNEL_COMBO), wideChannel, textProperty='currentText')
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.PC_WIDE_CHANNEL_COMBO), wideChannel, textProperty='currentText')
	
	def standardChannel(self, channel):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.STANDARD_CHANNEL_COMBO), channel, textProperty='currentText')
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.basicSettings.PC_STANDARD_CHANNEL_COMBO), channel, textProperty='currentText')
	
	def ssidBroadcastEnabled(self, checked=True):
		if self.isRouter:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.basicSettings.SSID_BROADCAST_ENABLED), checked)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.basicSettings.PC_SSID_BROADCAST_ENABLED), checked)
			
	def ssidBroadcastDisabled(self, checked=True):
		if self.isRouter:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.basicSettings.SSID_BROADCAST_DISABLED), checked)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.basicSettings.PC_SSID_BROADCAST_DISABLED), checked)

class BasicWirelessSettings(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = BasicWirelessSettingsCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def networkMode(self, mode):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.basicSettings.MODE_COMBO), mode)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.basicSettings.PC_MODE_COMBO), mode)

	def networkName(self, ssid):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.basicSettings.SSID_EDIT), ssid)
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.basicSettings.PC_SSID_EDIT), ssid)
	
	def radioBand(self, band):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.basicSettings.RADIO_BAND), band)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.basicSettings.PC_RADIO_BAND), band)
	
	def wideChannel(self, wideChannel):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.basicSettings.WIDE_CHANNEL_COMBO), wideChannel)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.basicSettings.PC_WIDE_CHANNEL_COMBO), wideChannel)
	
	def standardChannel(self, channel):
		if self.isRouter:
			combo = findObject(self.objName(WirelessGuiConst.wireless.basicSettings.STANDARD_CHANNEL_COMBO))
		else:
			combo = findObject(self.objName(WirelessGuiConst.wireless.basicSettings.PC_STANDARD_CHANNEL_COMBO))
		for item in object.children(combo):
			if 'text' in object.properties(item):
				if channel in str(item.text):
					combo.setCurrentIndex(item.row)
	
	def ssidBroadcastEnabled(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.basicSettings.SSID_BROADCAST_ENABLED))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.basicSettings.PC_SSID_BROADCAST_ENABLED))
	
	def ssidBroadcastDisabled(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.basicSettings.SSID_BROADCAST_DISABLED))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.basicSettings.PC_SSID_BROADCAST_DISABLED))
	
	def saveSettingsButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.basicSettings.SAVE_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.basicSettings.PC_SAVE_SETTINGS_BUTTON))
	
	def cancelChangesButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.basicSettings.CANCEL_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.basicSettings.PC_CANCEL_SETTINGS_BUTTON))
	
class WepSecurityModeCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def encryption(self, encryption, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.ENCRYPTION_COMBO), textProperty='currentText', **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.ENCRYPTION_COMBO), encryption, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.PC_ENCRYPTION_COMBO), textProperty='currentText', **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.PC_ENCRYPTION_COMBO), encryption, **kwargs)
			
	def key1(self, key, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.KEY1_EDIT), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.KEY1_EDIT), key, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.PC_KEY1_EDIT), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.PC_KEY1_EDIT), key, **kwargs)
			

class WepSecurityMode(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = WepSecurityModeCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)

	def encryption(self, encryption):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.ENCRYPTION_COMBO), encryption)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.PC_ENCRYPTION_COMBO), encryption)
			
	def key1(self, key):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.KEY1_EDIT), key)
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wep.PC_KEY1_EDIT), key)

class WpaPersonalSecurityModeCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def encryption(self, encryption, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.ENCRYPTION_COMBO), textProperty='currentText', **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.ENCRYPTION_COMBO), encryption, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_ENCRYPTION_COMBO), textProperty='currentText', **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_ENCRYPTION_COMBO), encryption, **kwargs)
	
	def passphrase(self, passphrase, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PASSPRHASE_EDIT), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PASSPRHASE_EDIT), passphrase, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_PASSPRHASE_EDIT), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_PASSPRHASE_EDIT), passphrase, **kwargs)
			
			
class WpaPersonalSecurityMode(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = WpaPersonalSecurityModeCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def encryption(self, encryption):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.ENCRYPTION_COMBO), encryption)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_ENCRYPTION_COMBO), encryption)
	
	def passphrase(self, passphrase):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PASSPRHASE_EDIT), passphrase)
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_PASSPRHASE_EDIT), passphrase)

class WpaEnterpriseSecurityModeCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def encryption(self, encryption, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.ENCRYPTION_COMBO), textProperty='currentText', **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.ENCRYPTION_COMBO), encryption, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_ENCRYPTION_COMBO), textProperty='currentText', **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_ENCRYPTION_COMBO), encryption, **kwargs)
			
	def radiusServer_octet_1(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP1), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP1), ip, **kwargs)
			
	def radiusServer_octet_2(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP2), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP2), ip, **kwargs)
			
	def radiusServer_octet_3(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP3), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP3), ip, **kwargs)
			
	def radiusServer_octet_4(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP4), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP4), ip, **kwargs)
			
		
	def radiusServer(self, ip, **kwargs):
		ipList = ip.split('.')
		self.radiusServer_octet_1(ipList[0], **kwargs)
		self.radiusServer_octet_2(ipList[1], **kwargs)
		self.radiusServer_octet_3(ipList[2], **kwargs)
		self.radiusServer_octet_4(ipList[3], **kwargs)

	def sharedSecret(self, secret, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.SHARED_SECRET), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.SHARED_SECRET), secret, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_SHARED_SECRET), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_SHARED_SECRET), secret, **kwargs)
			

class WpaEnterpriseSecurityMode(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = WpaEnterpriseSecurityModeCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def encryption(self, encryption):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.ENCRYPTION_COMBO), encryption)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_ENCRYPTION_COMBO), encryption)
		
	def radiusServer(self, ip):
		ipList = ip.split('.')
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP1), ipList[0])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP2), ipList[1])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP3), ipList[2])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP4), ipList[3])
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP1), ipList[0])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP2), ipList[1])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP3), ipList[2])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP4), ipList[3])
			
	def sharedSecret(self, secret):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.SHARED_SECRET), secret)
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_SHARED_SECRET), secret)

class Wpa2PersonalSecurityModeCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def encryption(self, encryption, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.ENCRYPTION_COMBO), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.ENCRYPTION_COMBO), encryption, textProperty='currentText', **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_ENCRYPTION_COMBO), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_ENCRYPTION_COMBO), encryption, textProperty='currentText', **kwargs)
			
	
	def passphrase(self, passphrase, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PASSPRHASE_EDIT), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PASSPRHASE_EDIT), passphrase, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_PASSPRHASE_EDIT), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_PASSPRHASE_EDIT), passphrase, **kwargs)
			

class Wpa2PersonalSecurityMode(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = Wpa2PersonalSecurityModeCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def encryption(self, encryption):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.ENCRYPTION_COMBO), encryption)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_ENCRYPTION_COMBO), encryption)
	
	def passphrase(self, passphrase):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PASSPRHASE_EDIT), passphrase)
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaPersonal.PC_PASSPRHASE_EDIT), passphrase)

class Wpa2EnterpriseCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def encryption(self, encryption, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.ENCRYPTION_COMBO), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.ENCRYPTION_COMBO), encryption, textProperty='currentText', **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_ENCRYPTION_COMBO), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_ENCRYPTION_COMBO), encryption, textProperty='currentText', **kwargs)
			
	
	def radiusServer_octet_1(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP1), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP1), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP1), ip, **kwargs)
			

	def radiusServer_octet_2(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP2), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP2), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP2), ip, **kwargs)
			

	def radiusServer_octet_3(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP3), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP3), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP3), ip, **kwargs)
			
	def radiusServer_octet_4(self, ip, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP4), ip, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP4), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP4), ip, **kwargs)
			
			
	def radiusServer(self, ip, **kwargs):
		ipList = ip.split('.')
		self.radiusServer_octet_1(ipList[0], **kwargs)
		self.radiusServer_octet_2(ipList[1], **kwargs)
		self.radiusServer_octet_3(ipList[2], **kwargs)
		self.radiusServer_octet_4(ipList[3], **kwargs)
		
	def sharedSecret(self, secret, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.SHARED_SECRET), **kwargs)
			else:
				Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.SHARED_SECRET), secret)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_SHARED_SECRET), **kwargs)
			else:
				Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_SHARED_SECRET), secret)
			

class Wpa2Enterprise(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = Wpa2EnterpriseCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)

	def encryption(self, encryption):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.ENCRYPTION_COMBO), encryption)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_ENCRYPTION_COMBO), encryption)
		
	def radiusServer(self, ip):
		ipList = ip.split('.')
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP1), ipList[0])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP2), ipList[1])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP3), ipList[2])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.RADIUS_SERVER_IP4), ipList[3])
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP1), ipList[0])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP2), ipList[1])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP3), ipList[2])
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_RADIUS_SERVER_IP4), ipList[3])

	def sharedSecret(self, secret):
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.SHARED_SECRET), secret)
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.wirelessSecurity.wpaEnterprise.PC_SHARED_SECRET), secret)

class WirelessSecurityCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	def securityMode(self, mode, **kwargs):
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.SECURITY_MODE), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.SECURITY_MODE), mode, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.wirelessSecurity.PC_SECURITY_MODE), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.wirelessSecurity.PC_SECURITY_MODE), mode, **kwargs)


class WirelessSecurity(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.wep = WepSecurityMode(self)
		self.wpaPersonal = WpaPersonalSecurityMode(self)
		self.wpaEnterprise = WpaEnterpriseSecurityMode(self)
		self.wpa2Personal = Wpa2PersonalSecurityMode(self)
		self.wpa2Enterprise = Wpa2Enterprise(self)
		self.check = WirelessSecurityCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.wep.updateName(squishName)
		self.wpaPersonal.updateName(squishName)
		self.wpaEnterprise.updateName(squishName)
		self.wpa2Personal.updateName(squishName)
		self.wpa2Enterprise.updateName(squishName)
		self.check.updateName(squishName)
		
	def securityMode(self, mode):
		if self.isRouter:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.SECURITY_MODE), mode)
		else:
			Util().clickItem(self.objName(WirelessGuiConst.wireless.wirelessSecurity.PC_SECURITY_MODE), mode)

	def saveSettingsButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.wirelessSecurity.SAVE_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.wirelessSecurity.PC_SAVE_SETTINGS_BUTTON))
	
	def cancelChangesButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.wirelessSecurity.CANCEL_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.wirelessSecurity.PC_CANCEL_SETTINGS_BUTTON))

class WirelessMacFilterCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def enabled(self, checked=True):
		if self.isRouter:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.macFilters.ENABLED_RADIO), checked)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.macFilters.PC_ENABLED_RADIO), checked)
	
	def disabled(self, checked=True):
		if self.isRouter:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.macFilters.DISABLED_RADIO), checked)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.macFilters.PC_DISABLED_RADIO), checked)
	
	def preventPcsListed(self, checked=True):
		if self.isRouter:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.macFilters.PREVENT_PCS_LISTED_RADIO), checked)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.macFilters.PC_PREVENT_PCS_LISTED_RADIO), checked)
	
	def permitPcsListed(self, checked=True):
		if self.isRouter:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.macFilters.PERMIT_PCS_LISTS_RADIO), checked)
		else:
			Util().isChecked(self.objName(WirelessGuiConst.wireless.macFilters.PC_PERMIT_PCS_LISTS_RADIO), checked)
			
	def mac(self, mac, number, **kwargs):
		'''mac: String - (mac address to check)
		   number: Int - (1-50)'''
		if self.isRouter:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.macFilters.MAC_EDIT_BASE + str(number)), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.macFilters.MAC_EDIT_BASE + str(number)), mac, **kwargs)
		else:
			if 'property' in kwargs:
				Util().checkProperty(self.objName(WirelessGuiConst.wireless.macFilters.PC_MAC_EDIT_BASE + str(number)), **kwargs)
			else:
				Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.macFilters.PC_MAC_EDIT_BASE + str(number)), mac, **kwargs)
			
	
class WirelessMacFilter(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = WirelessMacFilterCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		
	def enabled(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.ENABLED_RADIO))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.PC_ENABLED_RADIO))
	
	def disabled(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.DISABLED_RADIO))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.PC_DISABLED_RADIO))
	
	def preventPcsListed(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.PREVENT_PCS_LISTED_RADIO))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.PC_PREVENT_PCS_LISTED_RADIO))
	
	def permitPcsListed(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.PERMIT_PCS_LISTS_RADIO))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.PC_PERMIT_PCS_LISTS_RADIO))
	
	def addMac(self, mac, lineNumber):
		'''mac: String - (mac address to add)
		   lineNumber: Int - (1-50)'''
		formattedMac = ''
		if not ':' in mac:
			for i, c in enumerate(mac):
				if i % 2 == 0 and not i == 0:
					formattedMac += ':'
				formattedMac += c
		else:
			formattedMac = mac
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.macFilters.MAC_EDIT_BASE + str(lineNumber)), formattedMac)
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.macFilters.PC_MAC_EDIT_BASE + str(lineNumber)), formattedMac)	
		
	def removeMac(self, lineNumber):
		#lineNumber: Int - (1-50)
		if self.isRouter:
			Util().setText(self.objName(WirelessGuiConst.wireless.macFilters.MAC_EDIT_BASE + str(lineNumber)), "<Ctrl+A>")
			Util().setText(self.objName(WirelessGuiConst.wireless.macFilters.MAC_EDIT_BASE + str(lineNumber)), "<Del>")
		else:
			Util().setText(self.objName(WirelessGuiConst.wireless.macFilters.PC_MAC_EDIT_BASE + str(lineNumber)), "<Ctrl+A>")
			Util().setText(self.objName(WirelessGuiConst.wireless.macFilters.PC_MAC_EDIT_BASE + str(lineNumber)), "<Del>")
			
	def saveSettingsButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.SAVE_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.PC_SAVE_SETTINGS_BUTTON))
	
	def cancelChangesButton(self):
		if self.isRouter:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.CANCEL_SETTINGS_BUTTON))
		else:
			Util().clickButton(self.objName(WirelessGuiConst.wireless.macFilters.PC_CANCEL_SETTINGS_BUTTON))
		
class AdvancedWirelessSettingsCheck(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def wirelessAuthenticationType(self, type):
		if self.isRouter:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.administration.WIRELESS_AUTHENTICATION_TYPE_COMBO), type)
		else:
			Util().textCheckPoint(self.objName(WirelessGuiConst.wireless.administration.PC_WIRELESS_AUTHENTICATION_TYPE_COMBO), type)


class AdvancedWirelessSettings(ConstantsHelper):
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.check = AdvancedWirelessSettingsCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def isVisible(self):
		return findObject(':CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_guiTab.QScrollArea1.qt_scrollarea_viewport.QWidget1.CBaseLinkSysGUI.CBaseAdvWirelessSecurity.m_middlePanel').visible
		
class Wireless:
	def __init__(self, parent):
		self.isRouter = parent.isRouter
		self.squishName = parent.squishName
		self.basicWirelessSettings = BasicWirelessSettings(self)
		self.wirelessSecurity = WirelessSecurity(self)
		self.macFilter = WirelessMacFilter(self)
		self.advancedWirelessSettings = AdvancedWirelessSettings(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.basicWirelessSettings.updateName(self.squishName)
		self.wirelessSecurity.updateName(self.squishName)
		self.macFilter.updateName(self.squishName)
		self.advancedWirelessSettings.updateName(self.squishName)
		
	def scrollToTop(self):
		if self.isRouter:
			Util().scrollTo(self.squishName + WirelessGuiConst.VERTICAL_SCROLLBAR, 0)
		else:
			Util().scrollTo(self.squishName + WirelessGuiConst.PC_VERTICAL_SCROLLBAR, 0)
			