##################################################
#@author: Chris Allen
#@summary: This includes squish specific syntax
##################################################

from squish import *
import inspect, os, time
import test
import inspect
import re
from API.Android.Utility.UtilConst import KeyboardConst


class SquishSyntax(object):
	#@summary: Tap on an object
	#@param p_obj: Object name
	def tap(self, p_obj): 
		try:
			obj = waitForObject(p_obj)
		except:
			obj = waitForObject(p_obj + "_2")
		tapObject(obj)
		
	def tapMenuItem(self, p_item):
		waitForObject(p_item)
		tapMenuItem(p_item)
	#@summary: Tap an object at a certain x,y coordinate
	#@param p_obj: Object to be clicked
	#@param p_x: X value
	#@param p_y: Y value
	def tap_x_y(self, p_obj, p_x, p_y):
		waitForObject(p_obj)
		tapObject(p_obj, p_x, p_y)
		
	def doubleTap(self, p_obj):
		waitForObject(p_obj)
		doubleTap(obj)
		
	def doubleTap_x_y(self, p_obj, p_x, p_y):
		waitForObject(p_obj)
		doubleTap(p_obj, p_x, p_y)
		
	def goBack(self):
		pass

	def saveScreenshot(self, filename = None, path = 'P:/AndroidScreenshots/'):
		#save date in format dd-mm-yy
		date = '-'.join(time.strftime("%d/%m/%Y").split('/'))
		if filename:
			#if filename is provided us date + filename
			name = filename + '-' + date
		else:
			#Otherwise get the file path of the script and save it to directory
			directory = inspect.stack()[-1][1]#os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
			#split directory at each / and get the second to last value
			#which is the folder containing test.py
			name = directory.split('/')[-2] + '-' + date
		if path == 'P:/AndroidScreenshots/':
			try:
				#try to access path on P drive
				os.listdir(path)
			except:
				#if P is not accessible add to local ptqa folder under src/AndroidScreenshots/
				dList = directory.split('/')
				path = '/'.join(dList[:dList.index('Squish')]) + '/AndroidScreenshots/'
				#raise('unable to access P:')
		#Append name and extension to path
		fullname = path + name + '.png'
		test.log(fullname)
		saveDesktopScreenshot(fullname)

	
	#@summary: This function taps by pressing 2s on the specified object
	#@param p_obj: Object to be pressed
	def longPress(self, p_obj):
		waitForObject(p_obj)
		longPress(p_obj)
	
	#@summary: This function taps by pressing 2s on the specified object at the x,y coordinates
	#@param p_obj: Object to be pressed
	#@param p_x: X value
	#@param p_y: Y value
	def longPress_x_y(self, p_obj, p_x, p_y):
		waitForObject(p_obj)
		longPress(p_obj, p_x, p_y)
	
	#@summary: openMenu(objectOrName);
	#This function taps the Android menu button. The specified objectOrName can refer to any object that is
	#visible, though Squish will record the object having the input focus.
	#@param p_obj: Menu Object
	def openMenu(self, p_obj):
		waitForObject(p_obj)
		openMenu(p_obj)

	def tapMenuItem(self, p_item):
		waitForObject(p_obj)
		tapMenuItem(p_item)
	
	def touchAndDrag(self, p_obj, p_x1, p_y1, p_x2, p_y2):
		waitForObject(p_obj)
		touchAndDrag(p_obj, p_x1, p_y1, p_x2, p_y2)
	
	#@summary: Add the text to the current text
	#@param p_obj: Object that the text will be added to
	#@param p_text: The text that will be added
	def typeText(self, p_obj, p_text):
		#from API.Android.Utility.UtilConst import KeyboardConst
		self.tap(waitForObject(p_obj))
		type(KeyboardConst.ANDROID_KEYBOARD, p_text)
		
	def type(self, p_text):
		#from API.Android.Utility.UtilConst import KeyboardConst
		type(KeyboardConst.ANDROID_KEYBOARD, p_text)
		
	def setTextValue(self, p_obj, p_text):
		setText(waitForObject(p_obj), p_text)
	
	def typeTextSE(self, p_obj, p_text):
		waitForObject(p_obj)
		type(KeyboardConst.ANDROID_KEYBOARD, p_text)
		
	#@summary: The textCheckPoint function is used to check if the search text is found inside a string
	#@param p_consoleText: The string that will be searched
	#@param p_searchText: The string that is being searched for
	#@param p_occurrenceNum: The number of times the string is expected
	def textCheckPoint(self, p_consoleText, p_searchText, p_occurrenceNum = -1):
		#test.log(str(p_consoleText) + '\t\t' + str(p_searchText))
		if len(p_searchText) == 0 and not len(p_consoleText) == 0:
			test.fail('Failed ', 'Empty text was not found')
			self.getLineNumForTextCheckPoint()
			return False
		if (p_occurrenceNum == -1):
			if (re.search(p_searchText, p_consoleText)):
				test.passes("Passed", p_searchText + " found")
				return True
			else:
				test.fail("Failed", p_searchText + " was not found")
				self.getLineNumForTextCheckPoint()
				return False
		else:
			print re.findall(p_searchText, p_consoleText)
			if len(re.findall(p_searchText, p_consoleText)) == p_occurrenceNum:
				test.passes("Passed", p_searchText + " found " + str(p_occurrenceNum) + " times")
				return True
			else:
				test.fail("Failed", p_searchText + " was not found " + str(p_occurrenceNum) + " times")
				self.getLineNumForTextCheckPoint()
				return False
	
	#@summary: The function below is used for the textCheckPoint function in order to return the line # if the textCheckPoint fails
	def getLineNumForTextCheckPoint(self):
		##Below is used to report the line number of where the textCheckPoint is called from ##
		##Get the items on the stack    
		callframe = inspect.stack()
		##Itterate through the stack
		for stackItem in callframe:
			##Set frame = to the frame object within the stack object
			frame = stackItem[0]
			##Once frame is set info will be set to the return of inspect.getframeinfo(frame) which returns a tuple of relevant information
			info = inspect.getframeinfo(frame)
			##Check that the filename in info is equal to test.py so that it only returns the line number of
			##test.py that it was called from
			if("test.py" in str(info[0])):
				##Report the line number and filename
				test.log("failed at line " +  str(info[1]) + " of " + str(info[0]))
				break
	
	def containText(selfself, p_obj, p_searchText):
		if re.search(waitForObject(p_obj).text, consoleText):
			return True
		else:
			return False
		
	def move(self, p_objName, p_x1, p_y1, p_x2, p_y2):
		waitForObject(p_objName)
		touchAndDrag(p_obj, p_x1, p_y1, p_x2, p_y2)
		
	def comparePlainText(self, p_obj, p_text):
		test.compare(findObject(p_obj).plainText, p_text)
		
	def compareText(self, p_obj, p_text):
		test.compare(findObject(p_obj).text, p_text)
		
	def gesture(self, p_obj, p_gesture):
		waitForObject(p_obj)
		gesture(p_obj, readGesture(p_gesture))
