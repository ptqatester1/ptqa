##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import DeviceBase
from API.Device.DeviceBase.CliBase.CliBaseConst import CliConst
from squish import *

class Cli(DeviceBase):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def copyButton(self):
		Util().clickButton(self.objName(CliConst.CLI_COPY))

	def pasteButton(self):
		Util().clickButton(self.objName(CliConst.CLI_PASTE))

	def setCliText(self, text, *moreText):
		for text in (text,) + moreText:
			Util().setConsoleText(self.objName(CliConst.CLI_CONSOLE), text)
	
	def typeText(self, text, *moreText):
		for text in (text,) + moreText:
			Util().typeText(self.objName(CliConst.CLI_CONSOLE), text)
	
	def configureIPAddress(self, interface, ip, subnet):
		self.setCliText("conf t")
		self.setCliText("int " + interface)
		self.setCliText("ip add " + ip + " " + subnet)
		self.setCliText("no shut")

	def startConsole(self):
		self.setCliText('no')
		self.setCliText('\r')
		self.setCliText('\r')

	def sendBreak(self):
		self.cliObject.grabKeyboard()#Make sure the native type goes to the CLI console
		Util().nativeType('<Ctrl+Shift+^>')
		Util().nativeType('x')
		self.cliObject.releaseKeyboard()#Release the grab on the keyboard so other objects can use it now
	
	def sendAbort(self):	
		self.cliObject.grabKeyboard()#Make sure the native type goes to the CLI console
		Util().nativeType('<Ctrl+Shift+^>')
		self.cliObject.releaseKeyboard()#Release the grab on the keyboard so other objects can use it now	
	
	def textCheckPoint(self, searchText, occurrenceNum = -1, **args):
		Util().textCheckPoint(self.objName(CliConst.CLI_CONSOLE), searchText, occurrenceNum, **args)
	
	@property
	def cliObject(self):
		return findObject(self.objName(CliConst.CLI_CONSOLE))
	
	@property
	def cliText(self):
		return str(self.cliObject.toPlainText())
	
	def hasText(self, text, **kwargs):
		if Util().hasText(self.cliText, text, **kwargs):
			return True
		else:
			return False
	
	def selectText(self, text, startingIndex):
		if startingIndex:
			self.cliObject.moveCursor(startingIndex)
		else:
			self.cliObject.moveCursor(QTextCursor.Start)
		self.cli.find(text)
	
	def waitForText(self, expectedText, maxWaitTime = 60, **kwargs):
		'''Can use any kwargs available in sliceConsoleText
		Example use case: self.waitForText('Received = [1234], 30, lines = 10)
						  Would check the last ten lines of text once every thousandth of a second
						  to see if they match the regex 'Received = [1234]'. It will do this until
						  the string is found or 30 seconds have gone by.
        lines: integer
            Number of lines to include starting at the end and going backwards.
            Example: lines = 10 would include the last 10 lines in p_consoleText
        chars: integer
            Number of previous characters to include in the search
            Example: chars = 100 would include the last 100 characters in p_consoleText
        string: string
            string to start at where it would include text from the last found instance of the string to the end
            Example: string = 'ping' would include from the last time ping appears in p_consoleText to the end of p_consoleText
        start: integer || string
            This can be an integer or string.
                If it is an integer it does the same as chars but the number is the starting index
                If it is a string it does the same as string but it will start from the first found instance of the string
        Stop: integer || string
            This is the same as start except telling the function where to stop. It finds the first occurrence after start
        Start/Stop
            Example:
                start = 0, stop = 100 would search the first 100 chars in the string
                start = 'ping', stop = 'Received = [1234]' would search from ping (inclusive) to the end of Received = [1234] (inclusive)
		'''
		cycles = maxWaitTime * 1000
		for i in range(cycles):
			consoleText = Util().sliceConsoleText(self.cliText, **kwargs)
			if expectedText in consoleText:
				return True
			snooze(.001)
		return False