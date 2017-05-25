##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from squish import *

class TerminalCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	def bitsPerSecond(self, bitsPerSecond, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(DesktopConst.terminal.BIT_PER_SEC_COMBO), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(DesktopConst.terminal.BIT_PER_SEC_COMBO), bitsPerSecond)
	
	def dataBits(self, dataBits, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(DesktopConst.terminal.DATA_BIT_COMBO), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(DesktopConst.terminal.DATA_BIT_COMBO), dataBits)
	
	def parity(self, parity, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(DesktopConst.terminal.PARITY_COMBO), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(DesktopConst.terminal.PARITY_COMBO), parity)
	
	def stopBits(self, stopBits, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(DesktopConst.terminal.STOP_BIT_COMBO), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(DesktopConst.terminal.STOP_BIT_COMBO), stopBits)
	
	def flowControl(self, flowControl, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(DesktopConst.terminal.FLOW_CONTROL_COMBO), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(DesktopConst.terminal.FLOW_CONTROL_COMBO), flowControl)

class Terminal(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = TerminalCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def bitsPerSecond(self, bitsPerSecond):
		Util().clickItem(self.objName(DesktopConst.terminal.BIT_PER_SEC_COMBO), bitsPerSecond)
	
	def dataBits(self, dataBits):
		Util().clickItem(self.objName(DesktopConst.terminal.DATA_BIT_COMBO), dataBits)
	
	def parity(self, parity):
		Util().clickItem(self.objName(DesktopConst.terminal.PARITY_COMBO), parity)
	
	def stopBits(self, stopBits):
		Util().clickItem(self.objName(DesktopConst.terminal.STOP_BIT_COMBO), stopBits)
	
	def flowControl(self, flowControl):
		Util().clickItem(self.objName(DesktopConst.terminal.FLOW_CONTROL_COMBO), flowControl)
	
	def okButton(self):
		Util().clickButton(self.objName(DesktopConst.terminal.OK_BUTT))
	
	def closeSettings(self):
		Util().clickButton(self.objName(DesktopConst.terminal.SETTINGS_CLOSE_BUTT))

	def setText(self, text, *moreText):
		for text in (text,) + moreText:
			Util().setConsoleText(self.objName(DesktopConst.terminal.TERMINAL_CONSOLE), text)

	def typeText(self, text, *moreText):
		for text in (text,) + moreText:
			Util().typeText(self.objName(DesktopConst.terminal.TERMINAL_CONSOLE), text)
	
	def closeTerminal(self):
		Util().clickButton(self.objName(DesktopConst.terminal.CLOSE_BUTT))
	
	def close(self):
		Util().clickButton(self.objName(DesktopConst.terminal.CLOSE_BUTT))
	
	def closeEmptyTerminal(self):
		Util().clickButton(self.objName(DesktopConst.terminal.CLOSE_BUTT_EMPTY))
	
	def configure(self, bitsPerSecond = 9600, dataBits = 8, parity = 'None', stopBits = 1, flowControl = 'None'):
		if bitsPerSecond:
			self.bitsPerSecond(str(bitsPerSecond))
		if dataBits:
			self.dataBits(str(dataBits))
		if parity:
			self.parity(parity)
		if stopBits:
			self.stopBits(str(stopBits))
		if flowControl:
			self.flowControl(flowControl)
		self.okButton()
		snooze(1)
	
	@property
	def cliObject(self):
		return findObject(self.objName(DesktopConst.terminal.TERMINAL_CONSOLE))
	
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

	def textCheckPoint(self, text, occurrenceNum = -1, **kwargs):
		Util().textCheckPoint(self.objName(DesktopConst.terminal.TERMINAL_CONSOLE), text, occurrenceNum, **kwargs)
	
	
	def emptyTerminalCheck(self, text, occurrenceNum = -1, **kwargs):
		Util().textCheckPoint(self.objName(DesktopConst.terminal.TERMINAL_CONSOLE_EMPTY), text, p_occurrenceNum=occurrenceNum, **kwargs)