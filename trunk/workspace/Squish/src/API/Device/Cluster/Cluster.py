from API.Utility.Util import Util
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbar import GoldenLogicalToolbar

class Cluster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def enter(self):
        Util().clickOnWorkspace(self.x, self.y)
    
    def exit(self):
        GoldenLogicalToolbar().backButton()