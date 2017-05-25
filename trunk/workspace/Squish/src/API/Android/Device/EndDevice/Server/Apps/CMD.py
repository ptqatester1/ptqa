##############################################################################
##Author: AbbasH
#@summary: CommandPrompt handles activities on the CommandPrompt window of PC
##############################################################################
from API.Android.Device.EndDevice.Server import ServerConst
from API.Android.Device.DeviceBase import DeviceBase
from squish import *

class CommandPrompt(DeviceBase): 
    def __init__(self):
        self.squishName = ""
    
    #@summary: update the actual name of object that squish uses to reference
    #@param p_squishName: display name of the device   
    def updateName(self, p_squishName):
        self.squishName = p_squishName

    #@summary: type commands into command prompt
    #@param p_text: command
    def setCliText(self, p_text):
		if textCheckpoint((ServerConst.CommandPrompt.KEYBOARD).visible, false):
			self.tap_x_y(ServerConst.CommandPrompt.KEYBOARD, 1, 1)
        self.setConsoleText(ServerConst.CommandPrompt.CONSOLE_TEXT, p_text)

    #@summary: create text checkpoint
    #@param p_text: command
    #@param p_occurrenceNum: number of times the search text occurs
    def textCheckPoint(self, p_text, p_occurrenceNum = -1):
        consoleText = str(findObject(ServerConst.CommandPrompt.CONSOLE_TEXT).plainText)
        super(DeviceBase, self).textCheckPoint(consoleText, p_text, p_occurrenceNum)