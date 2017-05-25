class MainContextMenu:
    OPTIONS = ':options_HTML_Object'
    PLACE_NOTE   = ':notes_HTML_Object'
    END_DEVICES = ':end_devices_HTML_Object'
    ROUTERS = ':routers_HTML_Object'
    SWITCHES = ':switches_HTML_Object'
    WIRELESS = ':wireless_HTML_Object'
    CLOUD = ':cloud_HTML_Object'
    SECURITY = ':security_HTML_Object'
    HUBS = ':hubs_HTML_Object'
    SHAPES = ':shapes_HTML_Object'
    MULTI_SELECT = ':multiSelect_HTML_Object'
            
class EndSubMenuConst:
    SNIFFER = ":Sniffer_HTML_Object"
    WIRELESS_END_DEVICE = ":WirelessEndDevice-PT_HTML_Object"
    WIRED_END_DEVICE = ":WiredEndDevice-PT_HTML_Object"
    PRINTER = ":Printer-PT_HTML_Object"
    IP_PHONE = ":7960_HTML_Object"
    VOIP = ":Home-VoIP-PT_HTML_Object"
    ANALOG_PHONE = ":Analog-Phone-PT_HTML_Object"
    SERVER = ":Server-PT_HTML_Object"
    TV = ":TV-PT_HTML_Object"
    PDA = ":SMARTPHONE-PT_HTML_Object"
    TABLET = ":TabletPC-PT_HTML_Object"
    LAPTOP = ":Laptop-PT_HTML_Object"
    WIRELESS_PC = ":Wireless PC_HTML_Object"
    PC = ":PC-PT_HTML_Object"
            
class RouterSubMenuConst:
    ROUTER_PT = ':Router-PT_HTML_Object'
    ROUTER_2911 = ":2911_HTML_Object"
    ROUTER_2901 = ":2901_HTML_Object"
    ROUTER_2811 = ":2811_HTML_Object"
    ROUTER_2621XM = ":2621XM_HTML_Object"
    ROUTER_2620XM = ":2620XM_HTML_Object"
    ROUTER_1941 = ":1941_HTML_Object"
    ROUTER_1841 = ":1841_HTML_Object"
    ROUTER_PT_EMPTY = ":Router-PT-Empty_HTML_Object"
    
class SwitchSubMenuConst:
    SWITCH_PT_EMPTY = ":Switch-PT-Empty_HTML_Object"
    SWITCH_3560 = ":3560-24PS_HTML_Object"
    SWITCH_2950 = ":2950-24_HTML_Object"
    SWITCH_2950T = ":2950T_HTML_Object"
    SWITCH_2960 = ":2960_HTML_Object"
    SWITCH_PT = ":Switch-PT_HTML_Object"
    BRIDGE_PT = ":Bridge-PT_HTML_Object"
    
class WirelessSubMenuConst:
    ACCESS_POINT_N = ":AccessPoint-PT-N_HTML_Object"
    ACCESS_POINT_A = ":AccessPoint-PT-A_HTML_Object"
    ACCESS_POINT_PT = ":AccessPoint-PT_HTML_Object"
    LINKSYS_ROUTER = ":Linksys-WRT300N_HTML_Object"
    CELL_TOWER = ":Cell-Tower_HTML_Object"
    CO_SERVER = ":Central-Office-Server_HTML_Object"
    
class CloudSubMenuConst:
    CLOUD_PT_EMPTY = ":Cloud-PT-Empty_HTML_Object"
    CLOUD_PT = ":Cloud-PT_HTML_Object"
    CABLE_MODEM = ":Cable-Modem-PT_HTML_Object"
    DSL_MODEM = ":DSL-Modem-PT_HTML_Object"
            
class SecuritySubMenuConst:
    ASA_5505 = ":5505_HTML_Object"
            
class HubsSubMenuConst:
    HUB = ":Hub-PT_HTML_Object"
    COAXIAL_SPLITTER = ":CoAxialSplitter-PT_HTML_Object"
    REPEATER = ":Repeater-PT_HTML_Object"
    None

class ShapeSubMenuConst:
    LINE = ":LineCreate_HTML_Object"
    RECTANGLE = ":RectangleCreate_HTML_Object"
    ELLIPSE = ":EllipseCreate_HTML_Object"
    OPTIONS = ":Options_HTML_Object"
    OPTIONS_DRAW = ':openShapeOptions_HTML_Object'  #this one is when you are in already in Draw mode, and you bring up the menu
    SHAPE_EDIT = ':shapesDisabled_HTML_Object'
    EXIT = ":exitMode_HTML_Object"

class MultiSelectMenuConst:
    SINGLE_SELECT = ''
    DRAG_SELECT = ''
    SHAPES_EDIT = ''

class DeviceContextMenu:
    DELETE = ':delete_HTML_Object'
    COPY = ":copy_HTML_Object"
    INSPECT = ":inspect_HTML_Object"
    PHYSICAL = ":physical_HTML_Object"
    ADD_COMPLEX_PDU = ":addComplexPDU_HTML_Object"
    ADD_PDU = ":addSimplePDU_HTML_Object"
    CONNECT = ":link_HTML_Object"
    MULTI_SELECT = ":multiSelect_HTML_Object"
    AUTO_CONNECT = ":autoConnect_HTML_Object"
    RENAME = ":rename_HTML_Object"
    None
    
class EndDeviceContextMenu(DeviceContextMenu):
    DESKTOP = ":desktop_HTML_Object"
    None
    
class CliDeviceContextMenu(DeviceContextMenu):
    CONSOLE = ":console_HTML_Object"
    None
    
class CableDevices:
    CHOOSE_CABLE = ":layer0IDBGID_HTML_Object"
    COAXIAL = ":8110_HTML_Object"
    CONSOLE = ":8108_HTML_Object"
    #SERIAL_DCE = ":x-button-3_HTML_Object"
    SERIAL_DCE = ":8106_HTML_Object"
    SERIAL_DTE = ":x-button-4_HTML_Object"
    PHONE = ":x-button-5_HTML_Object"
    FIBER = ":8103_HTML_Object"
    CROSSOVER = ":8101_HTML_Object"
    STRAIGHT = ":8100_HTML_Object"
    OCTAL = ":8111_HTML_Object"
	#CABLE = ":ext-container-10_HTML_Object"
    None

class InspectSubMenuConst:
    PORT_STATUS = ':PortStatus_HTML_Object'
    QOS = ':QoS_HTML_Object'
    NAT = ':NAT_HTML_Object'
    ARP = ':ARP_HTML_Object'
    IPV6_ROUTES = ':IPv6Routing_HTML_Object'
    IPV4_ROUTES = ':Routing_HTML_Object'
    
class MultiSelectMenuConst:
    DELETE = ':delete_HTML_Object'
    SINGLE_SELECT = ':touchSelect_HTML_Object'
    UNSELECT = ':unselect_HTML_Object'
    EXIT_MODE = ':exitMode_HTML_Object'
    CLUSTER = ':newCluster_HTML_Object'
    DRAG_SELECT = ':dragSelect_HTML_Object'
    
class ClusterSubMenuConst:
    ENTER = ":enter_HTML_Object"
    

class NotesMenu:
    EDIT = ':edit_HTML_Object'
    DELETE = ':delete_HTML_Object'
    MULTI_SELECT = ':multiSelect_HTML_Object'
    