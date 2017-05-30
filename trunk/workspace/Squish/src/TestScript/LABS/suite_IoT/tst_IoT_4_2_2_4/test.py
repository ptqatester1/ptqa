from API.Utility.Util import Util
from API.Utility import UtilConst
from API import functions

from API.Device.Ioe.MCU import MCU
from API.Device.EndDevice.PC.PC import PC
from API.Device.Switch.Switch import Switch
from API.Device.HomeGateway.HomeGateway import HomeGateway
from API.Device.Modem.Modem import Modem
from API.Device.EndDevice.TV.TV import TV
from API.ComponentBox import ComponentBoxConst

util = Util()

#Network devices
cable_modem = Modem(ComponentBoxConst.DeviceModel.CABLE_MODEM, 100, 100, 'Cable Modem0')
home_gateway = HomeGateway(ComponentBoxConst.DeviceModel.HOME_GATEWAY, 100, 100, 'Home Gateway0')

#End Devices
smartphone = PC(ComponentBoxConst.DeviceModel.PDA, 100, 100, 'Smartphone')
tablet = PC(ComponentBoxConst.DeviceModel.TABLET_PC, 100, 100, 'Tablet')
tv = TV(ComponentBoxConst.DeviceModel.TV, 100, 100, 'TV')

#IoE Devices
mcu =               MCU('MCU-PT', 100, 100, 'mcu')
solar_panel =       MCU('Solar Panel', 100, 100, 'Smart Solar Panel')
battery =           MCU('Battery', 100, 100, 'Smart Battery')
lamp =              MCU('Light', 100, 100, 'Smart Lamp')
window =            MCU('Window', 100, 100, 'Smart Window')
fan =               MCU('Fan', 100, 100, 'Smart Fan')
smoke_detector =    MCU('Smoke Detector', 100, 100, 'Smoke Detector')
temperature_meter = MCU('Temperature Meter', 100, 100, 'Temperature Meter')
alarm =             MCU('Alarm', 100, 100, 'Alarm')
smoke_sensor =      MCU('Smoke Sensor', 100, 100, 'Smoke Sensor')
coffee_maker =      MCU('Appliance', 100, 100, 'Smart Coffee Maker')
thermostat =        MCU('Thermostat', 100, 100, 'Smart Thermostat')
door =              MCU('Door', 100, 100, 'Smart Door')
garage_door =       MCU('Garage Door', 100, 100, 'Garage Door')
water_meter =       MCU('Water Meter', 100, 100, 'Water Meter')
sprinkler =         MCU('Water Sprinkler', 100, 100, 'Smart Sprinkler')
old_car =           MCU('Old Car', 100, 100, 'Old Car')
heating_unit =      MCU('Heater', 100, 100, 'Heating Unit')
cooling_unit =      MCU('Cooler', 100, 100, 'Cooling Unit')

ioe_devices = [
               solar_panel, battery, lamp, window, fan, smoke_detector,
               temperature_meter, alarm, smoke_sensor, coffee_maker,
               thermostat, door, garage_door, water_meter, sprinkler,
               old_car, heating_unit, cooling_unit
               ]

DOOR_LOCKED   = '1'
DOOR_UNLOCKED = '0'
DOOR_OPEN     = '1'
DOOR_CLOSED   = '0'
WINDOW_OPEN   = '1'
WINDOW_CLOSED = '0'
FAN_MAX_SPEED = '2'
FAN_MIN_SPEED = '1'
FAN_OFF_SPEED = '0'

def main():
    util.maximizePT()
    util.open('IoT_4_2_2_4.pka', UtilConst.IOT_TEST)
    interacting_with_the_smart_home()
    fog_computing_in_the_smart_home()
    None
   
def interacting_with_the_smart_home():
    checking_devices_listed_in_web_interface()
    checking_door_locking()
    checking_smoke_detector()
    checking_coffee_maker()

def checking_devices_listed_in_web_interface():
    go_to_device_web_interface()
    for device in ioe_devices:
        check_device_listed(device, get_control_page_object())
    tablet.close()

