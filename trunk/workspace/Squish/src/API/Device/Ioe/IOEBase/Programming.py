#*******************************************************#
#@Author: Chris Allen                                   #
#*******************************************************#

from API.Device.Ioe.IoeBaseConst import IoeBaseConst
from API.Device.DeviceBase.DeviceBase import SquishObjectName
from API.Device.EndDevice.PC.PC import PC
from API.SquishSyntax import SquishSyntax
from API.Device.DeviceBase import DeviceBase
from API.functions import WebviewTagFind
from API.functions import WebviewTagFind2 as TF
from API.Utility.Util import Util
from squish import *
import object
import test
import re

def qtClickSelect(p_obj):
	p_obj.setProperty('selected', True)
	p_obj.click()

def qtDoubleClickSelect(p_obj):
	p_obj.setProperty('selected', True)
	p_obj.doubleClick()
	
def qtClick(p_obj):
	findObject(p_obj).click()
	
class CreateProject(SquishObjectName):
	def __init__(self):
		self.squishName = ''
		self.util = Util()
		
	def updateName(self, p_squishName):
		self.squishName = p_squishName
	
	def setScriptName(self, p_name):
		webview = findObject(self.squishName + IoeBaseConst.programming.PROGRAMMING_WEBVIEW[:-1])
		webview.evaluateJavaScript('newName.value = "' + p_name + '"')
		None
	
	def selectType(self, p_type = ' '):
		if not p_type == ' ':
			webview = self.squishName + IoeBaseConst.programming.PROGRAMMING_WEBVIEW[:-1]
			typeSelection = webview + '.' + 'newProjectType'
			typeSelectionObject = findObject(typeSelection)
			options = object.children(typeSelectionObject)
			typeSelectionObject.click()
			snooze(2)
			for i, item in enumerate(options):
				try:
					if p_type in item.text:
						typeSelectionObject.setSelectedIndex(i)
						return
				except AttributeError, e:
					pass
				except Exception, e:
					raise (e)
			raise (p_type + ' Not found in options')
		None
	
	def create(self):
		webview = self.squishName + IoeBaseConst.programming.PROGRAMMING_WEBVIEW[:-1]
		nameDialog = webview + '.' + 'nameDialog'
		parentObject = object.parent(findObject(nameDialog))
		createButton = WebviewTagFind().findTagWithProperties(parentObject, 'BUTTON', {'innerText':'Create'})
		createButton.click()
		
		None
	
	def cancel(self):
		webview = self.squishName + IoeBaseConst.programming.PROGRAMMING_WEBVIEW[:-1]
		nameDialog = webview + '.' + 'nameDialog'
		parentObject = object.parent(findObject(nameDialog))
		cancelButton = findTagWithProperties(parentObject, 'BUTTON', {'innderText':'Cancel'})
		cancelButton.click()
		None

