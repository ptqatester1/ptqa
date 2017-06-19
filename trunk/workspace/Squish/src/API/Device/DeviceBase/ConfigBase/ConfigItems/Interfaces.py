##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst
from squish import *
import object
import test
from __builtin__ import object as Object
from API import functions

interface = ConfigConst.interface
util = Util()

class UpdateName(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
		if hasattr(self, 'check'):
			self.check.updateName(squishName)

class PortStatusCheck(UpdateName, SquishObjectName):
	def portStatus(self, checked = True):
		checkbox = findObject(self.objName(ConfigConst.interface.PORT_STATUS_CHECKBOX))
		Util().isChecked(checkbox, checked)

class PortStatus(UpdateName, SquishObjectName):
	def portStatus(self, checked=None):
		if checked == None:
			Util().click(self.objName(ConfigConst.interface.PORT_STATUS_CHECKBOX))
		else:
			checkbox = findObject(self.objName(ConfigConst.interface.PORT_STATUS_CHECKBOX))
			if checked == True:
				if not checkbox.checked:
					Util().click(self.objName(ConfigConst.interface.PORT_STATUS_CHECKBOX))
			elif checked == False:
				if checkbox.checked:
					Util().click(self.objName(ConfigConst.interface.PORT_STATUS_CHECKBOX))
			else:
				raise ValueError('Parameter should be None, True, or False')
			
class BandwidthCheck(UpdateName, SquishObjectName):
	def bandwidth(self, value, checked = True):
		'''
		value: String (The value of the checkbox to check)
		checked: Bool (To check if checked or unchecked)
		'''
		value = value.lower()
		if not value in ['auto', '10', '100', '1000']:
			raise ValueError('Expected must be Auto, 10, 100, or 1000')
		if value == 'auto':
			Util().isChecked(self.objName(ConfigConst.interface.BANDWIDTH_AUTO_CHECKBOX), checked)
		elif value == '10':
			Util().isChecked(self.objName(ConfigConst.interface.BANDWIDTH_10_MBPS_RADIO), checked)
		elif value == '100':
			Util().isChecked(self.objName(ConfigConst.interface.BANDWIDTH_100_MBPS_RADIO), checked)
		elif value == '1000':
			Util().isChecked(self.objName(ConfigConst.interface.BANDWIDTH_1000_MBPS_RADIO), checked)
			
class Bandwidth(UpdateName, SquishObjectName):
	def bandwidth(self, setting=None):
		'''settings can be 1000, 100, 10, or auto'''
		autocheckbox = findObject(self.objName(ConfigConst.interface.BANDWIDTH_AUTO_CHECKBOX))
		if setting == None:
			Util().click(autocheckbox)
			return
		setting = str(setting)
		if setting.lower() == 'auto':
			if not autocheckbox.checked:
				Util().click(autocheckbox)
		else:
			if autocheckbox.checked:
				Util().click(autocheckbox)
			if setting.lower() == '10':
				Util().clickButton(self.objName(ConfigConst.interface.BANDWIDTH_10_MBPS_RADIO))
			elif setting.lower() == '100':
				Util().clickButton(self.objName(ConfigConst.interface.BANDWIDTH_100_MBPS_RADIO))
			elif setting.lower() == '1000':
				Util().clickButton(self.objName(ConfigConst.interface.BANDWIDTH_1000_MBPS_RADIO))
			else:
				raise ValueError('Must be Auto, 10, 100, or 1000')

class WirelessBandwidthCheck(UpdateName, SquishObjectName):
	def bandwidth(self, text):
		Util().textCheckPoint(self.objName(ConfigConst.interface.BANDWIDTH_EDIT), text)

class WirelessBandwidth(UpdateName, SquishObjectName):
	None

class DuplexCheck(UpdateName, SquishObjectName):
	def duplex(self, value, checked):
		value = value.lower()
		if not value in ['half', 'full', 'auto']:
			raise ValueError('Expected must be Auto, half, or full')
		if value == 'auto':
			Util().isChecked(self.objName(ConfigConst.interface.DUPLEX_AUTO_CHECKBOX), checked)
		elif value == 'half':
			Util().isChecked(self.objName(ConfigConst.interface.DUPLEX_HALF_RADIO), checked)
		elif value == 'full':
			Util().isChecked(self.objName(ConfigConst.interface.DUPLEX_FULL_RADIO), checked)
		
class Duplex(UpdateName, SquishObjectName):
	def duplex(self, setting=None):
		'''settings can be half, full, or auto None for toggle'''
		autocheckbox = findObject(self.objName(ConfigConst.interface.DUPLEX_AUTO_CHECKBOX))
		if setting == None:
			Util().click(autocheckbox)
		elif setting.lower() == 'auto':
			if not autocheckbox.checked:
				Util().click(autocheckbox)
		else:
			if autocheckbox.checked:
				Util().click(autocheckbox)
			if setting.lower() == 'half':
				Util().clickButton(self.objName(ConfigConst.interface.DUPLEX_HALF_RADIO))
			elif setting.lower() == 'full':
				Util().clickButton(self.objName(ConfigConst.interface.DUPLEX_FULL_RADIO))
			else:
				raise ValueError('Must be Auto, half, or full')
	
class MacAddressCheck(UpdateName, SquishObjectName):
	def mac(self, expected):
		Util().textCheckPoint(self.objName(ConfigConst.interface.MAC_ADDRESS_EDIT), expected)

class MacAddress(UpdateName, SquishObjectName):
	def mac(self, mac):
		Util().setText(self.objName(ConfigConst.interface.MAC_ADDRESS_EDIT), mac)

class IpConfigurationCheck(UpdateName, SquishObjectName):
	def dhcp(self, checked = True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(ConfigConst.interface.DHCP_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(ConfigConst.interface.DHCP_RADIO), checked)
	
	def static(self, checked = True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(ConfigConst.interface.STATIC_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(ConfigConst.interface.STATIC_RADIO), checked)

	def ip(self, ip, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(ConfigConst.interface.IP_ADDRESS_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(ConfigConst.interface.IP_ADDRESS_EDIT), ip)
		
	def subnet(self, subnet, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(ConfigConst.interface.SUBNET_MASK_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(ConfigConst.interface.SUBNET_MASK_EDIT), subnet)

class IpConfiguration(UpdateName, SquishObjectName):
	def dhcp(self):
		Util().clickButton(self.objName(ConfigConst.interface.DHCP_RADIO))
	
	def static(self):
		Util().clickButton(self.objName(ConfigConst.interface.STATIC_RADIO))

	def ip(self, ip):
		Util().setText(self.objName(ConfigConst.interface.IP_ADDRESS_EDIT), ip)
	
	def autoConfig(self):
		Util().clickButton(self.objName(ConfigConst.interface.IPv6_AUTO_CONFIG_RADIO))
		
	def getIp(self):
		return str(findObject(self.objName(ConfigConst.interface.IP_ADDRESS_EDIT)).text)
	
	def subnet(self, subnet):
		Util().setText(self.objName(ConfigConst.interface.SUBNET_MASK_EDIT), subnet)

class Ipv6ConfigurationCheck(UpdateName, SquishObjectName):
	def dhcpv6(self, checked = True):
		Util().isChecked(self.objName(ConfigConst.interface.IPv6_DHCP_RADIO), checked)
	
	def autoconfig(self, checked = True):
		Util().isChecked(self.objName(ConfigConst.interface.IPv6_AUTO_CONFIG_RADIO), checked)
	
	def staticv6(self, checked = True):
		Util().isChecked(self.objName(ConfigConst.interface.IPv6_STATIC_RADIO), checked)
	
	def ipv6(self, ipv6, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(ConfigConst.interface.IPv6_ADDRESS_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(ConfigConst.interface.IPv6_ADDRESS_EDIT), ipv6)
	
	def subnetv6(self, subnetv6, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(ConfigConst.interface.IPv6_SUBNET_MASK_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(ConfigConst.interface.IPv6_SUBNET_MASK_EDIT), subnetv6)
	
	def linkLocal(self, linkLocal):
		Util().textCheckPoint(self.objName(ConfigConst.interface.IPv6_LINK_LOCAL_ADDRESS_EDIT), linkLocal)

	def gatewayv6(self, gateway):
		Util().textCheckPoint(self.objName(ConfigConst.interface.IPv6_GATEWAY_EDIT), gateway)
	
	def dnsv6(self, dns):
		Util().textCheckPoint(self.objName(ConfigConst.interface.IPv6_DNS_EDIT), dns)

class Ipv6Configuration(UpdateName, SquishObjectName):
	def dhcpv6(self):
		Util().clickButton(self.objName(ConfigConst.interface.IPv6_DHCP_RADIO))
	
	def autoconfig(self):
		Util().clickButton(self.objName(ConfigConst.interface.IPv6_AUTO_CONFIG_RADIO))
	
	def staticv6(self):
		Util().clickButton(self.objName(ConfigConst.interface.IPv6_STATIC_RADIO))
	
	def ipv6(self, ipv6):
		Util().setText(self.objName(ConfigConst.interface.IPv6_ADDRESS_EDIT), ipv6)
	
	def subnetv6(self, subnetv6):
		Util().setText(self.objName(ConfigConst.interface.IPv6_SUBNET_MASK_EDIT), subnetv6)
	
	def linkLocal(self, linkLocal):
		Util().setText(self.objName(ConfigConst.interface.IPv6_LINK_LOCAL_ADDRESS_EDIT), linkLocal)
	
	def gatewayv6(self, gateway):
		Util().setText(self.objName(ConfigConst.interface.IPv6_GATEWAY_EDIT), gateway)
	
	def dnsv6(self, dns):
		Util().setText(self.objName(ConfigConst.interface.IPv6_DNS_EDIT), dns)

class TxRingLimitCheck(UpdateName, SquishObjectName):
	def txRingLimit(self, txRingLimit):
		Util().textCheckPoint(self.objName(ConfigConst.interface.TX_RING_LIMIT_EDIT), txRingLimit)

class TxRingLimit(UpdateName, SquishObjectName):
	def txRingLimit(self, txRingLimit):
		Util().setText(self.objName(ConfigConst.interface.TX_RING_LIMIT_EDIT), txRingLimit)

class WirelessSsidCheck(UpdateName, SquishObjectName):
	def ssid(self, ssid):
		Util().textCheckPoint(self.objName(interface.SSID_EDIT), ssid)

class WirelessSsid(UpdateName, SquishObjectName):
	def ssid(self, ssid):
		Util().setText(self.objName(interface.SSID_EDIT), ssid)

class WirelessChannelCheck(UpdateName, SquishObjectName):
	def channel(self, text):
		Util().textCheckPoint(self.objName(interface.CHANNEL_DROPDOWN), text)

class WirelessChannel(UpdateName, SquishObjectName):
	def channel(self, channel):
		Util().clickItem(self.objName(interface.CHANNEL_DROPDOWN), channel)

class WirelessAuthenticationBaseCheck(UpdateName, SquishObjectName):
	def disabled(self, checked = True):
		Util().isChecked(self.objName(interface.DISABLED_RADIO), checked)
	
	def wep(self, checked = True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(interface.WEP_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(interface.WEP_RADIO), checked)
	
	def wpapsk(self, checked = True):
		Util().isChecked(self.objName(interface.WPA_PSK_RADIO), checked)
	
	def wpa2psk(self, checked = True):
		Util().isChecked(self.objName(interface.WPA2_PSK_RADIO), checked)
	
	def wpa(self, checked = True):
		Util().isChecked(self.objName(interface.WPA_RADIO), checked)
	
	def wpa2(self, checked = True):
		Util().isChecked(self.objName(interface.WPA2_RADIO), checked)
	
	def wepkey(self, key, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(interface.PSK_PASS_PHRASE_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(interface.WEP_KEY_EDIT), key)
		
	def pskPassPhrase(self, passPhrase, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(interface.PSK_PASS_PHRASE_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(interface.PSK_PASS_PHRASE_EDIT), passPhrase)

	def encryption(self, encryption, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(interface.ENCRYPTION_TYPE_DROPDOWN), **kwargs)
		else:
			Util().textCheckPoint(self.objName(interface.ENCRYPTION_TYPE_DROPDOWN), encryption)

class WirelessAuthenticationBase(UpdateName, SquishObjectName):
	def disabled(self):
		Util().clickButton(self.objName(interface.DISABLED_RADIO))
	
	def wep(self):
		Util().clickButton(self.objName(interface.WEP_RADIO))
	
	def wpapsk(self):
		Util().clickButton(self.objName(interface.WPA_PSK_RADIO))
	
	def wpa2psk(self):
		Util().clickButton(self.objName(interface.WPA2_PSK_RADIO))
	
	def wpa(self):
		Util().clickButton(self.objName(interface.WPA_RADIO))
	
	def wpa2(self):
		Util().clickButton(self.objName(interface.WPA2_RADIO))
	
	def wepkey(self, key):
		Util().setText(self.objName(interface.WEP_KEY_EDIT), key)
		
	def pskPassPhrase(self, passPhrase):
		Util().setText(self.objName(interface.PSK_PASS_PHRASE_EDIT), passPhrase)

	def encryption(self, encryption):
		Util().clickItem(self.objName(interface.ENCRYPTION_TYPE_DROPDOWN), encryption)

class WirelessAuthenticationClientCheck(WirelessAuthenticationBaseCheck):
	def userId(self, id, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(interface.USER_ID_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(interface.USER_ID_EDIT), id)

	def password(self, password, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(interface.PASSWORD_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(interface.PASSWORD_EDIT), password)
		
class WirelessAuthenticationClient(WirelessAuthenticationBase):
	def userId(self, id):
		Util().setText(self.objName(interface.USER_ID_EDIT), id)

	def password(self, password):
		Util().setText(self.objName(interface.PASSWORD_EDIT), password)

class WirelessAuthenticationAPCheck(WirelessAuthenticationBaseCheck):
	def channel(self, channel):
		Util().textCheckPoint(self.objName(interface.CHANNEL_DROPDOWN), channel)
	
	def ipAddress(self, radiusServerIp):
		Util().textCheckPoint(self.objName(interface.RADIUS_IP), radiusServerIp)
	
	def sharedSecret(self, secret):
		Util().textCheckPoint(self.objName(interface.SHARED_SECRET), secret)
		
class WirelessAuthenticationAP(WirelessAuthenticationBase):
	def channel(self, channel):
		Util().clickItem(self.objName(interface.CHANNEL_DROPDOWN), channel)
	
	def ipAddress(self, radiusServerIp):
		Util().setText(self.objName(interface.RADIUS_IP), radiusServerIp)
	
	def sharedSecret(self, secret):
		Util().setText(self.objName(interface.SHARED_SECRET), secret)

class VlanCheck(UpdateName, SquishObjectName):
	def portType(self, expected):
		Util().textCheckPoint(self.objName(ConfigConst.interface.TRUNK_COMBO), expected, textProperty='currentText')
	
	def vlanNumber(self, expected):
		Util().textCheckPoint(self.objName(ConfigConst.interface.VLAN_SELECTION_TEXT), expected)

class Vlan(UpdateName, SquishObjectName):
	def portType(self, accessOrTrunk):
		Util().clickItem(self.objName(ConfigConst.interface.TRUNK_COMBO), accessOrTrunk)

	def vlanSelectionDropdownButton(self):
		Util().clickButton(self.objName(ConfigConst.interface.VLAN_SELECTION_DROPDOWN_BUTTON))
		
	def vlanNumber(self, number, name = None):
		self.vlanSelectionDropdownButton()
		dropdown_list = findObject(self.objName(interface.VLAN_SELECTION_DROPDOWN_LIST))
		scrollbar = findObject(self.objName(interface.VLAN_SELECTION_SCROLLBAR))
		for item in object.children(dropdown_list):
			child = object.children(item)[0]#The actual object
			text = str(child.text)
			if text.split(':')[0] == str(number):
				if name:
					if text.split(':')[-1] == name:
						scrollbar.setValue(item.y)
						Util().click(child)
						Util().click(waitForObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2"))
						return
				else:
					scrollbar.setValue(item.y)
					Util().click(child)
					Util().click(waitForObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2"))
					return
		raise ValueError('Could not find vlan %s:%s'%(number, name))
	
class CiscoWiredInterfaceCheck(PortStatusCheck, BandwidthCheck, DuplexCheck, MacAddressCheck, IpConfigurationCheck, TxRingLimitCheck):
	None

class CiscoWiredInterface(PortStatus, Bandwidth, Duplex, MacAddress, IpConfiguration, TxRingLimit):
	def __init__(self, parent):
		super(CiscoWiredInterface, self).__init__(parent)
		self.check = CiscoWiredInterfaceCheck(self)
		
class SerialInterfaceCheck(DuplexCheck, PortStatusCheck, IpConfigurationCheck, TxRingLimitCheck):
	def clockrate(self, clockrate):
		Util().textCheckPoint(self.objName(interface.CLOCKRATE_COMBO), clockrate)
	None
	
class SerialInterface(PortStatus, IpConfiguration, TxRingLimit):
	def __init__(self, parent):
		super(SerialInterface, self).__init__(parent)
		self.check = SerialInterfaceCheck(self)
	
	def clockrate(self, clockrate):
		validOptions = ['1200', '2400', '4800', '9600', '19200', '38400', '56000', '64000',
						'72000', '125000', '128000', '148000', '250000', '500000', '800000',
						'1000000', '1300000', '2000000', '4000000', 'Not Set']
		if not clockrate in validOptions:
			raise ValueError('%s is not in %s'%(clockrate, ', '.join(validOptions)))
		Util().clickItem(self.objName(interface.CLOCKRATE_COMBO), clockrate)
	
class SwitchInterfaceCheck(PortStatusCheck, BandwidthCheck, DuplexCheck, VlanCheck, TxRingLimitCheck):
	None

class SwitchInterface(PortStatus, Bandwidth, Duplex, Vlan, TxRingLimit):
	def __init__(self, parent):
		super(SwitchInterface, self).__init__(parent)
		self.check = SwitchInterfaceCheck(self)
		
class CiscoWirelessInterfaceCheck(PortStatusCheck, MacAddressCheck, IpConfigurationCheck, TxRingLimitCheck):
	None
	
class CiscoWirelessInterface(PortStatus, MacAddress, IpConfiguration, TxRingLimit):
	def __init__(self, parent):
		super(CiscoWirelessInterface, self).__init__(parent)
		self.check = CiscoWirelessInterfaceCheck(self)
		
class CellularInterfaceCheck(PortStatusCheck, IpConfigurationCheck, Ipv6ConfigurationCheck, UpdateName, SquishObjectName):
	def coverageRange(self, range):
		Util().textCheckPoint(self.objName(interface.COVERAGE_RATE_COMBO), range)
	
class CellularInterface(UpdateName, SquishObjectName):
	def __init__(self, parent):
		super(CellularInterface, self).__init__(parent)
		self.check = CellularInterfaceCheck(self)
		
	def dhcpRefresh(self):
		Util().clickButton(self.objName(ConfigConst.interface.DHCP_REFRESH))

	def dhcpv6Refresh(self):
		Util().clickButton(self.objName(ConfigConst.interface.DHCPv6_REFRESH))
	
class BluetoothInterface(PortStatus, UpdateName, SquishObjectName):
	def __init__(self, parent):
		super(BluetoothInterface, self).__init__(parent)
	
	def discoverButton(self):
		Util().clickButton(self.objName(ConfigConst.interface.bluetooth.DISCOVER_BUTTON))
	
	@property
	def bluetoothTableName(self):
		return self.objName(ConfigConst.interface.bluetooth.TABLE)

	@property
	def bluetoothTable(self):
		return findObject(self.bluetoothTableName)
	
	def pairButton(self):
		Util().clickButton(self.objName(ConfigConst.interface.bluetooth.PAIR_BUTTON))
	
	def selectDeviceInTable(self, device_name):
		for i in range(self.bluetoothTable.rowCount):
			name_cell = findObject('%s.item_%s/0' % (self.bluetoothTableName, i))
			name = name_cell.text
			if name == device_name:
				Util().click(name_cell)
				return
		raise ValueError('Unable to find device with name %s' % (device_name))
	
	def pair(self, device_name, select_popup_yes = True):
		self.selectDeviceInTable(device_name)
		self.pairButton()
		for i in range(10): # There is a short delay between clicking pair and the popup 
			snooze(0.1)
			if object.exists(ConfigConst.interface.bluetooth.BLUETOOTH_PAIRING_POPUP_DIALOG):
				if select_popup_yes:
					Util().clickButton(ConfigConst.interface.bluetooth.BLUETOOTH_PAIRING_POPUP_DIALOG_YES)
					return
				else:
					Util().clickButton(ConfigConst.interface.bluetooth.BLUETOOTH_PAIRING_POPUP_DIALOG_NO)
					return
			
		
class WiredInterfaceCheck(PortStatusCheck, BandwidthCheck, DuplexCheck, MacAddressCheck, IpConfigurationCheck, Ipv6ConfigurationCheck):
	None
	
class WiredInterface(PortStatus, Bandwidth, Duplex, MacAddress, IpConfiguration, Ipv6Configuration):
	def __init__(self, parent):
		super(WiredInterface, self).__init__(parent)
		self.check = WiredInterfaceCheck(self)
		
class WirelessInterfaceCheck(WirelessSsidCheck, WirelessBandwidthCheck, WirelessAuthenticationClientCheck, PortStatusCheck, MacAddressCheck, IpConfigurationCheck):
	None
	
class WirelessInterface(WirelessSsid, WirelessBandwidth, WirelessAuthenticationClient, PortStatus, MacAddress, IpConfiguration):
	def __init__(self, parent):
		super(WirelessInterface, self).__init__(parent)
		self.check = WirelessInterfaceCheck(self)

class ApWirelessInterfaceCheck(WirelessInterfaceCheck, WirelessChannelCheck):
	None
class ApWirelessInterface(WirelessInterface, WirelessChannel):
	def __init__(self, parent):
		super(ApWirelessInterface, self).__init__(parent)
		self.check = ApWirelessInterfaceCheck(self)

class InternetCheck(IpConfigurationCheck):
	def pppoe(self, checked = True):
		checkbox = self.objName(interface.PPPOE_RADIO)
		Util().isChecked(checkbox, checked)
	
	def username(self, expected):
		Util().textCheckPoint(self.objName(interface.PPPOE_USERNAME), expected)
	
	def password(self, expected, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(interface.PPPOE_PASSWORD), **kwargs)
		else:
			Util().textCheckPoint(self.objName(interface.PPPOE_PASSWORD), expected)
	
	def gateway(self, gateway):
		Util().textCheckPoint(self.objName(interface.GATEWAY_EDIT), gateway)
	
	def dns(self, dns):
		Util().textCheckPoint(self.objName(interface.DNS_EDIT), dns)
	
	
class Internet(IpConfiguration):
	def __init__(self, parent):
		super(Internet, self).__init__(parent)
		self.check = InternetCheck(self)
		
	def pppoe(self):
		Util().clickButton(self.objName(interface.PPPOE_RADIO))
	
	def username(self, pppoeUsername):
		Util().setText(self.objName(interface.PPPOE_USERNAME), pppoeUsername)
	
	def password(self, pppoePassword):
		Util().setText(self.objName(interface.PPPOE_PASSWORD), pppoePassword)
	
	def gateway(self, gateway):
		Util().setText(self.objName(interface.GATEWAY_EDIT), gateway)
	
	def dns(self, dns):
		Util().setText(self.objName(interface.DNS_EDIT), dns)
		
	def setInternetAddress(self, ip, subnet, gateway = None, dns = None):
		self.static()
		self.ip(ip)
		self.subnet(subnet)
		if gateway:
			self.gateway(gateway)
		if dns:
			self.dns(dns)
	
class LanCheck(UpdateName, SquishObjectName):
	def ip(self, expected):
		Util().textCheckPoint(self.objName(interface.IP_ADDRESS_EDIT), expected)
	
	def subnet(self, expected):
		Util().textCheckPoint(self.objName(interface.SUBNET_MASK_EDIT), expected)
		
class Lan(UpdateName, SquishObjectName):
	def __init__(self, parent):
		super(Lan, self).__init__(parent)
		self.check = LanCheck(self)
		
	def ip(self, ip):
		Util().setText(self.objName(interface.IP_ADDRESS_EDIT), ip)
	
	def subnet(self, subnet):
		Util().setText(self.objName(interface.SUBNET_MASK_EDIT), subnet)
	
class WirelessRouterInterfaceCheck(WirelessAuthenticationAPCheck, WirelessSsidCheck):
	None
	
class WirelessRouterInterface(WirelessAuthenticationAP, WirelessSsid):
	def __init__(self, parent):
		super(WirelessRouterInterface, self).__init__(parent)
		self.check = WirelessRouterInterfaceCheck(self)
		