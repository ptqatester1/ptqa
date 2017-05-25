from API.MenuBar.Extensions.Marvel.MarvelConst import MarvelConst
from API.MenuBar.Extensions.Marvel.Files import File
from API.MenuBar.Extensions.Marvel.Devices import Devices
from API.MenuBar.Extensions.Marvel.Feedback import Feedback
from API.MenuBar.Extensions.Marvel.Scoring import Scoring
from API.MenuBar.Extensions.Marvel.Sumarry import Summary
from API.MenuBar.Extensions.Marvel.ValidateScoring import ValidateScoring
from API.functions import WebviewTagFind2 as TF
from API.SquishSyntax import SquishSyntax
from API.MenuBar.Extensions.Extensions import Extensions
from API.MenuBar.Extensions.ExtensionsConst import ExtensionsConst
from API.functions import NotFoundException
from API.functions import pageLoadDecorator
from squish import *
class Tabs:
	def __init__(self):
		self.webview = MarvelConst.WINDOW
		self.squishSyntax = SquishSyntax()
		pass
	
	@pageLoadDecorator(MarvelConst.WINDOW)
	def file(self):
		self.squishSyntax.click(TF().findTagWithProperties(self.webview, 'A', {'innerText':'File'}))
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def scoring(self):
		self.squishSyntax.click(TF().findTagWithProperties(self.webview, 'A', {'innerText':'Scoring'}))
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def feedback(self):
		self.squishSyntax.click(TF().findTagWithProperties(self.webview, 'A', {'innerText':'Feedback'}))
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def devices(self):
		self.squishSyntax.click(TF().findTagWithProperties(self.webview, 'A', {'innerText':'Devices'}))
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def validateScoring(self):
		self.squishSyntax.click(TF().findTagWithProperties(self.webview, 'A', {'innerText':'Validate Scoring'}))
		
	@pageLoadDecorator(MarvelConst.WINDOW)
	def summary(self):
		self.squishSyntax.click(TF().findTagWithProperties(self.webview, 'A', {'innerText':'Summary'}))
		
class Marvel:
	def __init__(self):
		self.tabs = Tabs()
		self.file = File()
		self.scoring = Scoring()
		self.feedback = Feedback()
		self.devices = Devices()
		self.validateScoring = ValidateScoring()
		self.summary = Summary()
	
	def openMarvel(self):
		Extensions().selectExtensionsItem(ExtensionsConst.MARVEL)
		#wait for the marvel page to load