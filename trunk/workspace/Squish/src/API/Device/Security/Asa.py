##Chris Allen

from API.Device.DeviceBase.DeviceBase import DeviceBase, SquishObjectName
from API.Device.DeviceBase.ConfigBase.CiscoDeviceConfig import Config as ConfigBase
from API.Device.DeviceBase.PhysicalBase.PhysicalBase import Physical
from API.Device.DeviceBase.CliBase.CliBase import Cli
from API.ComponentBox import ComponentBoxConst
from squish import *
import object

##The following imports can be removed when the Clientless VPN classes are refactored out
from API.Utility.Util import Util
from API.Device.Security.AsaConst import AsaConst

def err(msg = ''): raise NotImplementedError(msg)

class BookmarkManager(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def bookmarkTitle(self, title):
        Util().setText(self.objName(AsaConst.config.clientlessVpn.bookmarkManager.TITLE_EDIT), title)
    
    def url(self, url):
        Util().setText(self.objName(AsaConst.config.clientlessVpn.bookmarkManager.URL_EDIT), url)
    
    def addButton(self):
        Util().clickButton(self.objName(AsaConst.config.clientlessVpn.bookmarkManager.ADD_BUTTON))
    
    def removeButton(self):
        Util().clickButton(self.objName(AsaConst.config.clientlessVpn.bookmarkManager.REMOVE_BUTTON))
    
    @property
    def bookmarkTableName(self):
        return self.objName(AsaConst.config.clientlessVpn.bookmarkManager.TABLE)
    
    @property
    def bookmarkTable(self):
        return findObject(self.bookmarkTableName)
    
    def selectBookmark(self, title):
        for i in range(self.bookmarkTable.rowCount):
            currentTitle = findObject(self.objName(AsaConst.config.clientlessVpn.bookmarkManager.TABLE + '.item_' + str(i) + '/0'))
            if currentTitle.text == title:
                Util().click(currentTitle)
                return
        raise ValueError('Could not find bookmark: ' + title)
    
    def add(self, title, url):
        self.bookmarkTitle(title)
        self.url(url)
        self.addButton()
    
    def remove(self, title):
        self.selectBookmark(title)
        self.removeButton()

class UserManager(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
    
    def updateName(self, squishName):
        self.squishName = squishName
    
    def username(self, username):
        Util().clickItem(self.objName(AsaConst.config.clientlessVpn.userManager.USERNAME_DROPDOWN), username)
    
    def bookmark(self, bookmark):
        Util().clickItem(self.objName(AsaConst.config.clientlessVpn.userManager.BOOKMARK_DROPDOWN), bookmark)
    
    def profileName(self, profileName):
        Util().setText(self.objName(AsaConst.config.clientlessVpn.userManager.PROFILE_NAME_EDIT), profileName)
    
    def groupPolicy(self, groupPolicy):
        Util().setText(self.objName(AsaConst.config.clientlessVpn.userManager.GROUP_POLICY_EDIT), groupPolicy)
    
    def setButton(self):
        Util().clickButton(self.objName(AsaConst.config.clientlessVpn.userManager.SET_BUTTON))
    
    def addUser(self, username, bookmark, profileName, groupPolicy):
        self.username(username)
        self.bookmark(bookmark)
        self.profileName(profileName)
        self.groupPolicy(groupPolicy)
        self.setButton()
        
    @property
    def userTableName(self):
        return self.objName(AsaConst.config.clientlessVpn.userManager.USER_TABLE)
    
    @property
    def userTable(self):
        return findObject(self.userTableName)

class ClientlessVpn(SquishObjectName):
    def __init__(self, parent):
        self.squishName = parent.squishName
        self.bookmarkManager = BookmarkManager(self)
        self.userManager = UserManager(self)
    
    def updateName(self, squishName):
        self.squishName = squishName
        self.bookmarkManager.updateName(squishName)
        self.userManager.updateName(squishName)
        
class Config(ConfigBase):
    def __init__(self, parent):
        self.squishName = parent.squishName
        super(Config, self).__init__(self)
        self.clientlessVpn = ClientlessVpn(self)
    
    def updateName(self, squishName):
        super(Config, self).updateName(squishName)
        self.clientlessVpn.updateName(squishName)

class Asa(DeviceBase):
    def __init__(self, p_model, p_x, p_y, p_displayName):
        self.deviceType = ComponentBoxConst.DeviceType.SECURITY
        super(Asa, self).__init__(p_model, p_x, p_y, p_displayName, self.deviceType)
        self.config = Config(self)
        self.physical = Physical(self)
        self.cli = Cli(self)
        
    def updateName(self):
        super(Asa, self).updateName()
        self.config.updateName(self.squishName)
        self.physical.updateName(self.squishName)
        self.cli.updateName(self.squishName)