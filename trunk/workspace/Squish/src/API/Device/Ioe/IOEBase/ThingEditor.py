#*******************************************************#
#@Author: Chris Allen                                   #
#*******************************************************#

from API.Device.Ioe.IoeBaseConst import IoeBaseConst
from API.Utility.Util import Util
from API.SquishSyntax import SquishSyntax
from API.Device.Ioe.MCUConst import MCUConst
from API.functions import isType
from squish import snooze
from API.Device.DeviceBase.DeviceBase import SquishObjectName

class Properties(SquishObjectName, object):
	def __init__(self):
		self.squishName = ''
		self.util = Util()
		None
	
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		
	def setComponentName(self, p_name):
		self.util.setText(self.objName(IoeBaseConst.thingEditor.Properties.COMPONENT_NAME), p_name)
	
	def removeButton(self):
		self.util.clickButton(self.objName(IoeBaseConst.thingEditor.Properties.REMOVE_BUTTON))

	def newImageButton(self, p_imagePath):
		self.util.clickButton(self.objName(IoeBaseConst.thingEditor.Properties.NEW_BUTTON))
		self.util.open(p_imagePath)	
	
	def noneRadio(self):
		self.util.clickButton(self.objName(IoeBaseConst.thingEditor.Properties.NONE_RADIO))
	
	def digitalRadio(self):
		self.util.clickButton(self.objName(IoeBaseConst.thingEditor.Properties.DIGITAL_RADIO))
	
	def analogRadio(self):
		self.util.clickButton(self.objName(IoeBaseConst.thingEditor.Properties.ANALOG_RADIO))
	
	def slot(self, p_slot):
		self.util.click(self.objName(IoeBaseConst.thingEditor.Properties.SLOT_DROPDOWN))
		if isType(p_slot, 'int'):
			p_slot = 'Slot ' + str(p_slot)
		snooze(1)
		self.util.clickItem(self.objName(IoeBaseConst.thingEditor.Properties.SLOT_DROPDOWN), p_slot)
	
	def isCurrentSlot(self, p_slot):
		self.util.textCheckPoint(self.objName(IoeBaseConst.thingEditor.Properties.SLOT_DROPDOWN), p_slot)
	
	def addComponent(self):
		self.util.clickButton(self.objName(IoeBaseConst.thingEditor.Properties.ADD_COMPONENT_BUTTON))
	
	def removeComponent(self, p_component):
		#This needs to be finished
		self.util.clickItem(self.objName(IoeBaseConst.thingEditor.Properties), p_component)
	
	def openFile(self, p_filePath):
		self.util.setText(self.objName(IoeBaseConst.thingEditor.Properties.OPEN_IMAGE_NAME), p_filePath)
		self.util.clickButton(self.objName(IoeBaseConst.thingEditor.Properties.OPEN_IMAGE_BUTTON))
		
