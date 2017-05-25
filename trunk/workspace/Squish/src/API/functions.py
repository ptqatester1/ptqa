#############################################################
#															#
#Chris Allen												#
#This file is for functions that are useful and common but 	#
#not necessarily part of squish interactions				#
#															#
#############################################################

from __builtin__ import int as integer
from __builtin__ import type as typeOf
import object
import squish
from squish import *
import inspect
import re
import os
import test
from API.Utility.UtilConst import PACKETTRACER

def getType(p_object):
	return typeOf(p_object)

#@Summary: This function is to check if the object is of a certain type
#@param p_object: The object to be checked
#@param p_type: The expected type
def isType(p_object, p_type):
	return p_type in str(typeOf(p_object))

def toInt(num):
	return integer(num)

#Takes a linux style file path / separators. Returns either that path or
#the windows style path separator if on windows
def pathFromOS(p_path):
	if os.name == 'posix':
		return p_path
	else:
		return p_path.replace('/', '\\')

def trace(p_filename = None):
	'''If filename is specified it will only show the trace for that file.
	function, line, filename'''
	currentFrame = inspect.currentframe()
	outerFrames = inspect.getouterframes(currentFrame)
	messages = []
	for currFrame in outerFrames:
		(frame,
		filename,
		line_number,
		function_name,
		lines,
		index) = currFrame		
				
		shortenedFilename = filename[filename.find('src'):]#Filename form ../API/ on
		filepath = '..' + os.path.sep + os.path.join(*(os.path.split(shortenedFilename)[:-1]))
		newfilename = os.path.split(shortenedFilename)[-1]
		
		msg = ('Line: ' + str(line_number) + ' function: ' + function_name +
			' of file ' + newfilename + ' at ' + filepath)
		if p_filename:
			if p_filename in newfilename:
				messages.append(msg)
		else:
			messages.append(msg)
	if len(messages) < 1:
		raise ValueError('The given filename was not found')
	return '\n'.join(messages)

#Simple conditional check
#Pass any condition to evaluate
#Example: check(not 1 > 2, 'checking if 1 is not great than 2') 
def check(condition, msg = ''):
	if condition:
		test.passes('Pass: ' + msg, trace('test.py'))
		return True
	else:
		test.fail('Fail: ' + msg, trace('test.py'))
		return False
		
#Modified from sre module
#Added standard chars because normal re.escape does anything not alpha-numeric
#If functionality of regular re.escape is required
def escapeRegex(pattern, standardChars = '(){}[].\\*^$+'):
	"Escape all non-alphanumeric characters in pattern."
	s = list(pattern)
	for i in range(len(pattern)):
		c = pattern[i]
		if not standardChars:
			if not ("a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9"):
				if c == "\000":
					s[i] = "\\000"
				else:
					s[i] = "\\" + c
		else:
			if c in standardChars:
				if c == "\000":
					s[i] = "\\000"
				else:
					s[i] = "\\" + c
	#import test
	#test.log(pattern[:0].join(s))
	return pattern[:0].join(s)

class Aut:
	def __init__(self):
		None
		
	def obj_walker(self, parent, buttonsText, max_depth = 10):
		'''Walk through all the child objects and look for a close button'''
		for child in object.children(parent):
			if 'text' in object.properties(child):
				for buttonText in buttonsText:
					if  buttonText in str(child.text):
						#import test
						#test.log(child.text)
						squish.mouseClick(child, 10, 10, Qt.NoModifier, Qt.LeftButton)
						return
			if max_depth > 0:
				self.obj_walker(child, buttonsText, max_depth - 1)
			else:
				return False
			
	def checkForModalWindows(self, attemptToCloseWithQtMethod=True, specifiedButton=None):	
		if specifiedButton:
			buttonsText = [specifiedButton]
		else:
			buttonsText = ['No', 'Cancel', 'Yes', 'OK', 'Ok']
		topLevelObjects = object.topLevelObjects()#All PT objects
		#hasModalWindows = [obj.modal for obj in topLevelObjects if 'modal' in object.properties(obj) and obj.modal == True]
		for obj in topLevelObjects:
			if 'modal' in object.properties(obj):
				if obj.modal and obj.visible:
					try:
						if attemptToCloseWithQtMethod:
							closeResult = obj.close()#Attempt to close via qt method
						else:
							closeResult = False
					except Exception, e:
						self.obj_walker(obj, buttonsText)#If close failed and threw an exception
					if not closeResult == True:
						self.obj_walker(obj, buttonsText)#If close failed with False return value
								
	def closePt(self):
		ptWindow = waitForObject(":CAppWindowBase")
		sendEvent('QCloseEvent', ptWindow)
		self.checkForModalWindows(attemptToCloseWithQtMethod=False, specifiedButton='No')

	def killAut(self):
		self.checkForModalWindows()
		if object.exists(':CAppWindowBase.CBaseCheckAnswerPage.m_closeButton'):
			Util().click(findObject(':CAppWindowBase.CBaseCheckAnswerPage.m_closeButton'))
		if object.exists(':Activity_Wizard'):
			awExit().exit()
		self.closePt()
		
	def startAut(self):
		aut = startApplication(PACKETTRACER)
		setApplicationContext(aut)
		return aut

class Clipboard:
	def __init__(self):
		pass
	
	def get(self):
		from squish import *
		return QApplication.clipboard()
		
	def getText(self):
		return str(self.get().text())
	
	def setText(self, p_text):
		self.get().setText(p_text)
	
	def clear(self):
		self.get().clear()
		
