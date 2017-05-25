##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from squish import *

class PopupWarnings(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		
	def updateName(self, squishName):
		self.squishName = squishName
		
	@property
	def serverDefaultGatewayWarningDialog(self):
		try:
			return findObject(self.objName(DesktopConst.ipConfiguration.DEFAULT_GATEWAY_WARNING_DIALOG))
		except LookupError, e:
			return False

	def serverDefaultGatewayWarningOkButton(self):
		Util().click(self.objName(DesktopConst.ipConfiguration.DEFAULT_GATEWAY_WARNING_OK_BUTTON))
	

class IpConfigCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	def ip(self, ip, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.IP_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.IP_EDIT), ip, **kwargs)
		
	def subnet(self, subnet, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.SUBNET_MASK_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.SUBNET_MASK_EDIT), subnet, **kwargs)
		
	def gateway(self, gateway, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.GATEWAY_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.GATEWAY_EDIT), gateway, **kwargs)
		
	def ipv6(self, ipv6, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.IPV6_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.IPV6_EDIT), ipv6, **kwargs)
		
	def subnetv6(self, subnetv6, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.SUBNETV6_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.SUBNETV6_EDIT), subnetv6, **kwargs)
		
	def linkLocal(self, linkLocal, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.LOCAL_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.LOCAL_EDIT), linkLocal, **kwargs)
		
	def gatewayv6(self, gatewayv6, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.GATEWAYv6_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.GATEWAYv6_EDIT), gatewayv6, **kwargs)
		
	def dns(self, dns, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.DNS_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.DNS_EDIT), dns, **kwargs)
		
	def dnsv6(self, dnsv6, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.DNSv6_EDIT), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.DNSv6_EDIT), dnsv6, **kwargs)
		
	def status(self, status, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.STATUS_LABEL), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.STATUS_LABEL), status, **kwargs)
	
	def statusv6(self, status, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.IPV6_STATUS), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ipConfiguration.IPV6_STATUS), status, **kwargs)
	
	def static(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.STATIC_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(DesktopConst.ipConfiguration.STATIC_RADIO), checked)
	
	def dhcp(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.DHCP_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(DesktopConst.ipConfiguration.DHCP_RADIO), checked)
	
	def staticv6(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.STATICv6_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(DesktopConst.ipConfiguration.STATICv6_RADIO), checked)
	
	def dhcpv6(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.DHCPv6_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(DesktopConst.ipConfiguration.DHCPv6_RADIO), checked)
		
	def autoconfig(self, checked=True, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ipConfiguration.AUTOCONFIGv6_RADIO), **kwargs)
		else:
			Util().isChecked(self.objName(DesktopConst.ipConfiguration.AUTOCONFIGv6_RADIO), checked)
	
	
class IpConfiguration(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = IpConfigCheck(self)
		self.popups = PopupWarnings(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		self.popups.updateName(squishName)
	
	def dhcp(self):
		Util().clickButton(self.objName(DesktopConst.ipConfiguration.DHCP_RADIO))
		
	def static(self):
		Util().clickButton(self.objName(DesktopConst.ipConfiguration.STATIC_RADIO))
	
	def ip(self, ip):
		Util().setText(self.objName(DesktopConst.ipConfiguration.IP_EDIT), ip)
	
	def getIp(self):
		return str(findObject(self.objName(DesktopConst.ipConfiguration.IP_EDIT)).text)
		
	def interface(self, interface):
		Util().clickItem(self.objName(DesktopConst.ipConfiguration.INTERFACES_DROPDOWN), interface)
		
	def subnet(self, subnet):
		Util().setText(self.objName(DesktopConst.ipConfiguration.SUBNET_MASK_EDIT), subnet)
	
	def gateway(self, gateway):
		Util().setText(self.objName(DesktopConst.ipConfiguration.GATEWAY_EDIT), gateway)
	
	def dns(self, dns):
		Util().setText(self.objName(DesktopConst.ipConfiguration.DNS_EDIT), dns)
	
	def dhcpv6(self):
		Util().clickButton(self.objName(DesktopConst.ipConfiguration.DHCPv6_RADIO))
	
	def autoconfig(self):
		Util().clickButton(self.objName(DesktopConst.ipConfiguration.AUTOCONFIGv6_RADIO))
	
	def staticv6(self):
		Util().clickButton(self.objName(DesktopConst.ipConfiguration.STATICv6_RADIO))
	
	def ipv6(self, ipv6):
		Util().setText(self.objName(DesktopConst.ipConfiguration.IPV6_EDIT), ipv6)
	
	def subnetv6(self, subnetv6):
		Util().setText(self.objName(DesktopConst.ipConfiguration.SUBNETV6_EDIT), subnetv6)
	
	def linkLocal(self, linkLocal):
		Util().setText(self.objName(DesktopConst.ipConfiguration.LOCAL_EDIT), linkLocal)
	
	def gatewayv6(self, gatewayv6):
		Util().setText(self.objName(DesktopConst.ipConfiguration.GATEWAYv6_EDIT), gatewayv6)
	
	def dnsv6(self, dnsv6):
		Util().setText(self.objName(DesktopConst.ipConfiguration.DNSv6_EDIT), dnsv6)

	def close(self):
		Util().clickButton(self.objName(DesktopConst.ipConfiguration.CLOSE_BUTT))

	def textCheckPoint(self, text, occurrenceNum = -1):
		Util().textCheckPoint(self.objName(DesktopConst.webbrowser.BROWSER_CONTENT_WINDOW), text, occurrenceNum)
		
	def setIPConfiguration(self, ip, subnet = None, gateway = None, dns = None):
		self.static()
		if ip:
			self.ip(ip)
		if subnet:
			self.subnet(subnet)
		if gateway:
			self.gateway(gateway)
		if dns: 
			self.dns(dns)
		
	def setIpv6Configuration(self, ip, subnet = None, gateway = None, dns = None):
		self.staticv6()
		if ip:
			self.ipv6(ip)
		if subnet:
			self.subnetv6(subnet)
		if gateway:
			self.gatewayv6(gateway)
		if dns: 
			self.dnsv6(dns)