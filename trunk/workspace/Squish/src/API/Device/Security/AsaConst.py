##Chris Allen

from API.Device.DeviceBase.ConfigBase.CiscoDeviceConfigConst import GlobalSettings, Switching, Interface, AlgorithmSettings
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import PhysicalConst


class BookmarkManagerConst:
	PAGE_HEADER = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASABookmarkManager.labelHeading"
	TITLE_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASABookmarkManager.m_bookmarksGroupBox.m_bookmarkTitleEdit"
	URL_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASABookmarkManager.m_bookmarksGroupBox.m_bookmarkUrlEdit"
	ADD_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASABookmarkManager.m_bookmarksGroupBox.m_bookmarksAddBtn"
	REMOVE_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASABookmarkManager.m_bookmarksGroupBox.m_bookmarksRemoveBtn"
	TABLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASABookmarkManager.m_bookmarksGroupBox.m_bookmarksTable"
	
class UserManagerConst:
	USERNAME_DROPDOWN = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASAUserManager.m_usernameCB"
	BOOKMARK_DROPDOWN = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASAUserManager.m_bookmarkCB"
	PROFILE_NAME_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASAUserManager.m_profileNameEdit"
	GROUP_POLICY_EDIT = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASAUserManager.m_groupPolicyEdit"
	SET_BUTTON = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASAUserManager.m_setBtn"
	USER_TABLE = ".c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.CASAUserManager.m_userAuthGroupBox.m_userAuthTable"
	
class ClientlessVpnConst:
	bookmarkManager = BookmarkManagerConst
	userManager = UserManagerConst

class ConfigConst:
	settings = GlobalSettings
	algorithmSettings = AlgorithmSettings
	interface = Interface
	vlandDatabase = Switching
	clientlessVpn = ClientlessVpnConst
	
class AsaConst:
	config = ConfigConst
	physical = PhysicalConst