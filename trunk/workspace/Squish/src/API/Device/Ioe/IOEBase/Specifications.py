#*******************************************************#
#@Author: Chris Allen                                   #
#*******************************************************#

from API.Device.Ioe.IoeBaseConst import IoeBaseConst
from API.SquishSyntax import SquishSyntax
from squish import findObject

class FormattingShortcuts(object):
	def __init__(self):
		self.squishName = ''
		None
	
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		self.clickButton = SquishSyntax().clickButton
	
	def bold(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.BOLD)
		None
	
	def italic(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.ITALIC)
		None
	
	def strikeThrough(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.STRIKETHROUGH)
		None
	
	def align(self, p_alignment = 'left'):
		alignment = p_alignment.lower()
		if alignment == 'left':
			self.clickButton(IoeBaseConst.specifications.shortCutButtons.ALIGN_LEFT)
		elif alignment == 'right':
			self.clickButton(IoeBaseConst.specifications.shortCutButtons.ALIGN_RIGHT)
		elif alignment == 'center':
			self.clickButton(IoeBaseConst.specifications.shortCutButtons.ALIGN_CENTER)
		elif alignment == 'justify':
			self.clickButton(IoeBaseConst.specifications.shortCutButtons.ALIGN_JUSTIFY)
		else:
			raise('Incorrect parameter provided')
		None
	
	def indent(self, p_increaseDecrease = 'increase'):
		indent = p_increaseDecrease.lower()
		if indent == 'increase':
			self.clickButton(IoeBaseConst.specifications.shortCutButtons.INCREASE_INDENT)
		elif indent == 'decrease':
			self.clickButton(IoeBaseConst.specifications.shortCutButtons.DECREASE_INDENT)
		else:
			raise('Incorrect parameter provided')
		None
	
	def numberedList(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.NUMBERED_LIST)
		None
	
	def bulletedList(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.BULLETED_LIST)
		None
	
	def insertImage(self, p_imagePath):
		raise('Not implemented yet')
	
		None
	
	def createLink(self, p_url):
		raise('Not implemented yet')
		None
	
	def insertHtml(self, p_html):
		raise('Not implemented yet')
		None
	
class EditShortcuts(object):
	def __init__(self):
		self.squishName = ''
		self.clickButton = SquishSyntax().clickButton
		None
	
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		
	def new(self, p_saveDiscardCancel = 'Discard', p_filename = None):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.NEW)
		None
		
	def open(self, p_filename):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.OPEN)
		None
	
	def save(self, p_filename):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.SAVE)
		None
	
	def undo(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.UNDO)
		None
	
	def redo(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.REDO)
		None
	
	def cut(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.CUT)
		None
	
	def copy(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.COPY)
		None
	
	def paste(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.PASTE)
		None
	
	def zoom(self, p_setting):
		'''integer value of the desired zoom level'''
		slider = findObject(IoeBaseConst.specifications.shortCutButtons.ZOOM_SLIDER)
		slider.setValue(p_setting)
	
	def zoomIn(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.ZOOM_IN)
	
	def zoomOut(self):
		self.clickButton(IoeBaseConst.specifications.shortCutButtons.ZOOM_OUT)

class Formatting(object):
	def __init__(self):
		self.squishName = ''
	
	def updateName(self, p_squishName):
		self.squishName = p_squishName
			
	def style(self, p_style):
		raise('not yet implemented')
	
	def align(self, p_alignment):
		raise('not yet implemented')
	
	def bold(self):
		raise('not yet implemented')
	
	def italic(self):
		raise('not yet implemented')
	
	def strikeThrough(self):
		raise('not yet implemented')
	
	def indent(self, p_increaseDecrease):
		raise('not yet implemented')
	
	def numberedList(self):
		raise('not yet implemented')
	
	def bulletedList(self):
		raise('not yet implemented')
	
	def fontName(self, p_font, p_okCancel = 'Ok'):
		raise('not yet implemented')
	
	def fontSize(self, p_fontSize, p_okCancel = 'Ok'):
		raise('not yet implemented')
	
	def fontColor(self, p_color, p_okCancel = 'Ok'):
		raise('not yet implemented')
	
	def backgroundColor(self, p_color, p_okCancel = 'Ok'):
		raise('not yet implemented')

class Edit(object):
	def __init__(self):
		self.squishName = ''
		self.sq = SquishSyntax()
	
	def updateName(self, p_squishName):
		self.squishName = p_squishName
	
	def setText(self, p_text):
		from squish import *
		#self.sq.nativeMouseClick(self.squishName + IoeBaseConst.specifications.TEXT_AREA, 100, 100)
		obj = findObject(self.squishName + IoeBaseConst.specifications.TEXT_AREA)
		obj.click()
		snooze(0.5)
		self.sq.nativeType('<Ctrl+a>')
		snooze(0.5)
		self.sq.nativeType('<Del>')
		snooze(0.5)
		self.sq.nativeType(p_text)
	
	def undo(self):
		raise('not yet implemented')
	
	def redo(self):
		raise('not yet implemented')
	
	def cut(self):
		raise('not yet implemented')
	
	def copy(self):
		raise('not yet implemented')
	
	def paste(self):
		raise('not yet implemented')
	
	def selectAll(self):
		raise('not yet implemented')
	
	def insertImage(self, p_imagePath):
		raise('not yet implemented')
	
	def createLink(self, p_url):
		raise('not yet implemented')

class Specifications(object):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.clickButton = SquishSyntax().clickButton
		self.formatShortcuts = FormattingShortcuts()
		self.editShortcuts = EditShortcuts()
		self.edit = Edit()
		self.formatting = Formatting()
		
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		self.formatShortcuts.updateName(p_squishName)
		self.editShortcuts.updateName(p_squishName)
		self.edit.updateName(p_squishName)
		self.formatting.updateName(p_squishName)

	def editButton(self):
		self.clickButton(IoeBaseConst.specifications.EDIT_BUTTON)
		None

	def advancedButton(self, status = 'on'):
		if (findObject(IoeBaseConst.specifications.ADVANCED_BUTTON).checked == True) and status == 'off' or (findObject(IoeBaseConst.specifications.ADVANCED_BUTTON).checked == False) and status == 'on':
			self.clickButton(IoeBaseConst.specifications.ADVANCED_BUTTON)
		
	
	@property
	def text(self):
		return findObject(self.squishName + IoeBaseConst.specifications.TEXT_AREA).innerText
