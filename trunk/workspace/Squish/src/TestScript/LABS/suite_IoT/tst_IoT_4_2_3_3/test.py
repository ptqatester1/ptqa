from API.Utility.Util import Util
from API.Utility import UtilConst
from API import functions

from API.Device.Ioe.MCU import MCU
from API.Device.Ioe.SBC import SBC
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.Device.Switch.Switch import Switch
from API.Device.HomeGateway.HomeGateway import HomeGateway
from API.Device.Router.Router import Router

from API.ComponentBox import ComponentBoxConst

util = Util()

# End Devices
pc_1 = PC(ComponentBoxConst.DeviceModel.PC, 550, 105, 'PC1')
pc_2 = PC(ComponentBoxConst.DeviceModel.PC, 610, 105, 'PC2')
external_pc = PC(ComponentBoxConst.DeviceModel.PC, 255, 520, 'External PC')
laptop = PC(ComponentBoxConst.DeviceModel.PC, 735, 365, 'Laptop')

# Servers
csp_server = Server(ComponentBoxConst.DeviceModel.SERVER, 200, 145, 'CSP Svr')
csp_server.ip = '209.165.201.3'

# Network Devices
home_gateway = HomeGateway(ComponentBoxConst.DeviceModel.HOME_GATEWAY, 740, 255, 'WH Gateway')
home_gateway.local_ip = '192.168.50.254'
warehouse_router = Router(ComponentBoxConst.DeviceModel.ROUTER_2911, 545, 270, 'Warehouse')
cloud_service_provider = Router(ComponentBoxConst.DeviceModel.ROUTER_2911, 200, 345, 'Cloud Service Provider')

#IoE Devices
sbc = SBC('SBC-PT', 990, 300, 'SBC')
motion_detector = MCU('Motion Detector', 840, 110, 'MD')
light = MCU('Light', 870, 220, 'Directed Light')
rocker_switch = MCU('Rcoker Switch', 970, 155, 'Directed Light SW')
webcam = MCU('Webcam', 865, 340, 'CAM')
trip_sensor = MCU('Trip Sensor', 830, 445, 'TS')

ioe_devices = [motion_detector, light, rocker_switch, webcam, trip_sensor]

# Registration Server Constatns
REGISTRATION_SERVER_URL = 'www.registrar1.pka'
USERNAME = 'pt_user'
PASSWORD = 'Pt_u53r_p@55w0rd'

# Wireless Security Constants
WIRELESS_SSID = "WhGateway"
WIRELESS_PASSWORD = 'IoTWh001'

def main():
    open_activity()
    register_iot_devices_to_the_registration_server()
    #add_conditions_in_the_registration_server()
    configure_strong_authentication_network_devices()
    configure_acl_to_restrict_traffic()
    configure_secure_web_communication_to_the_web_server()
    testing()

def open_activity():
    util.maximizePT()
    util.open('IoT_4_2_3_3.pka', UtilConst.IOT_TEST)
    util.speedUpConvergence()

def register_iot_devices_to_the_registration_server():
    add_user_to_registration_server()
    register_iot_devices()

def add_conditions_in_the_registration_server():
    add_conditions()
    
def configure_strong_authentication_network_devices():
    add_authentication_to_home_gateway()
    add_authentication_to_laptop()
    check_laptop_connected_to_home_gateway()
    configure_warehouse_router()
    
def configure_acl_to_restrict_traffic():
    configure_warehouse_router_acl()
    configure_cloud_service_provider_router_acl()
    
def configure_secure_web_communication_to_the_web_server():
    configure_csp_server()

def testing():
    check_motion_detector_triggered()
    for pc in [pc_1, pc_2]:
        check_unable_to_access_registration_server_from(pc)
        check_unable_to_access_via_http_from(pc)
        check_able_to_access_via_https_from(pc)

def add_user_to_registration_server():
    pc_1.select()
    pc_1.clickDesktopTab()
    pc_1.desktop.applications.webBrowser()
    pc_1.desktop.webBrowser.browse(REGISTRATION_SERVER_URL)
    pc_1.desktop.webBrowser.registrationServer.loginPage.signUpLink()
    pc_1.desktop.webBrowser.registrationServer.signUpPage.signUp(USERNAME, PASSWORD)
    pc_1.desktop.webBrowser.registrationServer.homePage.logoutLink()
    pc_1.close()
    
def register_iot_devices():
    for device in ioe_devices:
        device.select()
        device.clickConfigTab()
        device.config.settings.remoteServerRadio()
        device.config.settings.connect(REGISTRATION_SERVER_URL, USERNAME, PASSWORD)
        device.close()

