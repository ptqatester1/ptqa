##Chris Allen

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.Security.Asa import Asa

from API.Device.EndDevice.PC.PC import PC

from API.Device.Switch.Switch import Switch

from API.Device.EndDevice.Server.Server import Server

from API.ComponentBox import ComponentBoxConst

util = Util()
a0 = Asa(ComponentBoxConst.DeviceModel.ASA_5505, 100, 100, 'Asa0')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 300, 100, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 300, 300, 'PC1')
sw = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 200, 200, 'Switch0')
se = Server(ComponentBoxConst.DeviceModel.SERVER, 100, 300, 'Server0')

def main():
    util.init()
    create()
    configureCliCommands()
    addressHosts()
    setBookmarks()
    setUser()
    checkTables()
    
def create():
    a0.create()
    sw.create()
    p0.create()
    p1.create()
    se.create()
    
    a0.connect(sw)
    p0.connect(sw)
    p1.connect(sw)
    a0.connect(se)
    util.fastForwardTime()
    
def configureCliCommands():
    util.clickOnWorkspace(a0.x, a0.y)
    a0.updateName()
    a0.clickCliTab()
    a0.cli.setCliText('enable')
    a0.cli.setCliText('')
    a0.cli.setCliText('configure terminal')
    a0.cli.setCliText('hostname ciscoasa')
    a0.cli.setCliText('names')
    a0.cli.setCliText('interface Ethernet0/0')
    a0.cli.setCliText(' switchport access vlan 2')
    a0.cli.setCliText('interface Ethernet0/1')
    a0.cli.setCliText(' switchport access vlan 1')
    a0.cli.setCliText('interface Vlan1')
    a0.cli.setCliText(' nameif inside')
    a0.cli.setCliText(' security-level 100')
    a0.cli.setCliText(' ip address 192.168.1.1 255.255.255.0')
    a0.cli.setCliText('interface Vlan2')
    a0.cli.setCliText(' nameif outside')
    a0.cli.setCliText(' security-level 0')
    a0.cli.setCliText(' ip address 10.0.0.1 255.0.0.0')
    a0.cli.setCliText('webvpn')
    a0.cli.setCliText(' enable inside')
    a0.cli.setCliText(' enable outside')
    a0.cli.setCliText('username cisco password 4IncP7vTjpaba2aF encrypted')
    a0.cli.setCliText('telnet timeout 5')
    a0.cli.setCliText('ssh timeout 5')
    a0.cli.setCliText('dhcpd address 192.168.1.5-192.168.1.35 inside')
    a0.cli.setCliText('dhcpd enable inside')
    a0.cli.setCliText('dhcpd auto_config outside')
    for user in ['user1', 'user2', 'user3']:
        a0.cli.setCliText('username ' + user + ' password ' + user)
    a0.close()  
    
def addressHosts():
    p0.select()
    p0.clickDesktopTab()
    p0.desktop.applications.ipConfiguration()
    p0.desktop.ipConfiguration.setIPConfiguration('10.0.0.2', '255.0.0.0', '10.0.0.1', '')
    p0.close()
    
    p1.select()
    p1.clickDesktopTab()
    p1.desktop.applications.ipConfiguration()
    p1.desktop.ipConfiguration.setIPConfiguration('10.0.0.3', '255.0.0.0', '10.0.0.1', '')
    p1.close()
    
    util.clickOnWorkspace(se.x, se.y)
    se.updateName()
    se.clickDesktopTab()
    se.desktop.applications.ipConfiguration()
    se.desktop.ipConfiguration.setIPConfiguration('192.168.1.2', '255.255.255.0', '192.168.1.1')
    se.close()
    
def setBookmarks():
    util.clickOnWorkspace(a0.x, a0.y)
    a0.updateName()
    a0.clickConfigTab()
    a0.config.selectInterface('Bookmark Manager')
    a0.config.clientlessVpn.bookmarkManager.add('bookmark0', 'https://192.168.1.2')
    for i,bookmark in enumerate(['helloworld', 'copyrights', 'image']):
        a0.config.clientlessVpn.bookmarkManager.add('bookmark' + str(i+1), 'https://192.168.1.2/' + bookmark + '.html')

def setUser():
    a0.config.selectInterface('User Manager')
    a0.config.clientlessVpn.userManager.addUser('cisco', 'bookmark0', 'ciscoProfile', 'ciscoGroup')
    for i,user in enumerate(['user1', 'user2', 'user3']):
        a0.config.clientlessVpn.userManager.addUser(user, 'bookmark'+str(i+1), user + 'Profile', user + 'Group')

def checkTables():
    userRow0 = ['cisco', 'bookmark0', 'ciscoProfile', 'ciscoGroup']
    userRow1 = ['user1', 'bookmark1', 'user1Profile', 'user1Group']
    userRow2 = ['user2', 'bookmark2', 'user2Profile', 'user2Group']
    userRow3 = ['user3', 'bookmark3', 'user3Profile', 'user3Group']
    userRows = [userRow0, userRow1, userRow2, userRow3]
    table = a0.config.clientlessVpn.userManager.userTableName
    if findObject(table).rowCount == 4:
        test.passes('There are 4 users listed')
    else:
        test.fail('There are not 4 users listed')
    for i in range(findObject(table).rowCount):
        for j, text in enumerate(userRows[i]):
            util.textCheckPoint(table + '.item_' + str(i) + '/' + str(j), text)
    
    bookmark0 = ['bookmark0', 'https://192.168.1.2']
    bookmark1 = ['bookmark1', 'https://192.168.1.2/helloworld.html']
    bookmark2 = ['bookmark2', 'https://192.168.1.2/copyrights.html']
    bookmark3 = ['bookmark3', 'https://192.168.1.2/image.html']
    bookmarks = [bookmark0, bookmark1, bookmark2, bookmark3]
    table = a0.config.clientlessVpn.bookmarkManager.bookmarkTableName
    
    a0.config.selectInterface('Bookmark Manager')
    if findObject(table).rowCount == 4:
        test.passes('There are 4 users listed')
    else:
        test.fail('There are not 4 users listed')
    for i in range(findObject(table).rowCount):
        for j, text in enumerate(bookmarks[i]):
            util.textCheckPoint(table + '.item_' + str(i) + '/' + str(j), text)
    
    a0.config.clientlessVpn.bookmarkManager.remove('bookmark3')
    if a0.config.clientlessVpn.bookmarkManager.bookmarkTable.rowCount == 3:
        test.passes('There are 3 users listed')
    else:
        test.fail('There are not 3 users listed')
    None