######################
#@author: Pamela Vinco
######################
from API.functions import pathFromOS
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.EndDevice.PC.PC import PC
from API.MenuBar.File.Open.Open import Open

#Function initialization
util = Util()
openFile = Open()

#Device initialization
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 350, 40, "Server0")
server1 = Server(ComponentBoxConst.DeviceModel.SERVER, 350, 305, "Server1")
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 55, 180, "PC0")

def main():
    util.init()
    openSampleFile()
    startServer0()
    startSendServer1()
    checkpoint1()
    uploadUDPtest()
    startUdpSendServer1()
    checkpoint2()
    
def openSampleFile():
    openFile.openSamples(pathFromOS("Cisco Application Management/udp_test_app.pkt"))
    util.speedUpConvergence()
    
def startServer0():
    server0.select()
    server0.clickServicesTab()
    #Start VM
    server0.services.selectInterface('VM Management')
    server0.services.vmManagement.start()
    
    #Open Command Prompt
    server0.clickDesktopTab()
    server0.desktop.applications.commandPrompt()
    server0.close()
    
def startSendServer1():
    server1.select()
    server1.clickServicesTab()
    #Start VM
    server1.services.selectInterface('VM Management')
    server1.services.vmManagement.start()
    server1.close()

def checkpoint1():
    #Check that Server0 receives a message from Server1
    server0.select()
    snooze(1)
    server0.desktop.applications.commandPrompt()
    server0.desktop.commandPrompt.textCheckPoint("Received:Hello There! from 10.0.0.2")

def uploadUDPtest():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("https://10.0.0.2:8443")
    snooze(5)
    pc0.desktop.webBrowser.ciscoApplicationManagement.login("admin", "admin")   
    snooze(1)
    pc0.desktop.webBrowser.ciscoApplicationManagement.addDeploy("udpSend", "udpSend")
    snooze(5)
    pc0.close()
    
def startUdpSendServer1():
    server1.select()
    server1.clickServicesTab()
    #Start Udp Send VM
    server1.services.selectInterface('VM Management')
    server1.services.vmManagement.start()
    server1.close()

def checkpoint2():
    #Check that Server0 receives another message from Server1
    server0.select()
    snooze(1)
    server0.desktop.applications.commandPrompt()
    server0.desktop.commandPrompt.textCheckPoint("Received:Hello There! from 10.0.0.2", 2)
