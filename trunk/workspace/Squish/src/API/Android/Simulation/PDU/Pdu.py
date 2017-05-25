from API.Android.Simulation.PDU.PduConst import PduConst
from API.Android.Utility.Util import Util

class Pdu:
	def __init__(self):
		self.util = Util()
		self.tabs = Tabs()
		pass
	
	def closePduDetails(self):
		self.util.tap(PduConst.CLOSE_BUTTON)
	

class Tabs:
	def osiLayersTab(self):
		self.util.tap(PduConst.PduTabs.OSI_LAYERS)
	
	def pduInDetailsTab(self):
		self.util.tap(PduConst.PduTabs.PDU_IN_DETAILS)
	
	def pduOutDetailsTab(self):
		self.util.tap(PduConst.PduTabs.PDU_OUT_DETAILS)
	
	def eventListTab(self):
		self.util.tap(PduConst.PduTabs.EVENT_LIST)
		
		