#**************************************************************************
#@author: Thi Nguyen
#@summary: ComponentBoxConst hold common constant used in device type box
#and device specific box
#**************************************************************************
NETWORK_COMPONENT_BOX = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox"
DEVICE_TYPES_WIDGET = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget"
DEVICE_SPECIFIC_WIDGET = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1"
COMPONENTBOX_LABEL = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceLabel1"
SEARCH_LINE_EDIT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.QLineEdit1"
SEARCH_COMPONENT_BOX = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea17.qt_scrollarea_viewport.QWidget1'
TEMPLATE_COMPONENT_BOX = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea16.qt_scrollarea_viewport.QWidget1"

class DeviceGroup:
    NETWORK_DEVICES = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Network Devices'
    END_DEVICES = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceButton5'
    COMPONENTS = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Components'
    CONNECTIONS = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceButton3'
    MISCELLANEOUS = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceButton7'
    MULTIUSER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceButton1'
    
class DeviceType:
    ROUTER = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Routers"
    SWITCH = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Switches"
    HUB = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Hubs"
    WIRELESS_DEVICE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Wireless Devices"
    SECURITY = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Security"
    WAN = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.WAN Emulation"
    
    END_DEVICE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceButton5"
    HOME = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Home'
    SMART_CITY = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Smart City'
    INDUSTRIAL = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Industrial'
    POWER_GRID = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Power Grid'
    
    BOARDS = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Boards'
    ACTUATORS = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Actuators'
    SENSORS = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.Sensors'
    
    CONNECTION = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceButton3"
    
    #MISCELLANEOUS = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceButton8'
    MISCELLANEOUS = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceButton7'
    
    MULTIUSER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceTypesWidget.CDeviceButton1'
    
