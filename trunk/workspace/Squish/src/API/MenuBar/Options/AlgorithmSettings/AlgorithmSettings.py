#**************************************************************************
#@author: Tuan Hoang
#@summary: Algorithm Settings dialog
#**************************************************************************
from API.MenuBar.Options.AlgorithmSettings.AlgorithmSettingsConst import AlgorithmSettingsConst
from API.SquishSyntax import SquishSyntax

class AlgorithmSettings(SquishSyntax):
    def setHalfOpenSessionMult(self, p_value):
        self.setText(AlgorithmSettingsConst.HALF_OPEN_SESSION_MULTIPLIER, p_value)

    def setMaxNumConns(self, p_value):
        self.setText(AlgorithmSettingsConst.MAXIMUM_NUMBER_OF_CONNECTIONS, p_value)

    def setMaxNumOpenSessions(self, p_value):
        self.setText(AlgorithmSettingsConst.MAXIMUM_NUMBER_OF_OPENED_SESSIONS, p_value)

    def setStormCtrlMult(self, p_value):
        self.setText(AlgorithmSettingsConst.STORM_CONTROL_MULTIPLIER, p_value)