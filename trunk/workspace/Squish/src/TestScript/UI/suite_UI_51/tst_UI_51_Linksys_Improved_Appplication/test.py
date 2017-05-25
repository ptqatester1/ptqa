#Thi
from API.ComponentBox import ComponentBoxConst
from API.Device.LinksysRouter.LinksysRouter import LinksysRouter
from API.Device.EndDevice.PC.PC import PC
from API.Utility.Util import Util
from API.Utility.Util import UtilConst

from API.Device.Router.Router import Router
#Function initialization
util = Util()

#Device initialization
pc0 = PC(ComponentBoxConst.DeviceModel.PC, 563, 252, "PC0")
wirelessRouter0 = LinksysRouter(ComponentBoxConst.DeviceModel.LINKSYS, 315, 250, "Wireless Router0")
Router1 = Router(ComponentBoxConst.DeviceModel.ROUTER_1841, 450, 252, "Router1")

def main():
    createTopology()
    DHCP()
    DNS()
    HTTP()
    Telnet()
    TFTP()
    SMNP()
    removeAllEnableApps()
    DMZ_172_16_100_3()
    DMZ_172_16_100_4()
    DMZ_disabled()
    
def createTopology():
    #a.    Create and connect devices according to diagram.
    #a.    On PC0, remove ethernet interface and insert Linksys WRT-300N.
    util.open("UI20_Improved_Linksys.pkt", UtilConst.UI_TEST)
    util.speedUpConvergence()
    
def DHCP():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.ipConfiguration()
    pc0.desktop.ipConfiguration.dhcp()
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc0.desktop.ipConfiguration.dhcp()
    
    util.clickOnSimulation()
    util.clickOnRealtime()
    
    pc0.desktop.ipConfiguration.check.ip(None, property='enabled', value=False)
    pc0.desktop.ipConfiguration.check.gateway(None, property='enabled', value=False)
    pc0.desktop.ipConfiguration.check.subnet(None, property='enabled', value=False)
    pc0.desktop.ipConfiguration.check.dns(None, property='enabled', value=False)
    
    pc0.desktop.ipConfiguration.check.ip("169.254.100.1")
    pc0.desktop.ipConfiguration.check.gateway("0.0.0.0")
    pc0.desktop.ipConfiguration.check.subnet("255.255.0.0")
    pc0.desktop.ipConfiguration.check.dns("0.0.0.0")

    wirelessRouter0.select()
    wirelessRouter0.clickGuiTab()
    snooze(2)
    wirelessRouter0.gui.tabs.applicationsAndGaming()
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.enabledCheckbox(8, True)
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.saveSettingsButton()
    
    pc0.select()
    pc0.desktop.ipConfiguration.static()
    pc0.desktop.ipConfiguration.dhcp()
    
    util.fastForwardTime()
    
    pc0.desktop.ipConfiguration.check.ip("172.16.68.2")
    pc0.desktop.ipConfiguration.check.gateway("172.16.68.1")
    pc0.desktop.ipConfiguration.check.subnet("255.255.255.0")
    pc0.desktop.ipConfiguration.check.dns("172.16.67.10")
    pc0.desktop.ipConfiguration.close()
    
    wirelessRouter0.select()
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.enabledCheckbox(8, False)
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.saveSettingsButton()
    
def DNS():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping dns")
    util.speedUpConvergence()
    util.speedUpConvergence()
    pc0.desktop.commandPrompt.textCheckPoint("Ping request could not find host dns. Please check the name and try again", 1)
    pc0.desktop.commandPrompt.close()
    
    
    wirelessRouter0.select()
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.enabledCheckbox(1, True)
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.saveSettingsButton()
    

    
def HTTP():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("dns")
    snooze(2)
    #expect the authentication window
    wirelessRouter0.select()
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.enabledCheckbox(2, True)
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.saveSettingsButton()
    
    pc0.select()
    pc0.desktop.webBrowser.browse("dns")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc0.desktop.webBrowser.textCheckPoint("Welcome")
    pc0.desktop.webBrowser.close()

