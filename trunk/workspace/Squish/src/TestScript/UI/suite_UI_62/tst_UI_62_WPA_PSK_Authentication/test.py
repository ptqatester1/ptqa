########################
##Author: AbbasH
########################

from API.Utility.Util import Util
from API.Utility import UtilConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.DeviceBase.DesktopBase.DesktopBaseConst import IpConfiguration
from API.Device.Router.Router import Router
from API.ComponentBox import ComponentBoxConst
from API.MenuBar.File.Open.Open import Open
from API.functions import pathFromOS
import os

r = Router(ComponentBoxConst.DeviceModel.ROUTER_819, 178, 62, 'Router1')
p0 = PC(ComponentBoxConst.DeviceModel.PC, 85, 211, 'PC0')
p1 = PC(ComponentBoxConst.DeviceModel.PC, 263, 203, 'PC1')

p0IP = None
p1IP = None


util = Util()
openFile = Open()

def main():
    util.init()
    maketop()
    configureRouter()
    checkPCsIP()
    checkConnection()
    
def maketop():
    openFile.openSamples(pathFromOS("Router/819HGW/wpa_psk_authentication.pkt"))
    util.speedUpConvergence()    
    
def configureRouter():
    r.select()
    r.clickCliTab()
    r.cli.startConsole()
    r.cli.setCliText("enable")
    r.cli.setCliText("service-module wlan-ap 0 session")
    r.cli.setCliText("\r")
    r.cli.setCliText("enable")
    r.cli.setCliText("configure terminal")
    r.cli.setCliText("int dot11Radio 0")
    r.cli.setCliText("no shut")
    r.cli.setCliText("do show ip int brief")
    r.cli.textCheckPoint("Dot11Radio0            unassigned      YES NVRAM  up                    up")
    r.cli.setCliText("end")
    util.speedUpConvergence()
    r.close()

def checkPCsIP():
    global p0IP, p1IP
    p0.select()
    p0.clickDesktopTab()
    p0.desktop.applications.ipConfiguration()
    snooze(2)
    p0IP = str(findObject(p0.objName(IpConfiguration.IP_EDIT)).text)
    p0.close()

    p1.select()
    p1.clickDesktopTab()
    p1.desktop.applications.ipConfiguration()
    snooze(2)
    p1IP = str(findObject(p1.objName(IpConfiguration.IP_EDIT)).text)
    p1.close()
    
def checkConnection():    
    util.clickOnWorkspace(r.x, r.y)
    r.updateName()
    r.clickCliTab()
    r.cli.sendBreak()    
    r.cli.setCliText("ping 10.10.10.1")
    util.fastForwardTime()
    r.cli.setCliText("ping " + p0IP)
    util.fastForwardTime()
    r.cli.setCliText("ping " + p1IP)
    util.fastForwardTime()
    r.cli.textCheckPoint("Success rate is 0", 0)
    r.cli.textCheckPoint("Router#")
    r.cli.setCliText("1")
    r.cli.textCheckPoint("Resuming connection 1 to 10.10.10.1 ... ")
    r.close()
    
    p0.select()
    p0.clickDesktopTab()
    p0.desktop.applications.commandPrompt()
    p0.desktop.commandPrompt.setText("ping 10.10.10.1")
    util.fastForwardTime()
    p0.desktop.commandPrompt.setText("ping " + p0IP)
    util.fastForwardTime()
    p0.desktop.commandPrompt.textCheckPoint("Received = [1234]", 2)
    p0.close()

    p1.select()
    p1.clickDesktopTab()
    p1.desktop.applications.commandPrompt()
    p1.desktop.commandPrompt.setText("ping 10.10.10.1")
    util.fastForwardTime()
    p1.desktop.commandPrompt.setText("ping " + p0IP)
    util.fastForwardTime()
    p1.desktop.commandPrompt.textCheckPoint("Received = [1234]", 2)
    p1.close()
