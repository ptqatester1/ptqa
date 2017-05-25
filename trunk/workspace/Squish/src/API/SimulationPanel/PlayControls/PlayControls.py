#**************************************************************************
#@author: Tuan Hoang
#@summary: PlayControls handles Play Controls in Simulation Panel
#**************************************************************************
from API.SquishSyntax import SquishSyntax
from API.SimulationPanel.PlayControls.PlayControlsConst import PlayControlsConst
from squish import *
import object

class PlayControls:
    #@summary: A null function to initialize SquishSyntax
    def __init__(self):
        self.sq = SquishSyntax()
        None
    
    def back(self, p_times = 1, **kwargs):
        snoozeFactor = 0.5
        if 'snooze' in kwargs:
            snoozeFactor = kwargs['snooze']
        for i in range(p_times):
            snooze(snoozeFactor)
            self.sq.clickButton(PlayControlsConst.BACK)
    
    def autoCapture(self):
        raise NotImplementedError
    
    def captureForward(self, p_times = 1, **kwargs):
        if 'snooze' in kwargs:
            snoozeFactor = kwargs['snooze']
        else:
            snoozeFactor = 0.5
        for i in range(p_times):
            self.sq.clickButton(PlayControlsConst.CAPTURE_FORWARD)
            snooze(snoozeFactor)
            if object.exists(PlayControlsConst.BUFFER_FULL_WINDOW):
                self.sq.clickButton(PlayControlsConst.BUFFER_FULL_DIALOG_VIEW_PREVIOUS_EVENTS)
                break