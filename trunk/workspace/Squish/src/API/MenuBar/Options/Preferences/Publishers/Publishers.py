##Chris Allen

from API.Utility.Util import Util

def err(msg = ''): raise NotImplementedError(msg)

class FileDialog:
	def __init__(self):
		self.util = Util()
	
	def filename(self, filename):
		err()
	
	def openButton(self):
		err()
	
	def cancelButton(self):
		err()
		

class TrustedPublishers:
	def __init__(self):
		self.util = Util()
		self.fileDialog = FileDialog()
	
	def addButton(self):
		err()
	
	def removeButton(self):
		err()
	
	def selectPublisher(self, issuedTo = None, issuedBy = None, serialNumber = None):
		err()
	
	def add(self, filename):
		self.addButton()
		self.fileDialog.filename(filename)
		self.fileDialog.openButton()
	
	def remove(self, issuedTo, issuedBy, serialNumber):
		self.selectPublisher(issuedTo, issuedBy, serialNumber)
		self.removeButton()
		
		
class UntrustedPublishers:
	def __init__(self):
		self.util = Util()
	
	def addButton(self):
		err()
	
	def removeButton(self):
		err()
	
	def selectPublisher(self, issuedTo = None, issuedBy = None, serialNumber = None):
		err()
		
	def add(self, filename):
		self.addButton()
		self.fileDialog.filename(filename)
		self.fileDialog.openButton()
	
	def remove(self, issuedTo, issuedBy, serialNumber):
		self.selectPublisher(issuedTo, issuedBy, serialNumber)
		self.removeButton()
	
class Publishers:
	def __init__(self):
		self.trusted = TrustedPublishers()
		self.untrusted = UntrustedPublishers()
	