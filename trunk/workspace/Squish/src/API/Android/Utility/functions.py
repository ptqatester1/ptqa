########################################################################################################
#@author: Chris Allen
#@summary: This holds functions that need to be used by util and other classes that import util
########################################################################################################
from API.Android.SquishSyntax import SquishSyntax
from API.Android.Utility.UtilConst import *
from API.Android.Workspace.WorkspaceConst import LoginConst
from API.Android.Workspace.WorkspaceConst import NavigationBarConst
from API.Android.Workspace.WorkspaceConst import WorkspaceConst
from API.Android.ActionBar.ActionBarConst import ActionBarConst
from API.Android.ContextMenus.ContextMenusConst import DeviceContextMenu
from API.Android.ActionBar.File.SaveNetwork.SaveNetworkConst import SaveNetworkConst
from API.Android.ActionBar.File.LoadNetwork.LoadNetworkConst import LoadNetworkConst
from __builtin__ import type as objType
#from API.Android.ActionBar.File.LoadNetwork.LoadNetwork import LoadNetwork
from HTMLParser import HTMLParser
import test
import os
import object
from squish import *
import sys
import re
import csv
import operator
import imp
from API.Android.UserProfile.UserProfileConst import UserProfileConst

class functions:
	def __init__(self):
		pass
	
	#Used for finding unnamed html objects
	def findTag(self, startTag, searchTag, searchTagValue = ''):
		childValue = []
		if objType('') == objType(startTag):#Check if string otherwise assume its an object
			startTag = findObject(startTag)
		def getTag(startTag, searchTag, searchTagValue):
			children = object.children(startTag)
			for child in children:
				properties = object.properties(child)
				if 'tagName' in properties:
					if properties['tagName'] == searchTag:
						if searchTagValue:
							for key in properties:
								match = re.match(searchTagValue, str(properties[key]))
								if match:
									if str(match.group()) == str(properties[key]): 
										childValue.append(child)
										raise Exception('Breaking out of recursion')
										#return child
						else:
							childValue.append(child)
							raise Exception('Breaking out of recursion')
							#return child
				if child.numChildren > 0:
					getTag(child, searchTag, searchTagValue)
		try:
			getTag(startTag, searchTag, searchTagValue)
		except:
			pass
		if not childValue:
			raise Exception('Unable to find the value searched for')
		return childValue[0]
	
	class RecursionBreakout(Exception):
		pass
	#Also used for finding unamed html objects, but with higher precision. This uses a properties dictionary
	#which allows the caller to select a list of properties that must match before the object is returned
	#properties takes a dictionary with key being the property and val being the value
	def findTagWithProperties(self, startTag, searchTag, propertyDict):
		childValue = []
		if objType('') == objType(startTag):#Check if string otherwise assume its an object
			startTag = findObject(startTag)
		def getTag(startTag, searchTag, propertyDict):
			children = object.children(startTag)
			for child in children:
				properties = object.properties(child)
				try:
					foundItems = []
					if properties['tagName'] == searchTag:
						for k,v in propertyDict.iteritems():
							foundItems.append(re.search(v, str(properties[k])))#Append the result of comparing the value of properties with a key of k to v
						if not False in foundItems and not None in foundItems:
							childValue.append(child)
							raise self.RecursionBreakout('Breaking out of recursion')
					else:
						if child.numChildren > 0:
							getTag(child, searchTag, propertyDict)
				except AttributeError, e:
					if child.numChildren > 0:
						getTag(child, searchTag, propertyDict)
				except self.RecursionBreakout, e:
					raise self.RecursionBreakout(e)
				except Exception, e:
					raise Exception(e)
		try:
			getTag(startTag, searchTag, propertyDict)
		except self.RecursionBreakout, e:
			pass
		except Exception, e:
			raise Exception(e)
		if not childValue:
			raise Exception('Unable to find the value searched for')
		return childValue[0]

class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)
	
	def strip_tags(self, html):
		self.__init__()
		self.feed(html)
		return self.get_data()
	
class SuiteTesting:
	'''SuiteTesting class is used to test and entire suite at once without closing PT'''
	
	#@Purpose: Initialize the class
	#@param p_suite: the full path to the suite being tested
	#@param p_outfile: the full path to the file to print results to
	#@param p_os: The os being used ('Android', 'iOS')
	def __init__(self, p_suite, p_outfile, p_os):
		self.suite = p_suite
		self.os = p_os
		self.tests = []
		self.currentTest = ''
		self.modules = []
		self.exceptions = {}
		self.outfile = p_outfile
		
	#@purpose: To add __init__.py to any directories which may not have it.
	#This is necessary since python will not see the modules unless they have __init__.py
	def addInits(self):
		for r, d, f in os.walk(self.suite):
			if not '__init__.py' in d:
				fd = open(os.path.join(r, '__init__.py'), 'w')
				fd.close()
	
	#@purpose: get the tests that are inside the suite
	#Be sure to name the test running this class 'tst_groupTest'
	def getTests(self):
		for r, d, f in os.walk(self.suite):
			if 'test.py' in f and not 'grouptest' in r.lower():
				fullPath = os.path.abspath(r).split(os.path.sep)
				self.tests.append('.'.join(fullPath[fullPath.index('TestScript'):]))
				
	#@purpose: Map each test to a module import
	def createImports(self):
		
		for item in self.tests:
			exec 'from ' + item + ' import test as m'
			self.modules.append(m)
			del m #ensure no name conflicts

	#@purpose: This is where the tests are actually ran
	#Iterate over each module created in the createImports function
	#Try to run the main function for each module
	#If it runs successfully continue to the next one
	#else if there is a runtime error log the exception
	#	if android restart PT
	#	else (not sure what to do about iOS yet)
	#else log the exception
	def runTests(self):
		for module in self.modules:
			self.currentTest = module.__name__.split('.')[-2]
			try:
				module.main()
			except Exception, e:
				self.reset()
				self.exceptions[self.currentTest] = e
		
	#@purpose: Write the exceptions to a CSV file
	def writeOutput(self):
		sortedExceptions = sorted(self.exceptions.items(), key=operator.itemgetter(0))
		exceptionList = []
		header = ['Test', 'Result']
 		fd = open(self.outfile, 'wb')
		fd.write(','.join(header) + '\n')
		for item in sortedExceptions:
			fd.write(','.join([str(item[0]), str(item[1])]) + '\n')
		fd.close()
	
	def reset(self):
		obj = None
		exists = object.exists
		for i in range(240):
			if exists(UserProfileConst.SUBMIT_BUTTON) and findObject(UserProfileConst.SUBMIT_BUTTON).visible:
				tapObject(UserProfileConst.SUBMIT_BUTTON)
				snooze(5)
				obj = NavigationBarConst.WORKSPACE_BUTTON
			elif exists(NavigationBarConst.WORKSPACE_BUTTON) and findObject(NavigationBarConst.WORKSPACE_BUTTON).visible:
				obj = NavigationBarConst.WORKSPACE_BUTTON
			elif exists(SaveNetworkConst.CANCEL_BUTTON) and findObject(SaveNetworkConst.CANCEL_BUTTON).visible:
				obj = SaveNetworkConst.CANCEL_BUTTON
			elif exists(LoadNetworkConst.CANCEL_BUTTON) and findObject(LoadNetworkConst.CANCEL_BUTTON).visible:
				obj = LoadNetworkConst.CANCEL_BUTTON
			elif not obj:
				snooze(1)
			else:
				break
		tapObject(obj)
