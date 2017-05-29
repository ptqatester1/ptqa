from API.Utility.Util import Util
from API.Utility import UtilConst
from API import functions

from API.Device.Ioe.MCU import MCU

from API.ComponentBox import ComponentBoxConst

util = Util()

mcu = MCU('MCU-PT', 640, 300, 'MCU')
switch = MCU('Switch', 345, 95, 'Switch')
toggle_push_button = MCU('Toggle Push button', 290, 225, 'Toggle Push Button')
potentiometer = MCU('Potentiometer', 310, 365, 'Potentiometer')
flex_sensor = MCU('Flex Sensor', 250, 405, 'Flex Sensor')
lamp = MCU('Lamp', 935, 50, 'IoE1')
led = MCU('LED', 930, 195, 'IoE0')
siren = MCU('Siren', 950, 365, 'Siren')
motor = MCU('Motor', 935, 530, 'Motor')

def main():
    util.maximizePT()
    util.open('IoT_2_3_1_2.pka', UtilConst.IOT_TEST)
    the_sensors_and_the_pt_mcu()
    programming_the_mcu()

def the_sensors_and_the_pt_mcu():
    observe_device_interactions()

def programming_the_mcu():
    mcu.select()
    mcu.clickProgrammingTab()
    

def observe_device_interactions():
    check_device_interaction(switch, lamp, 'state', 1)
    check_device_interaction(toggle_push_button, led, 'level', 1023)
    check_device_drag_interaction(potentiometer, siren, 'state', 1023)
    #It seems like this can't really be tested by script that the value is
    #changing since the flex sensor returns to its original position
    check_device_drag_interaction(flex_sensor, motor, 'rotation', 1)

def check_device_interaction(interactive_device, controlled_device, property, expected_value):
    interactive_device.deviceInteraction()
    check_interaction(controlled_device, property, expected_value)
    
def check_device_drag_interaction(interactive_device, controlled_device, property, expected_value):
    interactive_device.deviceDragInteraction(0, 10, 50, 10, p_hold_time = 1)
    check_interaction(controlled_device, property, expected_value)
    
def check_interaction(controlled_device, property, expected_value):
    controlled_device.select()
    controlled_device.clickTab('Attributes')
    value = controlled_device.attribute.getPropertyValue(property)
    controlled_device.close()
    msg = 'Expected the property %s to be greater than or equal to %s got %s' % (property, expected_value, value)
    functions.check(float(value) >= expected_value, msg)
