from API.ComponentBox import ComponentBoxConst

from API.Device.Cloud.Cloud import Cloud
from API.Device.DeviceBase.PhysicalBase.PhysicalBaseConst import Modules
from API.Utility.Util import Util
from API.Utility.Util import UtilConst
#Function initialization
util = Util()

#Device initialization
cloud0 = Cloud(ComponentBoxConst.DeviceModel.CLOUD_EMPTY, 100, 200, "Cloud0")
cloud1 = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 200, 200, "Cloud1")

def main():
    util.init()
    createTopology()
    powerOnOff()
    zoom()

def createTopology():
    cloud0.create()
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cloud1.model, cloud1.x, cloud1.y)

    
    
def powerOnOff():
    util.clickOnWorkspace(cloud0.x, cloud0.y)
    cloud0.updateName()
    cloud0.clickConfigTab()
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Cloud is power on")
        cloud0.clickPhysicalTab()
    else:
        test.fail("Cloud is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    cloud0.physical.power(Modules.wan.cloud_pt_empty.power)
    cloud0.clickConfigTab()
    if (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Cloud is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    else:
        test.fail("Cloud is power on")
        cloud0.clickPhysicalTab()

    cloud0.physical.power(Modules.wan.cloud_pt_empty.power)
    cloud0.clickConfigTab()
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Cloud is power on")
    else:
        test.fail("Cloud is power off")
        
    util.clickOnWorkspace(cloud1.x, cloud1.y)
    cloud1.updateName()
    cloud1.clickConfigTab()
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Cloud is power on")
        cloud1.clickPhysicalTab()
    else:
        test.fail("Cloud is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    cloud1.physical.power(Modules.wan.cloud_pt.power)
    cloud1.clickConfigTab()
    if (object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Cloud is power off")
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    else:
        test.fail("Cloud is power on")
        cloud1.clickPhysicalTab()

    cloud1.physical.power(Modules.wan.cloud_pt.power)
    cloud1.clickConfigTab()
    if (not object.exists(UtilConst.ERROR_MESSAGE_OK)):
        test.passes("Cloud is power on")
    else:
        test.fail("Cloud is power off")
        
def zoom():
    util.clickOnWorkspace(cloud0.x, cloud0.y)
    cloud0.updateName()
    cloud0.clickPhysicalTab()
    cloud0.physical.zoomIn()
    test.compare(cloud0.physical.imageObject.maximumSize.width, 940)
    cloud0.physical.zoomOriginal()
    test.compare(cloud0.physical.imageObject.maximumSize.width, 470)    
    cloud0.physical.zoomOut()
    test.compare(cloud0.physical.imageObject.maximumSize.width, 313)
    cloud0.close()
    
    util.clickOnWorkspace(cloud1.x, cloud1.y)
    cloud1.updateName()
    cloud1.clickPhysicalTab()
    cloud1.physical.zoomIn()
    test.compare(cloud1.physical.imageObject.maximumSize.width, 940)
    cloud1.physical.zoomOriginal()
    test.compare(cloud1.physical.imageObject.maximumSize.width, 470)
    cloud1.physical.zoomOut()
    test.compare(cloud1.physical.imageObject.maximumSize.width, 313)