def checking_door_locking():
    lock_the_door()
    check_door_lock_state(DOOR_LOCKED)
    unlock_the_door()
    check_door_lock_state(DOOR_UNLOCKED)

def checking_smoke_detector():
    value_object = tablet.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject(smoke_detector.displayName, 2, 1)
    value_text = value_object.innerText
    msg = 'Expected smoke detector value of 0 got %s' % (value_text)
    functions.check(float(value_text) == 0.0, msg)

def checking_coffee_maker():
    coffee_maker.deviceInteraction()
    check_device_property_value(coffee_maker, 'state', '1')

def fog_computing_in_the_smart_home():
    run_the_classic_car()
    check_devices_after_running_car()
    stop_the_classic_car()
    check_devices_after_stopping_car()

def run_the_classic_car():
    old_car.deviceInteraction()
        
def check_devices_after_running_car():
    wait_for_smoke_level_greater_than(10.3)
    check_devices_when_levels_are_high()

def check_devices_after_stopping_car():
    wait_for_smoke_level_less_than(1)
    check_devices_when_levels_are_low()

def check_devices_when_levels_are_high():
    check_device_property_value(fan, 'state', FAN_MAX_SPEED)
    check_device_property_value(door, 'state', DOOR_OPEN)
    check_device_property_value(garage_door, 'state', DOOR_OPEN)
    check_device_property_value(window, 'state', WINDOW_OPEN)

def check_devices_when_levels_are_low():
    check_device_property_value(fan, 'state', FAN_OFF_SPEED)
    check_device_property_value(door, 'state', DOOR_CLOSED)
    check_device_property_value(garage_door, 'state', DOOR_CLOSED)
    check_device_property_value(window, 'state', WINDOW_CLOSED)
    
def lock_the_door():
    go_to_device_web_interface()
    set_door_lock(DOOR_LOCKED)
    tablet.close()
    
def unlock_the_door():
    go_to_device_web_interface()
    set_door_lock(DOOR_UNLOCKED)
    tablet.close()
    
def set_door_lock(lock_state):
    #lock_state: 0 for unlocked 1 for locked
    button = 1 if lock_state == 0 else 2
    door_lock_button = tablet.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject(door.displayName, 2, button)
    util.click(door_lock_button)
    
def check_door_lock_state(expected_lock_state):
    # expected_lock_state of 0 is unlocked.
    # expected_lock_state of 1 is locked.
    door.select()
    door.clickTab('Attributes')
    actual_lock_state = door.attribute.getPropertyValue('lock state')
    door.close()
    msg = 'Expected lock state of %s got %s' % (expected_lock_state, actual_lock_state)
    functions.check(actual_lock_state == expected_lock_state, msg)

def go_to_device_web_interface():
    tablet.select()
    tablet.clickDesktopTab()
    tablet.desktop.applications.webBrowser()
    tablet.desktop.webBrowser.browse('192.168.25.1')
    tablet.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')

def get_control_page_object():
    return tablet.desktop.webBrowser.registrationServer.homePage.getListObject()

def check_device_listed(device, control_page_object):
    control_page_text = control_page_object.innerText
    msg = 'Expected %s to be in %s' % (device, control_page_text)
    functions.check(device in control_page_text, msg)

def check_device_property_value(device, property, expected_value):
    device.select()
    device.clickTab('Attributes')
    actual_value = device.attribute.getPropertyValue(property)
    device.close()
    
    msg = 'Expected %s state to be %s got %s' % (device.displayName, expected_value, actual_value)
    functions.check(expected_value == actual_value, msg)

def wait_for_smoke_level_greater_than(value):
    #The code below should work but not tested
    # go_to_device_web_interface()
    # for i in range(10):
    #     value_object = tablet.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject(smoke_detector.displayName, 2, 1)
    #     value_text = value_object.innerText
    #     if float(value_text) > value:
    #         break
    #     util.speedUpConvergence()
    raise NotImplementedError('Unable to implement at time of writing due to PKA crashing')

def wait_for_smoke_level_less_than(value):
    #See wait_for_smoke_level_greater_than for implementation suggestion
    raise NotImplementedError('Unable to implement at time of writing due to PKA crashing')