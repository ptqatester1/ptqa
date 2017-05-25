#Thi
from API.ComponentBox import ComponentBoxConst
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Device.DeviceBase.WirelessGuiBase.WirelessGuiBaseConst import WirelessGuiConst
from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util
from API.Utility.Util import UtilConst

from API.Device.Router.Router import Router
#Function initialization
util = Util()

#Device initialization
laptop = PC(ComponentBoxConst.DeviceModel.LAPTOP, 182, 35, "Laptop0")
pc1 = PC(ComponentBoxConst.DeviceModel.PC, 184, 315, "PC1")
lanRouter = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 177, 223, "LANRouter")

pc0 = PC(ComponentBoxConst.DeviceModel.PC, 563, 252, "PC0")
wirelessRouter0 = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 313, 251, "Wireless Router0")
Router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 450, 252, "Router1")
def main():
    createTopology()
    createAccessPolicy()
    createAccessPolicy_checkpoint()
    checkPolicy1()
    checkPolicy2_before()
    changePolicy2()
    checkPolicy2_after()
    checkPolicy3()
    changeLinksysIP()
    
def createTopology():
    util.open("UI20_Improved_Linksys.pkt", UtilConst.UI_TEST)
    util.speedUpConvergence()

def createAccessPolicy():
    wirelessRouter0.select()
    wirelessRouter0.clickGuiTab()
    wirelessRouter0.gui.tabs.applicationsAndGaming()
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.enabledCheckbox(8, True)
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.saveSettingsButton()
    wirelessRouter0.gui.tabs.accessRestrictions()
    wirelessRouter0.gui.accessRestrictions.accessPolicy('1()')
    wirelessRouter0.gui.accessRestrictions.policyName('172_16_100_5')
    wirelessRouter0.gui.accessRestrictions.enabled()
    
    IPTuplet = [("1","5")]
    BlockedApps = ['HTTPS(443-443)', 'Telnet(23-23)', 'Ping(0-0)', 'HTTP(80-80)']
    wirelessRouter0.gui.accessRestrictions.createPolicy("1()", "172_16_100_5", 'enable', IPTuplet , 'allow', BlockedApps)
    IPTuplet = [("1","4")]
    BlockedApps = ['TFTP(69-69)']
    wirelessRouter0.gui.accessRestrictions.createPolicy("2()", "172_16_100_4", 'enable', IPTuplet, 'allow', BlockedApps)
    IPTuplet = [("1","2")]
    BlockedApps = ['HTTP(80-80)', 'SNMP(161-161)']
    wirelessRouter0.gui.accessRestrictions.createPolicy("3()", "172_16_100_2", 'disable', IPTuplet, 'allow', BlockedApps)
    
def createAccessPolicy_checkpoint():
    #check policy 1
    wirelessRouter0.gui.accessRestrictions.accessPolicy('1(172\\_16\\_100\\_5)')
    wirelessRouter0.gui.accessRestrictions.check.allow(True)
    wirelessRouter0.gui.accessRestrictions.check.enabled(True)
    wirelessRouter0.gui.accessRestrictions.check.policyName("172_16_100_5")
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.accessRestrictions.BLOCKED_APPLICATION_LIST).count, 3)
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.accessRestrictions.BLOCKED_APPLICATION_LIST + ".item_0/0").text, "HTTPS(443-443)")
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.accessRestrictions.BLOCKED_APPLICATION_LIST + ".item_1/0").text, "Telnet(23-23)")
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.accessRestrictions.BLOCKED_APPLICATION_LIST + ".item_2/0").text, "Ping(0-0)")
    wirelessRouter0.gui.accessRestrictions.editFilters.editRange("1", "5")

    wirelessRouter0.gui.accessRestrictions.accessPolicy('2(172\\_16\\_100\\_4)')
    wirelessRouter0.gui.accessRestrictions.check.deny(False)
    wirelessRouter0.gui.accessRestrictions.check.enabled(True)
    wirelessRouter0.gui.accessRestrictions.check.policyName("172_16_100_4")
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.accessRestrictions.BLOCKED_APPLICATION_LIST).count, 1)
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.accessRestrictions.BLOCKED_APPLICATION_LIST + ".item_0/0").text, "TFTP(69-69)")
    wirelessRouter0.gui.accessRestrictions.editFilters.editRange("1", "4")
    
    #check policy 3
    wirelessRouter0.gui.accessRestrictions.accessPolicy('3(172\\_16\\_100\\_2)')
    wirelessRouter0.gui.accessRestrictions.check.deny(False)
    wirelessRouter0.gui.accessRestrictions.check.enabled(False)
    wirelessRouter0.gui.accessRestrictions.check.policyName("172_16_100_2")
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.accessRestrictions.BLOCKED_APPLICATION_LIST).count, 2)
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.accessRestrictions.BLOCKED_APPLICATION_LIST + ".item_0/0").text, "HTTP(80-80)")
    test.compare(findObject(wirelessRouter0.squishName + WirelessGuiConst.accessRestrictions.BLOCKED_APPLICATION_LIST + ".item_1/0").text, "SNMP(161-161)")
    wirelessRouter0.gui.accessRestrictions.editFilters.editRange("1", "2")
    
