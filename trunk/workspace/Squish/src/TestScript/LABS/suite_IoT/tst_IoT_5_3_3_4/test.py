from API.Utility.Util import Util
from API.Utility import UtilConst

from API.Device.Ioe.MCU import MCU
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch

from API.ComponentBox import ComponentBoxConst

util = Util()

power_iot_server = Server(ComponentBoxConst.DeviceModel.SERVER, 100, 100, 'Power IoT Server')
laptop = Server(ComponentBoxConst.DeviceModel.LAPTOP, 100, 100, 'Laptop')

wind_turbine = MCU('Wind Turbine', 100, 100, 'Wind Turbine')
coal_co_detector = MCU('Coal CO Detector', 100, 100, 'Coal CO Detector')
wind_power_meter = MCU('Wind-Power Meter', 100, 100, 'Wind-Power Meter')
coal_plant_meter = MCU('Coal Plant Metere', 100, 100, 'Coal Plant Meter')
solar_cells = MCU('Solar-Cells', 100, 100, 'Solar-Cells')

power_grid_switch = MCU('Switch', 100, 100, 'Smart Power Grid Switch')

def main():
    open_activity()
    None

def open_activity():
    util.maximizePT()
    util.open('IoT_5_3_3_4.pka', UtilConst.IOT_TEST)
    util.speedUpConvergence()

def explore_the_smart_grid():
    understanding_the_devices_that_comprise_the_smart_grid()
    exploring_the_smart_power_grid_switch_program()

def understanding_the_devices_that_comprise_the_smart_grid():
    devices = [wind_turbine, coal_co_detector, wind_power_meter, coal_plant_meter, solar_cells]

    power_iot_server.ip = get_ip_of(power_iot_server)
    power_iot_server.username, power_iot_server.password = get_username_and_password()

    laptop.select()
    laptop.clickDesktopTab()
    laptop.desktop.applications.webBrowser()
    laptop.desktop.webBrowser.browse(power_iot_server.ip)
    laptop.desktop.webBrowser.registrationServer.loginPage.signIn(power_iot_server.username, power_iot_server.password)
    for device in devices:
        device_in_control_page(device.displayName(), get_control_page_object(laptop))
    laptop.close()
    
def exploring_the_smart_power_grid_switch_program():
    power_grid_switch.select()
    power_grid_switch.clickProgrammingTab()
    power_grid_switch.programming.selectScript('power_switch', 'main.js')
    power_grid_switch.programming.textCheckpoint('Switching to (Wind|Coal|Solar) Power')

def get_ip_of(device):
    device.select()
    device.clickDesktopTab()
    device.desktop.applications.ipConfiguration()
    ip = device.desktop.ipConfiguration.getIp()
    device.close()
    return ip

def get_username_and_password():
    power_iot_server.select()
    power_iot_server.clickServicesTab()
    power_iot_server.services.selectInterface('IoT')
    table = power_iot_server.services.ioe.tableName()
    username = findObject('%s.item_0/0').text
    password = findObject('%s.item_0/1').text
    power_iot_server.close()
    return username, password

def device_in_control_page(device, control_page_object):
    control_page_text = control_page_object.innerText
    msg = 'Expected %s to be in %s' % (device, control_page_text)
    functions.check(device in control_page_text, msg)

def get_control_page_object(browsing_device):
    return browsing_device.desktop.webBrowser.registrationServer.homePage.getListObject()