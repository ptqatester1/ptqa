#############################################
#@author: Chris Allen
#@summary: Functions related to user profile
#############################################
from API.Android.Utility.Util import Util
from API.Android.UserProfile.UserProfileConst import UserProfileConst
from squish import *
import object

class UserProfile:
	def __init__(self):
		self.util = Util()
		pass
	
	def editName(self, p_name):
		self.util.setText(UserProfileConst.NAME, p_name)
		
	def editEmail(self, p_email):
		self.util.setText(UserProfileConst.EMAIL, p_email)
	
	def editUserInfo(self, p_userInfo):
		self.util.setText(UserProfileConst.ADDITIONAL_INFO, p_userInfo)
	
	def submit(self):
		self.waitForVisible()
		self.util.tap(UserProfileConst.SUBMIT_BUTTON)
	
	def waitForVisible(self):
		for i in range(15):
			try:
				if not waitForObject(UserProfileConst.NAME).visible:
					snooze(1)
					continue
				break
			except:
				snooze(1)
				continue
			
	def createNewUser(self, p_name, p_email = '', p_userInfo = ''):
		self.waitForVisible()
		self.editName(p_name)
		if p_email:
			self.editEmail(p_email)
		if p_userInfo:
			self.editUserInfo(p_userInfo)
		self.submit()