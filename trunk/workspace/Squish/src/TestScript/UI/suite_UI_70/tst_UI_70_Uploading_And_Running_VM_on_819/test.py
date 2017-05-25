######################
#@author: Pamela Vinco
######################
from API.Utility.Util import Util
from API.ComponentBox import ComponentBoxConst
from API.Device.EndDevice.PC.PC import PC
from API.Device.Router.Router import Router
from API.MenuBar.File.Open.Open import Open
from API.functions import pathFromOS

#Function initialization
util = Util()
openFile = Open()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 65, 110, "PC0")
r0 = Router(ComponentBoxConst.DeviceModel.ROUTER_819_IOX, 215, 110, "Router0")

def main():
    util.init()
    openSampleFile()
    addVMviaBrowser()
    util.init()
    openSampleFile()
    addVMviaTFTP()
    
def openSampleFile():
    openFile.openSamples(pathFromOS("Router/819HG_4G_IOX/uploading_and_running_vm_on_819.pkt"))
    util.speedUpConvergence()
    
def addVMviaBrowser():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("https://172.1.1.1:8443")
    snooze(5)
    pc0.desktop.webBrowser.ciscoApplicationManagement.login("cisco", "cisco")   
    pc0.desktop.webBrowser.ciscoApplicationManagement.addDeploy("vm1", "vm1")
    snooze(5)
    test.compare(findObject(pc0.squishName + PCConst.Desktop.WebBrowser.CiscoApplicationManagementPage.Applications.APPLICATIONS_TABLE).numChildren, 2)
    pc0.maximizeDeviceWindow()
    snooze(5)
    pc0.desktop.webBrowser.clickLink(PCConst.Desktop.WebBrowser.CiscoApplicationManagementPage.Applications.APPLICATIONS_TABLE_ENTRY2_START)
    snooze(5)
    pc0.desktop.webBrowser.clearBrowserCache()
    test.compare(findObject(pc0.squishName + PCConst.Desktop.WebBrowser.CiscoApplicationManagementPage.Applications.MAIN_WEB_VIEW + ".DOCUMENT.HTML1.BODY1.DIV4.DIV1.DIV1.DIV3.DIV1.DIV1.DIV1.DIV2.DIV1.DIV1.DIV1.DIV1.DIV2.TABLE1.TBODY1.TR1.TD4.A1").simplifiedInnerText, "stop")
    pc0.close()
    
def addVMviaTFTP():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.tftpService()
    pc0.desktop.tftpService.setDirectory("+c:/_+vm1")
    
    #Upload VM1
    r0.select()
    r0.clickCliTab()
    r0.cli.setCliText('''
en
copy tftp flash
172.1.1.2
vm1.ova

''')
    util.fastForwardTime()
    
    #Install VM1
    r0.cli.setCliText("virtual-service install name vm1 package flash:/vm1.ova")
    r0.cli.textCheckPoint("%VIRT_SERVICE-5-INSTALL_STATE: Successfully installed virtual service vm1")
    
    #Activate VM1
    r0.cli.setCliText('''
conf t
virtual-service vm1
activate
do show virt list''')
    r0.cli.textCheckPoint('''Name                    Status             Package Name
------------------------------------------------------------------------------
abc                     Installed          abc.ova
vm1                     Activated          vm1.ova''')
    
    #Deactivate VM1
    r0.cli.setCliText('''
no activate
do show virt list''')
    r0.cli.textCheckPoint('''Name                    Status             Package Name
------------------------------------------------------------------------------
abc                     Installed          abc.ova
vm1                     Installed          vm1.ova''')

    #Uninstall VM1
    r0.cli.setCliText("end")
    r0.cli.setCliText("virtual-service uninstall name vm1")
    r0.cli.textCheckPoint("%VIRT_SERVICE-5-INSTALL_STATE: Successfully uninstalled virtual service vm1")
    r0.close()