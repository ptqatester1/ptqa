#**************************************************************************
#@author: Thi Nguyen
#@summary: Global handles activities on the Global tab of Router
#**************************************************************************
from API.Android.Utility.Util import Util

from API.Android.Device.DeviceBase import CliBase
class Cli(CliBase): 
    def __init__(self):
        self.util = Util()

