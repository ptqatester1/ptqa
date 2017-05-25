from API.Android.Scenario.ScenarioConst import ScenarioConst
from API.Android.Utility.Util import Util
from API.Android.Workspace.WorkspaceConst import WorkspaceConst
from squish import *
import test
import object

class EditScenario:
	def __init__(self):
		self.util = Util()
		
	def selectScenario(p_scenario):

		self.util.tap(ScenarioConst.SCENARIO_LIST)
		self.util.tap(p_scenario)

	def deleteScenario(self, p_scenario):
		if p_scenario == "":
			self.util.tap(ScenarioConst.DELETE_BUTTON)
		else:
			selectScenario(p_scenario)
			self.util.tap(ScenarioConst.DELETE_BUTTON)
		snooze(1)

	def createScenario(self):
		self.util.tap(ScenarioConst.NEW_BUTTON)
		snooze(1)