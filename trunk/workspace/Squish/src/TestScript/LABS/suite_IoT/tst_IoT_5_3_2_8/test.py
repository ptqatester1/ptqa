from API.Utility.Util import Util
from API.Utility import UtilConst
from API import functions

from API.Device.Ioe.MCU import MCU
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch
from API.Device.Cluster.Cluster import Cluster

from API.ComponentBox import ComponentBoxConst

util = Util()

# Clusters
isp_cloud_cluster     = Cluster(100, 100)
smart_grid_cluster    = Cluster(100, 100)
smart_home_cluster    = Cluster(100, 100)
smart_parking_cluster = Cluster(100, 100)
city_offices_cluster  = Cluster(100, 100)
smart_traffic_cluster = Cluster(100, 100)

city_it_laptop = PC(ComponentBoxConst.DeviceModel.LAPTOP, 100, 100, 'City-IT-Laptop')
parking_smart_phone = PC(ComponentBoxConst.DeviceModel.PDA, 100, 100, 'Smartphone0')

# IoE Devices
parking_server = MCU('MCU-PT', 100, 100, 'Parking Server')
parking_space1 = MCU('Metal Sensor', 100, 100, 'P-Space-1')
parking_space2 = MCU('Metal Sensor', 100, 100, 'P-Space-2')
parking_space3 = MCU('Metal Sensor', 100, 100, 'P-Space-3')
parking_space4 = MCU('Metal Sensor', 100, 100, 'P-Space-4')
parking_space5 = MCU('Metal Sensor', 100, 100, 'P-Space-5')
parking_street_cam = MCU('Webcam', 100, 100, 'P-Street-Cam')
parking_street_light1 = MCU('Light', 100, 100, 'Parking Street Light-1')
parking_street_light2 = MCU('Light', 100, 100, 'Parking Street Light-2')

red_car = MCU('Car', 100, 100, 'Red Car')
green_car = MCU('Car', 100, 100, 'Green Car')

paramedic = MCU('Car', 100, 100, 'Emergency Vehicle')
traffic_red_car = MCU('Car', 100, 100, 'Traffic Red Car')
traffic_light_n1 = MCU('Light', 100, 100, 'Traffic Light N1')
traffic_light_w1 = MCU('Light', 100, 100, 'Traffic Light W1')


parking_devices = [
                   parking_server, parking_space1, parking_space2, parking_space3,
                   parking_space4, parking_space5, parking_street_cam,
                   parking_street_light1, parking_street_light2
                   ]

def main():
    open_activity()
    explore_the_smart_city()
    None

def open_activity():
    util.maximizePT()
    util.open('IoT_5_3_2_8.pka', UtilConst.IOT_TEST)
    util.speedUpConvergence()

def explore_the_smart_city():    
    understanding_the_devices_that_comprise_the_smart_city()
    smart_parking()
    smart_traffic()
    None

def understanding_the_devices_that_comprise_the_smart_city():
    examine_the_isp_cluster_resources_offered_to_the_city()
    check_city_networks_connected_using_serial_cables()
    check_city_netowrks_connected_using_coax_cables()
    examine_city_offices_cluster()
    examine_which_networks_are_connected_wirelessly()
    examine_which_smart_home_devices_connect_to_cell_tower()
    examine_which_smart_parking_devices_connect_to_cell_tower()
    None

def examine_the_isp_cluster_resources_offered_to_the_city():
    #a.     Click the ISP Cluster and examine the resources that it offers to the city.
    isp_cloud_cluster.enter()
    isp_cloud_cluster.exit()
    None

def check_city_networks_connected_using_serial_cables():
    #b.    Click the back button. Which city networks are connected using the red serial cables?
    pass

def check_city_netowrks_connected_using_coax_cables():
    #c.     Which city networks are connected using the blue coaxial cables?
    pass

def examine_city_offices_cluster():
    #d.    Click the City Offices cluster. Why are there two connections leading to it from the ISP Cloud?
    city_offices_cluster.enter()
    city_offices_cluster.exit()

