##Chris Allen

from API.Utility.Util import Util
from API.MenuBar.Options.Preferences.Miscellaneous.MiscellaneousConst import MiscellaneousConst
from squish import *

class Miscellaneous:
    def __init__(self):
        self.util = Util()
    
    def promptRadio(self):
        self.util.clickButton(MiscellaneousConst.PROMPT)
    
    def autoClearEventListRadio(self):
        self.util.clickButton(MiscellaneousConst.AUTO_CLEAR_EVENT_LIST)
        
    def autoViewPreviousEventsRadio(self):
        self.util.clickButton(MiscellaneousConst.AUTO_VIEW_PREVIOUS_EVENTS)
    
    def bufferFilteredEventsOnly(self, checked = None):
        checkbox = findObject(MiscellaneousConst.BUFFER_FILTERED_EVENTS_ONLY)
        self.util.checkbox(checkbox, checked)
    
    def enhanceScreenReaderSupport(self, checked = None):
        checkbox = findObject(MiscellaneousConst.ENABLE_SCREEN_READER_SUPPORT)
        self.util.checkbox(checkbox, checked)
    
    def showDeviceDialogTaskbar(self, checked = None):
        checkbox = findObject(MiscellaneousConst.SHOW_DEVICE_DIALOG_TASKBAR)
        self.util.checkbox(checkbox, checked)
    
    def enableExternalNetworkAccess(self, checked = None):
        checkbox = findObject(MiscellaneousConst.ENABLE_EXTERNAL_NETWORK_ACCESS)
    
    def proxyType(self, type):
        self.util.clickItem(MiscellaneousConst.PROXY_TYPE_COMBO, type)
    
    def url(self, url):
        self.util.setText(MiscellaneousConst.URL_EDIT, url)
    
    def port(self, port):
        self.util.setText(MiscellaneousConst.PORT_EDIT, port)
    
    def username(self, username):
        self.util.setText(MiscellaneousConst.USERNAME_EDIT, username)
    
    def password(self, password):
        self.util.setText(MiscellaneousConst.PASSWORD_EDIT, password)
    
    def applyProxyButton(self):
        self.util.clickButton(MiscellaneousConst.APPLY_PROXY_BUTTON)