class Layout(object):	
	def __init__(self):
		self.squishName = ''
		self.util = Util()
		None
	
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		
	def moveImageByDrag(self, p_item, p_fromX, p_fromY, p_toX, p_toY):
		#This needs to be finished
		self.util.dragItemBy(p_obj, p_fromX, p_fromY, p_toX, p_toY)
		None
	
	def moveImageByProperties(self, p_itemObject, p_x, p_y):
		'''If using this call add a comment which item you are moving for the future if the object changes'''
		p_itemObject.setX(p_x)
		p_itemObject.setY(p_y)
	
	def bringItemForwardButton(self, p_itemObject = ''):
		'''If using this call add a comment which item you are moving for the future if the object changes'''
		if p_itemObject:
			self.util.selectImage(p_itemObject)
		self.util.clickButton(IoeBaseConst.thingEditor.Layout.BRING_ITEM_FORWARD_BUTTON)
		None
	
	def sendItemBackButton(self, p_itemObject = ''):
		'''If using this call add a comment which item you are moving for the future if the object changes'''
		if p_itemObject:
			self.util.selectImage(p_itemObject)
		self.util.clickButton(IoeBaseConst.thingEditor.Layout.SEND_ITEM_BACK_BUTTON)
		None
	
	def cycleSelectedImage(self, p_itemObject = ''):
		'''If using this call add a comment which item you are moving for the future if the object changes'''
		if p_itemObject:
			self.util.selectImage(p_itemObject)
		self.util.clickButton(IoeBaseConst.thingEditor.Layout.CYCLE_SELECTED_IMAGE_BUTTON)
		None
	
	def selectImage(self, p_imageX, p_imageY):
		'''If using this call add a comment which item you are moving for the future if the object changes
		Objects in the graphics view do not have identifiable names or attributes. X and Y values must be used'''
		self.util.click_x_y(p_obj, p_x, p_y)
		None
	
	def getImageObject(self, p_negativeImageIndex = 1):
		'''If using this call add a comment which item you are moving for the future if the object changes
		p_negativeImageIndex is used to get the child of object.children(<object>)[-p_negativeImageIndex]. A value of 1 will return the
		most recently added image in the graphics view. -2 the object before that and so on. The reason for using negative values is that
		it is easier to pull the last item.'''
		return object.children(findObject(self.squishName + IoeBaseConst.thingEditor.Layout.GRAPHICS_VIEW))[p_negativeImageIndex]
		
		
class Rules(object):
	def __init__(self):
		self.squishName = ''
		self.util = Util()
	
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		
	def selectSubComponent(self, p_row, p_component):
		self.util.click(IoeBaseConst.thingEditor.Rules.TABLE + '.item_' + str(p_row) + '/0')
		self.util.clickItem(IoeBaseConst.thingEditor.Rules.COMPONENT_DROPDOWN, p_component)
		None
	
	def selectSlotValue(self, p_row, p_slotValue1, p_slotValue2 = ''):
		'''For digital there is only one slot value but analog has 2'''
		self.util.click(IoeBaseConst.thingEditor.Rules.TABLE + '.item' + str(p_row) + '/1')
		if not p_slotValue2:
			self.util.clickItem(IoeBaseConst.thingEditor.Rules.SLOT_VALUE_DROPDOWN, p_slotValue1)
		else:
			self.util.setText(IoeBaseConst.thingEditor.Rules.SLOT_VALUE_SPINBOX_START, p_slotValue1)
			self.util.setText(IoeBaseConst.thingEditor.Rules.SLOT_VALUE_SPINBOX_STOP, p_slotValue2)
		None
	
	def selectImage(self, p_row, p_image):
		self.util.click(IoeBaseConst.thingEditor.Rules.TABLE + '.item' + str(p_row) + '/2')
		raise ('not finished')
		None
	
	def addButton(self):
		self.util.clickButton(IoeBaseConst.thingEditor.Rules.ADD_BUTTON)
		None
	
	def removeButton(self, p_ruleIndex):
		self.selectRule(p_ruleIndex)
		self.util.clickButton(IoeBaseConst.thingEditor.Rules.REMOVE_BUTTON)
		None
	
	def getTextOfCell(self, p_row, p_column = 0):
		from squish import findObject
		cell = findObject(self.squishName + IoeBaseConst.thingEditor.Rules.TABLE + '.item_' + str(p_row) + '/' + str(p_column))
		return cell.text
	
	def getCellObject(self, p_row, p_column = 0):
		from squish import findObject
		cell = findObject(self.squishName + IoeBaseConst.thingEditor.Rules.TABLE + '.item_' + str(p_row) + '/' + str(p_column))
		return cell
	
	def selectRule(self, p_index):
		'''index starting at 1 so it corresponds to the row number'''
		self.util.click(IoeBaseConst.thingEditor.Rules.RULE_NUMBER_COLUMN + p_index)

class ThingEditor(object):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.properties = Properties()
		self.layout = Layout()
		self.rules = Rules()
		
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		self.properties.updateName(p_squishName)
		self.layout.updateName(p_squishName)
		self.rules.updateName(p_squishName)
	
	def clickTab(self, p_tabName):
		Util().clickTab(MCUConst.thingEditor.TAB, p_tabName)
			