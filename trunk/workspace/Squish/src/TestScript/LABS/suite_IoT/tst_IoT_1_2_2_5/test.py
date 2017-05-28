from API.Utility.Util import Util
from API.Utility import UtilConst
from API import functions

from API.Device.Ioe.MCU import MCU
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch

from API.ComponentBox import ComponentBoxConst

util = Util()

solar_panel = MCU('Solar Panel', 100, 500, 'IoT0')
pc_0 = PC(ComponentBoxConst.DeviceModel.PC, 260, 230, 'PC0')
server = Server(ComponentBoxConst.DeviceModel.SERVER, 475, 240, 'Server')
switch = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 345, 310, 'Switch')
power_meter = MCU('Power Meter', 300, 700, 'IoT1')
battery = MCU('Battery', 500, 500, 'IoT2')
led_1 = MCU('LED', 790, 260, 'LED 1')
led_2 = MCU('LED', 790, 370, 'LED 2')
led_3 = MCU('LED', 790, 470, 'LED 3')
led_4 = MCU('LED', 800, 590, 'LED 4')

led_list = [led_1, led_2, led_3, led_4]
power_devices = [solar_panel, power_meter, battery]
for device in power_devices:
    device.network_port = 'FastEthernet0'
    if device is solar_panel:
        device.network_port = 'GigabitEthernet0'

initial_battery_power = None

def main():
    util.maximizePT()
    util.open('IoT_1_2_2_5.pka', UtilConst.IOT_TEST)
    adding_and_connecting_devices()
    configuring_the_devices()
    using_the_system()

def adding_and_connecting_devices():
    solar_panel.create()
    power_meter.create()
    battery.create()

    solar_panel.connect(power_meter, ComponentBoxConst.Connection.CONN_IOE, 'D0', 'D0')
    battery.connect(power_meter, ComponentBoxConst.Connection.CONN_IOE, 'D0', 'D1')
    global initial_battery_power
    initial_battery_power = get_battery_power()
    for i, led in enumerate(led_list):
        battery.connect(led, ComponentBoxConst.Connection.CONN_IOE, 'D' + str(i+1), 'D0')
    
    for i, device in enumerate(power_devices):
        switch_port = 'FastEthernet0/' + str(i+3)
        device.connect(switch, ComponentBoxConst.Connection.CONN_STRAIGHT, device.network_port, switch_port)
    
    util.speedUpConvergence()

def configuring_the_devices():
    for device in power_devices:
        device.select()
        device.clickConfigTab()
        device.config.selectInterface(device.network_port)
        device.config.interface.wired.dhcp()
        device.close()
        
    util.speedUpConvergence()
    
    for device in power_devices:
        device.select()
        device.clickConfigTab()
        device.config.selectInterface(device.network_port)
        device.config.interface.wired.check.ip("1\.0\.0\.\d{1,3}")
        device.close()
        
    for device in power_devices:
        device.select()
        device.clickConfigTab()
        device.config.selectInterface('Settings')
        device.config.settings.remoteServerRadio()
        device.config.settings.connect('1.0.0.1', 'admin', 'admin')
        device.close()
        
    util.speedUpConvergence()
    
def using_the_system():
    check_battery_draining()
    check_led_power_off()
    log_in_to_server()
    check_displayed_devices()

def check_battery_draining():
    current_battery_power = get_battery_power()
    msg = 'Expecting initial battery power of %s to be greater than current power of %s' % (initial_battery_power, current_battery_power)
    functions.check(initial_battery_power > current_battery_power, msg)

def check_led_power_off():
    # I don't think this check is necessary and it is a bit time consuming
    # This should be checked in the LED sample file anyway. Leaving this code here
    # for now though. -Chris
#     has_zero_value = False
#     for i in range(120):
#         snooze(1)
#         for led in led_list:
#             led.select()
#             led.clickTab('Attributes')
#             value = float(led.attribute.getPropertyValue('level'))
#             led.close()
#             if value == 0:
#                 has_zero_value = True
#                 break
#         if has_zero_value:
#             break
#     msg = 'Expected has_zero_value to evaluate to True. Got %s' % (has_zero_value)
#     functions.check(has_zero_value, msg)
    pass

def log_in_to_server():
    pc_0.select()
    pc_0.clickDesktopTab()
    pc_0.desktop.applications.webBrowser()
    pc_0.desktop.webBrowser.browse('1.0.0.1')
    pc_0.desktop.webBrowser.registrationServer.loginPage.signIn('admin', 'admin')

def check_displayed_devices():
    device_list = pc_0.desktop.webBrowser.registrationServer.homePage.getListObject()
    device_count = device_list.numChildren
    msg = 'Expect the list of devices to contain 3. Found %s' % (device_count)
    functions.check(device_count == 3, msg)
    for device in power_devices:
        check_device_in_list(device, device_list)

def check_device_in_list(device, device_list):
    condition = device.displayName in device_list.innerText
    msg = 'Expected %s to be in %s. Got %s' % (device.displayName, device_list.innerText, condition)
    functions.check(condition, msg)

def get_battery_power():
    battery.select()
    battery.clickTab('Attributes')
    power = float(battery.attribute.getPropertyValue('Available power'))
    battery.close()
    return power