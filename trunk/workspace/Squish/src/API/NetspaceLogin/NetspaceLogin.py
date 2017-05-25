from API.NetspaceLogin.NetspaceLoginConst import NetspaceLoginConst
from API.functions import WebviewTagFind2 as TF
from API.functions import NotFoundException
from API.SquishSyntax import SquishSyntax
from squish import *
import object

def customInteractions(func):	
	def waitForPage(*args, **kwargs):
		for i in range(20):
			if waitForObject(NetspaceLoginConst.WEBVIEW).evalJS("document.readyState") == "complete":
				SquishSyntax().clearCache(NetspaceLoginConst.WEBVIEW)
				return func(*args, **kwargs)
			snooze(1)
	return waitForPage


class NetspaceLogin:
	def __init__(self):
		self.squishSyntax = SquishSyntax()
		pass
	
	@customInteractions
	def loginLink(self):
		loginLink = self.getWebviewItem('headerLoginLink')
		loginLink.click()
		
	@customInteractions
	def screenNameEdit(self, p_name):
		nameEdit = self.getWebviewItem('_58_INSTANCE_fm_login')
		nameEdit.value = p_name
	
	@customInteractions
	def passwordEdit(self, p_password):
		passwordEdit = self.getWebviewItem('_58_INSTANCE_fm_password')
		passwordEdit.value = p_password
		
	@customInteractions
	def loginPopupLoginButton(self):
		parent = self.getWebviewItem('modal-buttons-container')
		object.children(parent)[-1].submit()
	
	@customInteractions
	def loginPopupCancelButton(self):
		parent = self.getWebviewItem('modal-buttons-container')
		object.children(parent)[0].click()
		
	@customInteractions
	def login(self, username = 'ptsatest5', password = 'Cisco123', p_login = True):
		self.loginLink()
		self.screenNameEdit(username)
		self.passwordEdit(password)
		if p_login:
			self.loginPopupLoginButton()
		else:
			self.loginPopupCancelButton()
		self.waitForLoggedIn()
	
	@customInteractions
	def getWebviewItem(self, p_id):
		item = None
		for i in range(30):
			try:
				item = TF().findTagWithID(NetspaceLoginConst.WEBVIEW, p_id)
				break
			except NotFoundException, e:
				snooze(1)
			except Exception, e:
				raise
		if item:
			return item
		else:
			raise ValueError('Could not find ' + p_id)
	
	def waitForLoggedIn(self):
		for i in range(60):
			if object.exists(NetspaceLoginConst.NETSPACE_BASE):
				snooze(1)
			else:
				break
	
	def guestLogin(self):
		self.squishSyntax.clickButton(NetspaceLoginConst.GUEST_LOGIN_BUTTON)
		for i in range(30):
			if findObject(NetspaceLoginConst.GUEST_LOGIN_BUTTON).text == 'Confirm Guest':
				break
			else:
				snooze(1)
		self.squishSyntax.clickButton(NetspaceLoginConst.GUEST_LOGIN_BUTTON)
		