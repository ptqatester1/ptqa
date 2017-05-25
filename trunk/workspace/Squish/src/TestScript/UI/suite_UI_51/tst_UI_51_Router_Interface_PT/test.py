##################################################################
#@author: Thi Nguyen
##############################################################
from API.ComponentBox import ComponentBoxConst
from API.Device.DeviceBase.ConfigBase.ConfigBaseConst import ConfigConst
from API.Device.Router.Router import Router
from API.Utility.Util import Util

#Function initialization
util = Util()

#Device initialization
router0 = Router(ComponentBoxConst.DeviceModel.ROUTER_PT, 100, 200, "router0")
def main():
    util.init()
    createTopology()
    router_PT()

def createTopology():
    router0.create()
    util.clickOnSimulation()
    util.clickOnRealtime()

def router_PT():
    router0.select()  
    router0.clickConfigTab()
    router0.config.selectInterface("FastEthernet0/0")
    checkPortStatus(1)
    checkBandwidth(1)
    checkDuplex(1) 
    checkMacAddress("000A.417B.2E04")
    checkIpAddress("10.1.1.1", "255.255.255.252")    
    router0.config.selectInterface("FastEthernet1/0")
    checkPortStatus(2)
    checkBandwidth(2)
    checkDuplex(2) 
    checkMacAddress("000A.417B.2E05")
    checkIpAddress("11.1.1.1", "255.255.255.252")
 
    router0.config.selectInterface("FastEthernet4/0")
    checkPortStatus(3)
    checkMacAddress("000A.417B.2E06")
    checkIpAddress("12.1.1.1", "255.255.255.252")
    router0.config.selectInterface("FastEthernet5/0")
    checkPortStatus(4)
    checkMacAddress("000A.417B.2E07")
    checkIpAddress("13.1.1.1", "255.255.255.252")
    router0.config.selectInterface("Serial2/0")
    checkPortStatus(5)
    checkIpAddress("14.1.1.5", "255.255.255.252")
    checkClockrate(1)
    router0.config.selectInterface("Serial3/0")
    checkPortStatus(6)
    checkIpAddress("15.1.1.1", "255.255.255.252")
    checkClockrate(2)
    
def checkClockrate(occurrence_num):
    clockrate = ["1200", "2400", "4800", "9600", "19200", "38400", "56000", "64000", "72000", "125000", "128000", "148000", "250000", "500000", "800000", "1000000", "1300000", "2000000", "4000000"]
    for i in range (0, len(clockrate)):
        router0.config.interface.serial.clockrate(clockrate[i])
        router0.cli.textCheckPoint("clock rate " + clockrate[i], occurrence_num)
    router0.config.interface.serial.clockrate("Not Set")
    router0.cli.textCheckPoint("no clock rate", occurrence_num)

def checkIpAddress(p_ip, p_subnet):
    router0.config.interface.ethernet.ip(p_ip)
    router0.config.interface.ethernet.subnet(p_subnet)
    util.click(router0.squishName + ConfigConst.interface.TX_RING_LIMIT_EDIT)
    snooze(2)
    router0.cli.textCheckPoint("ip address " + p_ip + " " + p_subnet) 

def checkMacAddress(p_mac):
    router0.config.interface.ethernet.mac(p_mac)
    util.click(router0.squishName + ConfigConst.interface.IP_ADDRESS_EDIT)
    util.click(router0.squishName + ConfigConst.interface.IP_ADDRESS_EDIT)
    snooze(2)
    router0.cli.textCheckPoint("mac-address " + p_mac) 

def checkBandwidth(occurrence_num):
    router0.config.interface.ethernet.bandwidth('100')
    router0.cli.textCheckPoint("speed 100", occurrence_num*2)
    router0.config.interface.ethernet.bandwidth('10')
    snooze(1)
    router0.cli.textCheckPoint("speed 10\n", occurrence_num)
    router0.config.interface.ethernet.bandwidth('Auto')
    router0.cli.textCheckPoint("speed auto", occurrence_num)

def checkDuplex(occurrence_num):
    router0.config.interface.ethernet.duplex('half')
    router0.cli.textCheckPoint("duplex half", occurrence_num*2)    
    router0.config.interface.ethernet.duplex('full')
    router0.cli.textCheckPoint("duplex full", occurrence_num)   
    router0.config.interface.ethernet.duplex('Auto')
    router0.cli.textCheckPoint("duplex auto", occurrence_num)  

def checkPortStatus(occurrence_num):
    snooze(1)
    router0.config.interface.ethernet.portStatus(True)
    snooze(2)
    router0.config.interface.ethernet.portStatus(True)
    router0.cli.textCheckPoint("no shutdown", occurrence_num)
    router0.cli.textCheckPoint("shutdown", occurrence_num) 