class Programming(SquishObjectName):
	def __init__(self, parent):
		self.squishName = parent.squishName
		self.qtClick = qtClick
		self.qtClickSelect = qtClickSelect
		self.qtDoubleClickSelect = qtDoubleClickSelect
		self.createProject = CreateProject()
		self.util = Util()
	
	def updateName(self, p_squishName):
		self.squishName = p_squishName
		self.createProject.updateName(self.squishName)
	
	def new(self):
		self.util.click(IoeBaseConst.programming.ADD_BUTTON)
		
	def newScript(self, p_scriptName, p_type = None, p_createCancel = 'Create'):
		self.new()
		snooze(1)
		self.createProject.setScriptName(p_scriptName)
		snooze(1)
		if p_type:
			self.createProject.selectType(p_type)
		if p_createCancel.lower() == 'create':
			self.createProject.create()
		else:
			self.createProject.cancel()
		
	def selectScript(self, p_scriptName, *p_moreScripts, **args):
		'''
		If called more than once in a row there will need to be a snooze in between
		in order to give the script list time to update
		p_moreScripts is to do multiple scripts with one call
		'''
		selectOnly = False
		if len(args.keys()) > 0:
			if 'selectOnly' in args:
				selectOnly = args['selectOnly']
		itemsToClick = []
		itemsToClick.append(p_scriptName)
		for item in p_moreScripts:
			itemsToClick.append(item)
		for item in itemsToClick:
			scriptList = findObject(self.squishName + IoeBaseConst.programming.SCRIPT_LIST)
			script = None
			for i in range(scriptList.numChildren):
				try:
					if item in scriptList.optionAt(i).text:
						script = scriptList.optionAt(i)
						break
				except AttributeError, e:
					print('Attribute error')
				except Exception, e:
					raise(e)
			if script and selectOnly and item == itemsToClick[-1]:
				self.qtClickSelect(script)
			elif script:
				self.qtDoubleClickSelect(script)
			else:
				raise('Could not find the script with that name')
			snooze(2)
		None
	
	def rename(self, p_newName):
		self.util.click(self.squishName + IoeBaseConst.programming.RENAME_BUTTON)
		snooze(1)
		webview = findObject(self.squishName + IoeBaseConst.programming.PROGRAMMING_WEBVIEW[:-1])
		renameBox = TF().findTagWithID(webview, 'newName')
		renameBox.setValue(p_newName)
		webview.evalJS('nameDialogRename.click()')
		None
		
	
	def removeScript(self, *p_scriptName):
		if p_scriptName:
			self.selectScript(*p_scriptName)
		webview = findObject(self.squishName + IoeBaseConst.programming.PROGRAMMING_WEBVIEW[:-1])
		deleteButton = TF().findTagWithID(webview, 'remove')
		deleteButton.click()
		dialog = TF().findTagWithID(webview, 'confirmDialog')
		yesButton = ':JavaScript Confirm - .qt_msgbox_buttonbox.Yes'
		self.util.click(yesButton)
		#yesButton = TF().findTagWithProperties(dialog, 'BUTTON', {'simplifiedInnerText':'Yes'})
		#yesButton.click()
		
	def run(self):
		for i in range(10):
			if findObject(self.objName(self.squishName + IoeBaseConst.programming.RUN_BUTTON)).innerText == 'Run':
				self.util.click(self.objName(self.squishName + IoeBaseConst.programming.RUN_BUTTON))
			else:
				break
			snooze(1)
		None
	
	def stop(self):
		for i in range(10):
			if findObject(self.objName(self.squishName + IoeBaseConst.programming.RUN_BUTTON)).innerText == 'Stop':
				self.util.click(self.objName(self.squishName + IoeBaseConst.programming.RUN_BUTTON))
			else:
				break
			snooze(1)
		None
	
	@property
	def scriptState(self):
		return str(findObject(self.squishName + IoeBaseConst.programming.RUN_BUTTON).innerText)
	
	def reload(self):
		for i in range(10):
			if findObject(self.squishName + IoeBaseConst.programming.RELOAD_BUTTON).innerText == 'Reload':
				self.util.click(self.squishName + IoeBaseConst.programming.RELOAD_BUTTON)
			else:
				break
			snooze(1)
		None
	
	def zoomIn(self):
		for i in range(10):
			if findObject(self.squishName + IoeBaseConst.programming.ZOOM_IN_BUTTON).innerText == '+':
				self.util.click(self.squishName + IoeBaseConst.programming.ZOOM_IN_BUTTON)
			else:
				break
			snooze(1)
		
		
	def clearOutputs(self):
		for i in range(5):
			self.util.click(self.objName(self.squishName + IoeBaseConst.programming.CLEAR_OUTPUTS_BUTTON))
		None
	
	def open(self, p_file):
		raise (Exception('Not implemented yet'))
	
	def getConsoleOutput(self):
		return findObject(self.squishName + IoeBaseConst.programming.OUTPUT_TEXT_AREA).value
		None
	
	def textCheckpoint(self, p_baseText, p_searchText, p_occurrenceNum = -1, **args):
		'''
		Pass a string into here for the base text.
		p_baseText is the text that will be searched
		p_searchText is the string being searched for
		p_occurrenceNum is the number of times it is expected
		'''
		if p_baseText == None:
			p_baseText = str(self.getConsoleOutput())
		Util().checkText(p_baseText, p_searchText, p_occurrenceNum, **args)
	
	def editScriptText(self, p_scriptText):
		webview = findObject(self.squishName + IoeBaseConst.programming.PROGRAMMING_WEBVIEW[:-1])
		newText = re.sub('"', '\\"', p_scriptText)
		newText = re.sub("'", "\\'", newText)
		newText = re.sub('\\n', '\\\\n', newText)
		webview.evaluateJavaScript('textEditor.setValue("' + newText + '")')
	
	def getScriptText(self):
		return str(findObject(self.squishName + IoeBaseConst.programming.PROGRAMMING_WEBVIEW[:-1]).evaluateJavaScript("textEditor.getValue()"))
	
	def insertAfter(self, p_stringToFind, p_stringToAdd):
		string = self.stripQuotedNewlines(self.getScriptText())
		startIndex = string.index(p_stringToFind) + len(p_stringToFind)
		newString = string[:startIndex] + p_stringToAdd + string[startIndex:]
		self.editScriptText(newString)
		
	def insertTextAtLine(self, p_lineNumber, p_text):
		currentScriptText = self.getScriptText()
		currentScriptText = self.stripQuotedNewlines(currentScriptText)
		s = ''
		splitText = currentScriptText.splitlines()
		for i, line in enumerate(splitText):
			if p_lineNumber - 1 == i:
				s += p_text + '\n'
			s += line + '\n'
		self.editScriptText(s)
		None
	
	def replaceTextAtLine(self, p_lineNumber, p_text):
		currentScriptText = self.getScriptText()
		currentScriptText = self.stripQuotedNewlines(currentScriptText)
		s = ''
		splitText = currentScriptText.splitlines()
		for i, line in enumerate(splitText):
			if p_lineNumber - 1 == i:
				s += p_text + '\n'
			else:
				s += line + '\n'
		self.editScriptText(s)
		None
	
	def removeTextAtLines(self, *p_lineNumbers):
		currentScriptText = self.getScriptText()
		currentScriptText = self.stripQuotedNewlines(currentScriptText)
		s = ''
		splitText = currentScriptText.splitlines()
		for i, line in enumerate(splitText):
			if i+1 in p_lineNumbers:
				continue
			s += line + '\n'
		self.editScriptText(s)
		None

	def stripQuotedNewlines(self, text):
		return re.sub('\\\\n', '\\\\\\\\n', text)
	
	def copy(self):
		for i in range(10):
			if findObject(self.squishName + IoeBaseConst.programming.COPY_BUTTON).innerText == 'Copy':
				self.util.click(self.squishName + IoeBaseConst.programming.COPY_BUTTON)
			else:
				break
			snooze(1)
		None
	
	def paste(self):
		for i in range(10):
			if findObject(self.squishName + IoeBaseConst.programming.PASTE_BUTTON).innerText == 'Paste':
				self.util.click(self.squishName + IoeBaseConst.programming.PASTE_BUTTON)
				break
			snooze(1)
		None				

	def getTextEditorObject(self):
		webview = findObject(self.squishName + IoeBaseConst.programming.PROGRAMMING_WEBVIEW[:-1])
		textEditor = TF().findTagWithID(webview, 'textEditor')
		return textEditor
	
	def hasErrorMsg(self):
		None