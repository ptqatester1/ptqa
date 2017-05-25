######################
#@author: Pamela Vinco
######################

from API.ComponentBox import ComponentBoxConst
from API.Utility.Util import Util
from API.Device.EndDevice.PC.PC import PC

util = Util()

#Device initialization
laptop = PC(ComponentBoxConst.DeviceModel.LAPTOP, 200, 100, "Laptop0")


def main():       
    util.init()
    createTopology()
    checkpoint()

def createTopology():
    util.createDevice(ComponentBoxConst.DeviceType.END_DEVICE, laptop.model, laptop.x, laptop.y)
    
def checkpoint():
    laptop.exists()
    