######################
#@author: Pamela Vinco
######################
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.EndDevice.Server.Server import Server
from API.MenuBar.File.Open.Open import Open
from API.functions import pathFromOS

#Function initialization
util = Util()
openFile = Open()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 50, 215, "PC0")
server0 = Server(ComponentBoxConst.DeviceModel.SERVER, 195, 115, "Server0")

def main():
    util.init()
    openSampleFile()
    addVM()
    runVM()
    
def openSampleFile():
    openFile.openSamples(pathFromOS("Cisco Application Management\\uploading_and_running_vm.pkt"))       
    util.speedUpConvergence()
    
def addVM():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("https://10.0.0.1:8443")
    snooze(5)
    pc0.desktop.webBrowser.clearBrowserCache()
    pc0.desktop.webBrowser.ciscoApplicationManagement.login("admin", "admin")   
    pc0.desktop.webBrowser.ciscoApplicationManagement.addDeploy("vm3", "vm3")
    snooze(5)
    test.compare(findObject(pc0.squishName + PCConst.Desktop.WebBrowser.CiscoApplicationManagementPage.Applications.APPLICATIONS_TABLE).numChildren, 3)
    pc0.maximizeDeviceWindow()
    snooze(5)
    pc0.desktop.webBrowser.clickLink(PCConst.Desktop.WebBrowser.CiscoApplicationManagementPage.Applications.APPLICATIONS_TABLE_ENTRY3_MANAGE)
    pc0.desktop.webBrowser.clearBrowserCache()
    test.compare(findObject(pc0.squishName + PCConst.Desktop.WebBrowser.CiscoApplicationManagementPage.MAIN_WEB_VIEW + ".DOCUMENT.HTML1.BODY1.DIV4.DIV1.DIV1.DIV1.DIV2.DIV1.DIV4").innerText, "vm3\n")
    pc0.close()
    
def runVM():
    server0.select()
    server0.clickServicesTab()
    server0.services.selectInterface('VM Management')
    server0.services.vmManagement.start()
    s0.close()