def add_conditions():
    '''
    Conditions:
              ⦁    Name it LightsOn1, if MD status On is true, then set
              Directed Light status to On AND set CAM status On to true.
              ⦁    Name it LightsOn2, if TS status On is true, then set
              Directed Light status to On AND set CAM status On to true.
              ⦁    Name it LightsOff, if both MD status On is false AND
              TS status On is false, then set Directed Light
              status to Off AND set CAM status On to false.
    '''
    log_in_to_registration_server()
    pc_1.desktop.webBrowser.registrationServer.homePage.conditionsLink()
    pc_1.close()
    raise NotImplementedError('Unable to set conditions while writing this lab')

def add_authentication_to_home_gateway():
    add_authentication_to_device(home_gateway, 'Wireless')

def add_authentication_to_laptop():
    add_authentication_to_device(laptop, 'Wireless0')
    
def check_laptop_connected_to_home_gateway():
    util.speedUpConvergence()
    laptop.select()
    laptop.clickDesktopTab()
    laptop.desktop.applications.commandPrompt()
    laptop.desktop.commandPrompt.setText('ping %s' % (home_gateway.local_ip))
    util.fastForwardTime()
    laptop.desktop.commandPrompt.textCheckPoint('Received = [1234]')
    laptop.close()

def configure_warehouse_router():
    warehouse_router.select()
    warehouse_router.clickCliTab()
    warehouse_router.cli.startConsole()
    warehouse_router.cli.setCliText('enable',
                                    'configure terminal',
                                    'banner login %Login with valid password%',
                                    'banner motd %Authorized Access Only! Unauthorized access is subject to Federal Prosecution.%',
                                    'enable secret AbcWh001',
                                    'username WhAdmin secret AbcLine001',
                                    'line console 0',
                                    'login local',
                                    'line vty 0 4',
                                    'login local',
                                    'end')
    warehouse_router.close()
    
def configure_warehouse_router_acl():
    warehouse_router.select()
    warehouse_router.clickCliTab()
    warehouse_router.cli.setCliText('configure terminal',
                                    'access-list 10 permit host 172.18.1.5',
                                    'access-list 10 permit host 209.165.201.5',
                                    'interface g0/2',
                                    'ip access-group 10 out',
                                    'end')
    warehouse_router.close()
    
def configure_cloud_service_provider_router_acl():
    cloud_service_provider.select()
    cloud_service_provider.clickCliTab()
    cloud_service_provider.cli.startConsole()
    cloud_service_provider.cli.setCliText('enable',
                                          'configure terminal',
                                          'access-list 110 permit ip host 209.165.200.226 host 209.165.201.5',
                                          'access-list 110 deny ip any host 209.165.201.5',
                                          'access-list 110 permit ip any any',
                                          'interface g0/0',
                                          'ip access-group 110 out',
                                          'end')
    cloud_service_provider.close()

def configure_csp_server():
    csp_server.select()
    csp_server.clickServicesTab()
    csp_server.services.selectInterface('HTTP')
    csp_server.services.http.httpOff()
    csp_server.services.http.httpsOn()
    csp_server.close()
    
def check_motion_detector_triggered():
    trigger_motion_detector()
    check_light_on()
    check_cam_on()

def check_unable_to_access_registration_server_from(pc):
    check_able_to_access(pc, REGISTRATION_SERVER_URL, 'Request Timeout')
    
def check_unable_to_access_via_http_from(pc):
    check_able_to_access(pc, 'http://' + csp_server.ip, '(Request Timeout|Server Reset Connection)')

def check_able_to_access_via_https_from(pc):
    check_able_to_access(pc, 'https://' + csp_server.ip, 'Cisco Packet Tracer')
    
def trigger_motion_detector():
    motion_detector.deviceDragInteraction(-20, 0, 40, 0, 1)
    
def check_light_on():
    check_device_property_value(light, 'state', '1')
    
def check_cam_on():
    check_device_property_value(webcam, 'state', '1')
    
def add_authentication_to_device(device, interface):
    device.select()
    device.clickConfigTab()
    device.config.selectInterface(interface)
    device.config.interface.wireless.ssid(WIRELESS_SSID)
    device.config.interface.wireless.wpa2psk()
    device.config.interface.wireless.pskPassPhrase(WIRELESS_PASSWORD)
    device.close()

def log_in_to_registration_server():
    pc_1.select()
    pc_1.clickDesktopTab()
    pc_1.desktop.applications.webBrowser()
    pc_1.desktop.webBrowser.browse(REGISTRATION_SERVER_URL)
    pc_1.desktop.webBrowser.registrationServer.loginPage.signIn(USERNAME, PASSWORD)

def check_device_property_value(device, property, expected_value):
    device.select()
    device.clickTab('Attributes')
    actual_value = device.attribute.getPropertyValue(property)
    device.close()
    
    msg = 'Expected %s state to be %s got %s' % (device.displayName, expected_value, actual_value)
    functions.check(expected_value == actual_value, msg)

def check_able_to_access(device, url, expected_response):
    device.select()
    device.clickDesktopTab()
    device.desktop.applications.webBrowser()
    device.desktop.webBrowser.browse(url)
    util.speedUpConvergence()
    device.desktop.webBrowser.check.content(expected_response)
    device.close()