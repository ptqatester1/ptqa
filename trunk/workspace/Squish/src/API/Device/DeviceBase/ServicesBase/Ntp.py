##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *
from API import functions

class NtpCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
		
	def on(self, checked = True):
		Util().isChecked(self.objName(ServicesConst.ntp.ON), checked)
	
	def off(self, checked = True):
		Util().isChecked(self.objName(ServicesConst.ntp.OFF), checked)
	
	def enable(self, checked = True):
		Util().isChecked(self.objName(ServicesConst.ntp.AUTHENTICATION_ENABLE), checked)
	
	def disable(self, checked = True):
		Util().isChecked(self.objName(ServicesConst.ntp.AUTHENTICATION_DISABLE), checked)
	
	def key(self, key, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.ntp.AUTHENTICATION_KEY), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(ServicesConst.ntp.AUTHENTICATION_KEY), key, **kwargs)
	
	def password(self, password, **kwargs):
		if 'property' in kwargs:
			if not 'value' in kwargs:
				raise ValueError('A property and expected value must be specified. Please specify an expected value')
			Util().checkProperty(self.objName(ServicesConst.ntp.AUTHENTICATION_PASSWORD), kwargs['property'], kwargs['value'])
		else:
			Util().textCheckPoint(self.objName(ServicesConst.ntp.AUTHENTICATION_PASSWORD), password, **kwargs)
		
	def month(self, month, **kwargs):
		Util().textCheckPoint(self.objName(ServicesConst.ntp.CALENDAR_MONTH_BUTTON), month, **kwargs)
	
	def year(self, year, **kwargs):
		Util().textCheckPoint(self.objName(ServicesConst.ntp.CALENDAR_YEAR_BUTTON), year, **kwargs)
	
	def day(self, day, **kwargs):
		for i in range(7):
			for j in range(7):
				calendarDay = findObject(self.objName(ServicesConst.ntp.CALENDAR_DAY) + '.item_%s/%s'%(i,j))
				if calendarDay.selected:
					functions.check(str(calendarDay.text) == str(day))
					return
		raise ValueError('Unabled to find a selected date')

class Ntp(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = NtpCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def on(self):
		Util().clickButton(self.objName(ServicesConst.ntp.ON))
	
	def off(self):
		Util().clickButton(self.objName(ServicesConst.ntp.OFF))
	
	def enable(self):
		Util().clickButton(self.objName(ServicesConst.ntp.AUTHENTICATION_ENABLE))
	
	def disable(self):
		Util().clickButton(self.objName(ServicesConst.ntp.AUTHENTICATION_DISABLE))
	
	def key(self, key):
		Util().setText(self.objName(ServicesConst.ntp.AUTHENTICATION_KEY), key)
	
	def password(self, password):
		Util().setText(self.objName(ServicesConst.ntp.AUTHENTICATION_PASSWORD), password)
		
	def authentication(self, key, password):
		self.on()
		self.enable()
		self.key(key)
		self.password(password)
	
	def month(self, month):
		Util().clickButton(self.objName(ServicesConst.ntp.CALENDAR_MONTH_BUTTON))
		snooze(1)
		Util().activateItem(self.objName(ServicesConst.ntp.CALENDAR_MONTH_DROPDOWN), month)
		snooze(1)
	
	def day(self, day):
		snooze(1)
		calendarTable = self.objName(ServicesConst.ntp.CALENDAR_DAY)
		for i in range(1, 7):#rows 1-6
			for j in range(7):
				currentDay = findObject(calendarTable + '.item_%s/%s'%(i, j))
				if currentDay.text == str(day):
					if float(day) > 28 and currentDay.row < 5:
						#In order to account for instances where the next or previous month is shown on the page this check needs to be here
						continue
					else:
						Util().click(currentDay)
	
	def year(self, year):
		snooze(1)
		Util().clickButton(self.objName(ServicesConst.ntp.CALENDAR_YEAR_BUTTON))
		snooze(1)
		currentYear = findObject(self.objName(ServicesConst.ntp.CALENDAR_YEAR_EDIT))
		if currentYear.value == float(year):
			return
		if currentYear.value > float(year):
			arrowKey = '<Down>'
		else:
			arrowKey = '<Up>'
		while not currentYear.value == float(year):
			Util().typeText(self.objName(ServicesConst.ntp.CALENDAR_YEAR_EDIT), arrowKey)
			currentYear = findObject(self.objName(ServicesConst.ntp.CALENDAR_YEAR_EDIT))
			
	def yearInvalidOk(self):
		Util().clickButton(self.objName(ServicesConst.ntp.YEAR_INVALID_OK))
		
	'''
	Was unable to get hour/minute/second/meridiem to work at this time
	
	def hour(self, hour):
		Util().click(self.objName(ServicesConst.ntp.TIME))
		Util().typeText(self.objName(ServicesConst.ntp.TIME), '<Home>')
		for i in range(2):
			Util().typeText(self.objName(ServicesConst.ntp.TIME), '<Del>')
		Util().typeText(self.objName(ServicesConst.ntp.TIME), hour)
	
	def minute(self, minute):
		Util().click(self.objName(ServicesConst.ntp.TIME))
		Util().typeText(self.objName(ServicesConst.ntp.TIME), '<Home>')
		snooze(0.5)
		Util().typeText(self.objName(ServicesConst.ntp.TIME), '<Tab>')
		Util().typeText(self.objName(ServicesConst.ntp.TIME), minute) 
	
	def second(self, second):
		Util().click(self.objName(ServicesConst.ntp.TIME))
		Util().typeText(self.objName(ServicesConst.ntp.TIME), '<Home>')
		for i in range(2):
			snooze(0.5)
			Util().typeText(self.objName(ServicesConst.ntp.TIME), '<Tab>')
		Util().typeText(self.objName(ServicesConst.ntp.TIME), second) 
	
	def meridiem(self, am_pm):
		timeEdit = findObject(self.objName(ServicesConst.ntp.TIME))
		if am_pm.upper() in str(timeEdit.text):
			return
		Util().click(self.objName(ServicesConst.ntp.TIME))
		Util().typeText(self.objName(ServicesConst.ntp.TIME), '<Home>')
		for i in range(3):
			Util().typeText(self.objName(ServicesConst.ntp.TIME), '<Tab>')
		Util().typeText(self.objName(ServicesConst.ntp.TIME), '<Down>') 
	'''
	
	def date(self, month, day, year):
		self.month(month)
		self.day(day)
		self.year(year)
	
	def time(self, hour, minute, second, am_pm):
		Util().click(self.objName(ServicesConst.ntp.TIME))
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Del>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Backspace>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), hour)
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Right>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Del>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Del>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), minute)
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Right>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Del>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Del>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), second)
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Right>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Del>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), "<Del>")
		Util().typeText(self.objName(ServicesConst.ntp.TIME), am_pm.upper())