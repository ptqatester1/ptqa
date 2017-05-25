##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.ServicesBase.ServicesBaseConst import ServicesConst
from squish import *

class HttpRow:
	def __init__(self, filename, edit, delete):
		self.filename = filename
		self.edit = edit
		self.delete = delete

class HttpEditCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def filename(self, filename):
		Util().textCheckPoint(self.objName(ServicesConst.http.httpEdit.FILE_NAME), filename)
	
	def fileManager(self):
		raise NotImplementedError
		Util().clickButton(self.objName(ServicesConst.http.httpEdit.FILE_MANAGER))
	
	def save(self):
		raise NotImplementedError
		Util().clickButton(self.objName(ServicesConst.http.httpEdit.SAVE))
	
	def text(self, expected, **kwargs):
		Util().textCheckPoint(self.objName(ServicesConst.http.httpEdit.EDITOR), expected, **kwargs)

class HttpEdit(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.check = HttpEditCheck(self)
	
	def updateName(self, squishName):
		self.squishName = squishName
		self.check.updateName(squishName)
	
	def filename(self, filename):
		Util().setText(self.objName(ServicesConst.http.httpEdit.FILE_NAME), filename)
	
	def fileManager(self):
		Util().clickButton(self.objName(ServicesConst.http.httpEdit.FILE_MANAGER))
	
	def save(self):
		Util().clickButton(self.objName(ServicesConst.http.httpEdit.SAVE))
	
	def setText(self, text):
		Util().setText(self.objName(ServicesConst.http.httpEdit.EDITOR), text)

class HttpCheck(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
	
	def updateName(self, squishName):
		self.squishName = squishName
	
	def httpOn(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.http.HTTP_ON), checked)
	
	def httpOff(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.http.HTTP_OFF), checked)
	
	def httpsOn(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.http.HTTPS_ON), checked)
	
	def httpsOff(self, checked=True):
		Util().isChecked(self.objName(ServicesConst.http.HTTPS_OFF), checked)
		

class Http(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.edit = HttpEdit(self)
		self.check = HttpCheck(self)
		
	def updateName(self, squishName):
		self.squishName = squishName
		self.edit.updateName(self.squishName)
		self.check.updateName(squishName)
	
	@property
	def fileTableName(self):
		return self.objName(ServicesConst.http.FILE_TABLE)
	
	@property
	def fileTable(self):
		return findObject(self.fileTableName)
	
	def httpOn(self):
		Util().clickButton(self.objName(ServicesConst.http.HTTP_ON))
	
	def httpOff(self):
		Util().clickButton(self.objName(ServicesConst.http.HTTP_OFF))
	
	def httpsOn(self):
		Util().clickButton(self.objName(ServicesConst.http.HTTPS_ON))
	
	def httpsOff(self):
		Util().clickButton(self.objName(ServicesConst.http.HTTPS_OFF))
	
	def getFileRow(self, filename):
		'''Return an object containing the objects of each column for the row with the matching file name
		example:
			getFileRow('index.html')
		returns: object(object filename, object edit, object delete)'''
		for i in range(self.fileTable.rowCount):
			rowFilename = str(findObject(self.objName(ServicesConst.http.FILE_TABLE + '.item_' + str(i) + '/0')).text)
			if rowFilename == filename:
				return HttpRow(findObject(self.objName(ServicesConst.http.FILE_TABLE + '.item_' + str(i) + '/0')),
							findObject(self.objName(ServicesConst.http.FILE_TABLE + '.item_' + str(i) + '/1')),
							findObject(self.objName(ServicesConst.http.FILE_TABLE + '.item_' + str(i) + '/2')))
		raise ValueError('Could not find a file named ' + filename)
	
	def selectFile(self, filename):
		Util().click(self.getFileRow(filename).filename)
	
	def editFile(self, filename):
		Util().click(self.getFileRow(filename).edit)

	def deleteFile(self, filename):
		Util().click(self.getFileRow(filename).delete)
		Util().clickButton(self.objName(ServicesConst.http.CONFIRM_DELETE_YES))
	
	def newFileButton(self):
		Util().clickButton(self.objName(ServicesConst.http.NEW_FILE))
	
	def importButton(self):
		Util().clickButton(self.objName(ServicesConst.http.IMPORT_FILE))
