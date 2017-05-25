########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.CellTower.CellTower import CellTower
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase import DeviceBaseConst
from API.functions import trace, check
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import Modules
util = Util()
cell = CellTower(ComponentBoxConst.DeviceModel.CELL_TOWER, 175, 80, 'Cell Tower0')

def main():
    util.init()
    create()
    checkConfigTab()
    checkModulesDesc()
    checkZoom()
    checkModuleReplace()
    checkCustomizeIconButtons()
    
def create():
    cell.create()
    cell.select()

def checkConfigTab():
    cell.clickConfigTab()
    cell.config.settings.displayName('Cell')
    cell.config.settings.check.displayName('Cell')
    
    cell.config.selectInterface("Coaxial0")
    test.compare(waitForObject(":CBaseDeviceWidgetClass.c_physicalTab.qt_tabwidget_stackedwidget.m_menuCfgTab.BaseIntCfgUniversal.mainScrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents_2.noconfigLabel").text, "Configurations are not available.", trace('test.py'))
    test.fail("it is reminder to add Coaxial0 UI tests when they are implemented.", trace('test.py'))
    cell.config.selectInterface("3G/4G Server1")
    cell.config.interface.cellular.check.portStatus(True)
    cell.config.interface.cellular.check.coverageRange('1000.00')
    
    
def checkModulesDesc():
    cell.clickPhysicalTab()
    cell.physical.selectModule('PT-CELL-NM-1CX')
    cell.physical.checkModuleText("The PT-CELL-NM-1CX card features a single coaxial connector, which is used for a cable modem service connection.")

    cell.physical.selectModule('PT-CELL-NM-3G/4G')
    cell.physical.checkModuleText("The PT-CELL-NM-3G/4G module provides one cellular interface suitable for connection to 3G/4G networks.")

def checkZoom():        
    physicalImage = cell.physical.imageObject
    test.compare(physicalImage.width, 233, trace('test.py'))
    test.compare(physicalImage.height, 60, trace('test.py'))

    cell.physical.zoomIn()
    test.compare(physicalImage.width, 467, trace('test.py'))
    test.compare(physicalImage.height, 120, trace('test.py'))

    for i in range(2):
        cell.physical.zoomOut()
    test.compare(physicalImage.width, 155, trace('test.py'))
    test.compare(physicalImage.height, 40, trace('test.py'))
    
    cell.physical.zoomOut()
    test.compare(physicalImage.width, 116, trace('test.py'))
    test.compare(physicalImage.height, 30, trace('test.py'))

    cell.physical.zoomOriginal()
    test.compare(physicalImage.width, 233, trace('test.py'))
    test.compare(physicalImage.height, 60, trace('test.py'))
    
def removeModule(num):
    try:
        cell.dragAndDrop(CellTowerConst.Physical.SLOT_BASE + num, 16, 15, CellTowerConst.Physical.Module.PT_CELL_NM_1CX, 79, 12)
    except LookupError, e:
        None
    except Exception, e:
        raise
    

def checkModuleReplace():
    cell.physical.removeModule(Modules.wireless.cell_tower.slot0)
    
    cell.physical.addModule('PT-CELL-NM-1CX', Modules.wireless.cell_tower.slot0)
    cell.physical.removeModule(Modules.wireless.cell_tower.slot0)
    
    cell.physical.addModule('PT-CELL-NM-3G/4G', Modules.wireless.cell_tower.slot0)
    cell.physical.removeModule(Modules.wireless.cell_tower.slot0)
    

def checkCustomizeIconButtons():
    cell.physical.customizeIconInPhysicalViewButton()
    cell.physical.customView.okButton()
    
    cell.physical.customizeIconInLogicalViewButton() 
    cell.physical.customView.okButton()
