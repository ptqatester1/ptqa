from API.ComponentBox import ComponentBoxConst
from API.Device.Cloud.Cloud import Cloud

from API.Utility.Util import Util
from API.Utility.Util import UtilConst
from API.MenuBar.File.File import File

#Function initialization
util = Util()
fileMenu = File()

#Device initialization
cloud0 = Cloud(ComponentBoxConst.DeviceModel.CLOUD_EMPTY, 100, 200, "CLOUD_EMPTY")
cloud1 = Cloud(ComponentBoxConst.DeviceModel.CLOUD, 200, 200, "CLOUD")

def main():
    util.init()
    createTopology()
    cloud0_empty()
    frameRelay()
    ethernet()

def createTopology():
    cloud0.create()
    util.createDevice(ComponentBoxConst.DeviceType.WAN, cloud1.model, cloud1.x, cloud1.y)
    
def cloud0_empty():
    #Add empty connections and check that an error message is shown
    util.clickOnWorkspace(cloud0.x, cloud0.y)
    cloud0.updateName()
    cloud0.clickConfigTab()
    cloud0.config.selectInterface("Frame Relay")
    cloud0.config.connections.frameRelay.addButton()
    snooze(1)
    if (object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        test.passes("Error message shown")
    else:
        test.fail("Error message is not shown")
        
    cloud0.config.selectInterface("Cable")
    cloud0.config.connections.cable.addButton()
    snooze(1)
    if (object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        test.passes("Error message shown")
    else:
        test.fail("Error message is not shown")
        
    cloud0.config.selectInterface("DSL")
    cloud0.config.connections.dsl.addButton()
    snooze(1)
    if (object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        test.passes("Error message shown")
    else:
        test.fail("Error message is not shown")
    cloud0.close()

def frameRelay(): 
    util.clickOnWorkspace(cloud1.x, cloud1.y)
    cloud1.updateName()
    cloud1.clickConfigTab()
    cloud1.config.selectInterface("Serial0")
    cloud1.config.interface.serial.add("100", "100")
    
    #Add duplicate and check that an error message is shown
    cloud1.config.interface.serial.add("100", "100")
    snooze(1)
    if (object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        test.passes("Error message shown")
    else:
        test.fail("Error message is not shown")
    cloud1.config.interface.serial.add("101", "101")
    
    #Add DLCI for each of the interface
    cloud1.config.selectInterface("Serial1")
    cloud1.config.interface.serial.add("200", "200")
    cloud1.config.interface.serial.add("201", "201")
    
    cloud1.config.selectInterface("Serial2")
    cloud1.config.interface.serial.add("300", "300")
    cloud1.config.interface.serial.add("301", "301")
    
    cloud1.config.selectInterface("Serial3")
    cloud1.config.interface.serial.add("400", "400")
    cloud1.config.interface.serial.add("401", "401")
    
    cloud1.config.selectInterface("Frame Relay")
    cloud1.config.connections.frameRelay.add("Serial0", "100", "Serial1", "200")
    
    #Add a duplicate connection and check that an error message is shown
    cloud1.config.connections.frameRelay.add("Serial0", "100", "Serial1", "200")
    snooze(1)
    if (object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        test.passes("error message shown")
    else:
        test.fail("error message is not shown")
        
    #Continue adding connections and check that they are saved in the connections view
    cloud1.config.connections.frameRelay.add("Serial1", "201", "Serial2", "300")
    cloud1.config.connections.frameRelay.add("Serial2", "301", "Serial3", "400")
    cloud1.config.connections.frameRelay.add("Serial3", "401", "Serial0", "101")
    test.compare(cloud1.config.connections.frameRelay.frameRelayTable.rowCount, 4)
    
    #Delete the connections and check that the connections view is empty
    for i in range (0,4):
        cloud1.config.connections.frameRelay.removeRow(0)
    test.compare(cloud1.config.connections.frameRelay.frameRelayTable.rowCount, 0)
    cloud1.close()

def ethernet():
    util.clickOnWorkspace(cloud1.x, cloud1.y)
    cloud1.updateName()
    cloud1.clickConfigTab()
    
    #Add phone numbers to modem interfaces
    cloud1.config.selectInterface("Modem4")
    cloud1.config.interface.modem.phoneNumber("444")
    cloud1.config.selectInterface("Modem5")
    if (object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
    cloud1.config.interface.modem.phoneNumber("555")
    
    #Check default state of Cable
    cloud1.config.selectInterface("Cable")
    cloud1.config.connections.cable.check.toPort('')
    cloud1.config.connections.cable.addButton()
    snooze(1)
    if (object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        test.passes("Error message shown")
    else:
        test.fail("Error message is not shown")
                
    #Check default state of DSL
    cloud1.config.selectInterface("DSL")
    snooze(2)
    cloud1.config.connections.dsl.check.toPort("Ethernet6")

    #Add DSL connection and check that they are saved in the connections view
    cloud1.config.connections.dsl.add("Modem4", "Ethernet6")
    cloud1.config.connections.dsl.add("Modem5", "Ethernet6")
    test.compare(cloud1.config.connections.dsl.dslTable.rowCount, 2)
    
    #Remove DSL connection and check that the connections view is empty
    for i in range (0,2):
        cloud1.config.connections.dsl.removeRow(0)
        
    test.compare(cloud1.config.connections.dsl.dslTable.rowCount, 0)
    
    #Switch to cable
    cloud1.config.selectInterface("Ethernet6")
    cloud1.config.interface.ethernet.cable()
    
    cloud1.config.selectInterface("DSL")
    cloud1.config.connections.dsl.addButton()
    if (object.exists(UtilConst.ERROR_MESSAGE_POPUP)):
        util.clickButton(UtilConst.ERROR_MESSAGE_OK)
        test.passes("Error message shown")
    else:
        test.fail("Error message is not shown")
    cloud1.config.connections.dsl.check.toPort('')
    
    cloud1.config.selectInterface("Cable")
    cloud1.config.connections.cable.check.toPort("Ethernet6")
    
    #Add cable connection
    cloud1.config.connections.cable.add("Coaxial7", "Ethernet6")
    test.compare(cloud1.config.connections.cable.cableTable.rowCount, 1)
    
    #Remove cable connection
    cloud1.config.connections.cable.removeRow(0)
    test.compare(cloud1.config.connections.cable.cableTable.rowCount, 0)
    
    #Switch to DSL
    cloud1.config.selectInterface("Ethernet6")
    cloud1.config.interface.ethernet.dsl()
    
    cloud1.config.selectInterface("DSL")
    cloud1.config.connections.dsl.check.toPort("Ethernet6")
    
    cloud1.config.selectInterface("Cable")
    cloud1.config.connections.cable.check.toPort("")