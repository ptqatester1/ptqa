######################
#@author: Pamela Vinco
######################

from API.MenuBar.File.File import File
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

from API.Utility.Util import UtilConst

util = Util()
fileMenu = File()
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 72, 80, "PC0")

def main():
    util.init()
    openPKZ()

def openPKZ():
    util.open("PKZTest.pkz", UtilConst.UI_TEST)
    pc0.exists()