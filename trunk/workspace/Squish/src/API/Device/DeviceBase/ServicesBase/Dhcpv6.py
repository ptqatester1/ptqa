##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *
import object

class Dhcpv6PoolConfig(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def poolName(self, poolName):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.POOL_NAME), poolName)
	
	def dnsName(self, dnsName):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.DNS_NAME), dnsName)
	
	def domainName(self, domainName):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.DOMAIN_NAME), domainName)
		
	def savebutton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.SAVE_BUTTON))
		
	def dhcpv6PoolFields(self, poolName, dnsName, domainName):
		self.poolName(poolName)
		self.dnsName(dnsName)
		self.domainName(domainName)
	
class Ipv6PrefixDelegationConfig(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def ipv6Address(self, ipv6Address):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.IPV6_LINE1), ipv6Address)
	
	def subnet(self, subnet):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.IPV6_LINE2), subnet)
	
	def dhcpv6UniqueIdentifier(self, uid):
		'''Example: 00-01-00-01-14-77-21-A2-00-50-56-AA-5E-EE'''
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.DUID), uid)
	
	def validLifetime(self, validLifetime):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.VALID_LIFETIME), validLifetime)
	
	def preferredLifetime(self, preferredLifetime):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.PREFERRED_LIFETIME), preferredLifetime)
		
	def ipv6PrefixDelegationFields(self, ipv6Address, subnet, uid, validLifetime, preferredLifetime):
		self.ipv6Address(ipv6Address)
		self.subnet(subnet)
		self.dhcpv6UniqueIdentifier(uid)
		self.validLifetime(validLifetime)
		self.preferredLifetime(preferredLifetime)

class Ipv6PrefixPoolConfig(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def localPoolName(self, localPoolName):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.LOCAL_POOL_NAME), localPoolName)
	
	def validLifetime(self, validLifetime):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.VALID_POOL_LIFETIME), validLifetime)
	
	def preferredLifetime(self, preferredLifetime):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Pool_Config.PREFERRED_POOL_LIFETIME), preferredLifetime)
		
	def ipv6PrefixPoolFields(self, localPoolName, localValidLifetime, localPreferredLifetime):
		self.localPoolName(localPoolName)
		self.validLifetime(localValidLifetime)
		self.preferredLifetime(localPreferredLifetime)

class PoolConfig(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.dhcpv6Pool = Dhcpv6PoolConfig(self)
		self.ipv6PrefixDelegation = Ipv6PrefixDelegationConfig(self)
		self.ipv6PrefixPool = Ipv6PrefixPoolConfig(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.dhcpv6Pool.updateName(squishName)
		self.ipv6PrefixDelegation.updateName(squishName)
		self.ipv6PrefixPool.updateName(squishName)

class DHCPv6PoolCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.poolConfig = PoolConfig(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.poolConfig.updateName(squishName)
		
	def poolList(self, poolList):
		Util().textCheckPoint(self.objName(ServicesConst.dhcpv6.POOL_LIST), poolList, textProperty='currentText')
	
	def createPoolButton(self):
		raise NotImplementedError
		#Util().clickButton(self.objName(ServicesConst.dhcpv6.CREATE_POOL))
		
	def removePoolButton(self):
		raise NotImplementedError
		#Util().clickButton(self.objName(ServicesConst.dhcpv6.REMOVE_POOL))
	
	def dnsServer(self, dnsServer):
		Util().textCheckPoint(self.objName(ServicesConst.dhcpv6.DNS), dnsServer)
	
	def domainName(self, domainName):
		Util().textCheckPoint(self.objName(ServicesConst.dhcpv6.DOMAIN), domainName)
	
	def createButton(self):
		raise NotImplementedError
		#Util().clickButton(self.objName(ServicesConst.dhcpv6.PREFIX_CREATE_BUTTON))
	
	def editButton(self):
		raise NotImplementedError
		#Util().clickButton(self.objName(ServicesConst.dhcpv6.PREFIX_EDIT_BUTTON))
	
	def removeButton(self):
		raise NotImplementedError
		#Util().clickButton(self.objName(ServicesConst.dhcpv6.PREFIX_REMOVE_BUTTON))
	
	@property
	def prefixDelegationPoolTable(self):
		return findObject(self.objName(ServicesConst.dhcpv6.PREFIX_TABLE))

class DHCPv6Pool(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.poolConfig = PoolConfig(self)
		self.check = DHCPv6PoolCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.poolConfig.updateName(squishName)
		self.check.updateName(squishName)
	
	def poolList(self, poolList):
		Util().clickItem(self.objName(ServicesConst.dhcpv6.POOL_LIST))
	
	def createPoolButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.CREATE_POOL))
		
	def removePoolButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.REMOVE_POOL))
	
	def dnsServer(self, dnsServer):
		Util().setText(self.objName(ServicesConst.dhcpv6.DNS), dnsServer)
	
	def domainName(self, domainName):
		Util().setText(self.objName(ServicesConst.dhcpv6.DOMAIN), domainName)
	
	def createButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.PREFIX_CREATE_BUTTON))
	
	def editButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.PREFIX_EDIT_BUTTON))
	
	def removeButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.PREFIX_REMOVE_BUTTON))
	
	@property
	def prefixDelegationPoolTable(self):
		return findObject(self.objName(ServicesConst.dhcpv6.PREFIX_TABLE))
	
	def addNewDhcpv6Pool(self, poolName, dnsName, domainName, ipv6Address, subnet, uid, validLifetime, preferredLifetime, localPoolName, localValidLifetime, localPreferredLifetime):
		self.createPoolButton()
		self.poolConfig.dhcpv6Pool.dhcpv6PoolFields(poolName, dnsName, domainName)
		self.poolConfig.ipv6PrefixDelegation.ipv6PrefixDelegationFields(ipv6Address, subnet, uid, validLifetime, preferredLifetime)
		self.poolConfig.ipv6PrefixPool.ipv6PrefixPoolFields(localPoolName, localValidLifetime, localPreferredLifetime)
		self.poolConfig.dhcpv6Pool.savebutton()
		
	def selectPrefixDelegationAt(self, row):
		Util().clickItem(self.prefixDelegationPoolTable, row +"/0")
		
