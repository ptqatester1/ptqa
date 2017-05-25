from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
import squish
import object

class ApplicationLabelsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self._closeWindows = parent._closeWindows
		
	def updateName(self, squishName):
		self.squishName = squishName

	def aaaAccounting(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.AAA_ACCOUNTING), **kwargs)
		
	def ipConfiguration(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.IP_CONFIGURATION), **kwargs)
		
	def dialUp(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.DIAL_UP), **kwargs)
		
	def terminal(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.TERMINAL), **kwargs)
		
	def commandPrompt(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.COMMAND_PROMPT), **kwargs)
		
	def webBrowser(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.WEB_BROWSER), **kwargs)
		
	def pcWireless(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.PC_WIRELESS), **kwargs)
		
	def vpn(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.VPN), **kwargs)
		
	def trafficGenerator(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.TRAFFIC_GENERATOR), **kwargs)
		
	def mibBrowser(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.MIB_BROWSER), **kwargs)
		
	def ciscoIpCommunicator(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.IP_COMMUNICATOR), **kwargs)
		
	def email(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.EMAIL), **kwargs)
		
	def pppoeDialer(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.PPPOE_DIALER), **kwargs)
		
	def textEditor(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.TEXT_EDITOR), **kwargs)
		
	def firewall(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.FIREWALL), **kwargs)
		
	def firewallv6(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.FIREWALL_IPV6), **kwargs)
		
	def netflow(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.NETFLOW_COLLECTOR), **kwargs)
		
	def ioxIde(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.IOX_IDE), **kwargs)
		
	def tftpService(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.TFTP_SERVICE), **kwargs)
		
	def ioeMonitor(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.IOE_MONITOR), **kwargs)
		
	def ioeIde(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.labels.IOE_IDE), **kwargs)


class ApplicationLabels(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self._closeWindows = parent._closeWindows
		self.check = ApplicationLabelsCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)

class ApplicationsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self._closeWindows = parent._closeWindows
		
	def updateName(self, squishName):
		self.squishName = squishName
		
	def aaaAccounting(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.AAA_ACCOUNTING), **kwargs)
		
	def ipConfiguration(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.IP_CONFIGURATION), **kwargs)
		
	def dialUp(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.DIAL_UP), **kwargs)
		
	def terminal(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.TERMINAL), **kwargs)
		
	def commandPrompt(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.COMMAND_PROMPT), **kwargs)
		
	def webBrowser(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.WEB_BROWSER), **kwargs)
		
	def pcWireless(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.PC_WIRELESS), **kwargs)
		
	def vpn(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.VPN), **kwargs)
		
	def trafficGenerator(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.TRAFFIC_GENERATOR), **kwargs)
		
	def mibBrowser(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.MIB_BROWSER), **kwargs)
		
	def ciscoIpCommunicator(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.IP_COMMUNICATOR), **kwargs)
		
	def email(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.EMAIL), **kwargs)
		
	def pppoeDialer(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.PPPOE_DIALER), **kwargs)
		
	def textEditor(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.TEXT_EDITOR), **kwargs)
		
	def firewall(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.FIREWALL), **kwargs)
		
	def firewallv6(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.FIREWALL_IPV6), **kwargs)
		
	def netflow(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.NETFLOW_COLLECTOR), **kwargs)
		
	def ioxIde(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.IOX_IDE), **kwargs)
		
	def tftpService(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.TFTP_SERVICE), **kwargs)
		
	def ioeMonitor(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.IOE_MONITOR), **kwargs)
		
	def ioeIde(self, **kwargs):
		self._closeWindows()
		Util().checkProperty(self.objName(DesktopConst.applications.IOE_IDE), **kwargs)

class Applications(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = ApplicationsCheck(self)
		self.labels = ApplicationLabels(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		self.labels.updateName(squishName)
	
	def _closeWindows(self):
		window = '.c_physicalTab.qt_tabwidget_stackedwidget.m_DeskTopTab.scrollArea.qt_scrollarea_viewport.desktopScrollAreaWidgetContents.CDesktopApplet1'
		try:
			obj = squish.findObject(self.objName(window))
		except LookupError, e:
			obj = None
		if obj:
			try:
				obj.close()
			except RuntimeError, e:
				pass#Possible to get a runtime error if the object is being destroyed when found
		
	def aaaAccounting(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.AAA_ACCOUNTING))
		Util().snooze(.5)
		
	def ipConfiguration(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.IP_CONFIGURATION))
		Util().snooze(.5)
		
	def dialUp(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.DIAL_UP))
		Util().snooze(.5)
		
	def terminal(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.TERMINAL))
		Util().snooze(.5)
		
	def commandPrompt(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.COMMAND_PROMPT))
		Util().snooze(.5)
		
	def webBrowser(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.WEB_BROWSER))
		Util().snooze(.5)
		
	def pcWireless(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.PC_WIRELESS))
		Util().snooze(.5)
		
	def vpn(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.VPN))
		Util().snooze(.5)
		
	def trafficGenerator(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.TRAFFIC_GENERATOR))
		Util().snooze(.5)
		
	def mibBrowser(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.MIB_BROWSER))
		Util().snooze(.5)
		
	def ciscoIpCommunicator(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.IP_COMMUNICATOR))
		Util().snooze(.5)
		
	def email(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.EMAIL))
		Util().snooze(.5)
		
	def pppoeDialer(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.PPPOE_DIALER))
		Util().snooze(.5)
		
	def textEditor(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.TEXT_EDITOR))
		Util().snooze(.5)
		
	def firewall(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.FIREWALL))
		Util().snooze(.5)
		
	def firewallv6(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.FIREWALL_IPV6))
		Util().snooze(.5)
		
	def netflow(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.NETFLOW_COLLECTOR))
		Util().snooze(.5)
		
	def ioxIde(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.IOX_IDE))
		Util().snooze(.5)
		
	def tftpService(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.TFTP_SERVICE))
		Util().snooze(.5)
		
	def ioeMonitor(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.IOE_MONITOR))
		Util().snooze(.5)
		
	def ioeIde(self):
		self._closeWindows()
		Util().clickButton(self.objName(DesktopConst.applications.IOE_IDE))
		Util().snooze(.5)