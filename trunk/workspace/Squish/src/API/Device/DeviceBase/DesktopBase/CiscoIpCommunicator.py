##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst

class CiscoIpCommunicator(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = CiscoIpCommunicatorCheck(self)

	def updateName(self, squishName):
		self.squishName = squishName

	def newCallButton(self):
		Util().clickButton(self.objName(DesktopConst.ciscoIpCommunicator.NewCall_Mode.NEW_CALL))

	def numberButton(self, number):
		Util().clickButton(self.objName(DesktopConst.ciscoIpCommunicator.NewCall_Mode.NUMBER + str(number)))

	def cancelButton(self):
		Util().clickButton(self.objName(DesktopConst.ciscoIpCommunicator.CANCEL_BUTTON))

	def answerButton(self):
		Util().clickButton(self.objName(DesktopConst.ciscoIpCommunicator.ANSWER_BUTT))
		
	def endButton(self):
		Util().clickButton(self.objName(DesktopConst.ciscoIpCommunicator.END_CALL))

	def dialButton(self):
		Util().clickButton(self.objName(DesktopConst.ciscoIpCommunicator.Dial_Mode.DIAL_BUTT))

	def speakerButton(self):
		Util().clickButton(self.objName(DesktopConst.ciscoIpCommunicator.SPEAKER))

	def call(self, number):
		self.newCallButton()
		for num in str(number):#Convert number into string so that it can be iterated over
			self.numberButton(num)
		#self.dialButton()
	
	def close(self):
		Util().close(self.objName(DesktopConst.ciscoIpCommunicator.MAIN_SCREEN))
		
class CiscoIpCommunicatorCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		
	def updateName(self, squishName):
		self.squishName = squishName
		
	def number(self, number, **kwargs):
		if 'property' in kwargs:
			Util().checkProperty(self.objName(DesktopConst.ciscoIpCommunicator.LINE_NUMBER_LABEL), **kwargs)
		else:
			Util().textCheckPoint(self.objName(DesktopConst.ciscoIpCommunicator.LINE_NUMBER_LABEL), number)
			
	def soundStatus(self, text):
		Util().textCheckPoint(self.objName(DesktopConst.ciscoIpCommunicator.DO_RE_MI_LABEL), text)