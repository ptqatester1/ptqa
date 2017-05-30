from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Toolbar.GoldenLogicalToolbar.GoldenLogicalToolbar import GoldenLogicalToolbar

from API.Device.Ioe.MCU import MCU
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst

util = Util()

class Cluster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def enter(self):
        Util().clickOnWorkspace(self.x, self.y)
    
    def exit(self):
        GoldenLogicalToolbar().backButton()

# Clusters
warehouse = Cluster(100, 100)
casting_factory = Cluster(100, 100)
power_station = Cluster(100, 100)

# Warehouse End Devices
w_pc1 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'W-PC1')
w_pc2 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'W-PC2')
w_laptop1 = PC(ComponentBoxConst.DeviceModel.LAPTOP, 100, 100, 'W-Laptop1')

# Factory End Devices
f_manager_smartphone = PC(ComponentBoxConst.DeviceModel.PDA, 100, 100, 'F-Manager-Smartphone')
f_pc1 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-PC-1')
f_pc2 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-PC-2')
f_pc3 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-PC-3')
f_pc4 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-PC-4')
f_pc5 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-PC-5')
f_pc6 = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-PC-6')
f_showroom_tablet = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-Showroom-Tablet')
f_office_laptop = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-Office-Laptop')
f_shipping_tablet = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-Shipping-Tablet')
f_assembly_laptop = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-Assembly-Laptop')
f_wrapping_tablet = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'Wrapping Tablet')
f_it_laptop = PC(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-IT-Laptop')
f_server = Server(ComponentBoxConst.DeviceModel.PC, 100, 100, 'F-Server')
webserver = Server(ComponentBoxConst.DeviceModel.PC, 100, 100, 'Webserver')


# Warehouse IoE Devices
north_window = MCU('Window', 100, 100, 'W North Window')
old_car = MCU('Old Car', 100, 100, 'IoE3')
fork_lift1 = MCU('Siren', 100, 100, 'W-Forklift-1')
north_fan = MCU('Fan', 100, 100, 'W-North-Fan')
co2_detector = MCU('CO2 Detector', 100, 100, 'W-CO2 Detector')
fork_lift2 = MCU('Siren', 100, 100, 'W-Forklift-2')
south_fan = MCU('Fan', 100, 100, 'W-South-Fan')
co_detector = MCU('CO Detector', 100, 100, 'W-CO-Detector')
south_window = MCU('Window', 100, 100, 'W-South-Window')
fork_lift3 = MCU('Siren', 100, 100, 'W-Forklift-3')
rfid_reader = MCU('RFID Reader', 100, 100, 'W-RFID-Reader')
rfid_card = MCU('RFID Card', 100, 100, 'W-RFID-Tag-000')
coffee_maker = MCU('Appliance', 100, 100, 'W-Coffee')

# Factory IoE Devices
mcu = MCU('MCU-PT', 100, 100, 'MCU0')
f_window = MCU('Window', 100, 100, 'F-MM-Window')
f_temperature_monitor = MCU('Temperature Monitor', 100, 100, 'F-MM-Temp')
f_fan = MCU('Fan', 100, 100, 'Fan')
f_humiture_monitor = MCU('Humiture Monitor', 100, 100, 'F-RM-CP-Humiture')
f_humidifier = MCU('Humidifier', 100, 100, 'F-CP-Humidifier')
f_thermostat = MCU('Thermostat', 100, 100, 'F-Clay-Casting')
a_temperature_monitor = MCU('Temperature Monitor', 100, 100, 'A-Temperature Sensor')
a_light_switch = MCU('Rocker Switch', 100, 100, 'A-Light-Switch') 
a_push_button = MCU('Push Button', 100, 100, 'A-Start Process')
a_potentiometer = MCU('Potentiometer', 100, 100, 'A-Conveyor Speed')
a_flex_sensor = MCU('Flex Sensor', 100, 100, 'Clay-Flex Sensor')
a_motor = MCU('Motor', 100, 100, 'Mixing Motor')
a_siren = MCU('Siren', 100, 100, 'Speed Warning')
a_light = MCU('Light', 100, 100, 'Running')
a_fan1 = MCU('Fan', 100, 100, 'F-Assembly-Fan-2')
a_process_indicator = MCU('LED', 100, 100, 'Process Indicator')
a_fan2 = MCU('Fan', 100, 100, 'F-Assembly-Fan-1')
fire_sprinkler = MCU('Fire Sprinkler', 100, 100, 'Assembly Fire-Sprinkler')
a_rfid_reader = MCU('RFID Reader', 100, 100, 'A-RFID-Reader')
a_rfid_card = MCU('RFID Card', 100, 100, 'A-RFID-Card')

# Power Station IoE Devices
wind_turbine = MCU('Wind Turbine', 100, 100, 'PS-Wind Turbine')
battery = MCU('Battery', 100, 100, 'PS-Battery')

# Warehouse Network Devices
warehouse_sw = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 100, 100, 'Warehouse-SW')
warehouse_rt = Router(ComponentBoxConst.DeviceModel.ROUTER_1941, 100, 100, 'W-Router')