def checkPolicy1():
    test.log("bug#3403")
    laptop.select()
    laptop.clickDesktopTab()
    laptop.desktop.applications.commandPrompt()
    laptop.desktop.commandPrompt.setText("ping 10.1.1.2")
    util.speedUpConvergence()
    laptop.desktop.commandPrompt.textCheckPoint("Reply from 10.1.1.2", 0)
    laptop.desktop.commandPrompt.setText("telnet 172.16.68.1")
    util.clickOnSimulation()
    util.clickOnRealtime()
    laptop.select()
    laptop.desktop.commandPrompt.textCheckPoint("Connection timed out; remote host not responding")

    laptop.desktop.applications.webBrowser()
    snooze(2)
    laptop.desktop.webBrowser.browse("https://10.1.1.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    laptop.desktop.webBrowser.textCheckPoint("Request Timeout")
    pc1.select()
    pc1.clickDesktopTab()
    pc1.desktop.applications.commandPrompt()
    pc1.desktop.commandPrompt.setText("ping 10.1.1.2")
    util.speedUpConvergence()
    pc1.desktop.commandPrompt.textCheckPoint("Reply from 10.1.1.2")
    pc1.desktop.commandPrompt.setText("telnet 172.16.68.1")
    snooze(3)
    pc1.desktop.commandPrompt.setText("cisco")
    snooze(2)
    pc1.desktop.commandPrompt.textCheckPoint("InternetRouter", 1)
    pc1.desktop.commandPrompt.setText("exit")
    pc1.desktop.applications.webBrowser()
    snooze(2)
    pc1.desktop.webBrowser.browse("10.1.1.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc1.desktop.webBrowser.browse("10.1.1.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc1.desktop.webBrowser.browse("10.1.1.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc1.desktop.webBrowser.textCheckPoint("hello")
    
def checkPolicy2_before():
    lanRouter.select()
    lanRouter.clickCliTab()
    lanRouter.cli.setCliText("\r")
    lanRouter.cli.setCliText("enable")
    lanRouter.cli.setCliText("copy tftp: flash:")
    lanRouter.cli.setCliText("10.1.1.2")
    lanRouter.cli.setCliText("c1841-ipbasek9-mz.124-12.bin")
    lanRouter.cli.setCliText("\r")
    util.speedUpConvergence()
    lanRouter.cli.textCheckPoint("Error opening tftp://10.1.1.2/c1841-ipbasek9-mz.124-12.bin \(Timed out\)")

    
def changePolicy2():
    wirelessRouter0.gui.accessRestrictions.accessPolicy('2(172\\_16\\_100\\_4)')
    wirelessRouter0.gui.accessRestrictions.enabled()
    wirelessRouter0.gui.accessRestrictions.saveSettingsButton()
    
def checkPolicy2_after():
    lanRouter.select()
    lanRouter.cli.setCliText("copy tftp: flash:")
    lanRouter.cli.setCliText("10.1.1.2")
    lanRouter.cli.setCliText("c1841-ipbasek9-mz.124-12.bin")
    lanRouter.cli.setCliText("\r")
    util.speedUpConvergence()
    lanRouter.cli.textCheckPoint("Error opening tftp://10.1.1.2/c1841-ipbasek9-mz.124-12.bin \(Timed out\)", 2)
    
def checkPolicy3():
    test.log("bug#3818")
    wirelessRouter0.gui.accessRestrictions.accessPolicy('3(172\\_16\\_100\\_2)')
    wirelessRouter0.gui.accessRestrictions.enabled()
    wirelessRouter0.gui.accessRestrictions.saveSettingsButton()
    pc1.select()
    pc1.desktop.applications.commandPrompt()
    pc1.desktop.commandPrompt.setText("snmpget /v 1 /a 10.1.1.1 /c testro /o .1.3.6.1.2.1.1.1.0")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc1.desktop.commandPrompt.setText("snmpget /d")
    pc1.desktop.commandPrompt.textCheckPoint("SNMP request timed out")
    
    laptop.select()
    laptop.desktop.applications.commandPrompt()
    laptop.desktop.commandPrompt.setText("snmpget /v 1 /a 10.1.1.1 /c testro /o .1.3.6.1.2.1.1.1.0")
    util.clickOnSimulation()
    util.clickOnRealtime()
    test.log("bug#3871")
    laptop.desktop.commandPrompt.setText("snmpget /d")
    laptop.desktop.commandPrompt.textCheckPoint(".1.3.6.1.2.1.1.1.0 \(.iso.org.dod.internet.mgmt.mib-2.system.sysDescr.0\)\nOctetString\nCisco IOS Software, 1841 Software \(C1841-ADVIPSERVICESK9-M\), Version 12.4\(15\)T1, RELEASE SOFTWARE \(fc2\)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright \(c\) 1986-2007 by Cisco Systems, Inc.\nCompiled Wed 18-Jul-07 04:52 by pt_team\n")

    laptop.desktop.applications.webBrowser()
    snooze(2)
    laptop.desktop.webBrowser.browse("10.1.1.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    laptop.desktop.webBrowser.textCheckPoint("Request Timeout", 0)
    laptop.desktop.webBrowser.browse("https://10.1.1.2")
    util.clickOnSimulation()
    util.clickOnRealtime()
    laptop.desktop.webBrowser.textCheckPoint("Request Timeout", 1)

def changeLinksysIP():
    wirelessRouter0.select()
    wirelessRouter0.gui.tabs.setup()
    wirelessRouter0.gui.setup.basicSetup.networkSetup.routerIp.ip ("172.16.100.1")
    wirelessRouter0.gui.setup.basicSetup.saveSettingsButton()
    wirelessRouter0.gui.tabs.accessRestrictions()
    wirelessRouter0.gui.accessRestrictions.editListButton()
    test.compare(findObject(":CBasePCIPListDlg.m_middlePanel.lblIP1").text, "172.16.100.")
