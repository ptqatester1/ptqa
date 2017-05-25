########################################
#@author: Chris Allen                  #
#@summary: Constants for device cabling#
########################################

from API.Android.ContextMenus.ContextMenusConst import CableDevices

class CableTypeMenu:
    OCTAL = CableDevices.OCTAL
    COAXIAL = CableDevices.COAXIAL
    CONSOLE = CableDevices.CONSOLE
    CROSSOVER = CableDevices.CROSSOVER
    FIBER = CableDevices.FIBER
    PHONE = CableDevices.PHONE
    SERIAL_DCE = CableDevices.SERIAL_DCE
    SERIAL_DTE = CableDevices.SERIAL_DTE
    STRAIGHT = CableDevices.STRAIGHT
    CHOOSE_CABLE = CableDevices.CHOOSE_CABLE
    
    CONNECTION_VIEW = ':ConnectionView_HTML_Object'
    CHOOSE_CABLE_VIEW = ':drawComponentID-main_HTML_Object'
	
class PortInterface: 
	PORT_BASE = ":webview.x-connection-"
	PORT_END = "_HTML_Object"
