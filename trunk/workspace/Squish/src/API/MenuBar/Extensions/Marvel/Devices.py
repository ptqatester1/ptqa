from API.SquishSyntax import SquishSyntax

class Initial:
	def __init__(self):
		self.sq = SquishSyntax()
	
	def selectDevice(self, p_device):
		raise
	
	def deleteButton(self):
		raise
class Answer:
	def __init__(self):
		self.sq = SquishSyntax()
	
	def selectDevice(self, p_device):
		raise
	
	def deleteButton(self):
		raise

class Devices:
	def __init__(self):
		self.sq = SquishSyntax()
		self.initial = Initial()
		self.answer = Answer()
	
	def reloadMetaButton(self):
		raise