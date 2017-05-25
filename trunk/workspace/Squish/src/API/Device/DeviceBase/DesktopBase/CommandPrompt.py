##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from squish import *

class CommandPrompt(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def setText(self, text):
		Util().setConsoleText(self.objName(DesktopConst.commandPrompt.CONSOLE_TEXT), text)
		
	def type(self, text):
		Util().typeText(self.objName(DesktopConst.commandPrompt.CONSOLE_TEXT), text)
	
	def textCheckPoint(self, text, occurrenceNum = -1, **kwargs):
		Util().textCheckPoint(self.objName(DesktopConst.commandPrompt.CONSOLE_TEXT), text, occurrenceNum, **kwargs)
		
	def close(self):
		Util().clickButton(self.objName(DesktopConst.commandPrompt.CLOSE_BUTT))

	@property
	def cliObject(self):
		return findObject(self.objName(DesktopConst.commandPrompt.CONSOLE_TEXT))

	@property
	def cliText(self):
		return str(self.cliObject.toPlainText())

	def waitForText(self, expectedText, maxWaitTime = 60, **kwargs):
		'''Can use any kwargs available in sliceConsoleText
		Example use case: self.waitForText('Received = [1234], 30, lines = 10)
						  Would check the last ten lines of text once every thousandth of a second
						  to see if they match the regex 'Received = [1234]'. It will do this until
						  the string is found or 30 seconds have gone by.
		'''
		cycles = maxWaitTime * 1000
		for i in range(cycles):
			consoleText = Util().sliceConsoleText(self.cliText, **kwargs)
			if expectedText in consoleText:
				return True
			snooze(.001)
		return False
