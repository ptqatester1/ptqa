from API.Utility.Util import Util
from API.Utility import UtilConst
from API import functions

from API.Device.Ioe.MCU import MCU
from API.Device.Ioe.SBC import SBC

from API.ComponentBox import ComponentBoxConst

util = Util()

coffee_maker = MCU('Appliance', 300, 100, 'Coffee Maker')
coffee_maker.sbc_port = 'D1'
sbc = SBC('SBC-PT', 100, 300, 'SBC0')
counter_top_lamp = MCU('Light', 300, 300, 'Counter Top Lamp')
counter_top_lamp.sbc_port = 'D2'
motion_sensor = MCU('Motion Sensor', 100, 500, 'Motion Sensor')
motion_sensor.sbc_port = 'D9'

devices = [coffee_maker, counter_top_lamp, motion_sensor]

def main():
    util.maximizePT()
    util.open('IoT_3_3_1_4.pka', UtilConst.IOT_TEST)
    adding_the_necessary_devices()
    programming_the_sbc()

def adding_the_necessary_devices():
    add_devices()
    change_names_to_match_diagram()
    connect_the_devices()

def programming_the_sbc():
    create_new_script()
    write_program()
    testing()
    
def create_new_script():
    sbc.select()
    sbc.clickProgrammingTab()
    sbc.programming.newScript('main.py', 'Empty - Python')
    snooze(1)
    sbc.programming.selectScript('main.py')
    snooze(1)
    
def write_program():
    script_text = '''
from gpio import *
from time import *
def main():
    while True:
        motion_sensor = digitalRead(9)
        if motion_sensor == HIGH:
            print("Someone's awake.");
            print("Making Coffee...");
            customWrite(1,1)
            customWrite(2,1)
            delay(6000)
            print("Done. Coffee is ready.");
            customWrite(1,0)
            customWrite(2,0)
        delay(500)
if __name__ == "__main__":
    main()'''
    sbc.programming.editScriptText(script_text)
    sbc.programming.run()
    sbc.close()

def testing():
    motion_sensor.deviceDragInteraction(-30, 0, 40, 0, 1)
    util.speedUpConvergence()
    sbc.select()
    sbc.clickProgrammingTab()
    output = sbc.programming.getConsoleOutput()
    for text in ['Making Coffee...', 'Someone\'s awake.', 'Done. Coffee is ready.']:
        msg = 'Expected %s to be in %s' % (text, output)
        functions.check(text in output, msg)
    
def add_devices():
    for device in devices + [sbc]:
        device.create()

def change_names_to_match_diagram():
    for device in devices + [sbc]:
        device.select()
        device.clickConfigTab()
        device.config.settings.displayName(device.displayName)
        device.close()

def connect_the_devices():
    for device in devices:
        sbc.connect(device, ComponentBoxConst.Connection.CONN_IOE, device.sbc_port, 'D0')