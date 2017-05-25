######################
#@author: Pamela Vinco
######################
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.Server.Server import Server
from API.MenuBar.File.Open.Open import Open
from API.functions import pathFromOS

#Function initialization
util = Util()
openFile = Open()

#Device initialization
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 85, 50, "Server0")
server1 = Server(ComponentBoxConst.DeviceModel.SERVER, 410, 60, "Server1")

def main():
    util.init()
    openSampleFile()
    startServer1()
    startServer0()
    checkpoint()
    
def openSampleFile():
    openFile.openSamples(pathFromOS("Cisco Application Management/tcp_test_app.pkt"))
    util.speedUpConvergence()
    
def startServer1():
    server1.select()
    server1.clickServicesTab()
    #Start VM
    server1.services.selectInterface('VM Management')
    server1.services.vmManagement.start()
    #test.compare(str(findObject(server1.squishName + ServerConst.Services.VmManagement.START_BUTTON).text), "Stop")
    
    #Open Command Prompt
    server1.clickDesktopTab()
    server1.desktop.applications.commandPrompt()
    
def startServer0():
    server0.select()
    server0.clickServicesTab()
    #Start VM
    server0.services.selectInterface('VM Management')
    server0.services.vmManagement.start()
    #test.compare(str(findObject(server0.squishName + ServerConst.Services.VmManagement.START_BUTTON).text), "Stop")
    
def checkpoint():
    #Check that Server1 receives a message from Server0
    server1.select()
    snooze(1)
    server1.desktop.applications.commandPrompt()
    server1.desktop.commandPrompt.textCheckPoint("new client: 10.0.0.1:1025")