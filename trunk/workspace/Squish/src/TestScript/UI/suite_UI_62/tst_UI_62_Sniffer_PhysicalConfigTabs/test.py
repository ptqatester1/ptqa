########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.Sniffer.Sniffer import Sniffer
from API.Device.EndDevice.Sniffer import SnifferConst
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import Modules

util = Util()
sniffer = Sniffer(ComponentBoxConst.DeviceModel.SNIFFER, 175, 80, 'Sniffer0')

def main():
    util.init()
    create()
    checkConfigTab()
    checkModulesDesc()
    checkZoom()
    checkModuleReplace()
    checkCustomizeIconButtons()
    
def create():    
    sniffer.create()
    sniffer.select()
    
def checkConfigTab():
    sniffer.clickConfigTab()
    sniffer.config.settings.displayName('SNFR')
    sniffer.config.settings.check.displayName('SNFR')
    
def checkModulesDesc():
    sniffer.clickPhysicalTab()
    sniffer.physical.selectModule('PT-REPEATER-NM-1CE')
    sniffer.physical.checkModuleText("The PT-REPEATER-NM-1CE features a single Ethernet port that can connect a LAN backbone which can also support either six PRI connections to aggregate ISDN lines, or 24 synchronous/asynchronous ports.")

    sniffer.physical.selectModule('PT-REPEATER-NM-1CFE')
    sniffer.physical.checkModuleText("The PT-REPEATER-NM-1CFE Module provides one Fast-Ethernet interface for use with copper media. Ideal for a wide range of LAN applications, the Fast Ethernet network modules support many internetworking features and standards. Single port network modules offer autosensing 10/100BaseTX or 100BaseFX Ethernet. The TX (copper) version supports virtual LAN (VLAN) deployment.", escape=True)

    sniffer.physical.selectModule('PT-REPEATER-NM-1CGE')
    sniffer.physical.checkModuleText("The single-port Cisco Gigabit Ethernet Network Module (part number PT-REPEATER-NM-1CGE) provides Gigabit Ethernet copper connectivity for access routers. The module is supported by the Cisco 2691, Cisco 3660, Cisco 3725, and Cisco 3745 series routers. This network module has one gigabit interface converter (GBIC) slot to carry any standard copper or optical Cisco GBIC.", escape=True)

    sniffer.physical.selectModule('PT-REPEATER-NM-1FFE')
    sniffer.physical.checkModuleText("The PT-REPEATER-NM-1FFE Module provides one Fast-Ethernet interface for use with fiber media. Ideal for a wide range of LAN applications, the Fast Ethernet network modules support many internetworking features and standards. Single port network modules offer autosensing 10/100BaseTX or 100BaseFX Ethernet.", escape=True)

    sniffer.physical.selectModule('PT-REPEATER-NM-1FGE')
    sniffer.physical.checkModuleText("The single-port Cisco Gigabit Ethernet Network Module (part number PT-REPEATER-NM-1FGE) provides Gigabit Ethernet optical connectivity for access routers. The module is supported by the Cisco 2691, Cisco 3660, Cisco 3725, and Cisco 3745 series routers. This network module has one gigabit interface converter (GBIC) slot to carry any standard copper or optical Cisco GBIC.", escape=True)

def checkZoom():
    test.compare(sniffer.physical.imageObject.width, 150)
    test.compare(sniffer.physical.imageObject.height, 55)

    sniffer.physical.zoomIn()
    test.compare(sniffer.physical.imageObject.width, 300)
    test.compare(sniffer.physical.imageObject.height, 110)

    for i in range(2):
        sniffer.physical.zoomOut()
    test.compare(sniffer.physical.imageObject.width, 100)
    test.compare(sniffer.physical.imageObject.height, 36)
    
    sniffer.physical.zoomOut()
    test.compare(sniffer.physical.imageObject.width, 75)
    test.compare(sniffer.physical.imageObject.height, 27)

    sniffer.physical.zoomOriginal()
    test.compare(sniffer.physical.imageObject.width, 150)
    test.compare(sniffer.physical.imageObject.height, 55)

def remove_from_port_0():
    sniffer.physical.removeModule(Modules.endDevice.sniffer.slot0)
    
def remove_from_port_1():
    sniffer.physical.removeModule(Modules.endDevice.sniffer.slot1)

def add_module_to_slot_0(module_name):
    sniffer.physical.addModule(module_name, Modules.endDevice.sniffer.slot0)

def add_module_to_slot_1(module_name):
    sniffer.physical.addModule(module_name, Modules.endDevice.sniffer.slot1)

def checkModuleReplace():    
    remove_from_port_0() 
    clickButton(waitForObject(":Error.qt_msgbox_buttonbox.OK"))
    sniffer.physical.power(Modules.endDevice.sniffer.power)    
    
    remove_from_port_0()
    remove_from_port_1()
    
    add_module_to_slot_0('PT-REPEATER-NM-1CE')
    add_module_to_slot_1('PT-REPEATER-NM-1CFE')
    
    remove_from_port_0()
    remove_from_port_1()
    
    add_module_to_slot_0('PT-REPEATER-NM-1CGE')
    add_module_to_slot_1('PT-REPEATER-NM-1FFE')
    
    remove_from_port_0()
    remove_from_port_1()
    
    add_module_to_slot_0('PT-REPEATER-NM-1FGE')
    add_module_to_slot_1('PT-REPEATER-NM-1CE')
    
    sniffer.physical.power(Modules.endDevice.sniffer.power)    
    
def checkCustomizeIconButtons():
    sniffer.physical.customizeIconInPhysicalViewButton()
    clickButton(waitForObject(":CBaseDeviceWidgetClass.CBaseCustomImage.m_okButton"))
    
    sniffer.physical.customizeIconInLogicalViewButton() 