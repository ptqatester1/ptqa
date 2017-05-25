########################
##Author: AbbasH
########################


from API.Device.Router.Router import Router
from API.Utility import UtilConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Toolbar.CommonToolsBar.CommonToolsBarConst import CommonToolsBarConst

util = Util()

r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_1941, 100, 100, "Router0")
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_2901, 300, 100, "Router1")

def main():
    util.init()
    createDevices()
    configTopology()
    checkPoint1()
    checkPoint2()
    
def createDevices():
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r0.model, r0.x, r0.y)
    util.createDevice(ComponentBoxConst.DeviceType.ROUTER, r1.model, r1.x, r1.y)
    #Intentional Misconfiguration
    util.connect(r0.x, r0.y, r1.x, r1.y, ComponentBoxConst.Connection.CONN_STRAIGHT, "GigabitEthernet0/0", "GigabitEthernet0/0")
    util.speedUpConvergence()    

def configTopology():
    r0.select()
    r0.clickCliTab()
    r0.cli.startConsole()
    r0.cli.setCliText("enable")
    r0.cli.setCliText("configure terminal")
    r0.cli.setCliText("int gig0/0")
    r0.cli.setCliText("ip address 192.168.0.2 255.255.255.0")
    r0.cli.setCliText("no shut")
    r0.cli.setCliText("end")

    r1.select()
    r1.clickCliTab()
    r1.cli.startConsole()
    r1.cli.setCliText("enable")
    r1.cli.setCliText("configure terminal")
    r1.cli.setCliText("int gig0/0")
    r1.cli.setCliText("ip address 192.168.0.3 255.255.255.0")
    r1.cli.setCliText("no shut")
    r1.cli.setCliText("end")    

    util.speedUpConvergence()
    
def checkPoint1():

    r0.select()
    r0.cli.setCliText("ping 192.168.0.3")
    util.fastForwardTime()
    r0.cli.textCheckPoint("Success rate is 0 percent")  
    r0.close()  
    
    r1.select()
    r1.cli.setCliText("ping 192.168.0.2")
    util.fastForwardTime()
    r1.cli.textCheckPoint("Success rate is 0 percent")
    r1.close()

def checkPoint2():
    util.clickOnWorkspace(10, 10)
    util.clickButton(CommonToolsBarConst.DELETE_TOOL)  
    util.clickOnWorkspace(200, 100)
    util.connect(r0.x, r0.y, r1.x, r1.y, ComponentBoxConst.Connection.CONN_AUTO, "", "")
    util.speedUpConvergence()
    snooze(1)  
    r0.select()
    r0.cli.setCliText("ping 192.168.0.3")
    util.fastForwardTime()
    r0.cli.textCheckPoint("Success rate is 0 percent", 1)  
    r0.close()  
    
    r1.select()
    r1.cli.setCliText("ping 192.168.0.2")
    util.fastForwardTime()
    r1.cli.textCheckPoint("Success rate is 0 percent", 1)
    r1.close()    