class DeviceModel:
    #Routers
    ROUTER_1941 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton2"
    ROUTER_2901 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton6"
    ROUTER_2911 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton7"
    ROUTER_819_IOX = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton8"
    ROUTER_819 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton9"
    ROUTER_829 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton10"
    ROUTER_1240 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton11"
    ROUTER_4321 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton12"
    ROUTER_PT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton13"
    ROUTER_PT_EMPTY = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton14"
    ROUTER_1841 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    ROUTER_2620XM = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton3"
    ROUTER_2621XM = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton4"
    ROUTER_2811 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea1.qt_scrollarea_viewport.QWidget1.CDeviceButton5"
    
    #Switches 
    SWITCH_2960 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea2.qt_scrollarea_viewport.QWidget1.CDeviceButton3"
    SWITCH_PT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea2.qt_scrollarea_viewport.QWidget1.CDeviceButton4"
    SWITCH_PT_EMPTY = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea2.qt_scrollarea_viewport.QWidget1.CDeviceButton5"
    SWITCH_3560_24PS = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea2.qt_scrollarea_viewport.QWidget1.CDeviceButton6"
    SWITCH_3650_24PS = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea2.qt_scrollarea_viewport.QWidget1.CDeviceButton7"
    SWITCH_IE_2000 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea2.qt_scrollarea_viewport.QWidget1.CDeviceButton8"
    BRIDGE_PT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea2.qt_scrollarea_viewport.QWidget1.CDeviceButton9"
    SWITCH_2950_24 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea2.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    SWITCH_2950T = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea2.qt_scrollarea_viewport.QWidget1.CDeviceButton2"
   
    #Hubs
    HUB_PT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea3.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    REPEATER_PT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea3.qt_scrollarea_viewport.QWidget1.CDeviceButton2"
    COAXIAL_SPLITTER_PT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea3.qt_scrollarea_viewport.QWidget1.CDeviceButton3"
    
    #Wireless Device
    ACCESSPOINT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    ACCESSPOINT_A = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton2"
    ACCESSPOINT_AC = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton3"
    ACCESSPOINT_N = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton4"
    LINKSYS = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton5"
    HOME_GATEWAY = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton6"
    CELL_TOWER = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton7"
    CO_SERVER = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton8"
    WLC_2504 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton9"
    WLC_PT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton10"
    LAP_3702i = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton11"
    LAP_PT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea4.qt_scrollarea_viewport.QWidget1.CDeviceButton12"
    
    
    #Security
    ASA_5505 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea8.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    
    #WAN
    CLOUD = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea9.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    CLOUD_EMPTY = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea9.qt_scrollarea_viewport.QWidget1.CDeviceButton2"
    DSL_MODEM = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea9.qt_scrollarea_viewport.QWidget1.CDeviceButton3"
    CABLE_MODEM = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea9.qt_scrollarea_viewport.QWidget1.CDeviceButton4"
    
    #End Devices
    PC = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    LAPTOP = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton2"
    SERVER = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton3"
    PRINTER = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton4"
    IPPHONE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton5"
    VOIP = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton6"
    ANALOG_PHONE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton7"
    TV = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton8"
    TABLET_PC = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton9"
    PDA = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton10"
    WIRELESS_END_DEVICE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton11"
    WIRED_END_DEVICE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton12"
    SNIFFER = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea7.qt_scrollarea_viewport.QWidget1.CDeviceButton13"
        
    #Home
    IOE_APPLIANCE = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton1'
    IOE_BATTERY = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton2'
    IOE_CEILING_FAN = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton5'
    IOE_DOOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton4'
    IOE_FIRE_SPRINKLER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton5'
    IOE_GARAGE_DOOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton6'
    IOE_HOME_SPEAKER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton7'
    IOE_HUMIDIFIER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton8'
    IOE_HUMIDITY_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton9'
    IOE_HUMITURE_MONITOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton10'
    IOE_LAWN_SPRINKLER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton11'
    IOE_LIGHT = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton12'
    IOE_SUN = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton13'
    IOE_WEBCAM = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton14'
    IOE_WINDOW = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1.CDeviceButton15'
    
    #Smart City
    IOE_ATM_PRESSURE_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton1'
    IOE_CO2_DETECTOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton3'
    IOE_CO_DETECTOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton4'
    IOE_OLD_CAR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton5'
    IOE_PUSH_BUTTON_TOGGLE_SWITCH = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton6'
    IOE_RFID_CARD = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton7'
    IOE_RFID_READER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton8'
    IOE_SOLAR_PANEL = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton9'
    IOE_STREET_LAMP = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton10'
    IOE_WIND_TURBINE = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea11.qt_scrollarea_viewport.QWidget1.CDeviceButton11'
    
    #Industrial
    IOE_FIRE_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea12.qt_scrollarea_viewport.QWidget1.CDeviceButton2'
    IOE_SERVO = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea12.qt_scrollarea_viewport.QWidget1.CDeviceButton6'
    IOE_SIGNAL_GENERATOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea12.qt_scrollarea_viewport.QWidget1.CDeviceButton7'
    IOE_TRIP_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea12.qt_scrollarea_viewport.QWidget1.CDeviceButton8'
    
    #Power Grid
    POWER_METER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea13.qt_scrollarea_viewport.QWidget1.CDeviceButton2'
    
    #Components
    IOE_MCU = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea5.qt_scrollarea_viewport.QWidget1.CDeviceButton1'
    IOE_SBC = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea5.qt_scrollarea_viewport.QWidget1.CDeviceButton2'
    IOE_THING = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea5.qt_scrollarea_viewport.QWidget1.CDeviceButton3'
    
    #Actuator
    IOE_LCD = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea14.qt_scrollarea_viewport.QWidget1.CDeviceButton4'
    IOE_MOTOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea14.qt_scrollarea_viewport.QWidget1.CDeviceButton6'
    IOE_PIEZO_SPEAKER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea14.qt_scrollarea_viewport.QWidget1.CDeviceButton7'
    RGB_LED = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea14.qt_scrollarea_viewport.QWidget1.CDeviceButton8'
    LED = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea14.qt_scrollarea_viewport.QWidget1.CDeviceButton8'
    IOE_SIREN = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea14.qt_scrollarea_viewport.QWidget1.CDeviceButton10'
    SMART_LED = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea14.qt_scrollarea_viewport.QWidget1.CDeviceButton11'
    IOE_SMOKE_DETECTOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea14.qt_scrollarea_viewport.QWidget1.CDeviceButton12'
    
    #Sensor
    IOE_FLEX_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton1'
    IOE_GENERIC_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton2'
    IOE_LED = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton3'
    IOE_MEMBRANE_POTENTIOMETER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton4'
    IOE_METAL_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton5'
    IOE_MOTION_DETECTOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton6'
    IOE_PHOTO_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton7'
    IOE_POTENTIOMETER = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton8'
    IOE_PUSH_BUTTON_TOGGLE = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton10'
    IOE_PUSH_BUTTON = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton11'
    SOUND_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton12'
    IOE_SWITCH = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton13'
    TEMPERATURE_MONITOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton14'
    IOE_TEMPERATURE_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton15'
    IOE_THERMOSTAT = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton16'
    WATER_LEVEL_MONITOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton18'
    IOE_WIND_SENSOR = ':CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea15.qt_scrollarea_viewport.QWidget1.CDeviceButton19'
    
    #Miscellaneous
    CUSTOM_1841 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea16.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    CUSTOM_2621XM = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea16.qt_scrollarea_viewport.QWidget1.CDeviceButton2"
    CUSTOM_2811 = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea16.qt_scrollarea_viewport.QWidget1.CDeviceButton3"
    CUSTOM_WIRELESS_PC = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea16.qt_scrollarea_viewport.QWidget1.CDeviceButton4"
    #Multiuser
    MULTIUSER = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea19.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    
    #Misc
    CUSTOM_TEMPLATE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea16.qt_scrollarea_viewport.QWidget1"
    CUSTOM_DEVICES_SPECIFIC_BOX = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea10.qt_scrollarea_viewport.QWidget1"
    MODEL_LABEL_BOX = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget. (Select a Device to Drag and Drop to the Workspace)"

class Connection:
    CONN_AUTO = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton1"
    CONN_CONSOLE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton2"
    CONN_STRAIGHT = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton3"
    CONN_CROSS = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton4"
    CONN_FIBER = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton5"
    CONN_PHONE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton6"
    CONN_COAXIAL = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton7"
    CONN_SERIAL_DCE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton8"
    CONN_SERIAL_DTE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton9"
    CONN_OCTAL = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton10"
    CONN_IOE = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton11"
    CONN_USB = ":CAppWindowBase.centralwidget.m_pNetWorkCompBoxFrame.QSplitter1.CNetworkComponentBox.DeviceSpecificWidget.QScrollArea6.qt_scrollarea_viewport.QWidget1.CDeviceButton12"