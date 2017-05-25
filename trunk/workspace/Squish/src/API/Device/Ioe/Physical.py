#@author: Chris Allen

from API.Device.DeviceBase import PhysicalBase
from API.Device.Ioe import IoeConst
from API.Utility.Util import Util
from squish import *
import object

class Physical(PhysicalBase):
    def __init__(self):
        self.squishName = ""
        self.util = Util()
        
    #@summary: update the actual name of object that squish uses to reference
    #@param p_squishName: display name of the device         
    def updateName(self, p_squishName):
        self.squishName = p_squishName
        super(Physical, self).updateName(self.squishName)
    
    def addNetworkModule(self, p_moduleName):
        self.scrollTo(IoeConst.Physical.MODULE_LIST_VERTICAL_SCROLLBAR, 0)
        if not p_moduleName.startswith('PT'):
            p_moduleName = ''.join(['PT-IOE-NM-1', p_moduleName.upper()])
        slot = findObject(self.squishName + IoeConst.Physical.Modules.NETWORK_MODULE_SLOT)
        networkModule = findObject(self.squishName + IoeConst.Physical.Modules.MODULE_BASE + p_moduleName)
        self.util.dragAndDrop(networkModule, int(networkModule.width/2), int(networkModule.height/2), slot, int(slot.width/2), int(slot.height/2))
        
    def addIoeModule(self, p_moduleName):
        sensors = ['ATOMOSPHERIC_PRESSURE_SENSOR', 'CLOCK', 'CO2_DETECTOR', 'CO_DETECTOR', 'HUMIDITY_SENSOR',
                   'MOTION_DETECTOR', 'PHOTO_SENSOR', 'RAIN_SENSOR', 'SCALE', 'SMOKE_DETECTOR', 'TEMPERATURE_SENSOR',
                   'TIMER', 'TRIP_SENSOR', 'WATER_DETECTOR', 'WEBCAM', 'WINDOW', 'WIND_SENSOR']
        actuators = ['APPLIANCE', 'CEILING_FAN', 'FIRE_SPRINKLER', 'HUMIDIFIER', 'LAWN_SPRINKLER', 'LIGHT',
                     'ON_OFF_DEVICE', 'SIREN']
        other = ['DOOR', 'GARAGE_DOOR', 'SOLAR_PANEL', 'THERMOSTAT', 'WIND_GENERATOR']
        #if ord(p_moduleName[0].upper()) >= ord('S'):
        #    height = findObject(self.squishName + IoeConst.Physical.MODULE_LIST_VERTICAL_SCROLLBAR).height
        #    self.scrollTo(IoeConst.Physical.MODULE_LIST_VERTICAL_SCROLLBAR, height)
        #else:
        #    self.scrollTo(IoeConst.Physical.MODULE_LIST_VERTICAL_SCROLLBAR, 0)
        module = '_'.join(p_moduleName.split(' ')).upper()
        if module.upper() in sensors:
            self.scrollTo(IoeConst.Physical.MODULE_LIST_VERTICAL_SCROLLBAR, 88)
        else:
             height = findObject(self.squishName + IoeConst.Physical.MODULE_LIST_VERTICAL_SCROLLBAR).height
             self.scrollTo(IoeConst.Physical.MODULE_LIST_VERTICAL_SCROLLBAR, height)
        if len(p_moduleName.split(' ')) > 1:
            p_moduleName = '_'.join(p_moduleName.split(' '))
        slot = findObject(self.squishName + IoeConst.Physical.Modules.IOE_MODULE_SLOT)
        ioeModule = findObject(self.squishName + IoeConst.Physical.Modules.MODULE_BASE + p_moduleName.upper())
        self.util.dragAndDrop(ioeModule, int(ioeModule.width/2), int(ioeModule.height/2), slot, int(slot.width/2), int(slot.height/2))
        self.scrollTo(IoeConst.Physical.MODULE_LIST_VERTICAL_SCROLLBAR, 0)#Return to 0 after done
        
        pass
        
    def removeIoeModule(self, p_moduleName):
        self.maximizeDeviceWindow()
        if len(p_moduleName.split(' ')) > 1:
            p_moduleName = '_'.join(p_moduleName.split(' '))
        slot = findObject(self.squishName + IoeConst.Physical.Modules.IOE_MODULE_SLOT)
        ioeModule = findObject(self.squishName + IoeConst.Physical.Modules.MODULE_BASE + p_moduleName.upper())
        self.scrollTo(IoeConst.Physical.MODULE_LIST_VERTICAL_SCROLLBAR, 237)
        self.util.dragAndDrop(slot, int(slot.width/2), int(slot.height/2), ioeModule, int(ioeModule.width/2), int(ioeModule.height/2))
        self.restoreWindow()
        
        pass