######################
#Author: Alex Leung ##
######################
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.Server.Server import Server
from API.Device.Router.Router import Router
from API.MenuBar.File.Open.Open import Open
from API.functions import pathFromOS
from API.functions import pathFromOS

#Function initialization
util = Util()
openFile = Open()

#Device initialization
util = Util()
s0 = Server(ComponentBoxConst.DeviceModel.SERVER, 170, 41, "Server0")
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_819_IOX, 245, 265, "Router0")

def main():
    openSampleFile()
    startUdpReceive()
    startUdpSend()
    checkpoint()
    
def openSampleFile():
    util.init()
    openFile.openSamples(pathFromOS("Router/819HG_4G_IOX/udp_test_app_on_819.pkt"))
    util.speedUpConvergence()
    
def startUdpReceive():
    s0.select()
    s0.clickServicesTab()
    s0.services.selectInterface('VM Management')
    s0.services.vmManagement.start()
    #s0.clickButton(ServerConst.Services.VmManagement.START_BUTTON)
    s0.clickTab('Desktop')
    s0.desktop.applications.commandPrompt()
    s0.close()

    
def startUdpSend():
    r0.select()
    r0.clickCliTab()
    r0.cli.setCliText('''
en
conf t
virtual-service UdpSend
activate
''')
    util.fastForwardTime()
    r0.cli.setCliText('no activate',
                      'activate',
                      'no activate',
                      'activate')
    r0.close()
       
def checkpoint():
    s0.select()
    s0.desktop.applications.commandPrompt()
    s0.desktop.commandPrompt.textCheckPoint("Received:Hello There! from 10.0.0.2")