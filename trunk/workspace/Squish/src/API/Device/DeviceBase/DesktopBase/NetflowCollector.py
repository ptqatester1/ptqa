##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst
from API.SquishSyntax import SquishSyntax
import object

class Netflow(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName
	
	def on(self):
		Util().clickButton(self.objName(DesktopConst.netflowCollector.NETFLOW_ON_RADIO))
	
	def off(self):
		Util().clickButton(self.objName(DesktopConst.netflowCollector.NETFLOW_OFF_RADIO))
	
	def close(self):
		Util().clickButton(self.objName(DesktopConst.netflowCollector.CLOSE_BTN))
		
	@property
	def netflowChartName(self):
		return self.objName(DesktopConst.netflowCollector.PIE_CHART_PAGE)
		
	@property
	def netflowChart(self):
		return findObject(self.netflowChartName)
		
	@property
	def netflowItemList(self):
		itemList = []
		for item in object.children(self.netflowChart):
			if 'text' in object.properties(item):
				itemList.append(item)
		return itemList

	@property
	def netflowDetailPage(self):
		return findObject(self.objName(DesktopConst.netflowCollector.DETAILS_PAGE_HTML))

	@property
	def netflowDetailText(self):
		return str(self.netflowDetailPage.text)
	
	@property
	def hasNetflowItems(self):
		if self.netflowItemList:
			return True
		return False
	
	def selectNetflowItem(self, row = 0):
		'''Row starts at 0'''
		if not self.hasNetflowItems:
			raise LookupError('No netflow items in the chart')
		item = self.netflowItemList[row]
		Util().click(item)
	
	def checkText(self, itemName, value):
		for line in self.netflowDetailText.splitlines():
			name = line.split(':')[0]
			val = ':'.join(line.split(':')[1:])
			if itemName in name:
				Util().textCheckPoint(val, value)
				return
		raise ValueError('Unable to find item: ' + itemName)