def Telnet():
    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("telnet lanrouter")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc0.desktop.commandPrompt.textCheckPoint("Connection refused by remote host")
    pc0.desktop.commandPrompt.close()
    
    wirelessRouter0.select()
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.enabledCheckbox(3, True)
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.saveSettingsButton()
    

    pc0.select()
    pc0.clickDesktopTab()
    pc0.desktop.applications.commandPrompt()
    snooze(5)
    pc0.desktop.commandPrompt.setText("telnet lanrouter")
    snooze(3)
    pc0.desktop.commandPrompt.setText("cisco")
    snooze(2)
    pc0.desktop.commandPrompt.textCheckPoint("LAN_Router")
    pc0.desktop.commandPrompt.close()
    
def TFTP():
    Router1.select()
    Router1.clickCliTab()
    Router1.cli.setCliText("\r")
    Router1.cli.setCliText("enable")
    Router1.cli.setCliText("copy tftp: flash:")
    Router1.cli.setCliText("dns")
    Router1.cli.setCliText("c1841-ipbasek9-mz.124-12.bin")
    Router1.cli.setCliText("\r")
    util.speedUpConvergence()

    Router1.cli.textCheckPoint("%Error opening tftp://dns/c1841-ipbasek9-mz\\.124-12\\.bin \(Cannot resolve domain name\)")
    util.clickOnWorkspace(wirelessRouter0.x, wirelessRouter0.y)
    
    wirelessRouter0.select()
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.ip(4, '3')
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.enabledCheckbox(4, True)
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.saveSettingsButton()
    
    Router1.select()
    Router1.clickCliTab()
    Router1.cli.setCliText("\r")
    Router1.cli.setCliText("enable")
    Router1.cli.setCliText("configure terminal")
    Router1.cli.setCliText("ip name-server 172.16.67.10")
    Router1.cli.setCliText("end")
    Router1.cli.setCliText("copy tftp: flash:")
    Router1.cli.setCliText("dns")
    Router1.cli.setCliText("c1841-ipbasek9-mz.124-12.bin")
    Router1.cli.setCliText("\r")
    util.speedUpConvergence()
    Router1.cli.setCliText("show flash")
    Router1.cli.textCheckPoint("16599160 c1841-ipbasek9-mz.124-12.bin", 1)

def SMNP():
    Router1.cli.setCliText("configure terminal")
    Router1.cli.setCliText("snmp-server community testro ro")
    Router1.cli.setCliText("snmp-server community testrw rw")
    Router1.cli.setCliText("end")

    pc0.select()
    pc0.clickDesktopTab()

    pc0.desktop.applications.commandPrompt()
    snooze(5)
    pc0.desktop.commandPrompt.setText("exit")
    pc0.desktop.commandPrompt.setText("snmpget /v 1 /a 172.16.67.10 /c testro /o .1.3.6.1.2.1.1.1.0")
    util.speedUpConvergence()
    pc0.desktop.commandPrompt.setText("snmpget /d")
    pc0.desktop.commandPrompt.textCheckPoint("SNMP request timed out")
    util.clickOnWorkspace(wirelessRouter0.x, wirelessRouter0.y)
    
    wirelessRouter0.select()
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.ip(4, '4')
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.enabledCheckbox(4, True)
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.saveSettingsButton()
    
    #wirelessRouter0.updateName()
    #wirelessRouter0.gui.app.setDefaultAppPortForwarding("SNMP", "4", LinksysRouterConst.Gui.ApplicationsAndGaming.ENABLE_CHECKBOX_5, 5)
    #wirelessRouter0.clickButton(LinksysRouterConst.Gui.ApplicationsAndGaming.SAVE_BUTT)
    
    pc0.select()
    pc0.desktop.commandPrompt.setText("snmpget /v 1 /a 172.16.67.10 /c testro /o .1.3.6.1.2.1.1.1.0")
    util.speedUpConvergence()
    pc0.desktop.commandPrompt.setText("snmpget /d")
    pc0.desktop.commandPrompt.textCheckPoint("C1841-ADVIPSERVICESK9-M")
    pc0.desktop.commandPrompt.close()
    
def removeAllEnableApps():
    wirelessRouter0.select()
    for i in range(5):
        wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.enabledCheckbox(i + 1, False)
    wirelessRouter0.gui.applicationsAndGaming.singlePortFowarding.saveSettingsButton()
    
    
