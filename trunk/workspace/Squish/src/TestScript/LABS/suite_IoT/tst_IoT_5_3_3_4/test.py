from API.Utility.Util import Util
from API.Utility import UtilConst

from API.Device.Ioe.MCU import MCU
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch

from API.ComponentBox import ComponentBoxConst

util = Util()

solar_panel = MCU('Solar Panel', 100, 100, 'IoE0')
pc_0 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'PC')
server = Server(ComponentBoxConst.DeviceModel.SERVER, 100, 100, 'Server')
switch = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 100, 100, 'Switch')
power_meter = MCU('Power Meter', 100, 100, 'IoE1')
batter = MCU('Battery', 100, 100, 'IoE2')
led_1 = MCU('LED', 100, 100, 'LED 1')
led_2 = MCU('LED', 100, 100, 'LED 2')
led_3 = MCU('LED', 100, 100, 'LED 3')
led_4 = MCU('LED', 100, 100, 'LED 4')

def main():
    open_activity()
    None

def open_activity():
    util.maximizePT()
    util.open('IoT_5_3_3_4.pka', UtilConst.IOT_TEST)
    util.speedUpConvergence()

def explore_the_smart_grid():
    None

def understanding_the_devices_that_comprise_the_smart_grid():
    None
    
def exploring_the_smart_power_grid_switch_program():
    None
    
def reflection():
    None

def challenge_task():
    None