from API.Utility.Util import Util
from API.Utility import UtilConst

from API import functions

from API.Device.Ioe.MCU import MCU
from API.Device.Ioe.SBC import SBC
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch

from API.ComponentBox import ComponentBoxConst

util = Util()

servo = MCU('Servo', 300, 100, 'IoE0')
sbc = SBC('SBC-PT', 100, 300, 'IoE1')
led = MCU('LED', 300, 300, 'LED 1')

def main():
    util.open('IoT_2_2_1_4.pka', UtilConst.IOT_TEST)
    build_the_circuit()
    program_the_sbc()
    None

def build_the_circuit():
    place_the_components()
    connecting_the_components()
    
def place_the_components():
    servo.create()
    sbc.create()
    led.create()

def connecting_the_components():
    sbc.connect(servo, ComponentBoxConst.Connection.CONN_IOE, 'D0', 'D0')
    sbc.connect(led, ComponentBoxConst.Connection.CONN_IOE, 'D1', 'D0')
    
def program_the_sbc():
    run_the_default_program()
    modify_the_default_program()
    
    
def run_the_default_program():
    start_the_program()
    check_led_is_blinking()
    stop_the_program()
    
def start_the_program():
    sbc.select()
    sbc.clickProgrammingTab()
    sbc.programming.selectScript('Blink', 'main')
    sbc.programming.run()
    sbc.close()

def check_led_is_blinking():
    condition = lambda states: ('1023' in states) and ('0' in states)
    states = get_device_states(led, 'level', condition)
    msg = 'Expected 1023 and 0 to be in states. Got %s' % (condition(states))
    functions.check(condition(states), msg)

def stop_the_program():
    sbc.select()
    sbc.clickProgrammingTab()
    sbc.programming.selectScript('main')
    sbc.programming.stop()
    sbc.close()

def modify_the_default_program():
    sbc.select()
    sbc.clickProgrammingTab()
    sbc.programming.selectScript('main')
    sbc.programming.insertTextAtLine(9, '\t\tcustomWrite(0, 127)')
    sbc.programming.insertTextAtLine(12, '\t\tcustomWrite(0, -127)')
    sbc.programming.run()
    sbc.close()
    check_servo_is_moving()

def check_servo_is_moving():
    condition = lambda states: (len(set(states)) == 2)
    states = get_device_states(servo, 'servoAngle', condition)
    msg = 'Expected the servo to be at two different positions. Got %s' % (condition(states))
    functions.check(condition(states), msg)
    None
    
def get_device_states(device, property, exit_condition):
    states = []
    device.select()
    for i in range(20):
        device.clickTab('Attributes')
        states.append(device.attribute.getPropertyValue(property))
        device.clickProgrammingTab()
        if exit_condition(states):
            break
    device.close()
    return states