from API.SquishSyntax import SquishSyntax
from API.functions import WebviewTagFind2 as TF
from API.MenuBar.Extensions.Marvel.MarvelConst import MarvelConst

def getItem(searchTag, propertyDict, parent = None):
	if not parent:
		return TF().findTagWithProperties(MarvelConst.WINDOW, searchTag, propertyDict)
	else:
		return TF().findTagWithProperties(parent, searchTag, propertyDict)

class CurrentFeedback:
	def __init__(self):
		self.sq = SquishSyntax()
	
	def addButton(self):
		parent = getItem('DIV', {'innerText':'Current Feedback'})
		button = getItem('A', {'innerText':'Add'}, parent)
		self.sq.click(button)

	def deleteButton(self):
		parent = getItem('DIV', {'innerText':'Current Feedback'})
		button = getItem('A', {'innerText':'Delete'}, parent)
		self.sq.click(button)
	
	def selectFeedback(self, p_name):
		raise

class AvailableObservables:
	def __init__(self):
		self.sq = SquishSyntax()

class SelectedObservables:
	def __init__(self):
		self.sq = SquishSyntax()
	
class Observables:
	def __init__(self):
		self.selected = SelectedObservables()
		self.available = AvailableObservables()
		
class Points:
	def __init__(self):
		self.sq = SquishSyntax()
	
class Feedback:
	def __init__(self):
		self.points = Points()
		self.currentFeedback = CurrentFeedback()
		self.observables = Observables()