def DMZ_172_16_100_3():
    wirelessRouter0.select()
    wirelessRouter0.gui.tabs.dmz()
    wirelessRouter0.gui.applicationsAndGaming.dmz.enabled()
    wirelessRouter0.gui.applicationsAndGaming.dmz.ipAddress('3')
    wirelessRouter0.gui.applicationsAndGaming.dmz.saveSettingsButton()
    
    pc0.select()
    pc0.clickDesktopTab()
    #pc0.clickButton(PCConst.Desktop.CommandPrompt.CLOSE_BUTT)
    pc0.desktop.applications.ipConfiguration()
    
    pc0.desktop.ipConfiguration.static()
    pc0.desktop.ipConfiguration.dhcp()
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc0.desktop.ipConfiguration.check.ip("172.16.68.[2,3]")
    pc0.desktop.ipConfiguration.check.gateway("172.16.68.1")
    pc0.desktop.ipConfiguration.check.subnet("255.255.255.0")
    pc0.desktop.ipConfiguration.check.dns("172.16.67.10")
    pc0.desktop.ipConfiguration.close()
    
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping dns")
    util.speedUpConvergence()
    util.speedUpConvergence()
    pc0.desktop.commandPrompt.textCheckPoint("Ping request could not find host dns. Please check the name and try again", 1)
    pc0.desktop.commandPrompt.close()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("dns")
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc0.desktop.webBrowser.textCheckPoint("Welcome")
    pc0.desktop.webBrowser.close()
    
    Router1.select()
    Router1.cli.setCliText("copy tftp: flash:")
    Router1.cli.setCliText("172.16.67.10")
    Router1.cli.setCliText("c1841-ipbasek9-mz.124-12.bin")
    Router1.cli.setCliText("\r")
    Router1.cli.setCliText("\r")
    Router1.cli.setCliText("\r")
    Router1.cli.setCliText("\r")
    util.speedUpConvergence()
    Router1.cli.setCliText("show flash")
    Router1.cli.textCheckPoint("16599160 c1841-ipbasek9-mz.124-12.bin", 2)
    
def DMZ_172_16_100_4():
    wirelessRouter0.select()
    wirelessRouter0.gui.tabs.dmz()
    wirelessRouter0.gui.applicationsAndGaming.dmz.enabled()
    wirelessRouter0.gui.applicationsAndGaming.dmz.ipAddress('4')
    wirelessRouter0.gui.applicationsAndGaming.dmz.saveSettingsButton()
    
    pc0.select()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("telnet 172.16.67.10")
    snooze(3)
    pc0.desktop.commandPrompt.setText("cisco")
    snooze(5)
    pc0.desktop.commandPrompt.textCheckPoint("LAN_Router", 2)
    pc0.desktop.commandPrompt.setText("exit")
    pc0.desktop.commandPrompt.close()
    
def DMZ_disabled():
    wirelessRouter0.select()
    wirelessRouter0.gui.tabs.dmz()
    wirelessRouter0.gui.applicationsAndGaming.dmz.disabled()
    wirelessRouter0.gui.applicationsAndGaming.dmz.saveSettingsButton()
    
    pc0.select()
    pc0.clickDesktopTab()
    #pc0.clickButton(PCConst.Desktop.CommandPrompt.CLOSE_BUTT)
    pc0.desktop.applications.ipConfiguration()
    
    pc0.desktop.ipConfiguration.static()
    pc0.desktop.ipConfiguration.dhcp()
    util.clickOnSimulation()
    util.clickOnRealtime()
    pc0.desktop.ipConfiguration.check.ip("169.\d{1,3}.\d{1,3}.\d{1,3}")
    pc0.desktop.ipConfiguration.check.gateway("0.0.0.0")
    pc0.desktop.ipConfiguration.check.subnet("255.255.0.0")
    pc0.desktop.ipConfiguration.check.dns("0.0.0.0")
    pc0.desktop.ipConfiguration.close()
    pc0.desktop.applications.commandPrompt()
    pc0.desktop.commandPrompt.setText("ping dns")
    util.speedUpConvergence()
    util.speedUpConvergence()
    pc0.desktop.commandPrompt.textCheckPoint("Ping request could not find host dns. Please check the name and try again", 2)
    pc0.desktop.commandPrompt.close()
    pc0.desktop.applications.webBrowser()
    pc0.desktop.webBrowser.browse("dns")
    util.speedUpConvergence()
    pc0.desktop.webBrowser.textCheckPoint("Request Timeout", 0)