class Ipv6LocalPoolConfig(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
		
	def localPoolFields(self, localPool, poolPrefix, subnet, length):
		self.ipv6LocalPool(localPool)
		self.ipv6PoolPrefix(poolPrefix)
		self.subnet(subnet)
		self.prefixLengthToAssign(length)
		Util().snooze(2)
		self.saveButton()

	def ipv6LocalPool(self, localPool):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Local_Config.LOCAL_POOL), localPool)
	
	def ipv6PoolPrefix(self, poolPrefix):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Local_Config.POOL_PREFIX_LINE1), poolPrefix)
	
	def subnet(self, subnet):
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Local_Config.POOL_PREFIX_LINE2), subnet)
	
	def prefixLengthToAssign(self, length):
		'''1-128'''
		Util().setText(self.objName(ServicesConst.dhcpv6.DHCP_Local_Config.PREFIX_LENGTH), length)
	
	def saveButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.DHCP_Local_Config.SAVE_BUTTON))
	
	def cancelButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.DHCP_Local_Config.CANCEL_BUTTON))
	
class IPv6LocalPool(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.localPoolConfig = Ipv6LocalPoolConfig(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.localPoolConfig.updateName(squishName)
		
	def addNewLocalPool(self, localPool, poolPrefix, subnet, length):
		self.createButton()
		self.localPoolConfig.localPoolFields(localPool, poolPrefix, subnet, length)

	def createButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.LOCAL_CREATE_BUTTON))
	
	def selectLocalItem(self, row):
		Util().clickItem(self.objName(ServicesConst.dhcpv6.LOCAL_TABLE), row + "/0")
	
	def saveButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.DHCP_Local_Config.SAVE_BUTTON))
		
	def editButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.LOCAL_EDIT_BUTTON))
	
	def removeButton(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.LOCAL_REMOVE_BUTTON))
	
	@property
	def localPoolTable(self):
		return findObject(self.objName(ServicesConst.dhcpv6.LOCAL_TABLE))

class Dhcpv6Check(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def interface(self, interface):
		Util().textCheckPoint(self.objName(ServicesConst.dhcpv6.INTERFACE_DROPDOWN), interface, textProperty='currentText')
	
	def dhcpv6Pool(self, pool):
		Util().textCheckPoint(self.objName(ServicesConst.dhcpv6.POOL), pool)
	
	def on(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.dhcpv6.ON), checked)
	
	def off(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.dhcpv6.OFF), checked)

class Dhcpv6(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.dhcpv6Pool = DHCPv6Pool(self)
		self.ipv6LocalPool = IPv6LocalPool(self)
		self.check = Dhcpv6Check(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.dhcpv6Pool.updateName(squishName)
		self.ipv6LocalPool.updateName(squishName)
		self.check.updateName(squishName)
	
	def interface(self, interface):
		Util().clickItem(self.objName(ServicesConst.dhcpv6.INTERFACE_DROPDOWN), interface)
	
	def dhcpv6PoolSelect(self, pool):
		Util().clickItem(self.objName(ServicesConst.dhcpv6.POOL), pool)
	
	def on(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.ON))
	
	def off(self):
		Util().clickButton(self.objName(ServicesConst.dhcpv6.OFF))