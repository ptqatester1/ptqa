from API.Android.Simulation.EventList.EventListConst import EventListConst
from API.Android.Simulation.EventList.EventListConst import EventListFilterConst
from API.Android.Utility.Util import Util
from squish import *
import object
import test
from API.Android.ActionBar.OverFlowOptions.OverFlowOptions import OverFlow
from API.Android.ActionBar.OverFlowOptions.OverFlowOptionsConst import OverFlowConst
from API.Android.ActionBar.ActionBarConst import ActionBarConst
from API.Android.Utility.functions import MLStripper
import re

class EventList:
	def __init__(self):
		self.util = Util()
		self.strip = MLStripper()
	
	#Return a table of all the PDU information sorted by
	#Rows and columns see getPduInformation for usage
	def getAllPduInformation(self):
		stripTag = MLStripper()
		#Get the HTML
		s = str(findObject(EventListConst.EVENT_LIST).innerHTML)
		
		#Break up the HTML blocks
		split = re.sub('><', '>\n<', s).splitlines()
		
		#Blocks will hold a block for each of the lines in the event list
		blocks = []
		
		for l in split:
			if 'span' in l:
				blocks.append(l)
			
		tempRows = []
		for i, block in enumerate(blocks):
			tempRows.append(re.sub('> <', '>\n<', block).splitlines())
		
		table = []
		for i, cell in enumerate(tempRows):
			for l in cell:
				table.append(stripTag.strip_tags(l))
		
		t = []
		index = -1
		for i, item in enumerate(table):
			if i % 4 == 0:
				t.append([])
				index += 1
			t[index].append(item)
		
		return t

	#Returns the information about a specific cell
	def getPduInformation(self, p_row, p_column):
		return self.getAllPduInformation()[p_row][p_column]
	
	def compareField(self, p_expectedValue, p_row, p_column, p_exactMatch = False):
		text = self.getPduInformation(p_row, p_column)
		self.checkFieldText(p_expectedValue, text, p_exactMatch)
					
	def toggleEventList(self):
		self.util.tap(ActionBarConst.OVERFLOW_BUTTON)
		snooze(2)
		self.util.tap(OverFlowConst.PDU)
		snooze(5)
		None
		
	def showEventList(self):
		for i in range(5):
			if not self.isEventListVisible():
				self.toggleEventList()
				snooze(5)
				continue
			break
	
	def isEventListVisible(self):
		try:
			return findObject(EventListConst.EVENT_LIST).visible
		except:
			return False
		
	def forwardButton(self, p_times = 1):
		for i in range(p_times):
			self.util.tap(ActionBarConst.SIMULATION_FORWARD_BUTTON)
	
	def playButton(self):
		self.util.tap(ActionBarConst.SIMULATION_PLAY_BUTTON)
		
	def backButton(self, p_times = 1):
		for i in range(p_times):
			self.util.tap(ActionBarConst.SIMULATION_BACK_BUTTON)
		
	def checkPduLocation(self, p_row, p_atDevice, p_lastDevice = None, p_exactMatch = False):
		atDevice = self.getPduInformation(p_row, 2)
		lastDevice = self.getPduInformation(p_row, 1)
		self.checkFieldText(p_atDevice, atDevice)
		if p_lastDevice:
			self.checkFieldText(p_lastDevice, lastDevice)
		
	def isPduAtDevice(self, p_deviceName):
		pduInfo = self.getAllPduInformation()
		numberOfEvents = len(pduInfo)
		currentDevice = pduInfo[numberOfEvents-1][2]
		return self.compareFieldText(p_deviceName, currentDevice)
	
	def isPduFromDevice(self, p_deviceName):
		pduInfo = self.getAllPduInformation()
		numberOfEvents = len(pduInfo)
		fromDevice = pduInfo[numberOfEvents-1][1]
		return self.compareFieldText(p_deviceName, fromDevice)
	
	def isPduType(self, p_pduType):
		return self.compareFieldText(p_pduType, str(self.getCurrentPacketType()))
		
	def getCurrentPacketType(self):
		pduInfo = self.getAllPduInformation()
		numberOfEvents = len(pduInfo)
		currentType = pduInfo[numberOfEvents-1][3]
		return currentType
	
	def forwardUntilPacketIsAt(self, p_device, p_maxForwards = 100):
		for i in range(p_maxForwards):
			self.forwardButton()
			if self.isPduAtDevice('PC1'):
				break
			continue
	
	def forwardUntilPacketTypeIs(self, p_packetType, p_maxForwards = 100):
		for i in range(p_maxForwards):
			self.forwardButton()
			if str(self.getCurrentPacketType()) == p_packetType:
				break
			continue
	
	#This is to check the text received from the getPduInformation function
	#p_exactMatch is used to determine if the received text should be fixed
	#to not include the trailing ... characters
	def checkFieldText(self, p_expected, p_received, p_exactMatch = False):
		#Strip the trailing ... if p_exactMatch is false
		if not p_exactMatch:
			expected = re.sub('\.', '', p_expected)
			received = re.sub('\.', '', p_received)
		else:
			if p_received == p_expectedValue:
				return test.passes(str(p_expectedValue + ' and ' + p_received + ' match'))
			else:
				return test.fail(str(p_expectedValue + ' and ' + p_received + ' do not match'))
		
		#Should only execute if p_exactMatch is False
		if len(expected) >= len(received):
			if received in expected:
				test.passes('pass ' + received + ' in ' + expected)
			else:
				test.fail('Fail ' + received + ' not in ' + expected)
		else:
			if expected in received:
				test.passes('pass ' + expected + ' in ' + received)
			else:
				test.fail('Fail ' + expected + ' not in ' + received)
	
				
	def compareFieldText(self, p_expected, p_received, p_exactMatch = False):
		#Strip the trailing ... if p_exactMatch is false
		if not p_exactMatch:
			expected = re.sub('\.', '', p_expected)
			received = re.sub('\.', '', p_received)
		else:
			if p_received == p_expectedValue:
				return True
			else:
				return False
		
		#Should only execute if p_exactMatch is False
		if len(expected) >= len(received):
			if received in expected:
				return True
			else:
				return False
		else:
			if expected in received:
				return True
			else:
				return False

class EventListFilter:
	def __init__(self):
		self.util = Util()
		self.event = EventList()
	
	def toggleFilterWindow(self):
		self.util.tap(EventListConst.FILTER_BUTTON)
	
	def toggleShowAllNone(self):
		self.util.tap(EventListFilterConst.SHOW_ALL)
	
	def applyFilters(self):
		self.util.tap(EventListFilterConst.APPLY_FILTERS)
	
	def toggleFiltersItems(self, *filters):
		for item in filters:
			currentFilter = findObject(item)
			if currentFilter.screenRect.y == -1:
				self.resetFilterPosition()
			for i in range(30):    
				if not self.makeFilterVisible(item):
					continue
				break	
			self.util.tap(item)
			
	def makeFilterVisible(self, p_filter):
		f = findObject(p_filter)
		if f.screenRect.y == -1:
			self.util.swipe(1520, 900, 0, -100)
			return False
		elif f.screenRect.y > 900:
			self.util.swipe(1520, 300, 0, -100)
			return False
		elif f.screenRect.y < 200:
			self.util.swipe(1520, 900, 0, 100)
			return False
		else:
			return True
	
	def resetFilterPosition(self):
		for i in range(30):
			if not findObject(EventListFilterConst.ARP).screenRect.y > 200:
				self.util.swipe(1520, 900, 0, 100)
				continue
			break