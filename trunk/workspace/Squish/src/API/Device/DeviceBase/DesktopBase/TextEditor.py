##Chris Allen

from API.Utility.Util import Util
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import DesktopConst

class Open(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def selectFile(self, filename):
		err()

	def okButton(self):
		err()

	def cancelButton(self):
		err()

class Save(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def filename(filename):
		err()

	def okButton(self):
		err()

	def cancelButton(self):
		err()

class Import(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def filename(filename):
		err()

	def openButton(self):
		err()

	def cancelButton(self):
		err()

class File(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName

	def updateName(self, squishName):
		self.squishName = squishName

	def new(self):
		err()

	def open(self, filename):
		err()

	def save(self, filename):
		err()

	def importFile(self, filename):
		err()

	def exit(self):
		err()

class TextEditor(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.fileOption = File(self)
		self.importOption = Import(self)
		self.saveOption = Save(self)
		self.openOption = Open(self)

	def updateName(self, squishName):
		self.squishName = squishName
	
	def setText(self, text):
		Util().typeText(self.objName(DesktopConst.textEditor.TEXT_EDIT), text)

	def checkText(self, text, occurrenceNum = -1):
		Util().textCheckPoint(self.objName(DesktopConst.textEditor.TEXT_EDIT), text, occurrenceNum)

	def discard(self):
		Util().clickButton(self.objName(DesktopConst.textEditor.DISCARD_BUTT))
	
	def newFile(self, action = None, fileName = None):
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_BAR), 'File')
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_FILE), 'New')
		if (Util().checkObjectExist(self.objName(DesktopConst.textEditor.POPUP_DIALOG))):
			if action == 'cancel':
				Util().clickButton(self.objName(DesktopConst.textEditor.CANCEL_BUTTON))
			elif action == 'save':
				Util().clickButton(self.objName(DesktopConst.textEditor.SAVE_BUTTON))
				Util().setText(self.objName(DesktopConst.textEditor.SAVE_FILE_TEXT_EDIT), fileName)
				Util().clickButton(self.objName(DesktopConst.textEditor.SAVE_FILE_OK_BUTT))
			elif action == 'discard' or action == None:
				Util().clickButton(self.objName(DesktopConst.textEditor.DISCARD_BUTT))
			else:
				err()
	
	def openFile(self, action = None, item = None, saveFileName = None):
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_BAR), 'File')
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_FILE), 'Open')
		Util().clickItem(self.objName(DesktopConst.textEditor.FILES_TABLE), item)
		Util().clickButton(self.objName(DesktopConst.textEditor.OPEN_FILE_OK_BUTT))
		if (Util().checkObjectExist(self.objName(DesktopConst.textEditor.POPUP_DIALOG))):
			if action == 'discard' or action == None:
				Util().clickButton(self.objName(DesktopConst.textEditor.DISCARD_BUTT))
			elif action == 'cancel':
				Util().clickButton(self.objName(DesktopConst.textEditor.CANCEL_BUTTON))
			elif action == 'save':
				Util().clickButton(self.objName(DesktopConst.textEditor.SAVE_BUTTON))
				Util().setText(self.objName(DesktopConst.textEditor.SAVE_FILE_TEXT_EDIT), saveFileName)
				Util().clickButton(self.objName(DesktopConst.textEditor.SAVE_FILE_OK_BUTT))
			
	def saveFile(self, action = None, fileName = None):
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_BAR), 'File')
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_FILE), 'Save')
		if action == 'save' or action == None:
			Util().setText(self.objName(DesktopConst.textEditor.SAVE_FILE_TEXT_EDIT), fileName)
			Util().clickButton(self.objName(DesktopConst.textEditor.SAVE_FILE_OK_BUTT))
		elif action == 'cancel':
			Util().clickButton(self.objName(DesktopConst.textEditor.SAVE_FILE_CANCEL_BUTT)) 
	
	def exit(self, action = None, fileName = None):
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_BAR), 'File')
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_FILE), 'Exit')
		if (Util().checkObjectExist(self.objName(DesktopConst.textEditor.POPUP_DIALOG))):
			if action == 'cancel':
				Util().clickButton(self.objName(DesktopConst.textEditor.CANCEL_BUTTON))
			elif action == 'save':
				Util().clickButton(self.objName(DesktopConst.textEditor.SAVE_BUTTON))
				Util().setText(self.objName(DesktopConst.textEditor.SAVE_FILE_TEXT_EDIT), fileName)
				Util().clickButton(self.objName(DesktopConst.textEditor.SAVE_FILE_OK_BUTT))
			elif action == 'discard' or action == None:
				Util().clickButton(self.objName(DesktopConst.textEditor.DISCARD_BUTT))
				
	def importFile(self, fileName):
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_BAR), 'File')
		Util().activateItem(self.objName(DesktopConst.textEditor.MENU_FILE), 'Import')
		Util().setText(self.objName(DesktopConst.textEditor.IMPORT_FILES_TABLE), fileName)
		Util().clickButton(self.objName(DesktopConst.textEditor.IMPORT_FILE_OPEN_BUTT))
	
	def close(self):
		Util().clickButton(self.objName(DesktopConst.textEditor.CLOSE_BUTT))
