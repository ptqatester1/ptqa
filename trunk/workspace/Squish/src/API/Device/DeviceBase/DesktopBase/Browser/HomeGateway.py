##Chris Allen
##This class is very similar to the registration server class so most items will be inherited
##The reason for creating this class is that a few functions need to be overrode because the homegateway page is formatted slightly different in the HTML
from API.Device.DeviceBase.DesktopBase.Browser import RegistrationServer
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import WebBrowser
from API.SquishSyntax import SquishSyntax
from squish import *

class HomeGateway(RegistrationServer.RegistrationServer):
	def __init__(self, p_squishName):
		self.squishname = p_squishName
		self.loginPage = LoginPage(p_squishName)
		self.signUpPage = SignUpPage(p_squishName)
		self.homePage = HomePage(p_squishName)       
		self.configurePage = ConfigurePage(p_squishName)
		self.configureActionPage = ConfigureActionPage(p_squishName)
		pass

	def updateName(self, p_squishName):
		self.squishName = p_squishName
		self.loginPage.updateName(p_squishName)
		self.signUpPage.updateName(p_squishName)
		self.homePage.updateName(p_squishName)
		self.configurePage.updateName(p_squishName)
		self.configureActionPage.updateName(p_squishName)
		
class LoginPage(RegistrationServer.LoginPage):
	pass

class SignUpPage(RegistrationServer.SignUpPage):
	pass

class HomePage(RegistrationServer.HomePage):
	def getTableItem(self, p_row, p_column, p_isHeader = False):
		'''Rows should start at 2 for the first row that is not a header. The header row is row 1'''
		rows = WebBrowser.RegistrationServer.HomePageHomeGateway.TABLE_ROW
		#rows = WebBrowser.RegistrationServer.HomePage.TABLE_ROW <---Change from registration server
		if p_isHeader:
			cols = WebBrowser.RegistrationServer.ConfigurationPage.TABLE_HEADER_COLUMN
		else:
			cols = WebBrowser.RegistrationServer.ConfigurationPage.TABLE_COLUMN
		cell = rows + str(p_row) + cols + str(p_column)
		return cell
	
	def submitButton(self):
		self.click(WebBrowser.RegistrationServer.HomePageHomeGateway.SUBMIT_BUTTON)
	
	def homeLink(self):
		self.clickLink(WebBrowser.RegistrationServer.HomePageHomeGateway.HOME_LINK)
	
	def configureLink(self):
		self.clickLink(WebBrowser.RegistrationServer.HomePageHomeGateway.CONFIGURE_LINK)
	
	def logoutLink(self):
		self.clickLink(WebBrowser.RegistrationServer.HomePageHomeGateway.LOGOUT_LINK)
	
		
	def checkTableRowText(self, p_row, p_deviceCol = None, p_aliasCol = None, p_serialNumberCol = None,
						   p_statusCol = None, p_valueCol = None, p_delteCol = None):
		'''iterate over all provided parameters and check the corresponding cell for the parameter text'''
		vals = dict(locals())
		SquishSyntax().clearCache(self.squishName + '.CWorkstationWebBrowserBase.m_CWorkstationWebView')
		if p_row == 1:
			tableColumnTag = WebBrowser.RegistrationServer.HomePageHomeGateway.TABLE_HEADER_COLUMN
		else:
			tableColumnTag = WebBrowser.RegistrationServer.HomePageHomeGateway.TABLE_COLUMN
		cells = {'p_deviceCol':1, 'p_aliasCol':2, 'p_serialNumberCol':3, 'p_statusCol':4, 'p_valueCol':5, 'p_delteCol':6}
		None
		for key, val in vals.iteritems():
			if key == 'self' or val == None or key == 'p_row':
				continue
			snooze(1)
			if key == 'p_aliasCol':
				#For this the base squishSyntax Text checkpoint is used in order to be able to pass a string of text instead of a object or object name
				#The reason is that the p_alias is an input which uses value instead of text, innerText, etc.
				deviceText = findObject(self.squishName + WebBrowser.RegistrationServer.HomePageHomeGateway.TABLE_ROW + str(p_row) + tableColumnTag + str(cells[key]) + '.INPUT1').value
				passed = SquishSyntax().textCheckPoint(str(deviceText), str(val))
			else:
				deviceText = findObject(self.squishName + WebBrowser.RegistrationServer.HomePageHomeGateway.TABLE_ROW + str(p_row) + tableColumnTag + str(cells[key])).innerText
				passed = SquishSyntax().textCheckPoint(str(deviceText), str(val))
			if not passed:
				test.log('Failed. Key: ' + str(key) + ', val: ' + str(val) + ', deviceText: ' + str(deviceText))

class ConfigurePage(RegistrationServer.ConfigurePage):
	pass

class ConfigureActionPage(RegistrationServer.ConfigureActionPage):
	pass