########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.COServer.COServer import COServer
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase import DeviceBaseConst
from API.Device.COServer.COServerConst import COServerConst

util = Util()
server = COServer(ComponentBoxConst.DeviceModel.CO_SERVER, 175, 80, 'Central Office Server0')

def main():
    util.init()
    create()
    checkDHCP()
    checkDHCPv6()
    checkCellTower()
    checkPAPCHAP()
    
def create():    
    server.create()
    server.select()
    server.clickServicesTab()
    snooze(2)    

def checkDHCP():
    server.services.dhcp.check.ip("172.16.1.1")
    server.services.dhcp.check.maxUsers("50")
    server.services.dhcp.check.subnet("255.255.255.0")
    server.services.dhcp.check.dnsServer("0.0.0.0")
    test.compare(findObject(server.squishName + COServerConst.services.dhcp.DHCP_SUBNET_MASK).enabled, False)
    server.services.dhcp.check.ipAddressRange1("172")
    server.services.dhcp.check.ipAddressRange2("16")
    server.services.dhcp.check.ipAddressRange3("1")
    server.services.dhcp.check.ipAddressRange4("100")
    test.compare(findObject(server.squishName + COServerConst.services.dhcp.IP_ADDRESS_RANGE_1).enabled, False)
    test.compare(findObject(server.squishName + COServerConst.services.dhcp.IP_ADDRESS_RANGE_2).enabled, False)
    test.compare(findObject(server.squishName + COServerConst.services.dhcp.IP_ADDRESS_RANGE_3).enabled, False)
    test.compare(findObject(server.squishName + COServerConst.services.dhcp.IP_ADDRESS_RANGE_4).enabled, True)
    
    server.clickConfigTab()
    server.config.selectInterface('Cell Tower')
    snooze(2)
    server.config.interface.cellTower.check.ip("172.16.1.1")
    
def checkDHCPv6():
    server.clickServicesTab()
    server.services.selectInterface('DHCPv6')
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.ON).enabled, False)
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.OFF).enabled, False)
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.PREFIX_CREATE_BUTTON).enabled, False)
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.PREFIX_REMOVE_BUTTON).enabled, False)
    
    server.services.dhcpv6.dhcpv6Pool.selectPrefixDelegationAt("0")
    server.services.dhcpv6.dhcpv6Pool.dnsServer("1.1.1.1")
    server.services.dhcpv6.dhcpv6Pool.dnsServer(" ")
    server.services.dhcpv6.dhcpv6Pool.domainName("domain")
    server.services.dhcpv6.dhcpv6Pool.selectPrefixDelegationAt('0')
    server.services.dhcpv6.dhcpv6Pool.editButton()
    
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.DHCP_Pool_Config.POOL_NAME).text, "IPv6-Pool")
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.DHCP_Pool_Config.VALID_LIFETIME).text, "2592000")
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.DHCP_Pool_Config.PREFERRED_LIFETIME).text,  "604800")
    
    server.services.dhcpv6.dhcpv6Pool.poolConfig.ipv6PrefixPool.ipv6PrefixPoolFields("test", "4294967296", "1")
    util.clickButton(waitForObject(":Error.qt_msgbox_buttonbox.OK"))

    server.services.dhcpv6.dhcpv6Pool.poolConfig.ipv6PrefixPool.ipv6PrefixPoolFields("test", "4294967296", "")
    util.clickButton(waitForObject(":Error.qt_msgbox_buttonbox.OK"))
    
    server.services.dhcpv6.dhcpv6Pool.poolConfig.ipv6PrefixPool.ipv6PrefixPoolFields("test", "1", "")
    util.clickButton(waitForObject(":Error.qt_msgbox_buttonbox.OK"))
    
    server.services.dhcpv6.dhcpv6Pool.poolConfig.ipv6PrefixPool.ipv6PrefixPoolFields("test", "", "4294967296")
    util.clickButton(waitForObject(":Error.qt_msgbox_buttonbox.OK"))

    server.services.dhcpv6.dhcpv6Pool.poolConfig.ipv6PrefixPool.ipv6PrefixPoolFields("test", "", "1")
    util.clickButton(waitForObject(":Error.qt_msgbox_buttonbox.OK"))
    
    server.services.dhcpv6.dhcpv6Pool.poolConfig.ipv6PrefixPool.ipv6PrefixPoolFields("test", "4294967295", "60")    
    
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.PREFIX_ITEM2).text, "test")
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.PREFIX_ITEM3).text, "4294967295")
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.PREFIX_ITEM4).text, "60")
    
    server.services.dhcpv6.ipv6LocalPool.addNewLocalPool("New-Pool", "2001::2", "64", "129")
    util.clickButton(waitForObject(":Error.qt_msgbox_buttonbox.OK"))
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.ipv6PoolPrefix("1.1.1.1")
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.subnet("")
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.prefixLengthToAssign("128")
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.saveButton()
    util.clickButton(waitForObject(":Error.qt_msgbox_buttonbox.OK"))
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.ipv6PoolPrefix("2001::2")
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.subnet("64")
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.prefixLengthToAssign("128")
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.saveButton()
    
    server.services.dhcpv6.ipv6LocalPool.selectLocalItem("1")
    server.services.dhcpv6.ipv6LocalPool.editButton()
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.DHCP_Local_Config.IPv6_LOCAL_POOL_LABEL).text, "New-Pool")
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.DHCP_Local_Config.IPv6_LOCAL_POOL_LABEL).enabled, False)
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.ipv6PoolPrefix("")
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.subnet("")
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.prefixLengthToAssign("64")
    server.services.dhcpv6.ipv6LocalPool.localPoolConfig.saveButton()
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.LOCAL_TABLE + ".item_1/0").text, "New-Pool")
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.LOCAL_TABLE + ".item_1/1").text, "2001::2/64")
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.LOCAL_TABLE + ".item_1/2").text, "64")
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.LOCAL_TABLE).rowCount, 2)    
    server.services.dhcpv6.ipv6LocalPool.selectLocalItem("0")
    server.services.dhcpv6.ipv6LocalPool.removeButton()
    server.services.dhcpv6.ipv6LocalPool.selectLocalItem("0")
    server.services.dhcpv6.ipv6LocalPool.removeButton()
    test.compare(findObject(server.squishName + COServerConst.services.dhcpv6.LOCAL_TABLE).rowCount, 0)
    
def checkCellTower():
    server.services.selectInterface("CELL TOWER")
    server.services.cellTower.refreshButton()
    
def checkPAPCHAP():
    server.services.selectInterface("PAP/CHAP")
    server.services.papChap.add("admin", "P@$$", "CHAP", "Backbone")
    server.services.papChap.add("admin1", "pAsS", "PAP", "Coaxial0/1")
    server.services.papChap.interface("Backbone")
    server.services.papChap.selectUser("admin")
    server.services.papChap.check.username("admin")
    server.services.papChap.check.password("P\@\$\$")
    server.services.papChap.remove("admin")

    server.services.papChap.interface("Coaxial0/1")
    server.services.papChap.selectUser("admin1")
    server.services.papChap.check.username("admin1")
    server.services.papChap.check.password("pAsS")
    server.services.papChap.remove("admin1")
    
    server.services.papChap.check.username("")
        
