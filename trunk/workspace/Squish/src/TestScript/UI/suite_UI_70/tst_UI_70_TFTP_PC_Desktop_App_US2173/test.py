########################
##Author: AbbasH
########################

from API.Utility import UtilConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC

import os

#function initialization
util = Util()

pc = PC(ComponentBoxConst.DeviceModel.PC, 71, 108, "pc")    

def main():
    util.init()
    maketop()
    checkpoint()    

def maketop():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, pc.model, pc.x, pc.y)
        
def checkpoint():    
    pc.select()
    pc.clickDesktopTab()
    pc.desktop.applications.tftpService()
    pc.close()