def examine_which_networks_are_connected_wirelessly():
    #e.     Click the back button. Which city networks are wirelessly connected to the Cell-Tower?
    pass

def examine_which_smart_home_devices_connect_to_cell_tower():
    #f.     Which devices in the Smart Home are connected to the Cell-Tower?
    pass

def examine_which_smart_parking_devices_connect_to_cell_tower():
    #a.     Which devices in the Smart Parking cluster are connected to the Cell-Tower?
    pass

def smart_parking():
    interacting_with_smart_parking_cluster()
    interacting_with_smart_parking_cluster_as_regular_citizen()

def smart_traffic():
    smart_traffic_cluster.enter()
    util.dragAndDrop(util.currentWorkspace, paramedic.x, paramedic.y, util.currentWorkspace, paramedic.x + 500, paramedic.y)
    util.fastForwardTime()
    check_device_property_value(traffic_light_n1, 'state', '1')
    
    util.dragAndDrop(util.currentWorkspace, paramedic.x, paramedic.y, util.currentWorkspace, traffic_red_car.x - 100, traffic_red_car.y)
    util.fastForwardTime()
    check_device_property_value(traffic_light_w1, 'state', '1')
    
def interacting_with_smart_parking_cluster():
    city_offices_cluster.enter()
    city_it_laptop.select()
    city_it_laptop.clickDesktopTab()
    city_it_laptop.desktop.applications.webBrowser()
    city_it_laptop.desktop.webBrowser.browse('195.0.0.2')
    city_it_laptop.desktop.webBrowser.registrationServer.loginPage.signIn('Park', 'Park')
    for device in parking_devices:
        device_in_control_page(device.displayName, get_control_page_object(city_it_laptop))
    city_it_laptop.desktop.webBrowser.registrationServer.homePage.expandItem(parking_space1.displayName)
    parking_space_status = float(city_it_laptop.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject(parking_space1).text)
    
    msg = 'Expect parking space status of %s to be 0 got %s' % (parking_space1.displayName, parking_space_status)
    functions.check(0 == parking_space_status, msg)
    city_offices_cluster.exit()
    
    smart_parking_cluster.enter()
    util.dragAndDrop(util.currentWorkspace, red_car.x, red_car.y, util.currentWorkspace, parking_space1.x, parking_space1.y)
    util.fastForwardTime()
    smart_parking_cluster.exit()
    
    parking_space_status = float(city_it_laptop.desktop.webBrowser.registrationServer.homePage.getButtonOrValueObject(parking_space1).text)

    msg = 'Expect parking space status of %s to be greater than 0 got %s' % (parking_space1.displayName, parking_space_status)
    functions.check(0 < parking_space_status, msg)
    city_it_laptop.close()

def interacting_with_smart_parking_cluster_as_regular_citizen():
    smart_parking_cluster.enter()
    parking_smart_phone.select()
    parking_smart_phone.clickDesktopTab()
    parking_smart_phone.desktop.applications.webBrowser()
    parking_smart_phone.desktop.webBrowser.browse('10.10.10.10')
    util.fastForwardTime()
    for i in range(1, 6):
        text = 'Parking spot %s is free' % (i)
        if i == 1:
            text = 'Parking spot %s is taken' %(i)
        parking_smart_phone.desktop.webBrowser.check.content(text)
    
    util.dragAndDrop(util.currentWorkspace, green_car.x, green_car.y, util.currentWorkspace, parking_space5.x, parking_space5.y)
    util.speedUpConvergence()
    
    for i in range(1, 6):
        text = 'Parking spot %s is free' % (i)
        if i == 1 or i == 5:
            text = 'Parking spot %s is taken' %(i)
        parking_smart_phone.desktop.webBrowser.check.content(text)
    smart_parking_cluster.exit()

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

def get_control_page_object(browsing_device):
    return browsing_device.desktop.webBrowser.registrationServer.homePage.getListObject()