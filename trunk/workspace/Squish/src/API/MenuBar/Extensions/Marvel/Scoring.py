from API.SquishSyntax import SquishSyntax
from API.functions import WebviewTagFind2 as TF
from API.MenuBar.Extensions.Marvel.MarvelConst import MarvelConst
from API.functions import pageLoadDecorator
import object
from squish import *

def getItem(searchTag, propertyDict):
	return TF().findTagWithProperties(MarvelConst.WINDOW, searchTag, propertyDict)

class Level1:
	def __init__(self):
		self.sq = SquishSyntax()
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def add(self, p_name):
		self.addButton()
		self.editName('', p_name, addButton = True)
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def addButton(self):
		button = getItem('A', {'innerText':'Add'})
		self.sq.click(button)
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def deleteButton(self):
		button = getItem('A', {'innerText':'Delete'})
		self.sq.click(button)
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def selectPrimaryObservable(self, p_observable):
		raise
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def selectSelectedPrimaryObservable(self, p_observable):
		raise
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def editName(self, p_currentName, p_newName, **kwargs):
		if 'addButton' in kwargs:
			if kwargs['addButton'] == True:
				doubleClick = not kwargs['addButton']
			else:
				doubleClick = kwargs['addButton']
		else:
			doubleClick = True
		if p_currentName == '':
			p_currentName = '\xc2\xa0\n'
		bFoundName = False
		table = self.getNamePointsTable()
		tableBody = object.children(table)[2]
		trTags = object.children(tableBody)#Rows
		for tr in trTags:
			td = object.children(tr)[0]#Name cell
			if str(td.innerText) == p_currentName:
				if doubleClick:
					td.doubleClick()
				textinput = TF().findTagWithID(MarvelConst.WINDOW, 'textfield-1165-inputEl')
				import test
				test.warning('This needs updated to not use ID')
				snooze(2)
				self.sq.setText(textinput, p_newName)
				snooze(1)
				#self.sq.nativeType(p_newName)
				bFoundName = True
		if not bFoundName:
			raise ValueError('The value given for current name was not found')
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def editPoints(self, p_currentName, p_points):
		if p_currentName == '':
			p_currentName = '\xc2\xa0\n'
		bFoundName = False
		table = self.getNamePointsTable()
		tableBody = object.children(table)[2]
		trTags = object.children(tableBody)#Rows
		for tr in trTags:
			name = object.children(tr)[0]#Name cell
			points = object.children(tr)[1]#point cell
			if name.innerText == p_currentName:
				points.doubleClick()
				self.sq.nativeType(p_points)
				bFoundName = True
		if not bFoundName:
			raise ValueError('The value given for current name was not found')
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def getNamePointsTable(self):
		parent = getItem('DIV', {'innerText':'^Name\\nPoints'})
		table = object.children(
							object.children(
										object.children(parent)[1]
										)[0]
							)[0]#Table item
		#table = TF().getTag(parent, 'TABLE', {'id':'gridview'})
		return table
	
class Level2:
	def __init__(self):
		self.sq = SquishSyntax()
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def addButton(self):
		raise
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def deleteButton(self):
		raise
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def openAllNodesButton(self):
		raise
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def editName(self, p_name):
		raise
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def selectLowerLevelObservable(self, p_name):
		raise
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def selectSelectedObservable(self, p_name):
		raise
	
class Scoring:
	def __init__(self):
		self.sq = SquishSyntax()
		self.level1 = Level1()
		self.level2 = Level2()
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def claims(self, p_text):
		parent = getItem('TR', {'innerText':'Claims:'})
		lineedit = TF().findTagWithProperties(parent, 'INPUT', {'type':'text'})
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def description(self, p_text):
		parent = getItem('TR', {'innerText':'Description:'})
		lineedit = TF().findTagWithProperties(parent, 'TEXTAREA', {'type':'textarea'})
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def addNewTabButton(self):
		button = getItem('A', {'innerText':'+'})
		self.sq.click(button)
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def level1TabButton(self):
		button = getItem('A', {'innerText':'Level 1'})
		self.sq.click(button)
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def level2TabButton(self):
		button = getItem('A', {'innerText':'Level 2'})
		self.sq.click(button)
		