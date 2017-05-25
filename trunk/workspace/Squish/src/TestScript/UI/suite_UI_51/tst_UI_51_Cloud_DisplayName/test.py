from API.ComponentBox import ComponentBoxConst

from API.Device.Cloud.Cloud import Cloud

from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.MenuBar.File.File import File
from API.MenuBar.File.FileConst import FileConst
from API.MenuBar.File.Open.OpenConst import OpenConst

#Function initialization
util = Util()
fileMenu = File()

#Device initialization
cloud0 = Cloud(ComponentBoxConst.DeviceModel.CLOUD_EMPTY, 100, 200, "CLOUD_EMPTY")
cloud1 = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 200, 200, "CLOUD")

def main():
    util.init()
    createTopology()
    setDisplayName()
    checkpoint()

def createTopology():
    cloud0.create()
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cloud1.model, cloud1.x, cloud1.y)
    
def setDisplayName():
    util.clickOnWorkspace(cloud0.x, cloud0.y)
    cloud0.updateName()
    cloud0.clickConfigTab()
    cloud0.config.settings.displayName("CLOUD_EMPTY")
    cloud0.close()
        
    util.clickOnWorkspace(cloud1.x, cloud1.y)
    cloud1.updateName()
    cloud1.clickConfigTab()
    cloud1.config.settings.displayName("CLOUD")
    cloud1.close()
    
def checkpoint():        
    util.clickOnWorkspace(cloud0.x, cloud0.y+40)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "CLOUD_EMPTY")
    
    util.clickOnWorkspace(cloud1.x, cloud1.y+40)
    util.textCheckPoint(UtilConst.DEVICE_LABEL, "CLOUD")