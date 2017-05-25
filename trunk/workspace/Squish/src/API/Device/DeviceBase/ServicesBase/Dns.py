##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *

class ARecord(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def address(self, address):
		Util().setText(self.objName(ServicesConst.dns.IP_ADD), address)
	
class CName(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def hostname(self, hostname):
		Util().setText(self.objName(ServicesConst.dns.CNAME_HOSTNAME_EDIT), hostname)
	
class Soa(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def primaryServerName(self, serverName):
		Util().setText(self.objName(ServicesConst.dns.SOA_SERVER), serverName)
	
	def mailBox(self, mailbox):
		Util().setText(self.objName(ServicesConst.dns.SOA_MAILBOX), mailbox)
	
	def minimumTtl(self, ttl):
		Util().setText(self.objName(ServicesConst.dns.SOA_MIN_TTL), ttl)
	
	def refreshTime(self, refreshTime):
		Util().setText(self.objName(ServicesConst.dns.SOA_REFRESH_TIME), refreshTime)
	
	def retryTime(self, retryTime):
		Util().setText(self.objName(ServicesConst.dns.SOA_RETRY_TIME), retryTime)
	
	def expiryTime(self, expiryTime):
		Util().setText(self.objName(ServicesConst.dns.SOA_EXPIRE_TIME), expiryTime)
	
class NsRecord(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def serverName(self, serverName):
		Util().setText(self.objName(ServicesConst.dns.NS_SERVER_NAME), serverName)

class DnsCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.util = Util()
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def on(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.dns.ON), checked)
	
	def off(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.dns.OFF), checked)
	
	def pageTitle(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.PAGE_TITLE), text)
	
	def dnsServiceLabel(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.DNS_SERVICE_LABEL), text)
	
	def onRadioLabel(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.ON), text)
	
	def offRadioLabel(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.OFF), text)
	
	def resourceRecordsLabel(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.RESOURCE_RECORDS_LABEL), text)
	
	def addButtonText(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.ADD_BUTT), text)
	
	def saveButtonText(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.SAVE_BUTT), text)
	
	def removeButtonText(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.REMOVE_BUTT), text)
	
	def dnsCacheButtonText(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.CACHE_BUTT), text)
	
	def nameLabel(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.NAME_LABEL), text)
	
	def typeLabel(self, text):
		self.util.textCheckPoint(self.objName(ServicesConst.dns.TYPE_LABEL), text)
	
class DnsCacheDialog(SquishObjectName):	
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def clearCacheButton(self):
		Util().clickButton(self.objName(ServicesConst.dns.CACHE_CLEAR_BUTT))
	
	def cancelButton(self):
		Util().clickButton(self.objName(ServicesConst.dns.CACHE_CANCEL_BUTT))

class Dns(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.cname = CName(self)
		self.aRecord = ARecord(self)
		self.soa = Soa(self)
		self.nsRecord = NsRecord(self)
		self.cache = DnsCacheDialog(self)
		self.check = DnsCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.cname.updateName(squishName)
		self.aRecord.updateName(squishName)
		self.soa.updateName(squishName)
		self.nsRecord.updateName(squishName)
		self.cache.updateName(squishName)
		self.check.updateName(squishName)
	
	def on(self):
		Util().clickButton(self.objName(ServicesConst.dns.ON))
	
	def off(self):
		Util().clickButton(self.objName(ServicesConst.dns.OFF))
	
	def name(self, name):
		Util().setText(self.objName(ServicesConst.dns.DOMAIN_NAME), name)
	
	def type(self, recordType):
		Util().clickItem(self.objName(ServicesConst.dns.TYPE_COMBO), recordType)
	
	def addButton(self):
		Util().clickButton(self.objName(ServicesConst.dns.ADD_BUTT))
	
	def saveButton(self):
		Util().clickButton(self.objName(ServicesConst.dns.SAVE_BUTT))
	
	def removeButton(self):
		Util().clickButton(self.objName(ServicesConst.dns.REMOVE_BUTT))
	
	def dnsCacheButton(self):
		Util().clickButton(self.objName(ServicesConst.dns.CACHE_BUTT))
	
	@property
	def dnsTableName(self):
		return self.objName(ServicesConst.dns.LIST_VIEW)
	
	@property
	def dnsTable(self):
		return findObject(self.dnsTableName)
	
	def selectRecord(self, name = None, row = None):
		if name == None and row == None:
			raise TypeError('name or row can\'t be None')
		if not row == None:
			Util().click(self.dnsTableName + '.item_%s/0'%(row,))
			return
		for i in range(self.dnsTable.rowCount):
			currentNameObject = findObject(self.dnsTableName + '.item_%s/1'%(i,))
			if name in str(currentNameObject.text):
				Util().click(currentNameObject)
				return
		raise ValueError('Could not find item with name %s'%(name,))
							
	
	def remove(self, recordName):
		self.selectRecord(recordName)
		self.removeButton()
	
	def editA(self, recordName, name = None, address = None):
		self.selectRecord(recordName)
		self.type('A Record')
		if name:
			self.name(name)
		if address:
			self.aRecord.address(address)
		self.saveButton()
	
	def editCname(self, recordName, name = None, hostname = None):
		self.selectRecord(recordName)
		self.type('CNAME')
		if name:
			self.name(name)
		if hostname:
			self.cname.hostname(hostname)
		self.saveButton()
	
	def editNs(self, recordName, name = None, serverName = None):
		self.selectRecord(recordName)
		self.type('NS Record')
		if name:
			self.name(name)
		if serverName:
			self.nsRecord.serverName(serverName)
		self.saveButton()
	
	def editSoa(self, recordName, name = None, primaryServerName = None, mailbox = None, ttl = None, refreshTime = None, retryTime = None, expiryTime = None):
		self.selectRecord(recordName)
		self.type('SOA')
		if name:
			self.name(name)
		if primaryServerName:
			self.soa.primaryServerName(primaryServerName)
		if mailbox:
			self.soa.mailBox(mailbox)
		if ttl:
			self.soa.minimumTtl(ttl)
		if refreshTime:
			self.soa.refreshTime(refreshTime)
		if retryTime:
			self.soa.retryTime(retryTime)
		if expiryTime:
			self.soa.expiryTime(expiryTime)
		self.saveButton()
	
	def addA(self, name, address):
		self.type('A Record')
		self.name(name)
		self.aRecord.address(address)
		self.addButton()
	
	def addCname(self, name, hostname):
		self.type('CNAME')
		self.name(name)
		self.cname.hostname(hostname)
		self.addButton()
	
	def addNs(self, name, serverName):
		self.type('NS Record')
		self.name(name)
		self.nsRecord.serverName(serverName)
		self.addButton()
	
	def addSoa(self, name, primaryServerName, mailbox, ttl, refreshTime, retryTime, expiryTime):
		self.type('SOA')
		self.name(name)
		self.soa.primaryServerName(primaryServerName)
		self.soa.mailBox(mailbox)
		self.soa.minimumTtl(ttl)
		self.soa.refreshTime(refreshTime)
		self.soa.retryTime(retryTime)
		self.soa.expiryTime(expiryTime)
		self.addButton()