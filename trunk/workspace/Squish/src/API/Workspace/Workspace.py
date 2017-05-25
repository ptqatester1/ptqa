from API.Utility.Util import Util
from API.MenuBar.View.View import View
from API.MenuBar.View.ViewConst import ViewConst
from squish import *
import object

class ViewportConst:
	WINDOW = ':CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.CWorkspaceMiniView1'
	CONTENTS_TAB = ':CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.CWorkspaceMiniView1.viewport-toolbar.QToolButton1'
	WORKSPACE_TAB = ':CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.CWorkspaceMiniView1.viewport-toolbar.QToolButton2'
	BACK_BUTTON = ':CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.CWorkspaceMiniView1.viewport-toolbar.QToolButton3'
	VIEWPORT = ':CAppWindowBase.centralwidget.m_pWorkSpaceWnd.CViewArea_Window1.Viewport.Viewport'

class Viewport:
	def __init__(self):
		self.util = Util()
		None
	
	@property
	def viewport(self):
		return findObject(ViewportConst.VIEWPORT)
	
	@property
	def dimensions(self):
		return self.viewport.sceneRect
	
	@property
	def window(self):
		if object.exists(ViewportConst.WINDOW):
			return findObject(ViewportConst.WINDOW)
		return False
	
	def contents(self):
		self.util.clickButton(ViewportConst.CONTENTS_TAB)
	
	def workspace(self):
		self.util.clickButton(ViewportConst.WORKSPACE_TAB)
	
	def back(self):
		self.util.clickButton(ViewportConst.BACK_BUTTON)
	
	def goToViewport(self):
		if not self.window:
			View().selectViewItem(ViewConst.SHOW_VIEWPORT)
	
	def close(self):
		self.util.closeWindow(ViewportConst.WINDOW)
		
	def getObject(self, p_name, **kwargs):
		'''Return an object related to a device or container name or False if not found'''
		returnList = False
		if 'returnList' in kwargs:
			returnList = kwargs['returnList']
		foundItems = []
		viewportItems = object.children(self.viewport)
		for item in viewportItems:
			itemChildren = object.children(item)
			if itemChildren:
				for child in itemChildren:
					properties = object.properties(child)
					if 'text' in properties:
						if child.text == p_name:
							foundItems.append(object.parent(child))
		if returnList:
			return foundItems or False
		if foundItems:
			return foundItems[0]
		else:
			return False
		
class Workspace:
	def __init__(self):
		None