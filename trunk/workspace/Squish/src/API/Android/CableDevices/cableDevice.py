########################################
#@author: Chris Allen                  #
#@summary: Constants for device cabling#
########################################
from API.Android.SquishSyntax import SquishSyntax
from API.Android.ContextMenus.ContextMenusConst import CableDevices
from API.Android.CableDevices.cableDeviceConst import PortInterface
from API.Android.CableDevices.cableDeviceConst import CableTypeMenu
from API.Android.Workspace.WorkspaceConst import NavigationBarConst
from squish import *

class cableDevices (SquishSyntax):
	def __init__(self):
		pass
	
	def chooseCable(self, p_cable):
		self.tap(CableTypeMenu.CHOOSE_CABLE)
		self.tap(p_cable)
	
	def selectPorts(self, p_port1, p_port2):
		port1 = PortInterface.PORT_BASE + str(p_port1) + PortInterface.PORT_END
		port2 = PortInterface.PORT_BASE + str(p_port2) + PortInterface.PORT_END
		self.tap(port1)
		snooze(5)
		self.tap(port2)
		
	def selectPort(self, p_port):
		port = 	PortInterface.PORT_BASE + str(p_port) + PortInterface.PORT_END	
		self.tap(port)
		
	def selectDevices(self, p_dev1, p_dev2):
		p_dev1.select()
		snooze(1)
		p_dev1.menu.selectConnect()
		snooze(1)
		p_dev2.select()
	
	def connect(self, p_dev1, p_dev2, p_cableType, p_port1, p_port2):
		self.selectDevices(p_dev1, p_dev2)
		snooze(5)
		self.chooseCable(p_cableType)
		snooze(5)
		self.selectPorts(p_port1, p_port2)
		p_dev1.returnToWorkspace()

	def disconnect(self, p_dev1, p_dev2, p_port1):
		self.selectDevices(p_dev1, p_dev2)
		snooze(5)
		self.selectPort(p_port1)
		self.tap(NavigationBarConst.WORKSPACE_BUTTON)
		#p_dev1.returnToWorkspace()		
		
	def autoConnect(self, p_dev1, p_dev2):
		p_dev1.select()
		snooze(2)
		p_dev1.menu.selectAutoConnect()
		p_dev2.select()