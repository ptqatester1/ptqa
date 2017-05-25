#**************************************************************************
#@author: Thi Nguyen
#@summary: 
#**************************************************************************
from API.Android.Utility.Util import Util

from API.Android.Device.DeviceBase import CliBase
class Cli(CliBase): 
    def __init__(self):
        self.util = Util()

