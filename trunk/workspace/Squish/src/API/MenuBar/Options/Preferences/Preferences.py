##Chris Allen

from API.Utility.Util import Util
from API.MenuBar.Options.Options import Options
from API.MenuBar.Options.OptionsConst import OptionsConst
from API.MenuBar.Options.Preferences.Interface.Interface import Interface
from API.MenuBar.Options.Preferences.Administrative.Administrative import Administrative
from API.MenuBar.Options.Preferences.Hide.Hide import Hide
from API.MenuBar.Options.Preferences.Font.Font import Font
from API.MenuBar.Options.Preferences.Miscellaneous.Miscellaneous import Miscellaneous
from API.MenuBar.Options.Preferences.CustomInterfaces.CustomInterfaces import CustomInterfaces
from API.MenuBar.Options.Preferences.Publishers.Publishers import Publishers
from API.MenuBar.Options.Preferences.ImageCleanup.ImageCleanup import ImageCleanup
from squish import *
import object

#constants
from API.MenuBar.Options.Preferences.PreferencesConst import PreferencesConst

def err(msg = ''): raise NotImplementedError(msg)

#err('TODO:Custom interfaces, publishers, image cleanup')

class Tabs:
	def __init__(self):
		self.util = Util()
		
	def _clickTab(self, tab):
		'''tab - String (Name of the tab to be clicked)'''
		self.util.clickTab(PreferencesConst.TAB_BAR, tab)
	
	def interface(self):
		self._clickTab('Interface')
	
	def administrative(self):
		self._clickTab('Administrative')
	
	def hide(self):
		self._clickTab('Hide')
	
	def font(self):
		self._clickTab('Font')
	
	def miscellaneous(self):
		self._clickTab('Miscellaneous')
	
	def customInterfaces(self):
		self._clickTab('Custom Interfaces')
	
	def publishers(self):
		self._clickTab('Publishers')
	
	def imageCleanup(self):
		self._clickTab('Image Cleanup')
	

class Preferences:
	def __init__(self):
		self.util = Util()
		self.interface = Interface()
		self.administrative = Administrative()
		self.hide = Hide()
		self.font = Font()
		self.misc = Miscellaneous()
		self.customInterfaces = CustomInterfaces()
		self.publishers = Publishers()
		self.imageCleanup = ImageCleanup()
		self.tabs = Tabs()
			
	@property
	def window(self):
		'''Returns window object if found. False if not'''
		try:
			return findObject(PreferencesConst.PREFERENCES_WINDOW)
		except LookupError, e:
			return False
	
	def goToPreferences(self):
		Options().selectOptionsItem(OptionsConst.PREFERENCES)
	
	def close(self):
		self.util.close(PreferencesConst.PREFERENCES_WINDOW)