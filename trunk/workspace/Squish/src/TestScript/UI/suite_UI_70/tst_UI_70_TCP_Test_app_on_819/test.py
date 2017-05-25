######################
#Author: Alex Leung ##
######################

from API.Utility import UtilConst
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.Server.Server import Server

from API.Device.Router.Router import Router

from API.MenuBar.File.Open.Open import Open
from API.functions import pathFromOS
import os

#Function initialization
util = Util()
openFile = Open()

#Device initialization
util = Util()
s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 155, 305, "TCP Server")
s1 = Server(ComponentBoxConst.DeviceModel.SERVER, 165, 20, "TCP Client 1")
r1 = Router(ComponentBoxConst.DeviceModel.ROUTER_819_IOX, 265, 110, "Router1")

def main():
    openSampleFile()
    startTcpServer()
    startTcpClient()
    checkStarted()
    
def openSampleFile():
    util.init()
    openFile.openSamples(pathFromOS("Router/819HG_4G_IOX/tcp_client_app_on_819.pkt"))
    util.speedUpConvergence()

def startTcpServer():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('VM Management')
    s0.services.vmManagement.start()
    #s0.clickButton(ServerConst.Services.VmManagement.START_BUTTON)
    s0.clickTab('Desktop')
    s0.desktop.applications.commandPrompt()
    s0.close()

def startTcpClient():
    s1.select()
    s1.clickServicesTab()
    s1.services.selectInterface('VM Management')
    s1.services.vmManagement.start()
    #s1.clickButton(ServerConst.Services.VmManagement.START_BUTTON)
    s1.close()
    
    r1.select()
    r1.clickTab('CLI')
    r1.cli.startConsole()
    r1.cli.setCliText('enable',
                      'configure terminal',
                      'virtual-service tcp_client',
                      'activate')

def checkStarted():    
    s0.select()
    s0.desktop.applications.commandPrompt()
    s0.desktop.commandPrompt.textCheckPoint('new client: 172.1.1.1:1025')
    None

'''TCP Client App

On TCP Server, start the tcp_server app via Services tab > VM Management.   
Open the Command Prompt on the server.

On TCP Client 1, start tcp_client app via the Services tab > VM Management

On TCP Client 2, activate TCP Client app.  You may need to do 
"activate / no activate" a couple of times.

Router(config)#virtual-service tcp_client
Router(config-virt-serv)#activate


On the Server, observe the output:

 Packet Tracer SERVER Command Line 1.0
C:\>new client: 172.1.1.4:1025
new client: 172.1.1.1:1025'''