##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.DeviceBase.DesktopBase.DesktopApplications import Applications
from API.Device.DeviceBase.DesktopBase.IpConfiguration import IpConfiguration
from API.Device.DeviceBase.DesktopBase.DialUp import DialUp
from API.Device.DeviceBase.DesktopBase.Terminal import Terminal
from API.Device.DeviceBase.DesktopBase.CommandPrompt import CommandPrompt
from API.Device.DeviceBase.DesktopBase.WebBrowser import WebBrowser
from API.Device.DeviceBase.DesktopBase.PCWireless import PCWireless
from API.Device.DeviceBase.DesktopBase.VPN import Vpn
from API.Device.DeviceBase.DesktopBase.TrafficGenerator import TrafficGenerator
from API.Device.DeviceBase.DesktopBase.MIBBrowser import MIBBrowser
from API.Device.DeviceBase.DesktopBase.CiscoIpCommunicator import CiscoIpCommunicator
from API.Device.DeviceBase.DesktopBase.Email import Email
from API.Device.DeviceBase.DesktopBase.PppoeDialer import PppoeDialer
from API.Device.DeviceBase.DesktopBase.TextEditor import TextEditor
from API.Device.DeviceBase.DesktopBase.Firewall import Firewall
from API.Device.DeviceBase.DesktopBase.Firewallv6 import Firewallv6
from API.Device.DeviceBase.DesktopBase.NetflowCollector import Netflow
from API.Device.DeviceBase.DesktopBase.IoxIde import IoxIde
from API.Device.DeviceBase.DesktopBase.TftpService import TftpService
from API.Device.DeviceBase.DesktopBase.IoeMonitor import IoeMonitor
from API.Device.DeviceBase.DesktopBase.IoeIde import IoeIde
from API.Device.DeviceBase.DesktopBase.AaaAccounting import AaaAccounting
from API.Device.DeviceBase.DesktopBase.MQTT import Broker as MQTTBroker
from API.Device.DeviceBase.DesktopBase.MQTT import Client as MQTTClient

class Desktop:
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.applications = Applications(self)
		self.ipConfiguration = IpConfiguration(self)
		self.dialUp = DialUp(self)
		self.terminal = Terminal(self)
		self.commandPrompt = CommandPrompt(self)
		self.webBrowser = WebBrowser(self)
		self.pcWireless = PCWireless(self)
		self.vpn = Vpn(self)
		self.trafficGenerator = TrafficGenerator(self)
		self.mibBrowser = MIBBrowser(self)
		self.ciscoIpCommunicator = CiscoIpCommunicator(self)
		self.email = Email(self)
		self.pppoeDialer = PppoeDialer(self)
		self.textEditor = TextEditor(self)
		self.firewall = Firewall(self)
		self.firewallv6 = Firewallv6(self)
		self.netflow = Netflow(self)
		self.ioxIde = IoxIde(self)
		self.tftpService = TftpService(self)
		self.ioeMonitor = IoeMonitor(self)
		self.ioeIde = IoeIde(self)
		self.aaaAccounting = AaaAccounting(self)
		self.mqttBroker = MQTTBroker(self)
		self.mqttClient = MQTTClient(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.applications.updateName(self.squishName)
		self.ipConfiguration.updateName(self.squishName)
		self.dialUp.updateName(self.squishName)
		self.terminal.updateName(self.squishName)
		self.commandPrompt.updateName(self.squishName)
		self.webBrowser.updateName(self.squishName)
		self.pcWireless.updateName(self.squishName)
		self.vpn.updateName(self.squishName)
		self.trafficGenerator.updateName(self.squishName)
		self.mibBrowser.updateName(self.squishName)
		self.ciscoIpCommunicator.updateName(self.squishName)
		self.email.updateName(self.squishName)
		self.pppoeDialer.updateName(self.squishName)
		self.textEditor.updateName(self.squishName)
		self.firewall.updateName(self.squishName)
		self.firewallv6.updateName(self.squishName)
		self.netflow.updateName(self.squishName)
		self.ioxIde.updateName(self.squishName)
		self.tftpService.updateName(self.squishName)
		self.ioeMonitor.updateName(self.squishName)
		self.ioeIde.updateName(self.squishName)
		self.aaaAccounting.updateName(self.squishName)
		self.mqttBroker.updateName(self.squishName)
		self.mqttClient.updateName(self.squishName)