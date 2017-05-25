from API.Utility.Util import Util
from exceptions import ValueError
from exceptions import UserWarning
from API.ProjectManager.ProjectManagerConst import ProjectManagerConst
from API.MenuBar.Tools.Tools import Tools
from API.MenuBar.Tools.ToolsConst import ToolsConst
import test
from squish import *
import object
from API.functions import trace

class ProjectManager:
	def __init__(self):
		self.util = Util()
	
	def goToScriptManager(self):
		Tools().selectToolsItem('Script Project Manager ...')

	def selectScriptDevice(self, p_deviceName, p_projectName = None):
		deviceRowObj = self.getRowObjects(p_deviceName, p_projectName)[0]
		self.util.click(deviceRowObj)
		
	def selectScriptProject(self, p_projectName, p_deviceName = None):
		projectRowObj = self.getRowObjects(p_deviceName, p_projectName)[1]
		self.util.click(projectRowObj)
	
	def getRowObjects(self, p_deviceName = None, p_projectName = None, p_rowNumber = None):
		if not (p_rowNumber or p_deviceName or p_projectName):
			raise ValueError('Either row number, device name, or project name must be provided')
		if p_rowNumber:
			row = p_rowNumber
		else:
			row = self.getRowNumberOf(p_deviceName, p_projectName)
	
		column0 = findObject(ProjectManagerConst.TREEVIEW + '.item_' + str(row) + '/0')
		column1 = findObject(ProjectManagerConst.TREEVIEW + '.item_' + str(row) + '/1')
		column2 = findObject(ProjectManagerConst.TREEVIEW + '.item_' + str(row) + '/2')
		return [column0, column1, column2]
	
	def getRowInformation(self, p_deviceName = None, p_projectName = None, p_rowNumber = None):
		if not (p_rowNumber or p_deviceName or p_projectName):
			raise ValueError('Either row number, device name, or project name must be provided')
		rowObjs = self.getRowObjects(p_deviceName, p_projectName, p_rowNumber)
		return [r.text for r in rowObjs]#returns a list of the text in each column
	
	def getRowNumberOf(self, p_deviceName = None, p_projectName = None):
		if not (p_deviceName or p_projectName):
			raise ValueError('Either device name or project name must be provided')
		tree = self.getTree()
		for i in range(tree.topLevelItemCount):
			column0 = findObject(ProjectManagerConst.TREEVIEW + '.item_' + str(i) + '/0')
			column1 = findObject(ProjectManagerConst.TREEVIEW + '.item_' + str(i) + '/1')
			if p_deviceName and p_projectName:
				if (p_deviceName in column0.text and p_projectName in column1.text):
					return i
			elif p_deviceName:
				if (p_deviceName in column0.text):
					return i
			elif p_projectName:
				if (p_projectName in column1.text):
					return i
		raise UserWarning('Unable to find the script or device searched for possibly ' +
						'because the tree has not updated yet. Try putting a short snooze ' +
						'and check your spelling')
				
	def getTree(self):
		return findObject(ProjectManagerConst.TREEVIEW)
	
	def start(self):
		button = findObject(ProjectManagerConst.START_STOP_BUTTON)
		if button.text == 'Run':
			self.toggleStartStop()
			return True
		else:
			return False
	
	def stop(self):
		button = findObject(ProjectManagerConst.START_STOP_BUTTON)
		if button.text == 'Stop':
			self.toggleStartStop()
			return True
		else:
			return False
	
	def toggleStartStop(self):
		self.util.click(ProjectManagerConst.START_STOP_BUTTON)
		
	def startProjectAtDevice(self, p_projectName, p_deviceName):
		'''Returns true or false depending if the script was started(True) or already running(False)'''
		self.selectScriptDevice(p_deviceName, p_projectName)
		started = self.start()
		return started
	
	def stopProjectAtDevice(self, p_projectName, p_deviceName):
		'''Returns true or false depending if the script was stopped(True) or already stopped(False)'''
		self.selectScriptDevice(p_deviceName, p_projectName)
		stopped = self.stop()
		return stopped

	def isScripttRuning(self, p_projectName, p_deviceName):
		self.selectScriptDevice(p_deviceName, p_projectName)
		button = findObject(ProjectManagerConst.START_STOP_BUTTON)
		if button.text == 'Run':
			return False
		else:
			return True
	
	def checkIsScriptRunning(self, p_projectName, p_deviceName, expectRunning = True):
		state = self.isScripttRuning(p_projectName, p_deviceName)
		if not expectRunning:
			state = not state
		if state:
			test.passes('Pass:', 'Script is in expected state')
		else:
			test.fail('Fail:', 'Script is not in expected state\n' + trace('test.py'))
			
	def checkCpuUsageBelow(self, p_maxCpu, p_projectName, p_deviceName):
		actualCpu = self.getRowInformation(p_deviceName, p_projectName)[2]
		if actualCpu == '--':
			actualCpu = -1#Used for when the script is stopped
		if float(actualCpu[:-1]) < float(p_maxCpu):
			test.passes('Pass:', 'CPU Usage below ' + str(p_maxCpu))
		else:
			test.fail('Fail:', 'CPU Usage is not below ' + str(p_maxCpu), trace('test.py'))
	
	def getRowCount(self):
		return self.getTree().topLevelItemCount
	
	def close(self):
		self.util.close(ProjectManagerConst.WINDOW)
