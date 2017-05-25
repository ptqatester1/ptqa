from API.SquishSyntax import SquishSyntax
from API.MenuBar.Extensions.Marvel.MarvelConst import MarvelConst
from API.functions import WebviewTagFind2 as TF
from API.functions import pageLoadDecorator
from squish import *
import object

class File:
	def __init__(self):
		self.sq = SquishSyntax()
		pass
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def synchChanges(self):
		checkbox = TF().findTagWithProperties(MarvelConst.WINDOW, 'LABEL', {'innerText':'Synchronize Changes to PKA'})
		self.sq.click(checkbox)
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def browseExistingPKAButton(self):
		button = TF().findTagWithProperties(MarvelConst.WINDOW, 'A', {'innerText':'Browse For Existing PKA'})
		self.sq.click(button)
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def browseExistingPantherTaskXMLButton(self):
		button = TF().findTagWithProperties(MarvelConst.WINDOW, 'A', {'innerText':'Browse For Existing Panther Task XML'})
		self.sq.click(button)
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def saveButton(self):
		button = TF().findTagWithProperties(MarvelConst.WINDOW, 'A', {'innerText':'Save'})
		self.sq.click(button)
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def saveAsbutton(self):
		button = TF().findTagWithProperties(MarvelConst.WINDOW, 'A', {'innerText':'Save As'})
		self.sq.click(button)
	
	def filename(self, p_text):
		waitForObject(MarvelConst.FILE_NAME_EDIT)
		self.sq.setText(MarvelConst.FILE_NAME_EDIT, p_text)
	
	def openfileButton(self):
		waitForObject(MarvelConst.OPEN_BUTTON)
		self.sq.clickButton(MarvelConst.OPEN_BUTTON)
	
	def cancelButton(self):
		waitForObject(MarvelConst.CANCEL_BUTTON)
		self.sq.clickButton(MarvelConst.CANCEL_BUTTON)
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def openPKA(self, p_filename, p_open = True):
		self.browseExistingPKAButton()
		self.filename(p_filename)
		if p_open:
			self.openfileButton()
		else:
			self.cancelButton()
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def openXML(self, p_filename, p_open = True):
		self.openXML(p_filename, p_open)
		self.filename(p_filename)
		if p_open:
			self.openfileButton()
		else:
			self.cancelButton()
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def save(self):
		raise NotImplementedError('Future')
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def saveAs(self):
		raise NotImplementedError('Future')
	
	