def pageLoadDecorator(webviewName):
	from API.SquishSyntax import SquishSyntax
	def customInteraction(func):	
		def waitForPage(*args, **kwargs):
			for i in range(20):
				if waitForObject(webviewName).evalJS("document.readyState") == "complete":
					SquishSyntax().clearCache(webviewName)
					return func(*args, **kwargs)
				snooze(1)
		return waitForPage
	return customInteraction

#RecursionBreakout is a custom exception used soley for breaking recursion
class RecursionBreakout(Exception):
	pass
	
class NotFoundException(Exception):
	pass

class WebviewTagFind:
	def __init__(self):
		self.childValue = []
	#Used for finding unamed html objects, but with higher precision. This uses a properties dictionary
	#which allows the caller to select a list of properties that must match before the object is returned
	#properties takes a dictionary with key being the property and val being the value
	def findTagWithProperties(self, startTag, searchTag, propertyDict):
		if typeOf('') == typeOf(startTag):#Check if string otherwise assume its an object
			startTag = findObject(startTag)
		try:
			self.getTagObject(startTag, searchTag, propertyDict)
		except RecursionBreakout, e:
			pass
		if not self.childValue:
			raise NotFoundException()
		return self.childValue[0]
	
	def getTagObject(self, startTag, searchTag, propertyDict):
		try:
			for i in range(startTag.numChildren):#possibly numchildren -1
				currentTag = startTag.firstChild()
				bCorrectTag = self.checkIfCorrectTag(currentTag, searchTag, propertyDict)
				if bCorrectTag:
					self.childValue.append(currentTag)
					raise RecursionBreakout('Leaving recursion')
				else:
					self.getTagObject(currentTag, searchTag, propertyDict)
				currentTag = startTag.nextSibling()
				bCorrectTag = self.checkIfCorrectTag(currentTag, searchTag, propertyDict)
				if bCorrectTag:
					self.childValue.append(currentTag)
					raise RecursionBreakout('Leaving recursion')
				else:
					self.getTagObject(currentTag, searchTag, propertyDict)
				
		except RecursionBreakout, e:
			raise RecursionBreakout(e)
	
	
	def checkIfCorrectTag(self, currTag, searchTag, propertyDict):
		properties = object.properties(currTag)
		foundItems = []
		try:
			if properties and properties['tagName'] == searchTag:
				for k,v in propertyDict.iteritems():
					foundItems.append(re.search(v, str(properties[k])))#Append the result of comparing the value of properties with a key of k to v
				if not False in foundItems and not None in foundItems:
					return True
				else:
					return False
			else:
				return False
		except AttributeError, e:
			return False

#WebviewTagFind2 is a different implementation of the same concept.
#The reason for it is because the first one doesn't work with certain webviews and this with others
class WebviewTagFind2:
	def __init__(self):
		self.childValue = []
		
	def findTagWithProperties(self, startTag, searchTag, propertyDict):
		if getType('') == getType(startTag): #Check if string otherwise assume its an object
			startTag = findObject(startTag)
		try:
			self.getTag(startTag, searchTag, propertyDict)
		except RecursionBreakout, e:
			pass
		if not self.childValue:
			searchTerms = '\n'.join([str(k) + ':' + str(v) for k, v in propertyDict.items()])
			raise NotFoundException('Unable to find value searched for ' + searchTag + ' ' + searchTerms)
		if len(self.childValue) > 1:
			test.log(str(self.childValue))
		return self.childValue[0]
	
	def getTag(self, startTag, searchTag, propertyDict):
		children = object.children(startTag)
		for child in children:
			properties = object.properties(child)
			try:
				foundItems = []
				if properties['tagName'] == searchTag:
					for k,v in propertyDict.iteritems():
						foundItems.append(re.search(v, str(properties[k])))#Append the result of comparing the value of properties with a key of k to v
					if not False in foundItems and not None in foundItems:
						self.childValue.append(child)
						raise RecursionBreakout('Breaking out of recursion')
					else:
						if child.numChildren > 0:
							self.getTag(child, searchTag, propertyDict)
				else:
					if child.numChildren > 0:
						self.getTag(child, searchTag, propertyDict)
			except AttributeError, e:
				if child.numChildren > 0:
					self.getTag(child, searchTag, propertyDict)
			except RecursionBreakout, e:
				raise RecursionBreakout(e)
	
	def findTagWithID(self, startTag, id):
		if getType('') == getType(startTag):#Check if string otherwise assume its an object
			startTag = findObject(startTag)
		try:
			self.getTagWithID(startTag, id)
		except RecursionBreakout, e:
			pass
		if not self.childValue:
			import test
			test.log(trace('test.py'))
			searchTerms = id#'\n'.join([str(k) + ':' + str(v) for k, v in propertyDict.items()])
			raise NotFoundException('Unable to find value searched for ' + searchTerms)
		return self.childValue[0]
	
	def getTagWithID(self, startTag, id):
		children = object.children(startTag)
		for child in children:
			properties = object.properties(child)
			try:
				foundItems = []
# 				import test
# 				currID = str(properties['id'])
# 				if currID != '':
# 					test.log(currID)
				if properties['id'] == id:
					self.childValue.append(child)
					raise RecursionBreakout('Breaking out of recursion')
				else:
					if child.numChildren > 0:
						self.getTagWithID(child, id)
			except AttributeError, e:
				if child.numChildren > 0:
					self.getTagWithID(child, id)
			except RecursionBreakout, e:
				raise RecursionBreakout(e)
