from API.Android.SquishSyntax import SquishSyntax
from API.Android.ActionBar.File.Options.OptionsConst import OptionsConst
class Options(SquishSyntax):
    def __init__(self):
        pass
    
    def showPortLabels(self, p_trueOrFalse):
        pass
    
    def showDeviceNames(self, p_trueOrFalse):
        pass
    
    def showDeviceModel(self, p_trueOrFalse):
        pass
    
    def commandButtonLayoutLeft(self):
        self.tap(OptionsConst.COMMAND_BUTTON_LEFT)
        
    def commandButtonLayoutRight(self):
        self.tap(OptionsConst.COMMAND_BUTTON_RIGHT)