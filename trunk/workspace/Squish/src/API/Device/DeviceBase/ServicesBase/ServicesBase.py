##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.Aaa import Aaa
from API.Device.DeviceBase.ServicesBase.Dhcp import Dhcp
from API.Device.DeviceBase.ServicesBase.Dhcpv6 import Dhcpv6
from API.Device.DeviceBase.ServicesBase.Dns import Dns
from API.Device.DeviceBase.ServicesBase.Email import Email
from API.Device.DeviceBase.ServicesBase.Ftp import Ftp
from API.Device.DeviceBase.ServicesBase.Http import Http
from API.Device.DeviceBase.ServicesBase.Ioe import Ioe
from API.Device.DeviceBase.ServicesBase.Ntp import Ntp
from API.Device.DeviceBase.ServicesBase.Syslog import Syslog
from API.Device.DeviceBase.ServicesBase.Tftp import Tftp
from API.Device.DeviceBase.ServicesBase.VmManagement import VmManagement
from squish import *

class Services(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.http = Http(self)
		self.dhcp = Dhcp(self)
		self.dhcpv6 = Dhcpv6(self)
		self.tftp = Tftp(self)
		self.dns = Dns(self)
		self.syslog = Syslog(self)
		self.aaa = Aaa(self)
		self.ntp = Ntp(self)
		self.email = Email(self)
		self.ftp = Ftp(self)
		self.ioe = Ioe(self)
		self.vmManagement = VmManagement(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.http.updateName(self.squishName)
		self.dhcp.updateName(self.squishName)
		self.dhcpv6.updateName(self.squishName)
		self.tftp.updateName(self.squishName)
		self.dns.updateName(self.squishName)
		self.syslog.updateName(self.squishName)
		self.aaa.updateName(self.squishName)
		self.ntp.updateName(self.squishName)
		self.email.updateName(self.squishName)
		self.ftp.updateName(self.squishName)
		self.ioe.updateName(self.squishName)
		self.vmManagement.updateName(self.squishName)
	
	def getInterfaceObject(self, interface):
		obj = self.objName(".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.servicesScrollView.qt_scrollarea_viewport.QWidget1.QFrame1." + interface)
		return findObject(obj)

	def selectInterface(self, interface):
		'''Select which part of the services to interact with
		pc.services.selectInterface('HTTP')'''
		obj = self.objName(".c_physicalTab.qt_tabwidget_stackedwidget.m_servicesTab.servicesScrollView.qt_scrollarea_viewport.QWidget1.QFrame1." + interface)
		Util().clickButton(obj)
		snooze(0.5)
		