# Factory Network Devices
factory_main_sw = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 100, 100, 'Factory Main-SW')
factory_rt = Router(ComponentBoxConst.DeviceModel.ROUTER_2911, 100, 100, 'Factory-RT')
f_sw1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_IE_2000, 100, 100, 'F-SW-1')
f_sw2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_IE_2000, 100, 100, 'F-SW-2')
f_assembly_sw = Switch(ComponentBoxConst.DeviceModel.SWITCH_IE_2000, 100, 100, 'F-Assembly-SW')
# Power Station Network Devices
ps_remote_rt = Router(ComponentBoxConst.DeviceModel.ROUTER_819, 100, 100, 'PS-Remote-RT')

def main():
    open_activity()
    
    None

def open_activity():
    util.maximizePT()
    util.open('IoT_4_2_2_5.pka', UtilConst.IOT_TEST)
    util.speedUpConvergence()

def explore_the_connected_factory():
    None

def review_the_glazing_company_overview_page():
    warehouse.enter()
    w_pc1.select()
    w_pc1.clickDesktopTab()
    w_pc1.desktop.applications.webBrowser()
    w_pc1.desktop.webBrowser.browse('172.16.1.8')
    util.speedUpConvergence()
    w_pc1.desktop.webBrowser.check.content('Glaze Company')
    w_pc1.close()
    
def run_the_classic_car():
    old_car.deviceInteraction()
    for i in range(10):
        util.speedUpConvergence()
    check_device_property_value(north_window, 'state', '1')
    check_device_property_value(north_fan, 'state', '1')
    check_device_property_value(south_window, 'state', '1')
    check_device_property_value(south_fan, 'state', '1')
    warehouse.exit()
    
def review_the_connected_factory_network_settings():
    casting_factory.enter()
    f_it_laptop.select()
    f_it_laptop.clickDesktopTab()
    f_it_laptop.desktop.applications.textEditor()
    f_it_laptop.desktop.textEditor.openFile(None, 'IP-Network.txt')
    f_it_laptop.close()

def monitor_factory_sensor_settings():
    assembly_devices = [
                        a_temperature_monitor, a_fan2, a_push_button, a_light,
                        a_siren, a_flex_sensor, fire_sprinkler, a_fan1,
                        a_rfid_reader, a_process_indicator
                        ]
    prep_devices = [
                    f_temperature_monitor, f_fan, f_humiture_monitor,
                    f_humidifier, f_thermostat, f_window
                    ]
    ps_devices = [battery, wind_turbine]
    
    f_it_laptop.select()
    f_it_laptop.clickDesktopTab()
    f_it_laptop.desktop.applications.webBrowser()
    f_it_laptop.desktop.webBrowser.browse('factory')
    
    f_it_laptop.desktop.webBrowser.registrationServer.loginPage.signIn('Assembly', 'Assembly')
    for device in assembly_devices:
        device_in_control_page(device.displayName(), get_control_page_object())
        
    f_it_laptop.desktop.webBrowser.registrationServer.loginPage.signIn('Prep', 'Prep')
    for device in assembly_devices:
        device_in_control_page(device.displayName(), get_control_page_object())
        
    f_it_laptop.desktop.webBrowser.registrationServer.loginPage.signIn('PS', 'PS')
    for device in assembly_devices:
        device_in_control_page(device.displayName(), get_control_page_object())

def check_device_property_value(device, property, expected_value):
    device.select()
    device.clickTab('Attributes')
    actual_value = device.attribute.getPropertyValue(property)
    device.close()
    
    msg = 'Expected %s state to be %s got %s' % (device.displayName, expected_value, actual_value)
    functions.check(expected_value == actual_value, msg)

def device_in_control_page(device, control_page_object):
    control_page_text = control_page_object.innerText
    msg = 'Expected %s to be in %s' % (device, control_page_text)
    functions.check(device in control_page_text, msg)

def get_control_page_object():
    return f_it_laptop.desktop.webBrowser.registrationServer.homePage.getListObject()