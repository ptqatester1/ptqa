from API.Utility.Util import Util
from API.Utility import UtilConst
from API.MenuBar.File.Open.Open import Open
from API import functions

util = Util()

def main():
    open_sample('')

def open_sample(file_path):
    util.init()
    Open().openSamples(functions.pathFromOS(file_path))
    util.speedUpConvergence()