from API.ComponentBox import ComponentBoxConst
from API.Device.Switch.Switch import Switch
from API.Device.Router.Router import Router
from API.Device.Bridge.Bridge import Bridge
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import Modules
from API.Utility.Util import Util
from API.Utility import UtilConst
#Function initialization
util = Util()

#Device initialization
switch0 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950_24, 100, 200, "Switch0")
switch1 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2950T, 200, 200, "Switch1")
switch2 = Switch(ComponentBoxConst.DeviceModel.SWITCH_2960, 300, 200, "Switch2")
switch3 = Switch(ComponentBoxConst.DeviceModel.SWITCH_3560_24PS, 400, 200, "Multilayer Switch0")
switch4 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT, 500, 200, "Switch3")
switch5 = Switch(ComponentBoxConst.DeviceModel.SWITCH_PT_EMPTY, 600, 200, "Switch4")
bridge0 = Bridge(ComponentBoxConst.DeviceModel.BRIDGE_PT, 700, 200, "Bridge0")

def main():
    util.init()
    createTopology()
    powerOnOff()
    zoom()

def createTopology():
    for switch in [switch0, switch1, switch2, switch3, switch4, switch5, bridge0]:
        switch.create()
    util.fastForwardTime()
    
def powerOnOff():
    for switch in [switch0, switch1, switch2, switch3, switch4, switch5, bridge0]:
        switch.select()
        switch.clickConfigTab()
        if switch.config.popups.deviceMustBePoweredOnDialog:
            test.fail('Device is not powered on')
            switch.config.popups.deviceMustBePoweredOnOkButton()
        else:
            test.passes('The switch is powered on')
        switch.close()
        
    for switch in [switch4, switch5, bridge0]:
        switch.select()
        switch.clickPhysicalTab()
        if switch is switch4:    
            switch.physical.power(Modules.switch.s_pt.power)
        elif switch is switch5:
            switch.physical.power(Modules.switch.s_pt_empty.power)
        else:
            switch.physical.power(Modules.switch.s_bridge.power)
        switch.clickConfigTab()
        if switch.config.popups.deviceMustBePoweredOnDialog:
            test.passes('Device is not powered on')
            switch.config.popups.deviceMustBePoweredOnOkButton()
        else:
            test.fail('The switch is powered on')
        switch.close()

def zoom():
    switch0.select()
    switch0.clickPhysicalTab()
    switch0.physical.zoomIn()
    checkRange(switch0.physical.imageObject.maximumSize.width, 942)

    switch0.physical.zoomOriginal()
    checkRange(switch0.physical.imageObject.maximumSize.width, 471)

    for i in range(2):
        switch0.physical.zoomOut()
    checkRange(switch0.physical.imageObject.maximumSize.width, 235)
      
    switch0.close()
    switch1.select()
    switch1.clickPhysicalTab()
    switch1.physical.zoomIn()
    snooze(2)
    checkRange(switch1.physical.imageObject.maximumSize.width, 942)

    switch1.physical.zoomOriginal()
    snooze(2)
    checkRange(switch1.physical.imageObject.maximumSize.width, 471)
    for i in range(2):
        switch1.physical.zoomOut()
    snooze(2)
    checkRange(switch1.physical.imageObject.maximumSize.width, 235)
      
    switch1.close()
    switch2.select()
    switch2.clickPhysicalTab()
    switch2.physical.zoomIn()
    snooze(2)
    checkRange(switch2.physical.imageObject.maximumSize.width, 943)
    switch2.physical.zoomOriginal()

    snooze(2)
    checkRange(switch2.physical.imageObject.maximumSize.width, 471)
    for i in range(2):
        switch2.physical.zoomOut()
    snooze(2)
    checkRange(switch2.physical.imageObject.maximumSize.width, 235)
        
    switch2.close()
    switch3.select()
    switch3.clickPhysicalTab()
    switch3.physical.zoomIn()
    snooze(2)
    checkRange(switch3.physical.imageObject.maximumSize.width, 942)
    switch3.physical.zoomOriginal()
    snooze(2)
    checkRange(switch3.physical.imageObject.maximumSize.width, 471)
    for i in range(2):
        switch3.physical.zoomOut()
    snooze(2)
    checkRange(switch3.physical.imageObject.maximumSize.width, 235)
      
    switch3.close()
    switch4.select()
    switch4.clickPhysicalTab()
    switch4.physical.zoomIn()
    snooze(2)
    checkRange(switch4.physical.imageObject.maximumSize.width, 942)
    switch4.physical.zoomOriginal()
    snooze(2)
    checkRange(switch4.physical.imageObject.maximumSize.width, 471)
    for i in range(2):
        switch4.physical.zoomOut()
    snooze(2)
    checkRange(switch4.physical.imageObject.maximumSize.width, 235)
      
    switch4.close()
    switch5.select()
    switch5.clickPhysicalTab()
    switch5.physical.zoomIn()
    snooze(2)
    checkRange(switch5.physical.imageObject.maximumSize.width, 942)
    switch5.physical.zoomOriginal()
    snooze(2)
    checkRange(switch5.physical.imageObject.maximumSize.width, 471)
    for i in range(2):
        switch5.physical.zoomOut()
    snooze(2)
    checkRange(switch5.physical.imageObject.maximumSize.width, 235)
      
    switch5.close()
    util.clickOnWorkspace(bridge0.x, bridge0.y)
    bridge0.select()
    bridge0.clickPhysicalTab()
    bridge0.physical.zoomIn()
    # Verification Point 'VP2'
    snooze(2)
    checkRange(bridge0.physical.imageObject.maximumSize.width, 442)
    bridge0.physical.zoomOriginal()
    snooze(2)
    checkRange(bridge0.physical.imageObject.maximumSize.width, 221)
    for i in range(2):
        bridge0.physical.zoomOut()
    snooze(2)
    checkRange(bridge0.physical.imageObject.maximumSize.width, 110)

def checkRange(size, x):
    if size in range(x-15, x+15):
        test.passes("")
    else:
        test.fail("")
    
