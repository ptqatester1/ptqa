from API.Toolbar.MainToolBar.MainToolbarConst import MainToolbarConst
from API.Utility.Util import Util
from API.Device.Router.Router import Router
from API.Toolbar.MainToolBar.CustomDeviceWindowConst import CustomDeviceWindowConst
from API.ComponentBox import ComponentBoxConst
import test
from API.Toolbar.MainToolBar.CustomDeviceWindow import CustomDeviceWindow
from API import functions

#Function initialization
util = Util()
cdw = CustomDeviceWindow()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 100, 100, "Router0")
router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 200, 100, "Router1")
router2 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 300, 100, "Router2")

def main():
    util.init()
    addNewTemplate()
    addExistingTemplateCancel()
    addExistingTemplateSameName()    
    addExistingTemplateDifferentName()

def cleanup():
    removeTemplate()
    
def addNewTemplate():
    router0.create()
    cdw.goToTemplateManager()
    cdw.addTemplate(router0, 'FirstRouter1841Template', 'FirstRouter1841Template', 'Misc')
    if object.exists(ComponentBoxConst.DeviceModel.CUSTOM_TEMPLATE + ".CDeviceButton5"):
        test.passes("New Device button exists")
    else:
        test.fail("New Device button does not exist")
    
def addExistingTemplateCancel():
    cdw.goToTemplateManager()
    cdw.addTemplate(router0, 'FirstRouter1841Template', 'FirstRouter1841Template', 'Misc', '', newFileName=False)
    if object.exists(ComponentBoxConst.DeviceModel.CUSTOM_TEMPLATE + ".CDeviceButton6"):
        test.fail("New Device button exists")
    else:
        test.passes("New Device button does not exist")
        
def addExistingTemplateSameName():    
    cdw.addTemplate(router0, 'FirstRouter1841Template', 'FirstRouter1841Template', 'Misc')
    if object.exists(ComponentBoxConst.DeviceModel.CUSTOM_TEMPLATE + ".CDeviceButton6"):
        test.passes("New Device button exists")
    else:
        test.fail("New Device button does not exist")
    test.compare(findObject(ComponentBoxConst.DeviceModel.CUSTOM_TEMPLATE + ".CDeviceButton5").visible, False)  
    
def addExistingTemplateDifferentName():
    cdw.goToTemplateManager()
    cdw.addTemplate(router0, 'RouterExtra', 'RouterExtra', 'Misc')
    if object.exists(ComponentBoxConst.DeviceModel.CUSTOM_TEMPLATE + ".CDeviceButton6"):
        test.passes("New Device button exists")
    else:
        test.fail("New Device button does not exist")

def removeTemplate():
    functions.Aut().killAut()
    snooze(5)
    functions.Aut().startAut()
    util.init()
    cdw.goToTemplateManager()
    templates = ['Router0(0)', 'RouterExtra']
    for template in templates:
        if template in cdw.deviceList:
            cdw.removeDeviceTemplate(template)