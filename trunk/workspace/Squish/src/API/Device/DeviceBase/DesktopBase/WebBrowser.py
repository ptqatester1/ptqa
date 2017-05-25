##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.Device.DeviceBase.WirelessGuiBase.PcGui import Gui
from API.Device.DeviceBase.DesktopBase.Browser.RegistrationServer import RegistrationServer
from API.Device.DeviceBase.DesktopBase.Browser.HomeGateway import HomeGateway
from API.Device.DeviceBase.DesktopBase.Browser.CiscoApplicationManagement import CiscoApplicationManagement

class WebBrowserCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		
	def updateName(self, squishName):
		self.squishName = squishName
	
	def url(self, url):
		Util().textCheckPoint(self.objName(DesktopConst.webbrowser.URL_EDIT), url)
		
	def pageHeader(self, header):
		Util().textCheckPoint(self.objName(DesktopConst.webbrowser.BROWSER_CONTENT_HEADER), header)
		
	def content(self, content, occuranceNum = -1):
		Util().textCheckPoint(self.objName(DesktopConst.webbrowser.BROWSER_CONTENT_WINDOW), content, occuranceNum)
		
	def pageTitle(self, title):
		Util().textCheckPoint(self.objName(DesktopConst.webbrowser.PAGE_TITLE), title)

class WebBrowser(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = WebBrowserCheck(self)
		self.wirelessGui = Gui(self)
		self.registrationServer = RegistrationServer(self.squishName)
		self.homeGateway = HomeGateway(self.squishName)
		self.ciscoApplicationManagement = CiscoApplicationManagement(self.squishName)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
		self.wirelessGui.updateName(squishName)
		self.registrationServer.updateName(squishName)
		self.homeGateway.updateName(squishName)
		self.ciscoApplicationManagement.updateName(squishName)
	
	def authenticateRouter(self, user, password):
		self.user(user)
		self.password(password)
		self.ok()
	
	def continueEditGateway(self):
		Util().click(self.objName(DesktopConst.webbrowser.MAIN_WEB_VIEW + '.DOCUMENT.HTML1.BODY1.CENTER1.P1.A1'))
		
	def back(self):
		Util().clickButton(self.objName(DesktopConst.webbrowser.BACK_BUTT))
	
	def forward(self):
		Util().clickButton(self.objName(DesktopConst.webbrowser.FORWARD_BUTT))
	
	def browse(self, url):
		self.url(url)
		self.go()
		
	def url(self, url):
		Util().setText(self.objName(DesktopConst.webbrowser.URL_EDIT), url)
	
	def go(self):
		Util().clickButton(self.objName(DesktopConst.webbrowser.GO_BUTT))
	
	def stop(self):
		Util().clickButton(self.objName(DesktopConst.webbrowser.STOP_BUTT))
		
	def textCheckPoint(self, text, occurrenceNum = -1,  **kwargs):
		Util().textCheckPoint(self.objName(DesktopConst.webbrowser.BROWSER_CONTENT_WINDOW), text, occurrenceNum, **kwargs)
		
	def close(self):
		Util().clickButton(self.objName(DesktopConst.webbrowser.CLOSE_BUTT))
		
	def user(self, user):
		Util().setText(self.objName(DesktopConst.webbrowser.BROWSER_USERNAME_EDIT), user)
		
	def password(self, password):
		Util().setText(self.objName(DesktopConst.webbrowser.BROWSER_PASSWORD_EDIT), password)
		
	def ok(self):
		Util().clickButton(self.objName(DesktopConst.webbrowser.BROWSER_OK_BUTT))
	
	def asaUsername(self, username):
		Util().setText(self.objName(DesktopConst.webbrowser.ASA_USERNAME_EDIT), username)
	
	def asaPassword(self, password):
		Util().setText(self.objName(DesktopConst.webbrowser.ASA_PASSWORD_EDIT), password)
	
	def asaOkButton(self):
		Util().clickButton(self.objName(DesktopConst.webbrowser.ASA_AUTH_OK_BUTTON))
	
	def asaCancelButton(self):
		Util().clickButton(self.objName(DesktopConst.webbrowser.ASA_AUTH_CANCEL_BUTTON))
	
	def asaAuthentication(self, username, password, p_clickOK = True):
		self.asaUsername(username)
		self.asaPassword(password)
		if p_clickOK:
			self.asaOkButton()
		else:
			self.asaCancelButton()
		
	def authenticateCiscoApp(self, username, password):
		self.ciscoApplicationManagement.login(username, password)
	
	def deployCiscoApplication(self, p_appID, p_projectName):
		self.ciscoApplicationManagement.addDeploy(p_appID, p_projectName)

	def authenticateRegistrationServer(self, p_username, p_password):
		self.registrationServer.loginPage.signIn(p_username, p_password)